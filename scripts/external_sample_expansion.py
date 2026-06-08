#!/usr/bin/env python3
"""Validate and summarize the expanded external dry-run sample.

The expanded sample uses committed public-safe saved PR bodies from AI/devtool
repos outside `nferna26/anti-slop`. It runs existing Anti-Slop report-mode
entrypoints against an empty public fixture root so the sample can measure claim
density and cluster shape without committing external checkouts or requiring a
network/API/token at test time.
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
BASE_SUMMARY = ROOT / "proof" / "external-dry-run" / "summary.json"
EXP_DIR = ROOT / "proof" / "external-dry-run" / "expanded"
TARGETS_JSON = EXP_DIR / "targets.json"
SUMMARY_JSON = EXP_DIR / "summary.json"
SUMMARY_MD = EXP_DIR / "summary.md"
COMPARISON_JSON = EXP_DIR / "comparison.json"
COMPARISON_MD = EXP_DIR / "comparison.md"
ACTIONABILITY_JSON = EXP_DIR / "actionability.json"
ACTIONABILITY_MD = EXP_DIR / "actionability.md"
POLICY_DOC = ROOT / "docs" / "external-dry-run-policy.md"

SCHEMA = "anti-slop-external-sample-expansion.v1"
COMPARISON_SCHEMA = "anti-slop-external-sample-comparison.v1"
ACTIONABILITY_SCHEMA = "anti-slop-actionability-labels.v1"
MIN_TARGETS = 10
ALLOWED_LABELS = {"actionable", "non_actionable", "unclear", "excluded"}


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def load_targets() -> list[dict[str, Any]]:
    return read_json(TARGETS_JSON)


def normalize_reason(reason: str, status: str = "") -> str:
    text = reason.lower()
    if "no --issue-registry" in text:
        return "issue refs advisory without registry"
    if "file does not resolve" in text:
        return "file refs that do not resolve"
    if "test node" in text or "test reference" in text:
        return "test refs that do not resolve"
    if "unresolved source_card" in text or "unresolved card_id" in text:
        return "source/card refs that do not resolve"
    if "commit" in text and status == "advisory":
        return "commit refs advisory under local-git resolution"
    return re.sub(r"^(?:unresolved|advisory)\s+", "", reason).strip()[:120]


def run_target(target: dict[str, Any], tmp: Path, empty_root: Path) -> dict[str, Any]:
    body_path = ROOT / target["artifact_path"]
    body = body_path.read_text(encoding="utf-8")
    safe_id = re.sub(r"[^A-Za-z0-9_.-]+", "_", str(target["id"]))
    event_path = tmp / f"{safe_id}.event.json"
    receipt_path = tmp / f"{safe_id}.receipt.json"
    event_path.write_text(json.dumps({
        "pull_request": {
            "number": int(target.get("number", 0)),
            "body": body,
        },
    }, sort_keys=True), encoding="utf-8")
    cmd = [
        sys.executable,
        str(ROOT / "scripts" / "pr_provenance_from_github_event.py"),
        "--event", str(event_path),
        "--event-name", "pull_request",
        "--root", str(empty_root),
        "--report",
        "--json", str(receipt_path),
    ]
    proc = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(
            f"{target['id']} report-mode run exited {proc.returncode}: {proc.stderr or proc.stdout}"
        )
    receipt = read_json(receipt_path)
    checks = receipt.get("checks", {})
    hard_claims = 0
    hard_unresolved = 0
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
            hard_unresolved += len(unresolved)
        for item in unresolved:
            reasons[normalize_reason(str(item), "fail")] += 1
        advisory += len(advisory_items)
        for item in advisory_items:
            reasons[normalize_reason(str(item), "advisory")] += 1
    line_count = max(1, len(body.splitlines()))
    claim_count = sum(claim_types.values())
    return {
        "id": target["id"],
        "target": target["target"],
        "repo": target["repo"],
        "kind": target["kind"],
        "checker": "anti-slop-pr-event",
        "mode": "report",
        "root_mode": "empty_public_fixture_root_unavailable",
        "source": rel(body_path),
        "origin_url": target["origin_url"],
        "line_count": line_count,
        "claim_count": claim_count,
        "hard_claim_count": hard_claims,
        "hard_unresolved_count": hard_unresolved,
        "advisory_count": advisory,
        "checkable_claims_per_100_lines": round(claim_count / line_count * 100, 2),
        "claim_types": dict(sorted(claim_types.items())),
        "top_reasons": reasons.most_common(10),
    }


def summarize_artifacts(artifacts: list[dict[str, Any]]) -> dict[str, Any]:
    line_count = sum(int(a["line_count"]) for a in artifacts)
    claim_count = sum(int(a["claim_count"]) for a in artifacts)
    hard_claims = sum(int(a["hard_claim_count"]) for a in artifacts)
    hard_unresolved = sum(int(a["hard_unresolved_count"]) for a in artifacts)
    advisory = sum(int(a["advisory_count"]) for a in artifacts)
    reasons: Counter[str] = Counter()
    claim_types: Counter[str] = Counter()
    for artifact in artifacts:
        reasons.update(dict(artifact["top_reasons"]))
        claim_types.update(artifact["claim_types"])
    density = round(claim_count / line_count * 100, 2) if line_count else 0.0
    return {
        "schema_version": SCHEMA,
        "status": "dry_run_not_adoption",
        "target": "saved public PR bodies from external AI/devtool repos",
        "artifact_count": len(artifacts),
        "required_artifact_count": MIN_TARGETS,
        "repo_count": len({a["repo"] for a in artifacts}),
        "total_lines": line_count,
        "checkable_claim_count": claim_count,
        "hard_claim_count": hard_claims,
        "hard_unresolved_count": hard_unresolved,
        "advisory_count": advisory,
        "checkable_claims_per_100_lines": density,
        "hard_unresolved_rate": round(hard_unresolved / hard_claims, 4) if hard_claims else 0.0,
        "advisory_rate": round(advisory / claim_count, 4) if claim_count else 0.0,
        "root_mode": "empty_public_fixture_root_unavailable",
        "sample_status": "sufficient_external_public_artifacts"
        if len(artifacts) >= MIN_TARGETS else "blocked_insufficient_external_public_artifacts",
        "top_reasons": [{"reason": k, "count": v} for k, v in reasons.most_common(10)],
        "top_claim_types": [{"type": k, "count": v} for k, v in claim_types.most_common(10)],
        "notes": [
            "Report mode only; no outreach, adoption, GitHub API, token, model, or network runtime.",
            "External repo checkouts are not committed; root-dependent hard failures are actionability-labeled separately.",
            "Resolver facts only; not correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.",
        ],
        "artifacts": artifacts,
    }


def write_summary_markdown(summary: dict[str, Any]) -> None:
    lines = [
        "# Expanded External Dry-Run Summary",
        "",
        "Status: `dry_run_not_adoption`.",
        "",
        "This is a report-mode dry run over committed public-safe saved PR bodies from external AI/devtool repos. It does not contact repos at runtime, call GitHub APIs, use tokens, call models, open PRs, post comments, or automate adoption.",
        "",
        "External repo checkouts are not committed. Root-dependent hard failures are labeled separately for actionability and should not be treated as maintainer-ready findings.",
        "",
        "A finding means a reference or receipt did or did not resolve in the configured dry-run fixture. It does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.",
        "",
        "## Aggregate",
        "",
        f"- Schema: `{summary['schema_version']}`",
        f"- Target: {summary['target']}",
        f"- Artifacts: {summary['artifact_count']} ({summary['sample_status']})",
        f"- Repos: {summary['repo_count']}",
        f"- Checkable claims: {summary['checkable_claim_count']}",
        f"- Checkable claims per 100 lines: {summary['checkable_claims_per_100_lines']}",
        f"- Hard unresolved rate: {summary['hard_unresolved_rate']:.1%}",
        f"- Advisory rate: {summary['advisory_rate']:.1%}",
        f"- Root mode: {summary['root_mode']}",
        "",
        "## Top Reasons",
        "",
    ]
    for item in summary["top_reasons"] or []:
        lines.append(f"- {item['reason']}: {item['count']}")
    lines.extend(["", "## Targets", ""])
    for artifact in summary["artifacts"]:
        lines.append(f"- {artifact['id']}: {artifact['target']} ({artifact['repo']})")
    SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_comparison(expanded: dict[str, Any]) -> dict[str, Any]:
    base = read_json(BASE_SUMMARY)
    return {
        "schema_version": COMPARISON_SCHEMA,
        "status": "dry_run_not_adoption",
        "this_repo_sample": {
            "artifact_count": base["artifact_count"],
            "checkable_claims_per_100_lines": base["checkable_claims_per_100_lines"],
            "hard_unresolved_rate": base["hard_unresolved_rate"],
            "advisory_rate": base["advisory_rate"],
            "top_reasons": base["top_reasons"][:5],
        },
        "external_sample": {
            "artifact_count": expanded["artifact_count"],
            "repo_count": expanded["repo_count"],
            "checkable_claims_per_100_lines": expanded["checkable_claims_per_100_lines"],
            "hard_unresolved_rate": expanded["hard_unresolved_rate"],
            "advisory_rate": expanded["advisory_rate"],
            "top_reasons": expanded["top_reasons"][:5],
            "root_mode": expanded["root_mode"],
        },
        "interpretation": "External sample increases public-repo coverage but root-dependent hard failures are not maintainer-actionable until checked against real local checkouts.",
    }


def write_comparison_markdown(data: dict[str, Any]) -> None:
    t = data["this_repo_sample"]
    e = data["external_sample"]
    lines = [
        "# External Sample Comparison",
        "",
        f"- Schema: `{data['schema_version']}`",
        f"- Status: `{data['status']}`",
        "",
        "| Sample | Artifacts | Repos | Claims/100 lines | Hard unresolved | Advisory |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
        f"| This repo | {t['artifact_count']} | 1 | {t['checkable_claims_per_100_lines']} | {t['hard_unresolved_rate']:.1%} | {t['advisory_rate']:.1%} |",
        f"| External | {e['artifact_count']} | {e['repo_count']} | {e['checkable_claims_per_100_lines']} | {e['hard_unresolved_rate']:.1%} | {e['advisory_rate']:.1%} |",
        "",
        f"Interpretation: {data['interpretation']}",
    ]
    COMPARISON_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_sample() -> dict[str, Any]:
    targets = load_targets()
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        empty_root = tmp_path / "empty-root"
        empty_root.mkdir()
        artifacts = [run_target(target, tmp_path, empty_root) for target in targets]
    summary = summarize_artifacts(artifacts)
    write_json(SUMMARY_JSON, summary)
    write_summary_markdown(summary)
    comparison = build_comparison(summary)
    write_json(COMPARISON_JSON, comparison)
    write_comparison_markdown(comparison)
    return summary


def validate_targets(errors: list[str]) -> None:
    if not TARGETS_JSON.is_file():
        errors.append(f"missing expanded target config: {rel(TARGETS_JSON)}")
        return
    try:
        targets = load_targets()
    except Exception as exc:  # noqa: BLE001
        errors.append(f"could not load expanded targets: {exc}")
        return
    if len(targets) < MIN_TARGETS:
        errors.append(f"expected at least {MIN_TARGETS} expanded targets, found {len(targets)}")
    repos = {str(t.get("repo", "")) for t in targets}
    if "nferna26/anti-slop" in repos:
        errors.append("expanded target set must exclude nferna26/anti-slop")
    if len(repos) < MIN_TARGETS:
        errors.append(f"expected at least {MIN_TARGETS} distinct external repos, found {len(repos)}")
    for target in targets:
        for key in ("id", "target", "repo", "kind", "checker", "artifact_path", "origin_url", "reviewed_public_safe"):
            if key not in target:
                errors.append(f"expanded target missing {key}: {target}")
        if target.get("checker") != "anti-slop-pr-event":
            errors.append(f"expanded target must use anti-slop-pr-event report mode: {target.get('id')}")
        if target.get("kind") != "saved_public_pr_body":
            errors.append(f"expanded target must be saved_public_pr_body: {target.get('id')}")
        if target.get("reviewed_public_safe") is not True:
            errors.append(f"expanded target not marked reviewed_public_safe: {target.get('id')}")
        if "github.com/" not in str(target.get("origin_url", "")):
            errors.append(f"expanded target origin_url must be public GitHub URL: {target.get('id')}")
        path = ROOT / str(target.get("artifact_path", ""))
        if not path.is_file():
            errors.append(f"expanded target artifact missing: {rel(path)}")


def validate_summary(path: Path, schema: str, errors: list[str]) -> dict[str, Any] | None:
    if not path.is_file():
        errors.append(f"missing expanded summary artifact: {rel(path)}")
        return None
    data = read_json(path)
    if data.get("schema_version") != schema:
        errors.append(f"{rel(path)} schema mismatch: {data.get('schema_version')}")
    text = json.dumps(data, sort_keys=True)
    for forbidden in (str(ROOT), "/Users/", "GITHUB_TOKEN", "OPENAI_API_KEY", "ANTHROPIC_API_KEY"):
        if forbidden in text:
            errors.append(f"{rel(path)} contains forbidden private/token-like snippet: {forbidden}")
    return data


def validate_outputs(errors: list[str]) -> None:
    summary = validate_summary(SUMMARY_JSON, SCHEMA, errors)
    validate_summary(COMPARISON_JSON, COMPARISON_SCHEMA, errors)
    for path in (SUMMARY_MD, COMPARISON_MD):
        if not path.is_file():
            errors.append(f"missing expanded Markdown artifact: {rel(path)}")
        elif "/Users/" in path.read_text(encoding="utf-8"):
            errors.append(f"{rel(path)} contains private local path")
    if summary:
        if summary.get("artifact_count", 0) < MIN_TARGETS:
            errors.append(f"expanded summary artifact_count below {MIN_TARGETS}")
        if summary.get("repo_count", 0) < MIN_TARGETS:
            errors.append(f"expanded summary repo_count below {MIN_TARGETS}")
        if summary.get("status") != "dry_run_not_adoption":
            errors.append("expanded summary must remain dry_run_not_adoption")
        if summary.get("root_mode") != "empty_public_fixture_root_unavailable":
            errors.append("expanded summary must record root-unavailable fixture mode")


def validate_actionability(errors: list[str]) -> None:
    if not ACTIONABILITY_JSON.is_file():
        errors.append(f"missing actionability labels: {rel(ACTIONABILITY_JSON)}")
        return
    data = read_json(ACTIONABILITY_JSON)
    if data.get("schema_version") != ACTIONABILITY_SCHEMA:
        errors.append(f"actionability schema mismatch: {data.get('schema_version')}")
    allowed = set(data.get("allowed_labels", []))
    if allowed != ALLOWED_LABELS:
        errors.append(f"actionability allowed_labels mismatch: {sorted(allowed)}")
    labels = data.get("labels", [])
    if not labels:
        errors.append("actionability labels are empty")
    seen = {item.get("label") for item in labels}
    if not seen <= ALLOWED_LABELS:
        errors.append(f"unknown actionability labels: {sorted(seen - ALLOWED_LABELS)}")
    for item in labels:
        for key in ("cluster_key", "label", "count", "reason", "evidence_scope"):
            if key not in item:
                errors.append(f"actionability label missing {key}: {item}")
        if item.get("evidence_scope") not in {"aggregate_cluster", "excluded_root_unavailable"}:
            errors.append(f"invalid actionability evidence_scope: {item}")
    summary = data.get("summary", {})
    for key in ("total_labeled_findings", "actionable_rate", "non_actionable_rate", "excluded_rate", "useful_findings_status"):
        if key not in summary:
            errors.append(f"actionability summary missing {key}")
    if SUMMARY_JSON.is_file() and "total_labeled_findings" in summary:
        expanded = read_json(SUMMARY_JSON)
        expected_total = int(expanded.get("checkable_claim_count", 0))
        if int(summary["total_labeled_findings"]) != expected_total:
            errors.append(
                f"actionability total_labeled_findings must match expanded checkable_claim_count "
                f"({summary['total_labeled_findings']} != {expected_total})"
            )
        reason_counts = {item["reason"]: int(item["count"]) for item in expanded.get("top_reasons", [])}
        for item in labels:
            reason = str(item.get("cluster_key", "")).split("|")[-1]
            if reason in reason_counts and int(item.get("count", 0)) != reason_counts[reason]:
                errors.append(f"actionability count mismatch for {reason}: {item.get('count')} != {reason_counts[reason]}")
    if not ACTIONABILITY_MD.is_file():
        errors.append(f"missing actionability Markdown: {rel(ACTIONABILITY_MD)}")
    elif "raw line text" not in ACTIONABILITY_MD.read_text(encoding="utf-8").lower():
        errors.append(f"{rel(ACTIONABILITY_MD)} must state raw line text is omitted")


def validate_policy_doc(errors: list[str]) -> None:
    if not POLICY_DOC.is_file():
        errors.append(f"missing policy doc: {rel(POLICY_DOC)}")
        return
    text = POLICY_DOC.read_text(encoding="utf-8")
    for snippet in (
        "expanded external sample",
        "target-selection rules",
        "no-contact/no-outreach",
        "actionability labels",
        ACTIONABILITY_SCHEMA,
    ):
        if snippet not in text:
            errors.append(f"{rel(POLICY_DOC)} missing snippet: {snippet}")


def compatibility_errors(include_actionability: bool = True) -> list[str]:
    errors: list[str] = []
    validate_policy_doc(errors)
    validate_targets(errors)
    validate_outputs(errors)
    if include_actionability:
        validate_actionability(errors)
    return errors


def self_test() -> int:
    pre_errors: list[str] = []
    validate_policy_doc(pre_errors)
    validate_targets(pre_errors)
    if pre_errors:
        print("EXTERNAL SAMPLE SMOKE FAILED:")
        for error in pre_errors:
            print(f"  - {error}")
        return 1
    summary = run_sample()
    errors = compatibility_errors(include_actionability=True)
    if errors:
        print("EXTERNAL SAMPLE SMOKE FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(
        "EXTERNAL SAMPLE SMOKE PASSED: "
        f"{summary['artifact_count']} external public artifacts, "
        f"{summary['repo_count']} repos, "
        f"{summary['checkable_claims_per_100_lines']} claims/100 lines, "
        f"hard_unresolved={summary['hard_unresolved_rate']:.1%}, "
        f"advisory={summary['advisory_rate']:.1%}."
    )
    return 0


def check_only() -> int:
    errors = compatibility_errors(include_actionability=True)
    if errors:
        print("EXTERNAL SAMPLE COMPAT FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"EXTERNAL SAMPLE COMPAT PASSED: {SCHEMA}, comparison, and actionability artifacts are valid.")
    return 0


def check_actionability() -> int:
    errors: list[str] = []
    validate_actionability(errors)
    if errors:
        print("ACTIONABILITY LABEL CHECK FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"ACTIONABILITY LABEL CHECK PASSED: {ACTIONABILITY_SCHEMA} aggregate labels are valid.")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--check-actionability", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.self_test:
        return self_test()
    if args.check:
        return check_only()
    if args.check_actionability:
        return check_actionability()
    summary = run_sample()
    print(f"expanded external sample wrote {rel(SUMMARY_JSON)} ({summary['artifact_count']} artifacts)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
