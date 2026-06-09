#!/usr/bin/env python3
"""Report-mode external dry-run harness for saved public artifacts.

The harness runs existing Anti-Slop entrypoints in report mode only. It does not
call GitHub APIs, models, network services, tokens, or external repos at
runtime. Inputs are committed public-safe artifact files.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import argparse
import json
import re
import subprocess
import sys
import tempfile
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "proof" / "external-dry-run"
POLICY_DOC = ROOT / "docs" / "external-dry-run-policy.md"
TARGETS_JSON = OUT_DIR / "targets.json"
SUMMARY_JSON = OUT_DIR / "summary.json"
SUMMARY_MD = OUT_DIR / "summary.md"
SCHEMA_VERSION = "anti-slop-external-dry-run.v1"
POLICY_VERSION = "external-dry-run-policy.v1"
MIN_ARTIFACTS = 10
KILL_DENSITY_THRESHOLD = 5.0


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load_targets() -> list[dict[str, Any]]:
    data = json.loads(TARGETS_JSON.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("targets.json must be a list")
    return data


def _target_path(target: dict[str, Any]) -> Path:
    path = ROOT / str(target["artifact_path"])
    return path


def _root_path(target: dict[str, Any]) -> Path:
    return (ROOT / str(target.get("root", "."))).resolve()


def _event_number(target: dict[str, Any]) -> int:
    explicit = target.get("number")
    if isinstance(explicit, int):
        return explicit
    match = re.search(r"(\d+)$", str(target.get("id", "")))
    return int(match.group(1)) if match else 0


def _run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)


def _run_pr_event(target: dict[str, Any], tmp: Path) -> dict[str, Any]:
    source = _target_path(target)
    body = read_text(source)
    safe_id = re.sub(r"[^A-Za-z0-9_.-]+", "_", str(target["id"]))
    event = tmp / f"{safe_id}.event.json"
    receipt = tmp / f"{safe_id}.receipt.json"
    event.write_text(json.dumps({
        "pull_request": {
            "number": _event_number(target),
            "body": body,
        },
    }, sort_keys=True), encoding="utf-8")
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "pr_provenance_from_github_event.py"),
        "--event", str(event),
        "--event-name", "pull_request",
        "--root", str(_root_path(target)),
        "--report",
        "--json", str(receipt),
    ]
    proc = _run(cmd)
    if proc.returncode != 0:
        raise RuntimeError(
            f"{target['id']} anti-slop-pr-event report-mode run exited {proc.returncode}: "
            f"{proc.stderr or proc.stdout}"
        )
    data = json.loads(receipt.read_text(encoding="utf-8"))
    return _summarize_pr_receipt(target, source, body, data)


def _run_claims(target: dict[str, Any], tmp: Path) -> dict[str, Any]:
    source = _target_path(target)
    body = read_text(source)
    safe_id = re.sub(r"[^A-Za-z0-9_.-]+", "_", str(target["id"]))
    receipt = tmp / f"{safe_id}.claims.json"
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "gate_claims.py"),
        "--root", str(_root_path(target)),
        "--report",
        "--json", str(receipt),
    ]
    if target.get("receipts"):
        cmd.extend(["--receipts", str(ROOT / str(target["receipts"]))])
    if target.get("diff"):
        cmd.extend(["--diff", str(target["diff"])])
    cmd.append(str(source))
    proc = _run(cmd)
    if proc.returncode != 0:
        raise RuntimeError(
            f"{target['id']} anti-slop-claims report-mode run exited {proc.returncode}: "
            f"{proc.stderr or proc.stdout}"
        )
    data = json.loads(receipt.read_text(encoding="utf-8"))
    return _summarize_claims_receipt(target, source, body, data)


def normalize_reason(reason: str, status: str = "") -> str:
    text = reason.lower()
    if "no --issue-registry" in text:
        return "issue refs advisory without registry"
    if "file does not resolve" in text:
        return "file refs that do not resolve"
    if "test node not defined" in text or "test reference" in text or "test node" in text:
        return "test refs that do not resolve"
    if "unresolved source_card" in text or "unresolved card_id" in text:
        return "source/card refs that do not resolve"
    if "commit" in text and status == "advisory":
        return "commit refs advisory under local-git resolution"
    if "missing command receipt" in text:
        return "missing command receipt"
    if "missing metric receipt" in text or "metric receipt mismatch" in text:
        return "metric receipt missing or mismatched"
    return re.sub(r"^(?:unresolved|advisory)\s+", "", reason).strip()[:120]


def _summarize_pr_receipt(target: dict[str, Any], source: Path, body: str,
                          receipt: dict[str, Any]) -> dict[str, Any]:
    checks = receipt.get("checks", {})
    hard_claims = 0
    hard_failures = 0
    advisory = 0
    reasons: Counter[str] = Counter()
    claim_types: Counter[str] = Counter()
    for kind, check in checks.items():
        refs_checked = int(check.get("refs_checked", 0))
        unresolved = list(check.get("unresolved", []))
        advisory_items = list(check.get("advisory", []))
        claim_types[kind] += refs_checked
        if kind in {"file", "test", "card"}:
            hard_claims += refs_checked
            hard_failures += len(unresolved)
        elif kind == "issue" and receipt.get("issue_registry"):
            hard_claims += refs_checked
            hard_failures += len(unresolved)
        for item in unresolved:
            reasons[normalize_reason(str(item), "fail")] += 1
        advisory += len(advisory_items)
        for item in advisory_items:
            reasons[normalize_reason(str(item), "advisory")] += 1
    claim_count = sum(claim_types.values())
    line_count = max(1, len(body.splitlines()))
    return {
        "id": target["id"],
        "target": target["target"],
        "kind": target["kind"],
        "checker": "anti-slop-pr-event",
        "mode": "report",
        "source": rel(source),
        "origin_url": target.get("origin_url", ""),
        "line_count": line_count,
        "claim_count": claim_count,
        "hard_claim_count": hard_claims,
        "hard_unresolved_count": hard_failures,
        "advisory_count": advisory,
        "checkable_claims_per_100_lines": round(claim_count / line_count * 100, 2),
        "claim_types": dict(sorted(claim_types.items())),
        "top_reasons": reasons.most_common(10),
    }


def _summarize_claims_receipt(target: dict[str, Any], source: Path, body: str,
                              receipt: dict[str, Any]) -> dict[str, Any]:
    claims = list(receipt.get("claims", []))
    hard = [c for c in claims if c.get("tier") == "hard"]
    hard_fail = [c for c in hard if c.get("status") == "fail"]
    advisory = [c for c in claims if c.get("status") == "advisory"]
    reasons = Counter(normalize_reason(str(c.get("reason", "")), str(c.get("status", "")))
                      for c in hard_fail + advisory)
    claim_types = Counter(str(c.get("type", "unknown")) for c in claims)
    line_count = max(1, len(body.splitlines()))
    return {
        "id": target["id"],
        "target": target["target"],
        "kind": target["kind"],
        "checker": "anti-slop-claims",
        "mode": "report",
        "source": rel(source),
        "origin_url": target.get("origin_url", ""),
        "line_count": line_count,
        "claim_count": len(claims),
        "hard_claim_count": len(hard),
        "hard_unresolved_count": len(hard_fail),
        "advisory_count": len(advisory),
        "checkable_claims_per_100_lines": round(len(claims) / line_count * 100, 2),
        "claim_types": dict(sorted(claim_types.items())),
        "top_reasons": reasons.most_common(10),
    }


def run_targets() -> dict[str, Any]:
    targets = load_targets()
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        artifacts = []
        for target in targets:
            checker = target.get("checker")
            if checker == "anti-slop-pr-event":
                artifacts.append(_run_pr_event(target, tmp_path))
            elif checker == "anti-slop-claims":
                artifacts.append(_run_claims(target, tmp_path))
            else:
                raise ValueError(f"unsupported checker for {target.get('id')}: {checker}")
    return summarize(artifacts)


def summarize(artifacts: list[dict[str, Any]]) -> dict[str, Any]:
    artifact_count = len(artifacts)
    total_lines = sum(int(a["line_count"]) for a in artifacts)
    total_claims = sum(int(a["claim_count"]) for a in artifacts)
    hard_claims = sum(int(a["hard_claim_count"]) for a in artifacts)
    hard_unresolved = sum(int(a["hard_unresolved_count"]) for a in artifacts)
    advisory = sum(int(a["advisory_count"]) for a in artifacts)
    reasons: Counter[str] = Counter()
    claim_types: Counter[str] = Counter()
    targets = []
    for artifact in artifacts:
        reasons.update(dict(artifact.get("top_reasons", [])))
        claim_types.update(artifact.get("claim_types", {}))
        targets.append({
            "id": artifact["id"],
            "target": artifact["target"],
            "kind": artifact["kind"],
            "checker": artifact["checker"],
            "source": artifact["source"],
            "origin_url": artifact["origin_url"],
        })
    density = round(total_claims / total_lines * 100, 2) if total_lines else 0.0
    hard_unresolved_rate = round(hard_unresolved / hard_claims, 4) if hard_claims else 0.0
    advisory_rate = round(advisory / total_claims, 4) if total_claims else 0.0
    sample_status = (
        "sufficient_saved_public_artifacts"
        if artifact_count >= MIN_ARTIFACTS
        else "blocked_insufficient_public_artifacts"
    )
    kill_risk = "fail" if density < KILL_DENSITY_THRESHOLD else "pass"
    usefulness = (
        "useful" if sample_status.startswith("sufficient") and kill_risk == "pass"
        else "inconclusive"
    )
    return {
        "schema_version": SCHEMA_VERSION,
        "policy_version": POLICY_VERSION,
        "status": "dry_run_not_adoption",
        "sample_status": sample_status,
        "target": "saved public PR bodies from nferna26/anti-slop",
        "artifact_count": artifact_count,
        "required_artifact_count": MIN_ARTIFACTS,
        "total_lines": total_lines,
        "checkable_claim_count": total_claims,
        "hard_claim_count": hard_claims,
        "hard_unresolved_count": hard_unresolved,
        "advisory_count": advisory,
        "checkable_claims_per_100_lines": density,
        "hard_unresolved_rate": hard_unresolved_rate,
        "advisory_rate": advisory_rate,
        "top_reasons": [{"reason": k, "count": v} for k, v in reasons.most_common(10)],
        "top_claim_types": [{"type": k, "count": v} for k, v in claim_types.most_common(10)],
        "kill_criterion": {
            "risk": kill_risk,
            "rule": f"fail if checkable_claims_per_100_lines < {KILL_DENSITY_THRESHOLD}",
        },
        "usefulness": usefulness,
        "notes": [
            "Report mode only; no outreach, adoption, GitHub API, token, model, or network runtime.",
            "Resolver facts only; not correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.",
        ],
        "targets": targets,
        "artifacts": artifacts,
    }


def markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# External Dry-Run Summary",
        "",
        "Status: `dry_run_not_adoption`.",
        "",
        "This is a report-mode dry run over committed public-safe saved PR bodies. It does not contact repos at runtime, call GitHub APIs, use tokens, call models, open PRs, post comments, or automate adoption.",
        "",
        "A finding means a reference or receipt did or did not resolve. It does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.",
        "",
        "## Aggregate",
        "",
        f"- Schema: `{summary['schema_version']}`",
        f"- Policy: `{summary['policy_version']}`",
        f"- Target: {summary['target']}",
        f"- Artifacts: {summary['artifact_count']} ({summary['sample_status']})",
        f"- Checkable claims: {summary['checkable_claim_count']}",
        f"- Checkable claims per 100 lines: {summary['checkable_claims_per_100_lines']}",
        f"- Hard unresolved rate: {summary['hard_unresolved_rate']:.1%}",
        f"- Advisory rate: {summary['advisory_rate']:.1%}",
        f"- Kill-criterion risk: {summary['kill_criterion']['risk']} ({summary['kill_criterion']['rule']})",
        f"- Usefulness verdict: {summary['usefulness']}",
        "",
        "## Top Reasons",
        "",
    ]
    if summary["top_reasons"]:
        for item in summary["top_reasons"]:
            lines.append(f"- {item['reason']}: {item['count']}")
    else:
        lines.append("- None.")
    lines.extend(["", "## Top Claim Types", ""])
    if summary["top_claim_types"]:
        for item in summary["top_claim_types"]:
            lines.append(f"- {item['type']}: {item['count']}")
    else:
        lines.append("- None.")
    lines.extend(["", "## Sample Targets", ""])
    for target in summary["targets"]:
        lines.append(
            f"- {target['id']}: {target['target']} ({target['kind']}, {target['checker']})"
        )
    lines.extend(["", "## Artifact Metrics", ""])
    for artifact in summary["artifacts"]:
        lines.append(
            f"- {artifact['id']}: {artifact['claim_count']} claims, "
            f"{artifact['hard_unresolved_count']} hard unresolved, "
            f"{artifact['advisory_count']} advisory, "
            f"{artifact['checkable_claims_per_100_lines']} claims/100 lines"
        )
    return "\n".join(lines) + "\n"


def write_outputs(summary: dict[str, Any]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    write_json(SUMMARY_JSON, summary)
    SUMMARY_MD.write_text(markdown(summary), encoding="utf-8")


def required_policy_snippets() -> list[str]:
    return [
        POLICY_VERSION,
        "allowed inputs",
        "committed outputs",
        "redaction",
        "public PR-body",
        "no token",
        "no model",
        "no GitHub API",
        "no automated adoption",
        "opt-in outreach",
        SCHEMA_VERSION,
        "target",
        "artifact_count",
        "checkable_claims_per_100_lines",
        "hard_unresolved_rate",
        "advisory_rate",
        "top_reasons",
        "status",
        "policy_version",
    ]


def validate_policy(errors: list[str]) -> None:
    if not POLICY_DOC.is_file():
        errors.append(f"missing policy doc: {rel(POLICY_DOC)}")
        return
    text = POLICY_DOC.read_text(encoding="utf-8").lower()
    for snippet in required_policy_snippets():
        if snippet.lower() not in text:
            errors.append(f"{rel(POLICY_DOC)} missing snippet: {snippet}")


def validate_targets(errors: list[str]) -> None:
    if not TARGETS_JSON.is_file():
        errors.append(f"missing target config: {rel(TARGETS_JSON)}")
        return
    try:
        targets = load_targets()
    except Exception as exc:  # noqa: BLE001
        errors.append(f"could not load targets: {exc}")
        return
    if len(targets) < MIN_ARTIFACTS:
        errors.append(f"expected at least {MIN_ARTIFACTS} targets, found {len(targets)}")
    for target in targets:
        for key in ("id", "target", "kind", "checker", "artifact_path", "origin_url"):
            if key not in target:
                errors.append(f"target missing {key}: {target}")
        kind = target.get("kind")
        if kind not in {"saved_public_pr_body", "local_checkout_artifact"}:
            errors.append(f"unsupported target kind for {target.get('id')}: {kind}")
        checker = target.get("checker")
        if checker not in {"anti-slop-pr-event", "anti-slop-claims"}:
            errors.append(f"unsupported checker for {target.get('id')}: {checker}")
        path = _target_path(target) if "artifact_path" in target else None
        if path is not None and not path.is_file():
            errors.append(f"target artifact missing for {target.get('id')}: {rel(path)}")


def validate_summary_data(summary: dict[str, Any], errors: list[str]) -> None:
    required = {
        "schema_version": str,
        "target": str,
        "artifact_count": int,
        "checkable_claims_per_100_lines": (int, float),
        "hard_unresolved_rate": (int, float),
        "advisory_rate": (int, float),
        "top_reasons": list,
        "status": str,
        "policy_version": str,
    }
    for key, typ in required.items():
        if key not in summary:
            errors.append(f"summary missing required field: {key}")
        elif not isinstance(summary[key], typ):
            errors.append(f"summary field has wrong type: {key}")
    if summary.get("schema_version") != SCHEMA_VERSION:
        errors.append(f"summary schema mismatch: {summary.get('schema_version')}")
    if summary.get("policy_version") != POLICY_VERSION:
        errors.append(f"summary policy mismatch: {summary.get('policy_version')}")
    if summary.get("status") != "dry_run_not_adoption":
        errors.append(f"summary status must be dry_run_not_adoption: {summary.get('status')}")
    if int(summary.get("artifact_count", 0)) < MIN_ARTIFACTS:
        errors.append(f"summary artifact_count below {MIN_ARTIFACTS}: {summary.get('artifact_count')}")
    text = json.dumps(summary, sort_keys=True)
    forbidden = [str(ROOT), "/Users/", "GITHUB_TOKEN", "OPENAI_API_KEY", "ANTHROPIC_API_KEY"]
    for snippet in forbidden:
        if snippet in text:
            errors.append(f"summary contains forbidden private/token-like snippet: {snippet}")


def validate_summary_files(errors: list[str]) -> None:
    if not SUMMARY_JSON.is_file():
        errors.append(f"missing summary JSON: {rel(SUMMARY_JSON)}")
        return
    try:
        summary = json.loads(SUMMARY_JSON.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid summary JSON: {exc}")
        return
    validate_summary_data(summary, errors)
    if not SUMMARY_MD.is_file():
        errors.append(f"missing summary Markdown: {rel(SUMMARY_MD)}")
    else:
        md = SUMMARY_MD.read_text(encoding="utf-8")
        for snippet in (SCHEMA_VERSION, "dry_run_not_adoption", "Usefulness verdict"):
            if snippet not in md:
                errors.append(f"{rel(SUMMARY_MD)} missing snippet: {snippet}")
        if str(ROOT) in md or "/Users/" in md:
            errors.append(f"{rel(SUMMARY_MD)} contains private local path")


def check_compatibility() -> list[str]:
    errors: list[str] = []
    validate_policy(errors)
    validate_targets(errors)
    validate_summary_files(errors)
    return errors


def run_and_check() -> int:
    pre_errors: list[str] = []
    validate_policy(pre_errors)
    validate_targets(pre_errors)
    if pre_errors:
        print("EXTERNAL DRY-RUN SMOKE FAILED:")
        for error in pre_errors:
            print(f"  - {error}")
        return 1
    summary = run_targets()
    write_outputs(summary)
    errors = check_compatibility()
    if errors:
        print("EXTERNAL DRY-RUN SMOKE FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(
        "EXTERNAL DRY-RUN SMOKE PASSED: "
        f"{summary['artifact_count']} saved public artifacts, "
        f"{summary['checkable_claims_per_100_lines']} claims/100 lines, "
        f"hard_unresolved={summary['hard_unresolved_rate']:.1%}, "
        f"advisory={summary['advisory_rate']:.1%}, "
        f"status={summary['status']}."
    )
    return 0


def check_only() -> int:
    errors = check_compatibility()
    if errors:
        print("EXTERNAL DRY-RUN COMPAT FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"EXTERNAL DRY-RUN COMPAT PASSED: {SCHEMA_VERSION} aggregate and policy links are valid.")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true",
                        help="run report-mode dry run and schema compatibility check")
    parser.add_argument("--check", action="store_true",
                        help="validate committed policy, target config, and aggregate files")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.check:
        return check_only()
    if args.self_test:
        return run_and_check()
    summary = run_targets()
    write_outputs(summary)
    print(f"external dry run wrote {rel(SUMMARY_JSON)} and {rel(SUMMARY_MD)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
