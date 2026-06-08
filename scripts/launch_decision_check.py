#!/usr/bin/env python3
"""Machine-check launch decision artifacts for Anti-Slop Receipts.

This gate covers release/tag pin guidance, demo/launch assets, opt-in outreach
copy, and the evidence-based go/no-go memo. It is stdlib-only and does not call
GitHub APIs, models, network services, or tokens.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

README = ROOT / "README.md"
INSTALL = ROOT / "INSTALL_FOR_AGENTS.md"
LLMS = ROOT / "llms.txt"
CHECKLIST = ROOT / "docs" / "launch-checklist.md"
KB_INDEX = ROOT / "kb" / "index.md"
KB_LOG = ROOT / "kb" / "log.md"

RELEASE_PLAN = ROOT / "docs" / "release-install-plan.md"
RELEASE_NOTES = ROOT / "docs" / "release-notes-draft.md"
DEMO_REPO = ROOT / "docs" / "demo-repo.md"
OUTREACH = ROOT / "docs" / "maintainer-outreach-packet.md"
DECISION = ROOT / "docs" / "launch-decision.md"

ALLOWED_DECISIONS = {
    "launch",
    "launch narrower",
    "continue private learning loop",
    "pause",
}


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def read(path: Path, errors: list[str]) -> str:
    if not path.is_file():
        errors.append(f"missing file: {rel(path)}")
        return ""
    return path.read_text(encoding="utf-8")


def require_snippets(path: Path, snippets: list[str], errors: list[str]) -> None:
    text = read(path, errors)
    if not text:
        return
    for snippet in snippets:
        if snippet not in text:
            errors.append(f"{rel(path)} missing snippet: {snippet}")


def require_link(path: Path, target: Path, errors: list[str]) -> None:
    text = read(path, errors)
    if not text:
        return
    link = rel(target)
    if link not in text and f"../{link}" not in text and target.name not in text:
        errors.append(f"{rel(path)} missing link/reference to {link}")


def check_release_plan(errors: list[str]) -> None:
    require_snippets(RELEASE_PLAN, [
        "Anti-Slop Receipts is the product",
        "anti-slop-lineage remains the Python distribution",
        "operator approval",
        "Do not create a release tag from this tranche",
        "pip install \"anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@<tag-or-full-sha>\"",
        "full commit SHA",
        "release readiness checklist",
        "adopter update path",
        "No correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon claim",
    ], errors)
    require_snippets(RELEASE_NOTES, [
        "Draft release notes",
        "No release tag has been created",
        "deterministic reference/receipt resolution only",
        "anti-slop-claims",
        "anti-slop-run",
        "anti-slop-pr-event",
    ], errors)


def check_demo_assets(errors: list[str]) -> None:
    require_snippets(DEMO_REPO, [
        "make agent-claim-demo",
        "fake report FAILS",
        "receipt-backed report PASSES",
        "GITHUB_STEP_SUMMARY",
        "screenshot checklist",
        "GIF checklist",
        "reference/receipt resolution only",
        "HN-sized launch copy",
        "X-sized launch copy",
    ], errors)


def check_outreach(errors: list[str]) -> None:
    require_snippets(OUTREACH, [
        "proof/external-dry-run/summary.md",
        "proof/external-dry-run/clusters.md",
        "docs/kill-criteria.md",
        "report mode",
        "maintainer opt-in required",
        "no auto-open PRs/comments",
        "no model/API/token",
        "no GitHub API dependency",
        "opt-out",
        "when not to contact",
        "evidence summary format",
    ], errors)


def check_decision(errors: list[str]) -> None:
    text = read(DECISION, errors)
    if not text:
        return
    match = re.search(r"^Decision:\s*(.+)$", text, re.MULTILINE)
    if not match:
        errors.append(f"{rel(DECISION)} missing exact Decision line")
    else:
        decision = match.group(1).strip().lower()
        if decision not in ALLOWED_DECISIONS:
            errors.append(
                f"{rel(DECISION)} decision must be one of: {', '.join(sorted(ALLOWED_DECISIONS))}"
            )
    for snippet in [
        "proof/external-dry-run/summary.md",
        "proof/external-dry-run/clusters.md",
        "proof/external-dry-run/kill-criteria.json",
        "benchmarks/agent-claim-corpus-v0.1/results/summary.json",
        "make launch-check",
        "dry-run density",
        "benchmark mutations",
        "install success",
        "command receipt dogfood",
        "outreach readiness",
        "UNKNOWN",
        "PASS",
        "next narrow tranche",
        "deterministic reference/receipt resolution only",
    ]:
        if snippet not in text:
            errors.append(f"{rel(DECISION)} missing snippet: {snippet}")
    for criterion in [
        "claim density",
        "non-actionable after repairs",
        "useful findings",
        "install success",
        "command receipt dogfood",
        "maintainer keep-rate",
        "stale proof metrics",
        "platform clone risk",
    ]:
        if criterion not in text:
            errors.append(f"{rel(DECISION)} missing kill criterion: {criterion}")


def check_cross_links(errors: list[str]) -> None:
    for path in (README, INSTALL, LLMS, CHECKLIST, KB_INDEX):
        for target in (RELEASE_PLAN, DEMO_REPO, OUTREACH, DECISION):
            require_link(path, target, errors)
    require_snippets(KB_LOG, [
        "CORE-979",
        "CORE-980",
        "CORE-981",
        "CORE-982",
        "launch-decision-check",
    ], errors)


def main() -> int:
    errors: list[str] = []
    check_release_plan(errors)
    check_demo_assets(errors)
    check_outreach(errors)
    check_decision(errors)
    check_cross_links(errors)
    if errors:
        print("LAUNCH DECISION CHECK FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(
        "LAUNCH DECISION CHECK PASSED: release pin guidance, demo assets, "
        "outreach packet, go/no-go memo, and launch links are covered."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
