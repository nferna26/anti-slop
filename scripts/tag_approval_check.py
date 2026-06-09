#!/usr/bin/env python3
"""Machine-check the operator tag-approval decision packet."""

from __future__ import annotations

from pathlib import Path
import json
import re
import subprocess
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
INSTALL = ROOT / "INSTALL_FOR_AGENTS.md"
LLMS = ROOT / "llms.txt"
RELEASE_PLAN = ROOT / "docs" / "release-install-plan.md"
RELEASE_NOTES = ROOT / "docs" / "release-notes-draft.md"
LAUNCH_DECISION = ROOT / "docs" / "launch-decision.md"
PACKET = ROOT / "docs" / "tag-approval-packet.md"
MEMO = ROOT / "docs" / "operator-tag-decision.md"
KB_INDEX = ROOT / "kb" / "index.md"
KB_LOG = ROOT / "kb" / "log.md"
FRESH_SUMMARY = ROOT / "proof" / "fresh-install-smoke" / "summary.json"
FRESH_MD = ROOT / "proof" / "fresh-install-smoke" / "summary.md"
TAG_SUMMARY = ROOT / "proof" / "tag-install-smoke" / "summary.json"
TAG_MD = ROOT / "proof" / "tag-install-smoke" / "summary.md"
REAL_CHECKOUT = ROOT / "proof" / "real-checkout-learning" / "summary.json"
REAL_ACTIONABILITY = ROOT / "proof" / "real-checkout-learning" / "actionability.json"
REAL_DOGFOOD = ROOT / "proof" / "real-command-receipt-dogfood" / "summary.json"
KILL = ROOT / "proof" / "external-dry-run" / "kill-criteria.json"

FRESH_SCHEMA = "anti-slop-fresh-install-smoke.v1"
TAG_SCHEMA = "anti-slop-tag-install-smoke.v1"
TAG_NAME = "anti-slop-receipts-v0.1.0"
EXPECTED_CANDIDATE_COMMIT = "75ac7fbe80f62d50409ebc8fe1f736e9bc2fa649"
STALE_TAG_DOC_CANDIDATE = "4bda4fd727018a2a027ba8c660c48c30b8aa2144"
ALLOWED_PACKET_DECISIONS = {"ready_to_request_operator_tag", "tag_created_no_outreach", "not_ready_for_tag", "blocked"}
ALLOWED_OPERATOR_DECISIONS = {
    "request_operator_create_tag",
    "tag_created_no_outreach",
    "continue_private_learning_loop",
    "pause_or_narrow",
}
RELEASE_FACING = [
    README,
    INSTALL,
    LLMS,
    RELEASE_PLAN,
    RELEASE_NOTES,
    LAUNCH_DECISION,
    PACKET,
    MEMO,
]
BOUNDARY = (
    "does not prove correctness, relevance, source truth, support, safety, "
    "advice quality, reasoning, benchmark validity, statistical meaning, or canon"
)
STALE_TAG_SOURCE_DISCLOSURE = [
    "tag's embedded docs predate PR #46 finalization",
    "Decision: `ready_to_request_operator_tag`",
    f"candidate `{STALE_TAG_DOC_CANDIDATE}`",
    "`No tag has been created`",
    "Do not force-move `anti-slop-receipts-v0.1.0`",
    "installable package smoke passes",
    "GitHub release from v0.1.0 requires explicit disclosure",
    "safer path is creating `anti-slop-receipts-v0.1.1` after PR #46 merges and fresh tag-install proof passes",
]
STALE_TAG_SOURCE_DOCS = [
    PACKET,
    MEMO,
    RELEASE_PLAN,
    RELEASE_NOTES,
    LAUNCH_DECISION,
]
STALE_TAG_SOURCE_LINKS = [
    README,
    INSTALL,
    LLMS,
    KB_INDEX,
]


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def read(path: Path, errors: list[str]) -> str:
    if not path.is_file():
        errors.append(f"missing file: {rel(path)}")
        return ""
    return path.read_text(encoding="utf-8")


def read_json(path: Path, errors: list[str]) -> dict[str, Any]:
    if not path.is_file():
        errors.append(f"missing JSON: {rel(path)}")
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in {rel(path)}: {exc}")
        return {}


def require_snippets(path: Path, snippets: list[str], errors: list[str]) -> None:
    text = read(path, errors)
    if not text:
        return
    for snippet in snippets:
        if snippet not in text:
            errors.append(f"{rel(path)} missing snippet: {snippet}")


