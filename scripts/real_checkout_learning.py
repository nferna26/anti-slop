#!/usr/bin/env python3
"""Run report-mode checks against real local checkouts of public PR heads.

The committed outputs are aggregate and public-safe. Public repo checkouts and
full resolver receipts stay in temporary storage and are never committed.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EXPANDED_TARGETS = ROOT / "proof" / "external-dry-run" / "expanded" / "targets.json"
EXPANDED_SUMMARY = ROOT / "proof" / "external-dry-run" / "expanded" / "summary.json"
POLICY_DOC = ROOT / "docs" / "external-dry-run-policy.md"
OUT_DIR = ROOT / "proof" / "real-checkout-learning"
TARGETS_JSON = OUT_DIR / "targets.json"
SUMMARY_JSON = OUT_DIR / "summary.json"
SUMMARY_MD = OUT_DIR / "summary.md"
COMPARISON_JSON = OUT_DIR / "comparison.json"
COMPARISON_MD = OUT_DIR / "comparison.md"
ACTIONABILITY_JSON = OUT_DIR / "actionability.json"
ACTIONABILITY_MD = OUT_DIR / "actionability.md"

SCHEMA = "anti-slop-real-checkout-learning.v1"
TARGET_SCHEMA = "anti-slop-real-checkout-targets.v1"
COMPARISON_SCHEMA = "anti-slop-real-checkout-comparison.v1"
ACTIONABILITY_SCHEMA = "anti-slop-real-checkout-actionability.v1"
POLICY_VERSION = "external-dry-run-policy.v1"
MIN_TARGETS = 3
ALLOWED_LABELS = {"actionable", "non_actionable", "unclear", "excluded"}

# Evidence-led subset from proof/external-dry-run/expanded/summary.json:
# targets with concrete file refs, issue refs, or a commit advisory and public
# PR refs that can be fetched over git without GitHub API/token use.
SELECTED_TARGET_IDS = [
    "openai-openai-agents-python-pr-3544",
    "anthropics-anthropic-sdk-python-pr-1642",
    "pydantic-pydantic-ai-pr-5805",
    "modelcontextprotocol-python-sdk-pr-2773",
    "crewaiinc-crewai-pr-6042",
]


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


def run_cmd(cmd: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=str(cwd or ROOT), capture_output=True, text=True)


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
    return re.sub(r"^(?:unresolved|advisory)\s+", "", reason).strip()[:120]


def parse_line(reason: str) -> int | None:
    match = re.search(r"\bline\s+(\d+)\b", reason)
    return int(match.group(1)) if match else None


def parse_ref_kind(claim_type: str, reason: str) -> str:
    if claim_type == "issue":
        return "issue-number"
    if claim_type == "commit":
        return "commit-sha"
    if claim_type in {"card", "source_card", "card_id"}:
        return "source-card-id"
    if "does not resolve:" in reason:
        ref = reason.rsplit("does not resolve:", 1)[1].strip()
        suffix = Path(ref).suffix or "no-extension"
        return f"path depth={ref.count('/')} ext={suffix}"
    return "reference"


def selected_targets() -> list[dict[str, Any]]:
    targets = read_json(EXPANDED_TARGETS)
    by_id = {target["id"]: target for target in targets}
    selected: list[dict[str, Any]] = []
    for target_id in SELECTED_TARGET_IDS:
        target = dict(by_id[target_id])
        owner_repo = str(target["repo"])
        target["schema_version"] = TARGET_SCHEMA
        target["checkout_url"] = f"https://github.com/{owner_repo}.git"
        target["checkout_ref"] = f"refs/pull/{int(target['number'])}/head"
        target["root_mode"] = "real_public_checkout_pr_head"
        target["target_selection_reason"] = (
            "selected from expanded empty-root sample because it contained concrete "
            "file/issue/commit refs and a public PR head fetchable by git"
        )
        selected.append(target)
    return selected


def write_targets(targets: list[dict[str, Any]]) -> None:
    write_json(TARGETS_JSON, {
        "schema_version": TARGET_SCHEMA,
        "policy_version": POLICY_VERSION,
        "status": "dry_run_not_adoption",
        "target_selection": "3-5 public AI/devtool PR bodies with concrete refs from the expanded sample",
        "no_contact_no_outreach": True,
        "checkout_storage": "temporary local-only directories; external checkouts are not committed",
        "targets": targets,
    })


def checkout_target(target: dict[str, Any], checkout_parent: Path) -> tuple[Path | None, str, str, str]:
    checkout = checkout_parent / target["id"]
    if checkout.exists():
        shutil.rmtree(checkout)
    clone = run_cmd([
        "git",
        "clone",
        "--quiet",
        "--filter=blob:none",
        "--no-checkout",
        "--depth=1",
        str(target["checkout_url"]),
        str(checkout),
    ])
    if clone.returncode != 0:
        return None, "blocked_checkout_unavailable", "", (clone.stderr or clone.stdout).strip()[:240]
    fetch = run_cmd([
        "git",
        "-C",
        str(checkout),
        "fetch",
        "--quiet",
        "--depth=1",
        "origin",
        f"{target['checkout_ref']}:anti-slop-pr-head",
    ])
    if fetch.returncode != 0:
        return None, "blocked_checkout_unavailable", "", (fetch.stderr or fetch.stdout).strip()[:240]
    switch = run_cmd(["git", "-C", str(checkout), "checkout", "--quiet", "anti-slop-pr-head"])
    if switch.returncode != 0:
        return None, "blocked_checkout_unavailable", "", (switch.stderr or switch.stdout).strip()[:240]
    head = run_cmd(["git", "-C", str(checkout), "rev-parse", "HEAD"])
    if head.returncode != 0:
        return None, "blocked_checkout_unavailable", "", (head.stderr or head.stdout).strip()[:240]
    return checkout, "checked_out", head.stdout.strip(), ""


def run_pr_event(target: dict[str, Any], checkout: Path, tmp: Path) -> dict[str, Any]:
    body_path = ROOT / target["artifact_path"]
    body = body_path.read_text(encoding="utf-8")
    safe_id = re.sub(r"[^A-Za-z0-9_.-]+", "_", str(target["id"]))
    event_path = tmp / f"{safe_id}.event.json"
    receipt_path = tmp / f"{safe_id}.receipt.json"
    event_path.write_text(json.dumps({
        "pull_request": {
            "number": int(target["number"]),
            "body": body,
        },
    }, sort_keys=True), encoding="utf-8")
    proc = run_cmd([
        sys.executable,
        str(ROOT / "scripts" / "pr_provenance_from_github_event.py"),
        "--event", str(event_path),
        "--event-name", "pull_request",
        "--root", str(checkout),
        "--report",
        "--json", str(receipt_path),
    ])
    if proc.returncode != 0:
        raise RuntimeError(f"{target['id']} report-mode run exited {proc.returncode}: {proc.stderr or proc.stdout}")
    receipt = read_json(receipt_path)
    checks = receipt.get("checks", {})
    hard_claims = 0
    hard_unresolved = 0
    advisory = 0
    claim_types: Counter[str] = Counter()
    reasons: Counter[str] = Counter()
    findings: list[dict[str, Any]] = []
    for kind, check in checks.items():
        refs_checked = int(check.get("refs_checked", 0))
        unresolved = list(check.get("unresolved", []))
        advisory_items = list(check.get("advisory", []))
        claim_types[kind] += refs_checked
        if kind in {"file", "test", "card"}:
            hard_claims += refs_checked
            hard_unresolved += len(unresolved)
        for status, items in (("fail", unresolved), ("advisory", advisory_items)):
            if status == "advisory":
                advisory += len(items)
            for item in items:
                reason = str(item)
                normalized = normalize_reason(reason, status)
                reasons[normalized] += 1
                findings.append({
                    "target_id": target["id"],
                    "claim_type": kind,
                    "status": status,
                    "line": parse_line(reason),
                    "normalized_reason": normalized,
                    "ref_shape": parse_ref_kind(kind, reason),
                })
    claim_count = sum(claim_types.values())
    line_count = max(1, len(body.splitlines()))
    return {
        "id": target["id"],
        "target": target["target"],
        "repo": target["repo"],
        "kind": target["kind"],
        "checker": "anti-slop-pr-event",
        "mode": "report",
        "root_mode": "real_public_checkout_pr_head",
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
        "findings": findings,
    }


def blocked_artifact(target: dict[str, Any], status: str, reason: str) -> dict[str, Any]:
    body_path = ROOT / target["artifact_path"]
    body = body_path.read_text(encoding="utf-8")
    return {
        "id": target["id"],
        "target": target["target"],
        "repo": target["repo"],
        "kind": target["kind"],
        "checker": "anti-slop-pr-event",
        "mode": "report",
        "root_mode": "real_public_checkout_pr_head",
        "source": rel(body_path),
        "origin_url": target["origin_url"],
        "line_count": max(1, len(body.splitlines())),
        "claim_count": 0,
        "hard_claim_count": 0,
        "hard_unresolved_count": 0,
        "advisory_count": 0,
        "checkable_claims_per_100_lines": 0.0,
        "claim_types": {},
        "top_reasons": [["checkout unavailable", 1]],
        "checkout_status": status,
        "checkout_error": reason,
        "findings": [{
            "target_id": target["id"],
            "claim_type": "checkout",
            "status": "blocked",
            "line": None,
            "normalized_reason": "checkout unavailable",
            "ref_shape": "public-git-pr-head",
        }],
    }


def summarize(artifacts: list[dict[str, Any]], checkout_records: list[dict[str, Any]]) -> dict[str, Any]:
    total_lines = sum(int(a["line_count"]) for a in artifacts)
    total_claims = sum(int(a["claim_count"]) for a in artifacts)
    hard_claims = sum(int(a["hard_claim_count"]) for a in artifacts)
    hard_unresolved = sum(int(a["hard_unresolved_count"]) for a in artifacts)
    advisory = sum(int(a["advisory_count"]) for a in artifacts)
    checkout_success = sum(1 for c in checkout_records if c["checkout_status"] == "checked_out")
    blocked = len(checkout_records) - checkout_success
    reasons: Counter[str] = Counter()
    claim_types: Counter[str] = Counter()
    for artifact in artifacts:
        reasons.update(dict(artifact.get("top_reasons", [])))
        claim_types.update(artifact.get("claim_types", {}))
    density = round(total_claims / total_lines * 100, 2) if total_lines else 0.0
    hard_unresolved_rate = round(hard_unresolved / hard_claims, 4) if hard_claims else 0.0
    advisory_rate = round(advisory / total_claims, 4) if total_claims else 0.0
    if checkout_success < MIN_TARGETS:
        status = "blocked_checkout_unavailable"
    elif hard_unresolved_rate <= 0.25 and advisory_rate <= 0.75:
        status = "real_checkout_useful"
    else:
        status = "real_checkout_noisy"
    return {
        "schema_version": SCHEMA,
        "policy_version": POLICY_VERSION,
        "status": status,
        "target": "selected external public PR bodies checked against real local public PR-head checkouts",
        "artifact_count": len(artifacts),
        "required_checkout_success_count": MIN_TARGETS,
        "checkout_success_count": checkout_success,
        "checkout_blocked_count": blocked,
        "total_lines": total_lines,
        "checkable_claim_count": total_claims,
        "hard_claim_count": hard_claims,
        "hard_unresolved_count": hard_unresolved,
        "advisory_count": advisory,
        "checkable_claims_per_100_lines": density,
        "hard_unresolved_rate": hard_unresolved_rate,
        "advisory_rate": advisory_rate,
        "root_mode": "real_public_checkout_pr_head",
        "top_reasons": [{"reason": k, "count": v} for k, v in reasons.most_common(10)],
        "top_claim_types": [{"type": k, "count": v} for k, v in claim_types.most_common(10)],
        "checkout_records": checkout_records,
        "artifacts": [
            {k: v for k, v in artifact.items() if k != "findings"}
            for artifact in artifacts
        ],
        "notes": [
            "Report mode only; no outreach, adoption, GitHub API, token, model, or private repo.",
            "Public repo checkouts are temporary local-only storage and are not committed.",
            "Committed outputs omit raw resolver receipts, raw external file contents, and raw line text.",
            "Resolver facts only; not correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.",
        ],
    }


def write_summary_markdown(summary: dict[str, Any]) -> None:
    lines = [
        "# Real-Checkout Learning Summary",
        "",
        f"Status: `{summary['status']}`.",
        "",
        "This report-mode loop checks selected saved public PR bodies against temporary local checkouts of their public PR heads. It does not contact maintainers, open PRs/comments, use GitHub APIs/tokens, call models, or enforce anything.",
        "",
        "Committed output is aggregate only. Temporary checkouts and full resolver receipts are not committed.",
        "",
        "A finding means a reference or receipt did or did not resolve in the configured checkout. It does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.",
        "",
        "## Aggregate",
        "",
        f"- Schema: `{summary['schema_version']}`",
        f"- Policy: `{summary['policy_version']}`",
        f"- Artifacts: {summary['artifact_count']}",
        f"- Checkout success: {summary['checkout_success_count']}",
        f"- Checkout blocked: {summary['checkout_blocked_count']}",
        f"- Checkable claims: {summary['checkable_claim_count']}",
        f"- Claims per 100 lines: {summary['checkable_claims_per_100_lines']}",
        f"- Hard unresolved rate: {summary['hard_unresolved_rate']:.1%}",
        f"- Advisory rate: {summary['advisory_rate']:.1%}",
        "",
        "## Top Reasons",
        "",
    ]
    if summary["top_reasons"]:
        for item in summary["top_reasons"]:
            lines.append(f"- {item['reason']}: {item['count']}")
    else:
        lines.append("- None.")
    lines.extend(["", "## Targets", ""])
    for record in summary["checkout_records"]:
        lines.append(
            f"- {record['id']}: {record['target']} ({record['checkout_status']}, "
            f"head `{record.get('head', '')[:12] or 'unavailable'}`)"
        )
    SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_comparison(summary: dict[str, Any]) -> dict[str, Any]:
    expanded = read_json(EXPANDED_SUMMARY)
    selected_empty = [
        artifact for artifact in expanded.get("artifacts", [])
        if artifact.get("id") in SELECTED_TARGET_IDS
    ]
    empty_claims = sum(int(a.get("claim_count", 0)) for a in selected_empty)
    empty_hard = sum(int(a.get("hard_claim_count", 0)) for a in selected_empty)
    empty_fail = sum(int(a.get("hard_unresolved_count", 0)) for a in selected_empty)
    empty_adv = sum(int(a.get("advisory_count", 0)) for a in selected_empty)
    empty_lines = sum(int(a.get("line_count", 0)) for a in selected_empty)
    return {
        "schema_version": COMPARISON_SCHEMA,
        "policy_version": POLICY_VERSION,
        "status": "dry_run_not_adoption",
        "selected_target_count": len(SELECTED_TARGET_IDS),
        "empty_root_subset": {
            "root_mode": "empty_public_fixture_root_unavailable",
            "artifact_count": len(selected_empty),
            "checkable_claim_count": empty_claims,
            "checkable_claims_per_100_lines": round(empty_claims / empty_lines * 100, 2) if empty_lines else 0.0,
            "hard_unresolved_rate": round(empty_fail / empty_hard, 4) if empty_hard else 0.0,
            "advisory_rate": round(empty_adv / empty_claims, 4) if empty_claims else 0.0,
        },
        "real_checkout_subset": {
            "root_mode": summary["root_mode"],
            "artifact_count": summary["artifact_count"],
            "checkout_success_count": summary["checkout_success_count"],
            "checkable_claim_count": summary["checkable_claim_count"],
            "checkable_claims_per_100_lines": summary["checkable_claims_per_100_lines"],
            "hard_unresolved_rate": summary["hard_unresolved_rate"],
            "advisory_rate": summary["advisory_rate"],
            "status": summary["status"],
        },
        "interpretation": "Real checkouts test whether empty-root hard failures remain unresolved when the target repo tree is available.",
    }


def write_comparison_markdown(data: dict[str, Any]) -> None:
    empty = data["empty_root_subset"]
    real = data["real_checkout_subset"]
    lines = [
        "# Real-Checkout Comparison",
        "",
        f"- Schema: `{data['schema_version']}`",
        f"- Status: `{data['status']}`",
        "",
        "| Mode | Artifacts | Claims | Claims/100 lines | Hard unresolved | Advisory |",
        "| --- | ---: | ---: | ---: | ---: | ---: |",
        f"| Empty root subset | {empty['artifact_count']} | {empty['checkable_claim_count']} | {empty['checkable_claims_per_100_lines']} | {empty['hard_unresolved_rate']:.1%} | {empty['advisory_rate']:.1%} |",
        f"| Real checkout subset | {real['artifact_count']} | {real['checkable_claim_count']} | {real['checkable_claims_per_100_lines']} | {real['hard_unresolved_rate']:.1%} | {real['advisory_rate']:.1%} |",
        "",
        f"Interpretation: {data['interpretation']}",
    ]
    COMPARISON_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def label_for_finding(finding: dict[str, Any]) -> tuple[str, str]:
    reason = str(finding.get("normalized_reason", ""))
    status = str(finding.get("status", ""))
    if status == "blocked":
        return "excluded", "Checkout unavailable; excluded from usefulness rates."
    if reason == "issue refs advisory without registry":
        return "unclear", "Offline issue refs need a supplied issue registry before maintainer actionability."
    if reason == "commit refs advisory under local-git resolution":
        return "non_actionable", "Commit advisory means the checker resolved only local-git existence, not maintainer action."
    if status == "fail" and reason in {"file refs that do not resolve", "test refs that do not resolve"}:
        return "actionable", "A root-backed unresolved file/test reference is a concrete receipt-resolution finding."
    return "unclear", "Aggregate evidence is insufficient for a stronger actionability label."


def build_actionability(artifacts: list[dict[str, Any]]) -> dict[str, Any]:
    labels: list[dict[str, Any]] = []
    for artifact in artifacts:
        for idx, finding in enumerate(artifact.get("findings", []), start=1):
            label, reason = label_for_finding(finding)
            labels.append({
                "finding_id": f"{artifact['id']}:{idx}",
                "target_id": artifact["id"],
                "claim_type": finding["claim_type"],
                "status": finding["status"],
                "line": finding.get("line"),
                "normalized_reason": finding["normalized_reason"],
                "ref_shape": finding["ref_shape"],
                "label": label,
                "reason": reason,
                "evidence_scope": "real_checkout_aggregate_finding",
            })
    counts = Counter(item["label"] for item in labels)
    non_excluded = max(1, len(labels) - counts["excluded"])
    actionable_rate = round(counts["actionable"] / non_excluded, 4)
    non_actionable_rate = round(counts["non_actionable"] / non_excluded, 4)
    useful = (
        "PASS" if labels and actionable_rate >= 0.20 and non_actionable_rate <= 0.50
        else "FAIL"
    )
    return {
        "schema_version": ACTIONABILITY_SCHEMA,
        "policy_version": POLICY_VERSION,
        "allowed_labels": sorted(ALLOWED_LABELS),
        "label_scope": "every real-root finding; raw line text omitted",
        "summary": {
            "total_labeled_findings": len(labels),
            "actionable_count": counts["actionable"],
            "non_actionable_count": counts["non_actionable"],
            "unclear_count": counts["unclear"],
            "excluded_count": counts["excluded"],
            "actionable_rate": actionable_rate if labels else 0.0,
            "non_actionable_rate": non_actionable_rate if labels else 0.0,
            "excluded_rate": round(counts["excluded"] / len(labels), 4) if labels else 0.0,
            "useful_findings_status": useful,
        },
        "labels": labels,
        "notes": [
            "Labels are reviewer triage over resolver findings, not semantic correctness/relevance judgments.",
            "Raw line text and full resolver receipts are omitted.",
        ],
    }


def write_actionability_markdown(data: dict[str, Any]) -> None:
    summary = data["summary"]
    counts = Counter(item["label"] for item in data["labels"])
    reasons = Counter(item["normalized_reason"] for item in data["labels"])
    lines = [
        "# Real-Checkout Actionability Labels",
        "",
        f"- Schema: `{data['schema_version']}`",
        f"- Label scope: {data['label_scope']}",
        f"- Total findings: {summary['total_labeled_findings']}",
        f"- Actionable: {summary['actionable_count']} ({summary['actionable_rate']:.1%} over non-excluded)",
        f"- Non-actionable: {summary['non_actionable_count']} ({summary['non_actionable_rate']:.1%} over non-excluded)",
        f"- Unclear: {summary['unclear_count']}",
        f"- Excluded: {summary['excluded_count']}",
        f"- Useful findings status: `{summary['useful_findings_status']}`",
        "",
        "Raw line text and full resolver receipts are omitted. Labels are reviewer triage over deterministic reference/receipt findings only.",
        "",
        "## Label Counts",
        "",
    ]
    for label, count in sorted(counts.items()):
        lines.append(f"- {label}: {count}")
    lines.extend(["", "## Top Reasons", ""])
    for reason, count in reasons.most_common(10):
        lines.append(f"- {reason}: {count}")
    ACTIONABILITY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def run_real_checkout() -> dict[str, Any]:
    targets = selected_targets()
    write_targets(targets)
    artifacts: list[dict[str, Any]] = []
    checkout_records: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory(prefix="anti-slop-real-checkouts-") as tmp:
        tmp_path = Path(tmp)
        checkout_parent = tmp_path / "checkouts"
        checkout_parent.mkdir()
        for target in targets:
            checkout, status, head, error = checkout_target(target, checkout_parent)
            checkout_records.append({
                "id": target["id"],
                "target": target["target"],
                "repo": target["repo"],
                "checkout_status": status,
                "checkout_ref": target["checkout_ref"],
                "head": head,
                "blocked_reason": "public git checkout unavailable" if error else "",
            })
            if checkout is None:
                artifacts.append(blocked_artifact(target, status, "public git checkout unavailable"))
                continue
            artifacts.append(run_pr_event(target, checkout, tmp_path))
    summary = summarize(artifacts, checkout_records)
    write_json(SUMMARY_JSON, summary)
    write_summary_markdown(summary)
    comparison = build_comparison(summary)
    write_json(COMPARISON_JSON, comparison)
    write_comparison_markdown(comparison)
    actionability = build_actionability(artifacts)
    write_json(ACTIONABILITY_JSON, actionability)
    write_actionability_markdown(actionability)
    return summary


def validate_targets(errors: list[str]) -> None:
    if not TARGETS_JSON.is_file():
        errors.append(f"missing real-checkout targets: {rel(TARGETS_JSON)}")
        return
    data = read_json(TARGETS_JSON)
    if data.get("schema_version") != TARGET_SCHEMA:
        errors.append(f"real-checkout target schema mismatch: {data.get('schema_version')}")
    targets = data.get("targets", [])
    if len(targets) < MIN_TARGETS:
        errors.append(f"expected at least {MIN_TARGETS} real-checkout targets, found {len(targets)}")
    for target in targets:
        for key in ("id", "target", "repo", "artifact_path", "origin_url", "checkout_url", "checkout_ref", "reviewed_public_safe"):
            if key not in target:
                errors.append(f"real-checkout target missing {key}: {target}")
        if target.get("reviewed_public_safe") is not True:
            errors.append(f"real-checkout target not public-safe reviewed: {target.get('id')}")
        if "github.com/" not in str(target.get("checkout_url", "")):
            errors.append(f"real-checkout target checkout_url must be public GitHub git URL: {target.get('id')}")
        artifact = ROOT / str(target.get("artifact_path", ""))
        if not artifact.is_file():
            errors.append(f"real-checkout artifact missing: {rel(artifact)}")


def validate_json(path: Path, schema: str, errors: list[str]) -> dict[str, Any] | None:
    if not path.is_file():
        errors.append(f"missing real-checkout artifact: {rel(path)}")
        return None
    data = read_json(path)
    if data.get("schema_version") != schema:
        errors.append(f"{rel(path)} schema mismatch: {data.get('schema_version')}")
    text = json.dumps(data, sort_keys=True)
    for forbidden in (str(ROOT), "/Users/", "/private/var/", "GITHUB_TOKEN", "OPENAI_API_KEY", "ANTHROPIC_API_KEY"):
        if forbidden in text:
            errors.append(f"{rel(path)} contains forbidden private/token-like snippet: {forbidden}")
    return data


def validate_outputs(errors: list[str]) -> None:
    validate_targets(errors)
    summary = validate_json(SUMMARY_JSON, SCHEMA, errors)
    validate_json(COMPARISON_JSON, COMPARISON_SCHEMA, errors)
    actionability = validate_json(ACTIONABILITY_JSON, ACTIONABILITY_SCHEMA, errors)
    for path in (SUMMARY_MD, COMPARISON_MD, ACTIONABILITY_MD):
        if not path.is_file():
            errors.append(f"missing real-checkout Markdown artifact: {rel(path)}")
        else:
            text = path.read_text(encoding="utf-8")
            if "/Users/" in text or "/private/var/" in text:
                errors.append(f"{rel(path)} contains private local path")
    if summary:
        if summary.get("status") not in {"real_checkout_useful", "real_checkout_noisy", "blocked_checkout_unavailable"}:
            errors.append(f"invalid real-checkout status: {summary.get('status')}")
        if int(summary.get("artifact_count", 0)) < MIN_TARGETS:
            errors.append(f"real-checkout artifact_count below {MIN_TARGETS}")
        if int(summary.get("checkout_success_count", 0)) < MIN_TARGETS and summary.get("status") != "blocked_checkout_unavailable":
            errors.append("real-checkout status must be blocked when fewer than 3 checkouts succeed")
    if actionability:
        labels = actionability.get("labels", [])
        allowed = set(actionability.get("allowed_labels", []))
        if allowed != ALLOWED_LABELS:
            errors.append(f"real-checkout actionability allowed_labels mismatch: {sorted(allowed)}")
        if not labels:
            errors.append("real-checkout actionability labels are empty")
        seen = {item.get("label") for item in labels}
        if not seen <= ALLOWED_LABELS:
            errors.append(f"unknown real-checkout labels: {sorted(seen - ALLOWED_LABELS)}")
        for item in labels:
            for key in ("finding_id", "target_id", "claim_type", "status", "normalized_reason", "label", "reason", "evidence_scope"):
                if key not in item:
                    errors.append(f"real-checkout label missing {key}: {item}")
            if item.get("evidence_scope") != "real_checkout_aggregate_finding":
                errors.append(f"invalid real-checkout evidence_scope: {item}")
        if summary and int(actionability.get("summary", {}).get("total_labeled_findings", -1)) != (
            int(summary.get("hard_unresolved_count", 0)) + int(summary.get("advisory_count", 0))
        ):
            errors.append("real-checkout labels must cover every hard failure/advisory finding")


def validate_policy_doc(errors: list[str]) -> None:
    if not POLICY_DOC.is_file():
        errors.append(f"missing policy doc: {rel(POLICY_DOC)}")
        return
    text = POLICY_DOC.read_text(encoding="utf-8")
    for snippet in (
        "real local checkout",
        SCHEMA,
        ACTIONABILITY_SCHEMA,
        "temporary local-only directories",
        "no-contact/no-outreach",
    ):
        if snippet not in text:
            errors.append(f"{rel(POLICY_DOC)} missing snippet: {snippet}")


def compatibility_errors(include_actionability: bool = True) -> list[str]:
    errors: list[str] = []
    validate_policy_doc(errors)
    validate_outputs(errors)
    if not include_actionability and ACTIONABILITY_JSON.is_file():
        return errors
    return errors


def self_test() -> int:
    pre_errors: list[str] = []
    validate_policy_doc(pre_errors)
    if pre_errors:
        print("REAL CHECKOUT LEARNING FAILED:")
        for error in pre_errors:
            print(f"  - {error}")
        return 1
    summary = run_real_checkout()
    errors = compatibility_errors(include_actionability=True)
    if errors:
        print("REAL CHECKOUT LEARNING FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(
        "REAL CHECKOUT LEARNING PASSED: "
        f"{summary['checkout_success_count']} checkouts, "
        f"{summary['checkable_claim_count']} claims, "
        f"hard_unresolved={summary['hard_unresolved_rate']:.1%}, "
        f"advisory={summary['advisory_rate']:.1%}, "
        f"status={summary['status']}."
    )
    return 0


def check_only() -> int:
    errors = compatibility_errors(include_actionability=True)
    if errors:
        print("REAL CHECKOUT COMPAT FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"REAL CHECKOUT COMPAT PASSED: {SCHEMA}, comparison, and actionability artifacts are valid.")
    return 0


def check_actionability() -> int:
    errors: list[str] = []
    validate_json(ACTIONABILITY_JSON, ACTIONABILITY_SCHEMA, errors)
    if ACTIONABILITY_JSON.is_file():
        actionability = read_json(ACTIONABILITY_JSON)
        if not actionability.get("labels"):
            errors.append("real-checkout actionability labels are empty")
        if actionability.get("summary", {}).get("total_labeled_findings", 0) < 1:
            errors.append("real-checkout actionability must label at least one finding")
    if errors:
        print("REAL CHECKOUT ACTIONABILITY CHECK FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"REAL CHECKOUT ACTIONABILITY CHECK PASSED: {ACTIONABILITY_SCHEMA} labels are valid.")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--check-actionability", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.check:
        return check_only()
    if args.check_actionability:
        return check_actionability()
    if args.self_test:
        return self_test()
    summary = run_real_checkout()
    print(f"real-checkout learning wrote {rel(SUMMARY_JSON)} ({summary['status']})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
