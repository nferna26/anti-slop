#!/usr/bin/env python3
"""Public-safe report-mode audit of real agent/PR-body claim density.

The committed repo currently has a small saved-PR-body corpus, so this audit
combines those PR bodies with curated public-safe KB log entries that record
real agent/tranche reports. It always exits 0: this is evidence for adoption
calibration, not an enforcement gate.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import json
import re
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "proof" / "agent-claim-audit"
SUMMARY_JSON = OUT_DIR / "summary.json"
SUMMARY_MD = OUT_DIR / "summary.md"
PR_BODIES = ROOT / "proof" / "pr-provenance-dogfood" / "bodies"
KB_LOG = ROOT / "kb" / "log.md"

sys.path.insert(0, str(ROOT / "scripts"))
import gate_claims  # noqa: E402

KB_PREFIXES = (
    "- Gate run:",
    "- Decision:",
    "- Rejected/deferred:",
    "- Follow-up:",
    "- Tooling:",
    "- Tooling/OSS-readiness:",
    "- Eval run:",
)


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def kb_log_chunks(limit: int) -> list[dict]:
    chunks: list[dict] = []
    current_date = "unknown"
    for line_no, raw in enumerate(read(KB_LOG).splitlines(), start=1):
        if raw.startswith("## "):
            current_date = raw.removeprefix("## ").strip()
            continue
        stripped = raw.strip()
        if not stripped.startswith(KB_PREFIXES):
            continue
        if len(stripped) < 80:
            continue
        prefix = stripped.split(":", 1)[0].removeprefix("- ").lower().replace("/", "-")
        chunks.append({
            "id": f"kb-log-{len(chunks) + 1:02d}",
            "kind": "kb-log-entry",
            "source": f"kb/log.md:{line_no}",
            "date": current_date,
            "title": f"{current_date} {prefix}",
            "text": f"# KB Log Entry\n\nSource: kb/log.md:{line_no}\n\n{stripped}\n",
        })
        if len(chunks) >= limit:
            break
    return chunks


def artifact_inputs(tmp: Path) -> list[dict]:
    artifacts: list[dict] = []
    for path in sorted(PR_BODIES.glob("*.txt")):
        artifacts.append({
            "id": f"saved-{path.stem}",
            "kind": "saved-pr-body",
            "source": rel(path),
            "path": path,
            "text": read(path),
        })

    needed = max(0, 20 - len(artifacts))
    for chunk in kb_log_chunks(needed):
        path = tmp / f"{chunk['id']}.md"
        path.write_text(chunk["text"], encoding="utf-8")
        chunk["path"] = path
        artifacts.append(chunk)

    if len(artifacts) < 20:
        raise RuntimeError(f"need at least 20 real public-safe artifacts, found {len(artifacts)}")
    return artifacts[:20]


def normalize_reason(reason: str) -> str:
    if "missing command receipt" in reason:
        return "missing command receipts for historical validation claims"
    if "missing metric receipt" in reason:
        return "missing metric receipts for historical metric claims"
    if "file does not resolve" in reason:
        return "path refs that do not resolve in current checkout"
    if "line" in reason and "exceeds file length" in reason:
        return "line refs outside current file length"
    if "test does not resolve" in reason or "test node does not resolve" in reason:
        return "test refs that do not resolve in current checkout"
    if "issue does not resolve" in reason:
        return "issue refs absent from supplied registry"
    return re.sub(r": .+$", "", reason)


def audit_one(item: dict) -> dict:
    path = Path(item["path"])
    receipt = gate_claims.structured_receipt(
        artifact_path=path,
        root=ROOT,
        registry=None,
        require_reviewed_cards=False,
        diff_range=None,
        receipts_dir=None,
    )
    claims = receipt.get("claims", [])
    hard = [c for c in claims if c.get("tier") == "hard"]
    hard_fail = [c for c in hard if c.get("status") == "fail"]
    advisory = [c for c in claims if c.get("status") == "advisory"]
    line_count = max(1, len(item["text"].splitlines()))
    claim_types = Counter(c.get("type", "unknown") for c in claims)
    clusters = Counter(normalize_reason(c.get("reason", "")) for c in hard_fail)
    return {
        "id": item["id"],
        "kind": item["kind"],
        "source": item["source"],
        "line_count": line_count,
        "claim_count": len(claims),
        "hard_claim_count": len(hard),
        "hard_fail_count": len(hard_fail),
        "advisory_count": len(advisory),
        "checkable_claim_density_per_100_lines": round(len(claims) / line_count * 100, 2),
        "claim_types": dict(sorted(claim_types.items())),
        "hard_fail_clusters": dict(sorted(clusters.items())),
        "passed": bool(receipt.get("passed")),
    }


def summarize(items: list[dict], results: list[dict]) -> dict:
    total_lines = sum(r["line_count"] for r in results)
    total_claims = sum(r["claim_count"] for r in results)
    hard_claims = sum(r["hard_claim_count"] for r in results)
    hard_fails = sum(r["hard_fail_count"] for r in results)
    claim_types = Counter()
    clusters = Counter()
    for result in results:
        claim_types.update(result["claim_types"])
        clusters.update(result["hard_fail_clusters"])

    unresolved_rate = round(hard_fails / hard_claims, 4) if hard_claims else 0.0
    density = round(total_claims / total_lines * 100, 2) if total_lines else 0.0
    artifacts_with_claims = sum(1 for r in results if r["claim_count"])
    # Falsifier trend: report-mode adoption is trending pass only if real
    # public-safe artifacts have nontrivial checkable density and unresolved
    # hard claims stay under a conservative calibration threshold.
    falsifier_trend = (
        "pass" if artifacts_with_claims >= 15 and density >= 8.0 and unresolved_rate <= 0.35
        else "fail"
    )
    return {
        "schema_version": "anti-slop-agent-claim-density-audit.v0.1",
        "artifact_count": len(results),
        "artifact_mix": dict(sorted(Counter(item["kind"] for item in items).items())),
        "total_lines": total_lines,
        "claim_count": total_claims,
        "hard_claim_count": hard_claims,
        "hard_fail_count": hard_fails,
        "checkable_claim_density_per_100_lines": density,
        "unresolved_hard_claim_rate": unresolved_rate,
        "artifacts_with_claims": artifacts_with_claims,
        "top_claim_types": claim_types.most_common(10),
        "candidate_false_positive_clusters": clusters.most_common(10),
        "thirty_day_falsifier": {
            "trend": falsifier_trend,
            "rule": "pass if >=15 artifacts have claims, density >=8.0 claims/100 lines, and hard unresolved rate <=0.35",
            "scope": "report-mode calibration over committed public-safe real artifacts",
        },
        "artifacts": results,
    }


def markdown(summary: dict) -> str:
    lines = [
        "# Agent Claim Density Audit",
        "",
        "Report-mode audit over committed public-safe real artifacts. This does not contact external repos, call a model/API, or read local-only artifacts.",
        "",
        "Scope note: the committed saved-PR-body corpus currently has 8 PR bodies, so this audit uses 8 saved PR bodies plus 12 curated `kb/log.md` tranche/report entries. The KB entries are real public-safe project reports, not synthetic benchmark cases.",
        "",
        "A finding here means a reference or receipt did or did not resolve in the current checkout. It does not judge correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.",
        "",
        "## Summary",
        "",
        f"- Artifacts: {summary['artifact_count']} ({summary['artifact_mix']})",
        f"- Checkable claim density: {summary['checkable_claim_density_per_100_lines']} claims / 100 lines",
        f"- Hard unresolved rate: {summary['unresolved_hard_claim_rate']:.1%}",
        f"- Artifacts with at least one claim: {summary['artifacts_with_claims']}",
        f"- 30-day falsifier trend: {summary['thirty_day_falsifier']['trend'].upper()}",
        "",
        "## Top Claim Types",
        "",
    ]
    if summary["top_claim_types"]:
        for claim_type, count in summary["top_claim_types"]:
            lines.append(f"- {claim_type}: {count}")
    else:
        lines.append("- None.")
    lines.extend(["", "## Candidate False-Positive Clusters", ""])
    if summary["candidate_false_positive_clusters"]:
        for cluster, count in summary["candidate_false_positive_clusters"]:
            lines.append(f"- {cluster}: {count}")
    else:
        lines.append("- None.")
    lines.extend(["", "## Artifact Detail", ""])
    for result in summary["artifacts"]:
        lines.append(
            f"- {result['id']} ({result['kind']}, {result['source']}): "
            f"{result['claim_count']} claims, {result['hard_fail_count']} hard unresolved, "
            f"{result['checkable_claim_density_per_100_lines']} claims/100 lines"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        items = artifact_inputs(Path(tmp))
        results = [audit_one(item) for item in items]
    summary = summarize(items, results)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    SUMMARY_JSON.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    SUMMARY_MD.write_text(markdown(summary), encoding="utf-8")
    print(
        "agent-claim audit: "
        f"{summary['artifact_count']} artifacts, "
        f"density={summary['checkable_claim_density_per_100_lines']} claims/100 lines, "
        f"unresolved={summary['unresolved_hard_claim_rate']:.1%}, "
        f"30-day-trend={summary['thirty_day_falsifier']['trend']}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