def normalize_ws(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def require_normalized_snippets(path: Path, snippets: list[str], errors: list[str]) -> None:
    text = read(path, errors)
    if not text:
        return
    normalized = normalize_ws(text)
    for snippet in snippets:
        if normalize_ws(snippet) not in normalized:
            errors.append(f"{rel(path)} missing snippet: {snippet}")


def require_link(path: Path, target: Path, errors: list[str]) -> None:
    text = read(path, errors)
    if not text:
        return
    target_rel = rel(target)
    if target_rel not in text and f"../{target_rel}" not in text:
        errors.append(f"{rel(path)} missing link/reference to {target_rel}")


def current_head() -> str:
    proc = subprocess.run(["git", "rev-parse", "HEAD"], cwd=str(ROOT), capture_output=True, text=True)
    return proc.stdout.strip() if proc.returncode == 0 else ""


def git_show(ref_path: str) -> str:
    proc = subprocess.run(["git", "show", ref_path], cwd=str(ROOT), capture_output=True, text=True)
    return proc.stdout if proc.returncode == 0 else ""


def packet_candidate(text: str) -> str:
    match = re.search(r"Candidate commit:\s*`([0-9a-f]{40})`", text)
    return match.group(1) if match else ""


def memo_candidate(text: str) -> str:
    explicit = packet_candidate(text)
    if explicit:
        return explicit
    match = re.search(r"git tag -a\s+\S+\s+([0-9a-f]{40})", text)
    return match.group(1) if match else ""


def decision_line(text: str) -> str:
    match = re.search(r"^Decision:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip() if match else ""


def validate_expected_candidate(name: str, candidate: str, errors: list[str]) -> None:
    if candidate != EXPECTED_CANDIDATE_COMMIT:
        errors.append(
            f"{name} candidate must be {EXPECTED_CANDIDATE_COMMIT}, got {candidate or 'missing'}"
        )


def validate_fresh_summary(errors: list[str]) -> dict[str, Any]:
    data = read_json(FRESH_SUMMARY, errors)
    if not data:
        return {}
    if data.get("schema_version") != FRESH_SCHEMA:
        errors.append(f"fresh install schema mismatch: {data.get('schema_version')}")
    if data.get("status") not in {"pass", "blocked_fresh_install"}:
        errors.append(f"fresh install status must be pass or blocked_fresh_install for tag gate: {data.get('status')}")
    candidate = str(data.get("candidate_commit", ""))
    if not re.fullmatch(r"[0-9a-f]{40}", candidate):
        errors.append(f"fresh install candidate must be full SHA: {candidate}")
    validate_expected_candidate("fresh install summary", candidate, errors)
    if data.get("status") == "pass":
        commands = {str(item.get("command", "")).split()[0] for item in data.get("commands", [])}
        for required in ("anti-slop-lineage", "anti-slop-pr", "anti-slop-pr-event", "anti-slop-claims", "anti-slop-run"):
            if required not in commands:
                errors.append(f"fresh install missing command self-test: {required}")
        if data.get("report_mode_demo", {}).get("fabricated_ref_exposed") is not True:
            errors.append("fresh install summary must expose a fabricated report-mode ref")
    text = json.dumps(data, sort_keys=True)
    for forbidden in (str(ROOT), "/Users/", "/private/var/", "GITHUB_TOKEN", "OPENAI_API_KEY", "ANTHROPIC_API_KEY"):
        if forbidden in text:
            errors.append(f"{rel(FRESH_SUMMARY)} contains forbidden private/token-like snippet: {forbidden}")
    if not FRESH_MD.is_file():
        errors.append(f"missing fresh install Markdown summary: {rel(FRESH_MD)}")
    return data


def validate_tag_summary(errors: list[str]) -> dict[str, Any]:
    data = read_json(TAG_SUMMARY, errors)
    if not data:
        return {}
    if data.get("schema_version") != TAG_SCHEMA:
        errors.append(f"tag install schema mismatch: {data.get('schema_version')}")
    if data.get("status") != "pass":
        errors.append(f"tag install status must be pass for release finalization: {data.get('status')}")
    if data.get("tag_name") != TAG_NAME:
        errors.append(f"tag install summary must use {TAG_NAME}: {data.get('tag_name')}")
    target = str(data.get("target_commit", ""))
    if not re.fullmatch(r"[0-9a-f]{40}", target):
        errors.append(f"tag install target must be full SHA: {target}")
    validate_expected_candidate("tag install summary", target, errors)
    if data.get("status") == "pass":
        commands = {str(item.get("command", "")).split()[0] for item in data.get("commands", [])}
        for required in ("anti-slop-lineage", "anti-slop-pr", "anti-slop-pr-event", "anti-slop-claims", "anti-slop-run"):
            if required not in commands:
                errors.append(f"tag install missing command self-test: {required}")
        if data.get("report_mode_demo", {}).get("fabricated_ref_exposed") is not True:
            errors.append("tag install summary must expose a fabricated report-mode ref")
        source_docs = data.get("tag_source_docs", {})
        if source_docs.get("status") != "stale_pre_finalization_docs":
            errors.append("tag install summary must disclose stale pre-finalization tag-source docs")
        if source_docs.get("candidate_commit") != STALE_TAG_DOC_CANDIDATE:
            errors.append("tag install summary must record stale PR #44 source-doc candidate")
    text = json.dumps(data, sort_keys=True)
    for forbidden in (str(ROOT), "/Users/", "/private/var/", "GITHUB_TOKEN", "OPENAI_API_KEY", "ANTHROPIC_API_KEY"):
        if forbidden in text:
            errors.append(f"{rel(TAG_SUMMARY)} contains forbidden private/token-like snippet: {forbidden}")
    if not TAG_MD.is_file():
        errors.append(f"missing tag install Markdown summary: {rel(TAG_MD)}")
    else:
        tag_md = normalize_ws(TAG_MD.read_text(encoding="utf-8"))
        for snippet in STALE_TAG_SOURCE_DISCLOSURE:
            if normalize_ws(snippet) not in tag_md:
                errors.append(f"{rel(TAG_MD)} missing stale-source disclosure snippet: {snippet}")
    return data


def check_packet(errors: list[str]) -> None:
    text = read(PACKET, errors)
    if not text:
        return
    decision = decision_line(text)
    if decision not in ALLOWED_PACKET_DECISIONS:
        errors.append(f"{rel(PACKET)} decision must be one of {sorted(ALLOWED_PACKET_DECISIONS)}")
    candidate = packet_candidate(text)
    if not candidate:
        errors.append(f"{rel(PACKET)} missing full Candidate commit line")
    validate_expected_candidate("tag packet", candidate, errors)
    fresh = validate_fresh_summary(errors)
    if fresh and candidate and fresh.get("candidate_commit") != candidate:
        errors.append("tag packet candidate commit must match fresh install summary")
    if decision == "tag_created_no_outreach":
        tag = validate_tag_summary(errors)
        if tag and candidate and tag.get("target_commit") != candidate:
            errors.append("tag packet candidate commit must match tag install summary")
        state_snippets = [
            "Tag status: `anti-slop-receipts-v0.1.0` created and pushed",
            "Tag install smoke: PASS",
            rel(TAG_SUMMARY),
        ]
    else:
        state_snippets = ["No tag has been created"]
    for snippet in [
        "No GitHub release has been created",
        "operator approval required",
        "CI status: green",
        "Fresh install smoke: PASS",
        "Real checkout evidence: PASS",
        "Command receipt dogfood: PASS",
        "external adopter install success: UNKNOWN",
        "maintainer keep-rate: UNKNOWN",
        "platform clone risk: UNKNOWN",
        "no outreach",
        "no enforcement workflow",
        "deterministic reference/receipt resolution only",
        BOUNDARY,
        rel(FRESH_SUMMARY),
        rel(REAL_CHECKOUT),
        rel(REAL_ACTIONABILITY),
        rel(REAL_DOGFOOD),
        rel(KILL),
        *state_snippets,
    ]:
        if snippet not in text:
            errors.append(f"{rel(PACKET)} missing snippet: {snippet}")


def check_memo(errors: list[str]) -> None:
    text = read(MEMO, errors)
    if not text:
        return
    decision = decision_line(text)
    if decision not in ALLOWED_OPERATOR_DECISIONS:
        errors.append(f"{rel(MEMO)} decision must be one of {sorted(ALLOWED_OPERATOR_DECISIONS)}")
    candidate = memo_candidate(text)
    validate_expected_candidate("operator memo", candidate, errors)
    if decision == "tag_created_no_outreach":
        state_snippets = [
            "Tag status: `anti-slop-receipts-v0.1.0` created and pushed",
            "Exact tag target",
            "No GitHub release",
        ]
    else:
        state_snippets = [
            "Exact operator action needed next",
            "Do not run this automatically",
            "No tag has been created",
        ]
    for snippet in [
        "No outreach",
        "No enforcement",
        "external adopter install success: UNKNOWN",
        "maintainer keep-rate: UNKNOWN",
        "platform clone risk: UNKNOWN",
        "deterministic reference/receipt resolution only",
        BOUNDARY,
        *state_snippets,
    ]:
        if snippet not in text:
            errors.append(f"{rel(MEMO)} missing snippet: {snippet}")


def check_release_language(errors: list[str]) -> None:
    for path in RELEASE_FACING:
        text = read(path, errors)
        if not text:
            continue
        lines = text.splitlines()
        for number, line in enumerate(lines, start=1):
            previous = " ".join(lines[max(0, number - 4):number - 1])
            context = f"{previous} {line}"
            lower = re.sub(r"[*_`]", "", context.lower())
            line_lower = re.sub(r"[*_`]", "", line.lower())
            if re.search(r"\bproves?\b", line_lower):
                allowed = (
                    "does not prove" in lower
                    or "do not prove" in lower
                    or "not prove" in lower
                    or "cannot prove" in lower
                    or "proves only" in lower
                    or "prove only" in lower
                )
                if not allowed:
                    errors.append(f"{rel(path)}:{number} has unbounded prove/proves language")
            if "slop detector" in line_lower and not any(marker in lower for marker in ("not", "do not", "no ")):
                errors.append(f"{rel(path)}:{number} drifts into broad slop-detector wording")
            for term in ("source truth", "advice quality"):
                if term in line_lower and not any(marker in lower for marker in ("not", "does not", "do not", "no ")):
                    errors.append(f"{rel(path)}:{number} has unbounded {term} language")
        for snippet in ("no outreach", "operator approval", "deterministic reference/receipt resolution only"):
            if snippet not in text.lower():
                errors.append(f"{rel(path)} missing release-boundary snippet: {snippet}")


def check_docs_links(errors: list[str]) -> None:
    packet_text = read(PACKET, errors)
    final_tag_state = decision_line(packet_text) == "tag_created_no_outreach"
    for path in (README, INSTALL, LLMS, KB_INDEX):
        targets = [PACKET, MEMO, FRESH_MD]
        if final_tag_state:
            targets.append(TAG_MD)
        for target in targets:
            require_link(path, target, errors)
    log_snippets = [
        "CORE-991",
        "CORE-992",
        "CORE-993",
        "CORE-994",
        "tag-approval-check",
        "fresh-install-smoke",
    ]
    if final_tag_state:
        log_snippets.extend(["CORE-995", "CORE-996", "CORE-997", "CORE-998", "tag-install-smoke"])
    require_snippets(KB_LOG, log_snippets, errors)


def check_stale_tag_source_disclosure(errors: list[str]) -> None:
    tag_packet = git_show(f"{TAG_NAME}:docs/tag-approval-packet.md")
    for snippet in [
        "Decision: ready_to_request_operator_tag",
        STALE_TAG_DOC_CANDIDATE,
        "No tag has been created",
    ]:
        if snippet not in tag_packet:
            errors.append(f"{TAG_NAME} embedded tag packet no longer shows expected stale-source marker: {snippet}")

    for path in STALE_TAG_SOURCE_DOCS:
        require_normalized_snippets(path, STALE_TAG_SOURCE_DISCLOSURE, errors)
    for path in STALE_TAG_SOURCE_LINKS:
        require_normalized_snippets(
            path,
            [
                "tag's embedded docs predate PR #46 finalization",
                "GitHub release from v0.1.0 requires explicit disclosure",
                "anti-slop-receipts-v0.1.1",
            ],
            errors,
        )


def check_supporting_evidence(errors: list[str]) -> None:
    real = read_json(REAL_CHECKOUT, errors)
    action = read_json(REAL_ACTIONABILITY, errors)
    dogfood = read_json(REAL_DOGFOOD, errors)
    kill = read_json(KILL, errors)
    if real and real.get("status") != "real_checkout_useful":
        errors.append(f"real checkout evidence must remain useful: {real.get('status')}")
    if action and action.get("summary", {}).get("useful_findings_status") != "PASS":
        errors.append("real checkout actionability must remain PASS")
    if dogfood and dogfood.get("status") != "pass":
        errors.append("real command receipt dogfood must remain pass")
    if kill:
        unknown_ids = {
            item.get("id") for item in kill.get("criteria", [])
            if item.get("status") == "UNKNOWN"
        }
        for required in ("install_success_below_70_percent", "maintainer_keep_rate_zero_of_10", "platform_clone_risk"):
            if required not in unknown_ids:
                errors.append(f"kill criteria must keep {required} UNKNOWN")


def main() -> int:
    errors: list[str] = []
    check_packet(errors)
    check_memo(errors)
    check_release_language(errors)
    check_docs_links(errors)
    check_stale_tag_source_disclosure(errors)
    check_supporting_evidence(errors)
    if errors:
        print("TAG APPROVAL CHECK FAILED:")
        for error in errors:
            print(f"  - {error}")
        return 1
    print(
        "TAG APPROVAL CHECK PASSED: candidate consistency, required install "
        "proof, release language, and residual UNKNOWNs are covered."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
