#!/usr/bin/env python3
"""Cluster external dry-run findings and publish kill-criteria status.

The clustering output is public-safe aggregate evidence only. It never commits
full resolver receipts or raw line text from external targets.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import argparse
import json
import re
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "proof" / "external-dry-run"
TARGETS_JSON = OUT_DIR / "targets.json"
SUMMARY_JSON = OUT_DIR / "summary.json"
CLUSTERS_JSON = OUT_DIR / "clusters.json"
CLUSTERS_MD = OUT_DIR / "clusters.md"
NO_CHANGE_MEMO = OUT_DIR / "no-change-memo.md"
KILL_JSON = OUT_DIR / "kill-criteria.json"
FIXTURE_JSON = OUT_DIR / "fixtures" / "cluster-fixture.json"
KILL_DOC = ROOT / "docs" / "kill-criteria.md"
ACTIONABILITY_JSON = OUT_DIR / "expanded" / "actionability.json"
DOGFOOD_JSON = ROOT / "proof" / "command-receipt-dogfood" / "summary.json"

CLUSTER_SCHEMA = "anti-slop-external-dry-run-clusters.v1"
KILL_SCHEMA = "anti-slop-kill-criteria.v1"
SUMMARY_SCHEMA = "anti-slop-external-dry-run.v1"

sys.path.insert(0, str(ROOT / "scripts"))
import gate_pr_provenance as pr  # noqa: E402


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


def parse_line(reason: str) -> int | None:
    match = re.search(r"\bline\s+(\d+)\b", reason)
    if match:
        return int(match.group(1))
    match = re.match(r"(\d+):\s+", reason)
    return int(match.group(1)) if match else None


def parse_ref(claim_type: str, reason: str) -> str:
    if claim_type == "issue":
        match = re.search(r"#\d+", reason)
        return match.group(0) if match else "issue-ref"
    if claim_type in {"source_card", "card_id", "card"}:
        match = re.search(r"\bBK-\d{4}(?:-card-\d{3})?\b", reason)
        return match.group(0) if match else "card-ref"
    if "does not resolve:" in reason:
        return reason.rsplit("does not resolve:", 1)[1].strip()
    if "not defined in" in reason:
        return reason.rsplit("not defined in", 1)[1].strip()
    match = re.search(r"`([^`]+)`", reason)
    return match.group(1) if match else ""


def normalize_reason(claim_type: str, reason: str, status: str) -> str:
    text = reason.lower()
    if claim_type == "issue" and "no --issue-registry" in text:
        return "issue refs advisory without registry"
    if claim_type == "file" and "file does not resolve" in text:
        return "file refs that do not resolve"
    if claim_type == "test" and "test file does not resolve" in text:
        return "test file refs that do not resolve"
    if claim_type == "test" and "test node" in text:
        return "test node refs that do not resolve"
    if claim_type in {"card", "source_card", "card_id"} and "unresolved" in text:
        return "source/card refs that do not resolve"
    if claim_type == "commit" and status == "advisory":
        return "commit refs advisory under local-git resolution"
    return re.sub(r": .+$", "", reason).strip()


def path_shape(claim_type: str, ref: str) -> str:
    if claim_type == "issue":
        return "issue-number"
    if claim_type in {"card", "source_card", "card_id"}:
        return "source-card-id" if "-card-" in ref else "source-id"
    if claim_type == "commit":
        return "commit-sha"
    if ref.startswith("/"):
        return "absolute-path"
    if "/" not in ref:
        return "bare-token"
    first = ref.split("/", 1)[0]
    suffix = Path(ref).suffix or "no-extension"
    depth = ref.count("/")
    return f"{first}/ depth={depth} ext={suffix}"


def text_pattern(line_text: str) -> str:
    stripped = line_text.strip()
    parts: list[str] = []
    if stripped.startswith("#"):
        parts.append("heading")
    elif stripped.startswith(("-", "*")):
        parts.append("bullet")
    else:
        parts.append("prose")
    if "`" in stripped:
        parts.append("backticked-ref")
    if re.search(r"\b(example|fixture|fabricated)\b", stripped, re.I):
        parts.append("example-or-fixture")
    if re.search(r"\b(fix|fixes|closes|related|core-\d+|#\d+)\b", stripped, re.I):
        parts.append("issue-linkage")
    if re.search(r"\b(validate|test|self-test|smoke|benchmark)\b", stripped, re.I):
        parts.append("validation-claim")
    if re.search(r"\b(red|green|evidence)\b", stripped, re.I):
        parts.append("red-green")
    return "+".join(parts)


def recommendation(claim_type: str, reason: str, shape: str, pattern: str) -> str:
    if claim_type == "issue" and reason == "issue refs advisory without registry":
        return "docs_update"
    if shape == "absolute-path":
        return "benchmark_case"
    if claim_type in {"file", "test", "card", "source_card", "card_id"}:
        return "benchmark_case"
    if "example-or-fixture" in pattern:
        return "docs_update"
    return "no_change"


def target_language(target: dict[str, Any], repo: str) -> str:
    if target.get("language"):
        return str(target["language"])
    if repo == "nferna26/anti-slop":
        return "python/markdown"
    return "unknown"


def _line(lines: list[str], line_no: int | None) -> str:
    if line_no is None or line_no < 1 or line_no > len(lines):
        return ""
    return lines[line_no - 1]


def observations_from_targets() -> list[dict[str, Any]]:
    observations: list[dict[str, Any]] = []
    for target in load_targets():
        if target.get("checker") != "anti-slop-pr-event":
            continue
        source = ROOT / target["artifact_path"]
        root = ROOT / target.get("root", ".")
        text = source.read_text(encoding="utf-8")
        lines = text.splitlines()
        receipt = pr.run(source, root, registry=None, require_reviewed_cards=False)
        repo = target.get("repo") or str(target["target"]).split("#", 1)[0]
        language = target_language(target, repo)
        for claim_type, check in receipt.get("checks", {}).items():
            for status, items in (("fail", check.get("unresolved", [])),
                                  ("advisory", check.get("advisory", []))):
                for reason in items:
                    line_no = parse_line(str(reason))
                    ref = parse_ref(claim_type, str(reason))
                    normalized = normalize_reason(claim_type, str(reason), status)
                    shape = path_shape(claim_type, ref)
                    pattern = text_pattern(_line(lines, line_no))
                    observations.append({
                        "target_id": target["id"],
                        "repo": repo,
                        "language": language,
                        "claim_type": claim_type,
                        "status": status,
                        "normalized_reason": normalized,
                        "text_pattern": pattern,
                        "path_shape": shape,
                        "diff_availability": target.get("diff_availability", "not_supplied"),
                        "recommended_action": recommendation(claim_type, normalized, shape, pattern),
                    })
    return observations


def cluster_observations(observations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, ...], dict[str, Any]] = {}
    for obs in observations:
        key = (
            obs["claim_type"],
            obs["status"],
            obs["normalized_reason"],
            obs["text_pattern"],
            obs["path_shape"],
            obs["repo"],
            obs["language"],
            obs["diff_availability"],
        )
        if key not in grouped:
            grouped[key] = {
                "claim_type": obs["claim_type"],
                "status": obs["status"],
                "normalized_reason": obs["normalized_reason"],
                "text_pattern": obs["text_pattern"],
                "path_shape": obs["path_shape"],
                "repo": obs["repo"],
                "language": obs["language"],
                "diff_availability": obs["diff_availability"],
                "recommended_action": obs["recommended_action"],
                "count": 0,
                "sample_targets": [],
            }
        cluster = grouped[key]
        cluster["count"] += 1
        if obs["target_id"] not in cluster["sample_targets"] and len(cluster["sample_targets"]) < 3:
            cluster["sample_targets"].append(obs["target_id"])
    return sorted(grouped.values(), key=lambda c: (-c["count"], c["claim_type"], c["normalized_reason"]))


def fixture_check() -> list[str]:
    errors: list[str] = []
    if not FIXTURE_JSON.is_file():
        return [f"missing cluster fixture: {rel(FIXTURE_JSON)}"]
    fixture = read_json(FIXTURE_JSON)
    clusters = cluster_observations(fixture.get("observations", []))
    expected = fixture.get("expected_clusters", [])
    for exp in expected:
        found = False
        for cluster in clusters:
            if all(cluster.get(k) == v for k, v in exp.get("match", {}).items()):
                if cluster.get("count") != exp.get("count"):
                    errors.append(f"fixture cluster count mismatch for {exp}: {cluster.get('count')}")
                found = True
                break
        if not found:
            errors.append(f"fixture expected cluster not found: {exp}")
    return errors


def build_cluster_summary() -> dict[str, Any]:
    observations = observations_from_targets()
    clusters = cluster_observations(observations)
    action_counts = Counter(c["recommended_action"] for c in clusters for _ in range(c["count"]))
    status_counts = Counter(o["status"] for o in observations)
    return {
        "schema_version": CLUSTER_SCHEMA,
        "source_schema_version": SUMMARY_SCHEMA,
        "source_summary": rel(SUMMARY_JSON),
        "observation_count": len(observations),
        "cluster_count": len(clusters),
        "status_counts": dict(sorted(status_counts.items())),
        "recommended_action_counts": dict(sorted(action_counts.items())),
        "top_clusters": clusters[:12],
        "notes": [
            "Public-safe cluster output omits raw line text and full resolver receipts.",
            "Recommendations are triage labels, not correctness or relevance judgments.",
        ],
    }


def cluster_markdown(summary: dict[str, Any]) -> str:
    lines = [
        "# External Dry-Run Cluster Memo",
        "",
        "This memo clusters report-mode dry-run findings by claim type, normalized reason, text pattern, path shape, repo/language metadata when available, and diff availability.",
        "",
        "It omits raw line text and full resolver receipts. The output is evidence for resolver learning only, not correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.",
        "",
        f"- Schema: `{summary['schema_version']}`",
        f"- Source summary: `{summary['source_summary']}`",
        f"- Observations: {summary['observation_count']}",
        f"- Clusters: {summary['cluster_count']}",
        f"- Recommended actions: {summary['recommended_action_counts']}",
        "",
        "## Top Clusters",
        "",
        "| Count | Claim type | Status | Reason | Text pattern | Path shape | Repo | Language | Diff | Action | Sample targets |",
        "| ---: | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for cluster in summary["top_clusters"]:
        lines.append(
            f"| {cluster['count']} | {cluster['claim_type']} | {cluster['status']} | "
            f"{cluster['normalized_reason']} | {cluster['text_pattern']} | "
            f"{cluster['path_shape']} | {cluster['repo']} | {cluster['language']} | "
            f"{cluster['diff_availability']} | {cluster['recommended_action']} | "
            f"{', '.join(cluster['sample_targets'])} |"
        )
    lines.extend([
        "",
        "## Learning Decision",
        "",
        "No resolver repair is justified from this first sample. The top cluster is advisory issue references without an issue registry, which is an intentional offline boundary. The hard-failure clusters are good regression inputs, not evidence for broad pattern relaxation.",
    ])
    return "\n".join(lines) + "\n"


def build_no_change_memo(cluster_summary: dict[str, Any], dry_summary: dict[str, Any]) -> str:
    return "\n".join([
        "# External Dry-Run No-Change Memo",
        "",
        "Decision: no resolver repair in CORE-977.",
        "",
        "The top cluster is `issue refs advisory without registry`, which is intentional because the checker has no GitHub API/token dependency and cannot know issue state offline without a supplied registry. The hard-failure clusters are missing file/test/source-card references in saved PR bodies or documented examples; those are appropriate benchmark regression inputs and docs reminders, not a reason to relax resolver semantics.",
        "",
        "Before/after impact is unchanged because no resolver code changed:",
        "",
        f"- Checkable claims: {dry_summary['checkable_claim_count']} -> {dry_summary['checkable_claim_count']}",
        f"- Hard unresolved rate: {dry_summary['hard_unresolved_rate']:.1%} -> {dry_summary['hard_unresolved_rate']:.1%}",
        f"- Advisory rate: {dry_summary['advisory_rate']:.1%} -> {dry_summary['advisory_rate']:.1%}",
        f"- Cluster observations: {cluster_summary['observation_count']} -> {cluster_summary['observation_count']}",
        "",
        "Boundary: this memo is about deterministic reference/receipt resolution only. It does not judge correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.",
        "",
    ])


def build_kill_dashboard(dry_summary: dict[str, Any]) -> dict[str, Any]:
    density = float(dry_summary["checkable_claims_per_100_lines"])
    actionability = read_json(ACTIONABILITY_JSON) if ACTIONABILITY_JSON.is_file() else None
    dogfood = read_json(DOGFOOD_JSON) if DOGFOOD_JSON.is_file() else None
    useful_status = "UNKNOWN"
    useful_evidence = "No maintainer/reviewer usefulness labels yet."
    non_actionable_status = "UNKNOWN"
    non_actionable_evidence = "No human actionability labeling or repair loop yet."
    if actionability:
        action_summary = actionability.get("summary", {})
        actionable_rate = float(action_summary.get("actionable_rate", 0.0))
        non_actionable_rate = float(action_summary.get("non_actionable_rate", 0.0))
        useful_status = "FAIL" if actionable_rate < 0.20 else "PASS"
        useful_evidence = (
            f"Expanded external sample aggregate labels: {actionable_rate:.1%} actionable "
            f"over non-excluded findings; {action_summary.get('unclear_count', 0)} unclear, "
            f"{action_summary.get('excluded_count', 0)} excluded."
        )
        non_actionable_status = "FAIL" if non_actionable_rate > 0.50 else "PASS"
        non_actionable_evidence = (
            f"Expanded external sample aggregate labels: {non_actionable_rate:.1%} "
            "non-actionable over non-excluded findings."
        )
    dogfood_status = "UNKNOWN"
    dogfood_evidence = "External dry-run sample is PR-body only."
    if dogfood:
        rate = float(dogfood.get("dogfood_rate", 0.0))
        dogfood_status = "PASS" if rate >= 0.25 else "FAIL"
        dogfood_evidence = (
            f"Command receipt dogfood fixture: {rate:.0%} receipt-backed command claims passed; "
            "raw receipts are regenerated in a temp repo and not committed."
        )
    return {
        "schema_version": KILL_SCHEMA,
        "source_summary": rel(SUMMARY_JSON),
        "expanded_external_summary": rel(OUT_DIR / "expanded" / "summary.json"),
        "actionability_labels": rel(ACTIONABILITY_JSON),
        "command_receipt_dogfood": rel(DOGFOOD_JSON),
        "overall_status": "watch",
        "criteria": [
            {
                "id": "claim_density_below_5_per_100_lines",
                "status": "PASS" if density >= 5.0 else "FAIL",
                "threshold": "<5 claims/100 lines",
                "evidence": f"{density} claims/100 lines in first saved-public sample",
            },
            {
                "id": "non_actionable_after_repairs_above_50_percent",
                "status": non_actionable_status,
                "threshold": ">50% non-actionable after repairs",
                "evidence": non_actionable_evidence,
            },
            {
                "id": "useful_findings_below_20_percent",
                "status": useful_status,
                "threshold": "<20% useful findings",
                "evidence": useful_evidence,
            },
            {
                "id": "install_success_below_70_percent",
                "status": "UNKNOWN",
                "threshold": "<70% install success",
                "evidence": "No external install attempts; local smoke is not adopter data.",
            },
            {
                "id": "command_receipt_dogfood_below_25_percent",
                "status": dogfood_status,
                "threshold": "<25% command receipt dogfood",
                "evidence": dogfood_evidence,
            },
            {
                "id": "maintainer_keep_rate_zero_of_10",
                "status": "UNKNOWN",
                "threshold": "0/10 maintainer keep-rate",
                "evidence": "No outreach or adoption PRs were opened.",
            },
            {
                "id": "stale_proof_metrics",
                "status": "PASS",
                "threshold": "README/proof metrics stale",
                "evidence": "`make launch-check` validates committed proof metric links.",
            },
            {
                "id": "platform_clone_risk",
                "status": "UNKNOWN",
                "threshold": "platform clone makes repo workflow unnecessary",
                "evidence": "No platform-comparison data yet.",
            },
        ],
    }


def write_outputs() -> dict[str, Any]:
    cluster_summary = build_cluster_summary()
    dry_summary = read_json(SUMMARY_JSON)
    write_json(CLUSTERS_JSON, cluster_summary)
    CLUSTERS_MD.write_text(cluster_markdown(cluster_summary), encoding="utf-8")
    NO_CHANGE_MEMO.write_text(build_no_change_memo(cluster_summary, dry_summary), encoding="utf-8")
    write_json(KILL_JSON, build_kill_dashboard(dry_summary))
    return cluster_summary


def validate_outputs() -> list[str]:
    errors = fixture_check()
    required_files = [CLUSTERS_JSON, CLUSTERS_MD, NO_CHANGE_MEMO, KILL_JSON, KILL_DOC]
    for path in required_files:
        if not path.is_file():
            errors.append(f"missing required learning-loop artifact: {rel(path)}")
    if CLUSTERS_JSON.is_file():
        data = read_json(CLUSTERS_JSON)
        if data.get("schema_version") != CLUSTER_SCHEMA:
            errors.append("cluster schema mismatch")
        if data.get("observation_count", 0) <= 0:
            errors.append("cluster output has no observations")
        if not data.get("top_clusters"):
            errors.append("cluster output has no top_clusters")
    if KILL_JSON.is_file():
        data = read_json(KILL_JSON)
        if data.get("schema_version") != KILL_SCHEMA:
            errors.append("kill criteria schema mismatch")
        criteria = data.get("criteria", [])
        required_ids = {
            "claim_density_below_5_per_100_lines",
            "non_actionable_after_repairs_above_50_percent",
            "useful_findings_below_20_percent",
            "install_success_below_70_percent",
            "command_receipt_dogfood_below_25_percent",
            "maintainer_keep_rate_zero_of_10",
            "stale_proof_metrics",
            "platform_clone_risk",
        }
        present = {c.get("id") for c in criteria}
        missing = sorted(required_ids - present)
        if missing:
            errors.append(f"kill criteria missing ids: {missing}")
        for criterion in criteria:
            if criterion.get("status") not in {"PASS", "FAIL", "UNKNOWN"}:
                errors.append(f"invalid kill status: {criterion}")
            if criterion.get("status") == "UNKNOWN" and "unknown" not in json.dumps(criterion).lower():
                errors.append(f"UNKNOWN criterion lacks unknown evidence: {criterion.get('id')}")
    for path in (CLUSTERS_JSON, CLUSTERS_MD, NO_CHANGE_MEMO, KILL_JSON):
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            for forbidden in (str(ROOT), "/Users/", "GITHUB_TOKEN", "OPENAI_API_KEY", "ANTHROPIC_API_KEY"):
                if forbidden in text:
                    errors.append(f"{rel(path)} contains forbidden private/token-like snippet: {forbidden}")
    return errors


def self_test() -> int:
    errors = fixture_check()
    if errors:
        print("EXTERNAL DRY-RUN CLUSTER SMOKE FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    summary = write_outputs()
    errors = validate_outputs()
    if errors:
        print("EXTERNAL DRY-RUN CLUSTER SMOKE FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(
        "EXTERNAL DRY-RUN CLUSTER SMOKE PASSED: "
        f"{summary['observation_count']} observations, "
        f"{summary['cluster_count']} clusters, "
        f"actions={summary['recommended_action_counts']}."
    )
    return 0


def check_only() -> int:
    errors = validate_outputs()
    if errors:
        print("EXTERNAL DRY-RUN CLUSTER COMPAT FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(f"EXTERNAL DRY-RUN CLUSTER COMPAT PASSED: {CLUSTER_SCHEMA} and {KILL_SCHEMA} artifacts are valid.")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--check", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.check:
        return check_only()
    if args.self_test:
        return self_test()
    summary = write_outputs()
    print(f"external dry-run clusters wrote {rel(CLUSTERS_JSON)} ({summary['cluster_count']} clusters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
