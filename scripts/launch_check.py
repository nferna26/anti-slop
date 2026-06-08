#!/usr/bin/env python3
"""Machine-check launch-facing Anti-Slop Receipts surfaces.

This check guards public launch guarantees that are easy to drift in prose:
product/package naming, privacy/security posture, proof metric links, report-mode
workflow defaults, Step Summary support, and history placement. It is stdlib-only
and does not call GitHub APIs, models, network services, or tokens.
"""

from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

README = ROOT / "README.md"
INSTALL = ROOT / "INSTALL_FOR_AGENTS.md"
LLMS = ROOT / "llms.txt"
TEMPLATE = ROOT / "templates" / "anti-slop-report.yml"
AGENT_MATRIX = ROOT / "docs" / "agent-claim-verification.md"
ADOPTION_LOOP = ROOT / "docs" / "adoption-loop.md"
AGENT_CONTRACT = ROOT / "docs" / "agent-report-contract.md"
PR_PROVENANCE = ROOT / "docs" / "pr-provenance.md"
COMMAND_RECEIPTS = ROOT / "docs" / "command-receipts.md"
PRIVACY = ROOT / "docs" / "privacy-security.md"
NAMING = ROOT / "docs" / "package-install-naming.md"
CHECKLIST = ROOT / "docs" / "launch-checklist.md"
KB_INDEX = ROOT / "kb" / "index.md"
KB_LOG = ROOT / "kb" / "log.md"
CLAIMS_SCRIPT = ROOT / "scripts" / "gate_claims.py"
EVENT_SCRIPT = ROOT / "scripts" / "pr_provenance_from_github_event.py"
DEMO_OUTPUT = ROOT / "proof" / "agent-claim-demo" / "sample-output.md"
BENCHMARK_SUMMARY = ROOT / "benchmarks" / "agent-claim-corpus-v0.1" / "results" / "summary.json"
AUDIT_SUMMARY = ROOT / "proof" / "agent-claim-audit" / "summary.json"
HISTORY = "docs/history/books-kb-eval-lab.md"


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


def require_all_docs_link(path: Path, linked_docs: list[Path], errors: list[str]) -> None:
    text = read(path, errors)
    if not text:
        return
    for doc in linked_docs:
        link = rel(doc)
        if link not in text and f"../{link}" not in text:
            errors.append(f"{rel(path)} missing link/reference to {link}")


def percent(value: object) -> str:
    return f"{float(value):.1%}"


def check_readme_metrics(errors: list[str]) -> None:
    text = read(README, errors)
    if not text:
        return
    if not BENCHMARK_SUMMARY.is_file():
        errors.append(f"missing benchmark summary: {rel(BENCHMARK_SUMMARY)}")
        return
    if not AUDIT_SUMMARY.is_file():
        errors.append(f"missing audit summary: {rel(AUDIT_SUMMARY)}")
        return
    benchmark = json.loads(BENCHMARK_SUMMARY.read_text(encoding="utf-8"))
    audit = json.loads(AUDIT_SUMMARY.read_text(encoding="utf-8"))
    expected = [
        rel(BENCHMARK_SUMMARY),
        rel(AUDIT_SUMMARY),
        f"{benchmark['case_count']}-case",
        f"{percent(benchmark['catch_rate'])} catch rate",
        f"{percent(benchmark['false_fail_rate'])} false-fail rate",
        f"{audit['artifact_count']} real PR bodies",
        f"{audit['checkable_claim_density_per_100_lines']} checkable claims per 100 lines",
        f"{audit['unresolved_hard_claim_rate']:.1%} hard unresolved rate",
        f"30-day falsifier trend: {audit['thirty_day_falsifier']['trend'].upper()}",
    ]
    for snippet in expected:
        if snippet not in text:
            errors.append(f"README proof metric missing/stale: {snippet}")


def check_history_below_fold(errors: list[str]) -> None:
    text = read(README, errors)
    if not text:
        return
    history_index = text.find(HISTORY)
    if history_index == -1:
        errors.append(f"README missing history link: {HISTORY}")
        return
    for anchor in ("## Install", "## GitHub Action", "## Non-Goals", "## Privacy And Security"):
        anchor_index = text.find(anchor)
        if anchor_index == -1:
            errors.append(f"README missing launch section before history: {anchor}")
        elif history_index < anchor_index:
            errors.append(f"README history link appears before launch section: {anchor}")
    first_screen = text[:1400].lower()
    if "books-kb" in first_screen or "200-book" in first_screen:
        errors.append("README first screen still leads with books-KB/200-book framing")


def check_step_summary_support(errors: list[str]) -> None:
    require_snippets(CLAIMS_SCRIPT, [
        "--github-summary",
        "GITHUB_STEP_SUMMARY",
        "Anti-Slop Claims Report",
    ], errors)
    require_snippets(EVENT_SCRIPT, [
        "--github-summary",
        "GITHUB_STEP_SUMMARY",
        "Anti-Slop PR Body Report",
    ], errors)


