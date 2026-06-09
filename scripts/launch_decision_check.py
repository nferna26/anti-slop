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
RELEASE_BODY = ROOT / "docs" / "github-release-v0.1.1.md"
DEMO_REPO = ROOT / "docs" / "demo-repo.md"
OUTREACH = ROOT / "docs" / "maintainer-outreach-packet.md"
DECISION = ROOT / "docs" / "launch-decision.md"

ALLOWED_DECISIONS = {
    "continue_private_learning_loop",
    "prepare_tag_only",
    "tag_created_no_outreach",
    "clean_v011_tag_path",
    "narrow_public_preview_release",
    "prepare_opt_in_outreach",
    "pause_or_narrow",
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
        "anti-slop-receipts-v0.1.0",
        "anti-slop-receipts-v0.1.1",
        "v0.1.1 Source-Doc Invariant",
        "post-tag install proof may live outside the tag commit",
        "docs/github-release-v0.1.1.md",
        "GitHub Release record is the publication receipt",
        "pip install \"anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@<tag-or-full-sha>\"",
        "full commit SHA",
        "release readiness checklist",
        "adopter update path",
        "No correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon claim",
    ], errors)
    require_snippets(RELEASE_NOTES, [
        "Release body source",
        "anti-slop-receipts-v0.1.0",
        "anti-slop-receipts-v0.1.1",
        "v0.1.1 Source-Doc Invariant",
        "GitHub Release title",
        "deterministic reference/receipt resolution only",
        "anti-slop-claims",
        "anti-slop-run",
        "anti-slop-pr-event",
    ], errors)
    require_snippets(RELEASE_BODY, [
        "Anti-Slop Receipts v0.1.1 — deterministic receipt checks for AI coding-agent reports",
        "pip install \"anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@anti-slop-receipts-v0.1.1\"",
        "anti-slop-claims --self-test",
        "anti-slop-run -- make validate",
        "anti-slop-claims",
        "Report mode remains default",
        "does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon",
        "not a code review, security review, test-quality review, semantic diff review, or advice-quality review",
        "No outreach, external PR/comment/issue, maintainer contact, HN/X launch blast",
        "GitHub Release record is the publication receipt",
        "tag source docs were authored before a GitHub Release record could exist",
        "2-3 friendly external installs",
        "Suggested repository metadata",
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
        "proof/external-dry-run/expanded/summary.md",
        "proof/external-dry-run/expanded/actionability.json",
        "proof/real-checkout-learning/summary.json",
        "proof/real-checkout-learning/actionability.json",
        "proof/command-receipt-dogfood/summary.json",
        "proof/real-command-receipt-dogfood/summary.json",
        "proof/fresh-install-smoke/summary.json",
        "proof/tag-install-smoke/summary.json",
        "docs/github-release-v0.1.1.md",
        "proof/external-dry-run/clusters.md",
        "proof/external-dry-run/kill-criteria.json",
        "benchmarks/agent-claim-corpus-v0.1/results/summary.json",
        "make launch-check",
        "dry-run density",
        "benchmark mutations",
        "install success",
        "command receipt dogfood",
        "real checkout",
        "outreach readiness",
        "FAIL",
        "UNKNOWN",
        "PASS",
        "2-3 friendly external installs",
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
        for target in (RELEASE_PLAN, RELEASE_BODY, DEMO_REPO, OUTREACH, DECISION):
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
