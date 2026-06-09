#!/usr/bin/env python3
"""Mine public PR bodies for mechanically checkable receipt/reference claims.

Live mode fetches public merged PR metadata with ``gh``, checks selected PR
bodies in report mode against temporary public checkouts, and commits only
aggregate public-safe summaries. It does not contact maintainers, post comments,
open PRs/issues, run target project tests/builds, call models, or enforce.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import argparse
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "proof" / "public-pr-receipt-study"
TARGETS_JSON = OUT_DIR / "targets.json"
SUMMARY_JSON = OUT_DIR / "summary.json"
SUMMARY_MD = OUT_DIR / "summary.md"
ACTIONABILITY_JSON = OUT_DIR / "actionability.json"
ACTIONABILITY_MD = OUT_DIR / "actionability.md"
DOC = ROOT / "docs" / "public-pr-receipt-study.md"

TARGET_SCHEMA = "anti-slop-public-pr-receipt-targets.v1"
SUMMARY_SCHEMA = "anti-slop-public-pr-receipt-study.v1"
ACTIONABILITY_SCHEMA = "anti-slop-public-pr-actionability.v1"
POLICY_VERSION = "public-pr-receipt-study-policy.v1"

MIN_MANIFEST_REPOS = 15
MAX_MANIFEST_REPOS = 30
MIN_SAMPLE_ARTIFACTS = 50
MIN_SAMPLE_REPOS = 10
DEFAULT_FETCH_LIMIT = 20
DEFAULT_PER_REPO = 5

ALLOWED_LABELS = {"actionable", "non_actionable", "unclear", "excluded"}
GH_FIELDS = "number,title,body,mergedAt,headRefOid,baseRefName,url,mergeCommit"

KEYWORDS: list[tuple[str, int]] = [
    ("agent", 5),
    ("codex", 5),
    ("claude", 5),
    ("copilot", 4),
    ("generated", 3),
    ("automated", 2),
    ("ai", 2),
    ("receipt", 5),
    ("validation", 3),
    ("tests pass", 5),
    ("test passed", 5),
    ("pytest", 5),
    ("make ", 4),
    ("npm test", 4),
    ("pnpm test", 4),
    ("cargo test", 4),
    ("go test", 4),
    ("benchmark", 4),
    ("metric", 4),
    ("score", 2),
    ("updated", 1),
    ("added", 1),
    ("changed", 1),
    ("fixes #", 3),
]

CHECKABLE_RE = re.compile(
    r"([\w./-]+\.(?:md|py|js|ts|tsx|jsx|go|rs|yml|yaml|json|toml|sh|txt)"
    r"|tests?/[^\s`]+::[A-Za-z_]\w*|#\d+\b|`?make\s+[A-Za-z0-9_.:-]+`?\s+pass"
    r"|pytest\b.*\bpass|tests?\s+pass|score\s+(?:is|=)\s+-?\d+(?:\.\d+)?"
    r"|metric\s+improved\s+from\s+-?\d+(?:\.\d+)?\s+to\s+-?\d+(?:\.\d+)?)",
    re.IGNORECASE,
)


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


def run_cmd(cmd: list[str], cwd: Path | None = None, timeout: int = 120) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=str(cwd or ROOT), capture_output=True, text=True, timeout=timeout)


def slug(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "-", text.lower()).strip("-")


def artifact_id(repo: str, number: int) -> str:
    digest = hashlib.sha256(f"{repo}#{number}".encode("utf-8")).hexdigest()[:10]
    return f"{slug(repo)}-{digest}"


def body_line_count(body: str) -> int:
    return max(1, len(body.splitlines()))


def body_word_count(body: str) -> int:
    return len(re.findall(r"\b\w+\b", body))


def score_pr(title: str, body: str) -> tuple[int, list[str]]:
    text = f"{title}\n{body}".lower()
    score = 0
    hits: list[str] = []
    for keyword, weight in KEYWORDS:
        if keyword in text:
            score += weight
            hits.append(keyword.strip())
    if CHECKABLE_RE.search(body):
        score += 4
        hits.append("checkable-pattern")
    return score, sorted(set(hits))


def normalize_reason(reason: str, status: str = "") -> str:
    text = reason.lower()
    if "no --issue-registry" in text:
        return "issue refs advisory without registry"
    if "file does not resolve" in text:
        return "file refs unresolved"
    if "test node" in text or "test reference" in text or "test file does not resolve" in text:
        return "test refs unresolved"
    if "unresolved source_card" in text or "unresolved card_id" in text:
        return "source/card refs unresolved"
    if "commit" in text and status == "advisory":
        return "commit refs advisory under local-git resolution"
    if "missing command receipt" in text:
        return "command claims without receipts"
    if "missing metric receipt" in text:
        return "metric claims without receipts"
    if "metric receipt mismatch" in text:
        return "metric receipt mismatch"
    if "checkout unavailable" in text:
        return "checkout unavailable"
    return re.sub(r"^(?:unresolved|advisory)\s+", "", reason).strip()[:120]


def load_manifest() -> dict[str, Any]:
    return read_json(TARGETS_JSON)


def manifest_repos() -> list[dict[str, Any]]:
    data = load_manifest()
    repos = data.get("repositories", [])
    if not isinstance(repos, list):
        raise ValueError("targets.json repositories must be a list")
    return repos


def gh_pr_list(repo: str, limit: int) -> tuple[list[dict[str, Any]], str]:
    if not shutil.which("gh"):
        return [], "gh unavailable"
    proc = run_cmd([
        "gh",
        "pr",
        "list",
        "--repo",
        repo,
        "--state",
        "merged",
        "--limit",
        str(limit),
        "--json",
        GH_FIELDS,
    ], timeout=90)
    if proc.returncode != 0:
        return [], (proc.stderr or proc.stdout).strip()[:240] or "gh pr list failed"
    try:
        data = json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        return [], f"gh returned invalid JSON: {exc}"
    return [item for item in data if isinstance(item, dict)], ""


def select_public_prs(fetch_limit: int, per_repo: int, target_artifacts: int,
                      min_repos: int) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    selected: list[dict[str, Any]] = []
    fetch_records: list[dict[str, Any]] = []
    sparse_recent_candidates = 0
    for repo_cfg in manifest_repos():
        repo = str(repo_cfg["repo"])
        prs, error = gh_pr_list(repo, fetch_limit)
        if error:
            fetch_records.append({
                "repo": repo,
                "fetched": 0,
                "selected": 0,
                "status": "fetch_failed",
                "reason": error,
            })
            continue
        scored: list[dict[str, Any]] = []
        for pr_data in prs:
            body = str(pr_data.get("body") or "")
            title = str(pr_data.get("title") or "")
            score, hits = score_pr(title, body)
            if not body.strip() or body_word_count(body) < 25:
                sparse_recent_candidates += 1
            merge = pr_data.get("mergeCommit") or {}
            number = int(pr_data.get("number") or 0)
            scored.append({
                "repo": repo,
                "category": repo_cfg.get("category", ""),
                "number": number,
                "title": title,
                "body": body,
                "merged_at": pr_data.get("mergedAt") or "",
                "head_oid": pr_data.get("headRefOid") or "",
                "merge_oid": merge.get("oid") if isinstance(merge, dict) else "",
                "base_ref": pr_data.get("baseRefName") or "main",
                "url": pr_data.get("url") or "",
                "score": score,
                "filter_hits": hits,
                "selection_mode": "filter_match" if score > 0 else "fallback_recent_merged",
            })
        scored.sort(key=lambda item: (int(item["score"]), str(item["merged_at"])), reverse=True)
        primary = [item for item in scored if int(item["score"]) > 0 and item["body"].strip()]
        fallback = [item for item in scored if int(item["score"]) <= 0 and item["body"].strip()]
        chosen = primary[:per_repo]
        if len(chosen) < per_repo:
            chosen.extend(fallback[:per_repo - len(chosen)])
        selected.extend(chosen)
        fetch_records.append({
            "repo": repo,
            "fetched": len(prs),
            "selected": len(chosen),
            "status": "fetched",
            "filter_matches": len(primary),
            "fallback_selected": sum(1 for item in chosen if item["selection_mode"] == "fallback_recent_merged"),
        })
        if len(selected) >= target_artifacts and len({item["repo"] for item in selected}) >= min_repos:
            break
    return selected[:target_artifacts], {
        "fetch_records": fetch_records,
        "sparse_recent_candidates": sparse_recent_candidates,
    }


def clone_repo(repo: str, base_ref: str, checkout_parent: Path) -> tuple[Path | None, str]:
    path = checkout_parent / slug(repo)
    if path.exists():
        return path, ""
    proc = run_cmd([
        "git",
        "clone",
        "--quiet",
        "--filter=blob:none",
        "--depth=1",
        "--no-checkout",
        "--branch",
        base_ref,
        f"https://github.com/{repo}.git",
        str(path),
    ], timeout=240)
    if proc.returncode == 0:
        return path, ""
    fallback = run_cmd([
        "git",
        "clone",
        "--quiet",
        "--filter=blob:none",
        "--depth=1",
        "--no-checkout",
        f"https://github.com/{repo}.git",
        str(path),
    ], timeout=240)
    if fallback.returncode != 0:
        return None, (fallback.stderr or fallback.stdout or proc.stderr or proc.stdout).strip()[:240]
    return path, ""


def checkout_pr_state(repo_dir: Path, item: dict[str, Any]) -> tuple[str, str]:
    candidates = [
        ("merge_commit", item.get("merge_oid") or ""),
        ("head_commit", item.get("head_oid") or ""),
        ("base_ref_latest", item.get("base_ref") or "main"),
    ]
    errors: list[str] = []
    for mode, ref in candidates:
        if not ref:
            continue
        fetch_ref = ref if mode != "base_ref_latest" else str(ref)
        fetch = run_cmd(["git", "-C", str(repo_dir), "fetch", "--quiet", "--depth=1", "origin", fetch_ref],
                        timeout=180)
        if fetch.returncode != 0:
            errors.append(f"{mode}: {(fetch.stderr or fetch.stdout).strip()[:120]}")
            continue
        checkout = run_cmd(["git", "-C", str(repo_dir), "checkout", "--quiet", "--detach", "FETCH_HEAD"],
                           timeout=180)
        if checkout.returncode != 0:
            errors.append(f"{mode} checkout: {(checkout.stderr or checkout.stdout).strip()[:120]}")
            continue
        return "checked_out", mode
    return "blocked_checkout_unavailable", "; ".join(errors)[:240] or "checkout unavailable"


def run_pr_checker(body: str, root: Path, tmp: Path, safe_id: str) -> dict[str, Any]:
    body_path = tmp / f"{safe_id}.pr.md"
    receipt_path = tmp / f"{safe_id}.pr.json"
    body_path.write_text(body, encoding="utf-8")
    proc = run_cmd([
        sys.executable,
        str(ROOT / "scripts" / "gate_pr_provenance.py"),
        "--root",
        str(root),
        "--report",
        "--json",
        str(receipt_path),
        str(body_path),
    ], timeout=180)
    if proc.returncode != 0:
        raise RuntimeError(f"anti-slop-pr report-mode exited {proc.returncode}: {(proc.stderr or proc.stdout)[:500]}")
    return read_json(receipt_path)


def run_claims_checker(body: str, root: Path, tmp: Path, safe_id: str) -> dict[str, Any]:
    body_path = tmp / f"{safe_id}.claims.md"
    receipt_path = tmp / f"{safe_id}.claims.json"
    receipts = tmp / f"{safe_id}.empty-receipts"
    receipts.mkdir(exist_ok=True)
    body_path.write_text(body, encoding="utf-8")
    proc = run_cmd([
        sys.executable,
        str(ROOT / "scripts" / "gate_claims.py"),
        "--root",
        str(root),
        "--receipts",
        str(receipts),
        "--report",
        "--json",
        str(receipt_path),
        str(body_path),
    ], timeout=180)
    if proc.returncode != 0:
        raise RuntimeError(
            f"anti-slop-claims report-mode exited {proc.returncode}: {(proc.stderr or proc.stdout)[:500]}"
        )
    return read_json(receipt_path)


def summarize_pr_receipt(receipt: dict[str, Any]) -> tuple[Counter[str], int, int, int, Counter[str]]:
    checks = receipt.get("checks", {})
    claim_types: Counter[str] = Counter()
    reasons: Counter[str] = Counter()
    hard_claims = 0
    hard_unresolved = 0
    advisory = 0
    for kind, check in checks.items():
        refs_checked = int(check.get("refs_checked", 0))
        unresolved = list(check.get("unresolved", []))
        advisory_items = list(check.get("advisory", []))
        claim_types[str(kind)] += refs_checked
        if kind in {"file", "test", "card"}:
            hard_claims += refs_checked
            hard_unresolved += len(unresolved)
        elif kind == "issue" and receipt.get("issue_registry"):
            hard_claims += refs_checked
            hard_unresolved += len(unresolved)
        for item in unresolved:
            reasons[normalize_reason(str(item), "fail")] += 1
        advisory += len(advisory_items)
        for item in advisory_items:
            reasons[normalize_reason(str(item), "advisory")] += 1
    return claim_types, hard_claims, hard_unresolved, advisory, reasons


def summarize_receipt_claims(receipt: dict[str, Any]) -> tuple[Counter[str], int, int, Counter[str]]:
    claim_types: Counter[str] = Counter()
    reasons: Counter[str] = Counter()
    hard_claims = 0
    hard_unresolved = 0
    for claim in receipt.get("claims", []):
        claim_type = str(claim.get("type", "unknown"))
        if claim_type not in {"command_receipt", "metric_receipt"}:
            continue
        claim_types[claim_type] += 1
        if claim.get("tier") == "hard":
            hard_claims += 1
        if claim.get("status") == "fail":
            hard_unresolved += 1
            reasons[normalize_reason(str(claim.get("reason", "")), "fail")] += 1
        elif claim.get("status") == "advisory":
            reasons[normalize_reason(str(claim.get("reason", "")), "advisory")] += 1
    return claim_types, hard_claims, hard_unresolved, reasons


def blocked_artifact(item: dict[str, Any], status: str, reason: str) -> dict[str, Any]:
    line_count = body_line_count(item["body"])
    return {
        "artifact_id": artifact_id(item["repo"], int(item["number"])),
        "repo": item["repo"],
        "category": item["category"],
        "mode": "report",
        "root_mode": "temporary_public_checkout",
        "checkout_status": status,
        "checkout_ref_mode": "unavailable",
        "selection_score": item["score"],
        "selection_mode": item["selection_mode"],
        "line_count": line_count,
        "word_count": body_word_count(item["body"]),
        "sparse_body": body_word_count(item["body"]) < 25,
        "claim_count": 0,
        "hard_claim_count": 0,
        "hard_unresolved_count": 0,
        "advisory_count": 0,
        "checkable_claims_per_100_lines": 0.0,
        "claim_types": {},
        "top_reasons": [["checkout unavailable", 1]],
        "blocked_reason": reason,
    }


def run_artifact(item: dict[str, Any], repo_dir: Path, tmp: Path) -> dict[str, Any]:
    safe_id = artifact_id(item["repo"], int(item["number"]))
    status, ref_mode = checkout_pr_state(repo_dir, item)
    if status != "checked_out":
        return blocked_artifact(item, status, ref_mode)
    pr_receipt = run_pr_checker(item["body"], repo_dir, tmp, safe_id)
    claims_receipt = run_claims_checker(item["body"], repo_dir, tmp, safe_id)
    pr_types, pr_hard, pr_fail, advisory, pr_reasons = summarize_pr_receipt(pr_receipt)
    receipt_types, receipt_hard, receipt_fail, receipt_reasons = summarize_receipt_claims(claims_receipt)
    claim_types = pr_types + receipt_types
    reasons = pr_reasons + receipt_reasons
    claim_count = sum(claim_types.values())
    line_count = body_line_count(item["body"])
    return {
        "artifact_id": safe_id,
        "repo": item["repo"],
        "category": item["category"],
        "mode": "report",
        "root_mode": "temporary_public_checkout",
        "checkout_status": status,
        "checkout_ref_mode": ref_mode,
        "selection_score": item["score"],
        "selection_mode": item["selection_mode"],
        "line_count": line_count,
        "word_count": body_word_count(item["body"]),
        "sparse_body": body_word_count(item["body"]) < 25 or claim_count == 0,
        "claim_count": claim_count,
        "hard_claim_count": pr_hard + receipt_hard,
        "hard_unresolved_count": pr_fail + receipt_fail,
        "advisory_count": advisory,
        "checkable_claims_per_100_lines": round(claim_count / line_count * 100, 2),
        "claim_types": dict(sorted(claim_types.items())),
        "top_reasons": reasons.most_common(10),
    }


def run_live(fetch_limit: int, per_repo: int, target_artifacts: int, min_repos: int) -> dict[str, Any]:
    selected, selection_meta = select_public_prs(fetch_limit, per_repo, target_artifacts, min_repos)
    artifacts: list[dict[str, Any]] = []
    checkout_errors: list[dict[str, str]] = []
    with tempfile.TemporaryDirectory(prefix="anti-slop-public-pr-study-") as tmp_dir:
        tmp = Path(tmp_dir)
        checkout_parent = tmp / "checkouts"
        checkout_parent.mkdir()
        repos: dict[str, Path] = {}
        for item in selected:
            repo = item["repo"]
            if repo not in repos:
                repo_dir, error = clone_repo(repo, str(item.get("base_ref") or "main"), checkout_parent)
                if repo_dir is None:
                    checkout_errors.append({"repo": repo, "reason": error})
                    repos[repo] = checkout_parent / f"missing-{slug(repo)}"
                else:
                    repos[repo] = repo_dir
            repo_dir = repos[repo]
            if not repo_dir.exists():
                artifacts.append(blocked_artifact(item, "blocked_checkout_unavailable", "repo clone failed"))
                continue
            artifacts.append(run_artifact(item, repo_dir, tmp))
    summary = summarize(
        artifacts,
        selected,
        selection_meta,
        checkout_errors,
        target_artifacts,
        min_repos,
        fetch_limit,
        per_repo,
    )
    write_json(SUMMARY_JSON, summary)
    SUMMARY_MD.write_text(markdown_summary(summary), encoding="utf-8")
    actionability = build_actionability(summary)
    write_json(ACTIONABILITY_JSON, actionability)
    ACTIONABILITY_MD.write_text(markdown_actionability(actionability), encoding="utf-8")
    return summary


def summarize(artifacts: list[dict[str, Any]], selected: list[dict[str, Any]],
              selection_meta: dict[str, Any], checkout_errors: list[dict[str, str]],
              target_artifacts: int, min_repos: int, fetch_limit: int, per_repo: int) -> dict[str, Any]:
    total_lines = sum(int(a["line_count"]) for a in artifacts)
    total_claims = sum(int(a["claim_count"]) for a in artifacts)
    hard_claims = sum(int(a["hard_claim_count"]) for a in artifacts)
    hard_unresolved = sum(int(a["hard_unresolved_count"]) for a in artifacts)
    advisory = sum(int(a["advisory_count"]) for a in artifacts)
    repos = sorted({str(a["repo"]) for a in artifacts})
    checked_out = sum(1 for a in artifacts if a.get("checkout_status") == "checked_out")
    sparse_sample = sum(1 for a in artifacts if a.get("sparse_body"))
    reasons: Counter[str] = Counter()
    claim_types: Counter[str] = Counter()
    by_repo: Counter[str] = Counter()
    selection_modes: Counter[str] = Counter()
    for artifact in artifacts:
        reasons.update(dict(artifact.get("top_reasons", [])))
        claim_types.update(artifact.get("claim_types", {}))
        by_repo[str(artifact["repo"])] += 1
        selection_modes[str(artifact["selection_mode"])] += 1
    if sparse_sample:
        reasons["sparse PR bodies"] += sparse_sample
    density = round(total_claims / total_lines * 100, 2) if total_lines else 0.0
    sample_complete = len(artifacts) >= target_artifacts and len(repos) >= min_repos
    blockers = []
    if len(artifacts) < target_artifacts:
        blockers.append(f"selected {len(artifacts)} artifacts below requested {target_artifacts}")
    if len(repos) < min_repos:
        blockers.append(f"selected {len(repos)} repos below requested {min_repos}")
    blockers.extend([f"{item['repo']}: {item['reason']}" for item in checkout_errors[:5]])
    sample_status = "sufficient_public_pr_sample" if sample_complete else "partial_public_pr_sample"
    return {
        "schema_version": SUMMARY_SCHEMA,
        "policy_version": POLICY_VERSION,
        "status": "dry_run_not_adoption",
        "sample_status": sample_status,
        "target": "recent merged public PR bodies from popular AI/devtool repos",
        "requested_artifact_count": target_artifacts,
        "requested_repo_count": min_repos,
        "artifact_count": len(artifacts),
        "repo_count": len(repos),
        "repos": repos,
        "sampled_artifact_count_by_repo": dict(sorted(by_repo.items())),
        "selected_by": dict(sorted(selection_modes.items())),
        "fetch_limit_per_repo": fetch_limit,
        "selected_limit_per_repo": per_repo,
        "total_lines": total_lines,
        "checkable_claim_count": total_claims,
        "hard_claim_count": hard_claims,
        "hard_unresolved_count": hard_unresolved,
        "advisory_count": advisory,
        "checkout_success_count": checked_out,
        "checkout_blocked_count": len(artifacts) - checked_out,
        "sparse_pr_body_count": sparse_sample,
        "recent_sparse_candidate_count": int(selection_meta.get("sparse_recent_candidates", 0)),
        "checkable_claims_per_100_lines": density,
        "hard_unresolved_rate": round(hard_unresolved / hard_claims, 4) if hard_claims else 0.0,
        "advisory_rate": round(advisory / total_claims, 4) if total_claims else 0.0,
        "top_reasons": [{"reason": k, "count": v} for k, v in reasons.most_common(12)],
        "top_claim_types": [{"type": k, "count": v} for k, v in claim_types.most_common(12)],
        "fetch_records": selection_meta.get("fetch_records", []),
        "blockers": blockers,
        "surface_comparison": {
            "natural_pr_bodies": "sampled here",
            "agent_final_report": (
                "not directly sampled in this public-repo loop; existing dogfood reports show the "
                "structured surface can carry command receipts, but external adoption evidence is still needed"
            ),
            "current_hypothesis": (
                "AGENT_FINAL_REPORT.md is likely a cleaner receipt surface than natural PR bodies when teams "
                "want command/metric receipts, because natural PR bodies often mention validation without "
                "attaching machine-readable receipts"
            ),
        },
        "notes": [
            "Report mode only; no outreach, comments, external PRs/issues, maintainer contact, or enforcement.",
            "No target project tests/builds were run; checkouts were used only for deterministic reference resolution.",
            "Committed outputs omit raw PR body text, raw resolver receipts, raw API JSON, temp paths, and external repo contents.",
            "Findings are reference/receipt-resolution facts only; not correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.",
        ],
        "artifacts": [
            {k: v for k, v in artifact.items() if k not in {"blocked_reason"}}
            for artifact in artifacts
        ],
    }


def label_for_reason(reason: str) -> tuple[str, str]:
    if reason in {"file refs unresolved", "test refs unresolved"}:
        return "actionable", "Root-backed unresolved file/test refs are concrete reference-resolution findings."
    if reason in {"command claims without receipts", "metric claims without receipts", "metric receipt mismatch"}:
        return "unclear", "Natural PR bodies lack receipt attachment; useful actionability likely needs an explicit report/receipt workflow."
    if reason == "issue refs advisory without registry":
        return "unclear", "Offline issue references need a supplied registry before maintainer actionability."
    if reason == "commit refs advisory under local-git resolution":
        return "non_actionable", "Commit advisories are resolver caveats, not maintainer-ready findings."
    if reason == "sparse PR bodies":
        return "non_actionable", "Sparse natural PR bodies are a surface limitation, not a concrete repair item."
    if reason == "checkout unavailable":
        return "excluded", "Checkout failures are excluded from usefulness rates."
    return "unclear", "Aggregate pattern needs another pass before a stronger label."


def build_actionability(summary: dict[str, Any]) -> dict[str, Any]:
    labels = []
    for item in summary.get("top_reasons", [])[:12]:
        reason = str(item["reason"])
        label, why = label_for_reason(reason)
        labels.append({
            "cluster_key": reason,
            "count": int(item["count"]),
            "label": label,
            "reason": why,
            "evidence_scope": "aggregate_cluster",
        })
    counts = Counter(label["label"] for label in labels)
    total = sum(int(label["count"]) for label in labels)
    non_excluded = max(1, total - sum(int(label["count"]) for label in labels if label["label"] == "excluded"))
    actionable = sum(int(label["count"]) for label in labels if label["label"] == "actionable")
    non_actionable = sum(int(label["count"]) for label in labels if label["label"] == "non_actionable")
    unclear = sum(int(label["count"]) for label in labels if label["label"] == "unclear")
    return {
        "schema_version": ACTIONABILITY_SCHEMA,
        "policy_version": POLICY_VERSION,
        "allowed_labels": sorted(ALLOWED_LABELS),
        "label_scope": "bounded aggregate clusters; raw PR line text omitted",
        "summary": {
            "cluster_count": len(labels),
            "total_labeled_findings": total,
            "actionable_count": actionable,
            "non_actionable_count": non_actionable,
            "unclear_count": unclear,
            "excluded_count": sum(int(label["count"]) for label in labels if label["label"] == "excluded"),
            "actionable_rate": round(actionable / non_excluded, 4),
            "non_actionable_rate": round(non_actionable / non_excluded, 4),
            "unclear_rate": round(unclear / non_excluded, 4),
        },
        "labels": labels,
        "notes": [
            "Labels are reviewer triage over aggregate resolver clusters, not semantic correctness/relevance judgments.",
            "No raw external PR line text or full resolver receipts are committed.",
        ],
    }


def markdown_summary(summary: dict[str, Any]) -> str:
    lines = [
        "# Public PR Receipt Study Summary",
        "",
        "Status: `dry_run_not_adoption`.",
        "",
        "This is a report-mode mining loop over recent merged public PR bodies from AI/devtool repos. It does not contact maintainers, open external PRs/issues/comments, run target project tests/builds, call models, or enforce anything.",
        "",
        "A finding means a reference or receipt did or did not resolve in the configured public checkout. It does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.",
        "",
        "## Aggregate",
        "",
        f"- Schema: `{summary['schema_version']}`",
        f"- Policy: `{summary['policy_version']}`",
        f"- Sample status: `{summary['sample_status']}`",
        f"- Artifacts: {summary['artifact_count']} requested {summary['requested_artifact_count']}",
        f"- Repos: {summary['repo_count']} requested {summary['requested_repo_count']}",
        f"- Checkouts: {summary['checkout_success_count']} succeeded, {summary['checkout_blocked_count']} blocked",
        f"- Checkable claims: {summary['checkable_claim_count']}",
        f"- Claims per 100 lines: {summary['checkable_claims_per_100_lines']}",
        f"- Hard unresolved rate: {summary['hard_unresolved_rate']:.1%}",
        f"- Advisory rate: {summary['advisory_rate']:.1%}",
        f"- Sparse PR bodies in selected sample: {summary['sparse_pr_body_count']}",
        "",
        "## Top Findings",
        "",
    ]
    for item in summary["top_reasons"]:
        lines.append(f"- {item['reason']}: {item['count']}")
    lines.extend(["", "## Top Claim Types", ""])
    for item in summary["top_claim_types"]:
        lines.append(f"- {item['type']}: {item['count']}")
    lines.extend(["", "## Repos Counted", ""])
    for repo, count in summary["sampled_artifact_count_by_repo"].items():
        lines.append(f"- {repo}: {count} PR bodies")
    lines.extend([
        "",
        "## Surface Note",
        "",
        summary["surface_comparison"]["current_hypothesis"],
        "",
        "This loop does not prove that `AGENT_FINAL_REPORT.md` is better. It only shows that natural PR bodies frequently mention validation without attached machine-readable receipts, so a structured report remains the next surface to test.",
        "",
        "## Exclusions",
        "",
        "- Raw PR body text, raw resolver receipts, raw API JSON, external repo contents, temp checkout paths, credentials, and secrets are omitted.",
        "- Target project tests/builds were not run.",
        "- Pattern-level aggregate clusters are reported instead of name-and-shame examples.",
    ])
    if summary["blockers"]:
        lines.extend(["", "## Blockers", ""])
        for blocker in summary["blockers"]:
            lines.append(f"- {blocker}")
    return "\n".join(lines) + "\n"


def markdown_actionability(data: dict[str, Any]) -> str:
    summary = data["summary"]
    lines = [
        "# Public PR Receipt Study Actionability Labels",
        "",
        f"- Schema: `{data['schema_version']}`",
        f"- Label scope: {data['label_scope']}",
        f"- Labeled clusters: {summary['cluster_count']}",
        f"- Total labeled findings: {summary['total_labeled_findings']}",
        f"- Actionable: {summary['actionable_count']} ({summary['actionable_rate']:.1%} over non-excluded)",
        f"- Non-actionable: {summary['non_actionable_count']} ({summary['non_actionable_rate']:.1%} over non-excluded)",
        f"- Unclear: {summary['unclear_count']} ({summary['unclear_rate']:.1%} over non-excluded)",
        f"- Excluded: {summary['excluded_count']}",
        "",
        "Labels are aggregate reviewer triage over deterministic reference/receipt findings only. Raw PR line text and full resolver receipts are omitted.",
        "",
        "## Cluster Labels",
        "",
    ]
    for item in data["labels"]:
        lines.append(f"- `{item['label']}` {item['cluster_key']}: {item['count']} - {item['reason']}")
    return "\n".join(lines) + "\n"


def validate_manifest(errors: list[str]) -> None:
    if not TARGETS_JSON.is_file():
        errors.append(f"missing public PR receipt target manifest: {rel(TARGETS_JSON)}")
        return
    try:
        data = load_manifest()
    except Exception as exc:  # noqa: BLE001
        errors.append(f"could not load target manifest: {exc}")
        return
    if data.get("schema_version") != TARGET_SCHEMA:
        errors.append(f"target manifest schema mismatch: {data.get('schema_version')}")
    if data.get("policy_version") != POLICY_VERSION:
        errors.append(f"target manifest policy mismatch: {data.get('policy_version')}")
    repos = data.get("repositories", [])
    if not isinstance(repos, list):
        errors.append("target manifest repositories must be a list")
        return
    if not (MIN_MANIFEST_REPOS <= len(repos) <= MAX_MANIFEST_REPOS):
        errors.append(f"target manifest must contain {MIN_MANIFEST_REPOS}-{MAX_MANIFEST_REPOS} repos, found {len(repos)}")
    for snippet in (
        "recent merged public PR bodies",
        "agent/receipt-ish language",
        "report mode only",
        "no outreach",
        "no target project tests/builds",
    ):
        text = json.dumps(data).lower()
        if snippet.lower() not in text:
            errors.append(f"target manifest missing selection/policy snippet: {snippet}")
    for repo in repos:
        for key in ("repo", "category", "selection_reason"):
            if key not in repo:
                errors.append(f"target repo missing {key}: {repo}")


def validate_json_artifact(path: Path, schema: str, errors: list[str]) -> dict[str, Any] | None:
    if not path.is_file():
        errors.append(f"missing public PR receipt artifact: {rel(path)}")
        return None
    try:
        data = read_json(path)
    except Exception as exc:  # noqa: BLE001
        errors.append(f"could not load {rel(path)}: {exc}")
        return None
    if data.get("schema_version") != schema:
        errors.append(f"{rel(path)} schema mismatch: {data.get('schema_version')}")
    text = json.dumps(data, sort_keys=True)
    for forbidden in (
        str(ROOT),
        "/Users/",
        "/private/var/",
        "GITHUB_TOKEN",
        "OPENAI_API_KEY",
        "ANTHROPIC_API_KEY",
        '"body":',
        '"title":',
    ):
        if forbidden in text:
            errors.append(f"{rel(path)} contains forbidden raw/private snippet: {forbidden}")
    return data


def validate_summary(errors: list[str]) -> None:
    summary = validate_json_artifact(SUMMARY_JSON, SUMMARY_SCHEMA, errors)
    actionability = validate_json_artifact(ACTIONABILITY_JSON, ACTIONABILITY_SCHEMA, errors)
    for path in (SUMMARY_MD, ACTIONABILITY_MD):
        if not path.is_file():
            errors.append(f"missing public PR receipt Markdown artifact: {rel(path)}")
            continue
        text = path.read_text(encoding="utf-8")
        for forbidden in (str(ROOT), "/Users/", "/private/var/", "GITHUB_TOKEN", "OPENAI_API_KEY"):
            if forbidden in text:
                errors.append(f"{rel(path)} contains forbidden private/token-like snippet: {forbidden}")
    if summary:
        if summary.get("status") != "dry_run_not_adoption":
            errors.append(f"summary status must be dry_run_not_adoption: {summary.get('status')}")
        if summary.get("sample_status") == "sufficient_public_pr_sample":
            if int(summary.get("artifact_count", 0)) < MIN_SAMPLE_ARTIFACTS:
                errors.append(f"summary artifact_count below {MIN_SAMPLE_ARTIFACTS}")
            if int(summary.get("repo_count", 0)) < MIN_SAMPLE_REPOS:
                errors.append(f"summary repo_count below {MIN_SAMPLE_REPOS}")
        elif not summary.get("blockers"):
            errors.append("partial public PR sample must record blockers")
        if not summary.get("top_reasons"):
            errors.append("summary top_reasons must not be empty")
        if not summary.get("top_claim_types"):
            errors.append("summary top_claim_types must not be empty")
        notes = " ".join(summary.get("notes", []))
        for snippet in ("Report mode only", "No target project tests/builds", "reference/receipt-resolution facts only"):
            if snippet not in notes:
                errors.append(f"summary notes missing boundary: {snippet}")
    if actionability:
        allowed = set(actionability.get("allowed_labels", []))
        if allowed != ALLOWED_LABELS:
            errors.append(f"actionability allowed_labels mismatch: {sorted(allowed)}")
        labels = actionability.get("labels", [])
        if not labels:
            errors.append("actionability labels are empty")
        seen = {item.get("label") for item in labels}
        if not seen <= ALLOWED_LABELS:
            errors.append(f"unknown actionability labels: {sorted(seen - ALLOWED_LABELS)}")
        for item in labels:
            for key in ("cluster_key", "count", "label", "reason", "evidence_scope"):
                if key not in item:
                    errors.append(f"actionability label missing {key}: {item}")
        scope = str(actionability.get("label_scope", ""))
        if "raw PR line text omitted" not in scope:
            errors.append("actionability label_scope must state raw PR line text is omitted")


def validate_doc(errors: list[str]) -> None:
    if not DOC.is_file():
        errors.append(f"missing public PR receipt study doc: {rel(DOC)}")
        return
    text = DOC.read_text(encoding="utf-8")
    for snippet in (
        SUMMARY_SCHEMA,
        "proof/public-pr-receipt-study/summary.json",
        "report mode only",
        "No outreach",
        "No target project tests/builds",
        "AGENT_FINAL_REPORT.md",
        "does not prove correctness",
    ):
        if snippet not in text:
            errors.append(f"{rel(DOC)} missing snippet: {snippet}")


def compatibility_errors() -> list[str]:
    errors: list[str] = []
    validate_manifest(errors)
    validate_summary(errors)
    validate_doc(errors)
    return errors


def check_only() -> int:
    errors = compatibility_errors()
    if errors:
        print("PUBLIC PR RECEIPT STUDY CHECK FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    summary = read_json(SUMMARY_JSON)
    print(
        "PUBLIC PR RECEIPT STUDY CHECK PASSED: "
        f"{summary['artifact_count']} PR bodies, {summary['repo_count']} repos, "
        f"{summary['checkable_claims_per_100_lines']} claims/100 lines."
    )
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate committed aggregate artifacts")
    parser.add_argument("--self-test", action="store_true", help="alias for --check")
    parser.add_argument("--run-live", action="store_true", help="fetch public PR bodies and regenerate aggregate proof")
    parser.add_argument("--fetch-limit", type=int, default=DEFAULT_FETCH_LIMIT)
    parser.add_argument("--per-repo", type=int, default=DEFAULT_PER_REPO)
    parser.add_argument("--target-artifacts", type=int, default=MIN_SAMPLE_ARTIFACTS)
    parser.add_argument("--min-repos", type=int, default=MIN_SAMPLE_REPOS)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.check or args.self_test or not args.run_live:
        return check_only()
    pre_errors: list[str] = []
    validate_manifest(pre_errors)
    if pre_errors:
        print("PUBLIC PR RECEIPT STUDY LIVE RUN BLOCKED:")
        for error in pre_errors:
            print(f"  - {error}")
        return 1
    summary = run_live(args.fetch_limit, args.per_repo, args.target_artifacts, args.min_repos)
    errors = compatibility_errors()
    if errors:
        print("PUBLIC PR RECEIPT STUDY LIVE RUN WROTE OUTPUTS BUT CHECK FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(
        "PUBLIC PR RECEIPT STUDY LIVE RUN PASSED: "
        f"{summary['artifact_count']} PR bodies across {summary['repo_count']} repos; "
        f"{summary['checkable_claims_per_100_lines']} claims/100 lines; "
        f"hard_unresolved={summary['hard_unresolved_rate']:.1%}; "
        f"advisory={summary['advisory_rate']:.1%}."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