def check_workflow(errors: list[str]) -> None:
    text = read(TEMPLATE, errors)
    if not text:
        return
    for snippet in [
        "permissions:",
        "contents: read",
        "ANTI_SLOP_INSTALL_SPEC",
        "@<tag-or-full-sha>",
        "anti-slop-pr-event --root . --report",
        "anti-slop-run -- make validate",
        "anti-slop-claims --root . --receipts .anti-slop/receipts --json .anti-slop/claims.json --report AGENT_FINAL_REPORT.md",
        "GITHUB_STEP_SUMMARY",
        "actions/upload-artifact@v4",
        ".anti-slop/receipts/*.json",
        ".anti-slop/claims.json",
        "Report mode",
        "Anti-Slop Receipts",
        "anti-slop-lineage",
    ]:
        if snippet not in text:
            errors.append(f"{rel(TEMPLATE)} missing snippet: {snippet}")
    forbidden = ["contents: write", "pull-requests: write", "id-token: write"]
    for snippet in forbidden:
        if snippet in text:
            errors.append(f"{rel(TEMPLATE)} must not request write/token scope: {snippet}")


def check_product_naming(errors: list[str]) -> None:
    naming_required = [
        "Anti-Slop Receipts is the product name",
        "anti-slop-lineage remains the current Python distribution name",
        "anti-slop-claims is the canonical checker",
        "anti-slop-run is the receipt producer",
        "anti-slop-pr-event is the GitHub PR-body preset",
        "anti-slop-pr remains the PR-body compatibility wrapper",
        "No release or tag is created by this install guidance",
        "Do not rename adopter workflows to a broad slop detector",
    ]
    require_snippets(NAMING, naming_required, errors)
    for path in (README, INSTALL, LLMS, TEMPLATE):
        require_snippets(path, [
            "Anti-Slop Receipts",
            "anti-slop-lineage",
            "anti-slop-claims",
            "anti-slop-run",
            "anti-slop-pr-event",
        ], errors)
        require_all_docs_link(path, [NAMING], errors)


def check_privacy_doc(errors: list[str]) -> None:
    require_snippets(PRIVACY, [
        "local execution",
        "stdout/stderr hashes",
        "bounded excerpts",
        "artifact upload risk",
        "no telemetry",
        "no GitHub API token",
        "no model",
        "secrets",
        ".env",
        "private paths",
        "raw API JSON",
        "answer keys",
        "raw transcripts",
        "raw copyrighted text",
    ], errors)
    for path in (README, INSTALL, LLMS, AGENT_MATRIX, ADOPTION_LOOP, KB_INDEX):
        require_all_docs_link(path, [PRIVACY], errors)


def check_launch_checklist(errors: list[str]) -> None:
    require_snippets(CHECKLIST, [
        "Machine checks",
        "Manual checks",
        "make launch-check",
        "make adoption-smoke",
        rel(BENCHMARK_SUMMARY),
        rel(AUDIT_SUMMARY),
        "docs/privacy-security.md",
        "docs/package-install-naming.md",
        "report mode remains default",
        "no external outreach",
    ], errors)
    for path in (README, INSTALL, LLMS, KB_INDEX):
        require_all_docs_link(path, [CHECKLIST], errors)


def check_demo_output(errors: list[str]) -> None:
    require_snippets(DEMO_OUTPUT, [
        "Fake Report",
        "FAIL",
        "Receipt-Backed Report",
        "PASS",
    ], errors)


def check_cross_links(errors: list[str]) -> None:
    for path in (
        AGENT_MATRIX,
        ADOPTION_LOOP,
        AGENT_CONTRACT,
        PR_PROVENANCE,
        COMMAND_RECEIPTS,
        KB_INDEX,
    ):
        require_all_docs_link(path, [PRIVACY, NAMING], errors)
    require_snippets(KB_LOG, [
        "RC-cleanliness tranche",
        "CORE-967",
        "CORE-968",
        "CORE-969",
        "CORE-970",
        "launch-check",
    ], errors)


def main() -> int:
    errors: list[str] = []
    check_readme_metrics(errors)
    check_history_below_fold(errors)
    check_step_summary_support(errors)
    check_workflow(errors)
    check_product_naming(errors)
    check_privacy_doc(errors)
    check_launch_checklist(errors)
    check_demo_output(errors)
    check_cross_links(errors)
    if errors:
        print("LAUNCH CHECK FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(
        "LAUNCH CHECK PASSED: README proof links, naming posture, privacy/security "
        "doc, launch checklist, workflow template, Step Summary support, demo "
        "output, and history placement are covered."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
