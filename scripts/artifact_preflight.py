#!/usr/bin/env python3
"""Read-only preflight checks for books-kb artifacts.

This script turns the highest-value artifact guardrails into a report:
- source cards do not use book maps as evidence;
- claim/tension cards cite existing reviewed source cards;
- eval lineage avoids book maps and cites reviewed artifacts;
- eval case, score-sheet, and model-output receipts agree;
- frozen eval run packets that use calibration anchors have accepted anchors;
- WIP counts are visible against docs/wip-limits.md caps;
- public artifact files avoid private path markers and raw-source extensions.

By default it is report-only and always exits 0, so false positives can be
studied before this becomes part of the closing-gate suite. With `--strict` it
exits nonzero when blockers are found (warnings, including WIP-cap warnings,
never fail). `--self-test` runs the deterministic checks for the
judge-independence guard and exits nonzero on a regression. It changes nothing,
reads no local-only source files, makes no model/API calls, and creates no
artifacts.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys

MIN_BENCHMARK_RUNS = 3  # per docs/eval-benchmark-upgrade.md

ROOT = Path(__file__).resolve().parents[1]

BOOK_MAPS_DIR = ROOT / "corpus" / "book-maps"
SOURCE_CARDS_DIR = ROOT / "corpus" / "source-cards"
CLAIM_CARDS_DIR = ROOT / "corpus" / "claim-tension-cards"
CANON_CANDIDATES_DIR = ROOT / "corpus" / "canon-candidates"
EVALS_DIR = ROOT / "evals"
ACQ_REGISTRY = ROOT / "corpus" / "manifests" / "acquisition-registry.yaml"

PUBLIC_SWEEP_DIRS = [
    ROOT / "corpus",
    ROOT / "kb",
    ROOT / "docs",
    ROOT / "evals",
    ROOT / "runs",
]

CARD_ID_RE = re.compile(r"\bBK-\d{4}-card-\d{3}\b")
RAW_SOURCE_EXT_RE = re.compile(r"\.(epub|pdf|mobi|azw|azw3|djvu|cbz|cbr)\b", re.IGNORECASE)
PRIVATE_MARKERS = ("/Users/", "Desktop", "Archive.zip")
RESULT_STATUSES = {
    "partial",
    "inconclusive",
    "falsified",
    "dry_run_supported",
    "benchmark_supported",
}
WIP_CAPS = {
    "acquired_unmapped": 20,
    "book_maps_awaiting_review": 5,
    "source_cards_awaiting_review": 20,
    "claim_tension_awaiting_review": 10,
    "canon_candidates_awaiting_decision": 3,
}


@dataclass
class Finding:
    severity: str
    path: Path | None
    message: str

    def render(self) -> str:
        prefix = f"[{self.severity}]"
        if self.path is None:
            return f"{prefix} {self.message}"
        return f"{prefix} {rel(self.path)} — {self.message}"


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_scalar(value: str):
    value = value.strip()
    if value in {"", "null", "Null", "NULL", "~"}:
        return None
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    return strip_quotes(value)


def read_frontmatter(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    lines = read_text(path).splitlines()
    if not lines or lines[0].strip() != "---":
        return fields
    for raw in lines[1:]:
        if raw.strip() == "---":
            break
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw[:1] in (" ", "\t") or ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        fields[key.strip()] = strip_quotes(value)
    return fields


def parse_yaml_list(text: str, list_key: str) -> list[dict]:
    items: list[dict] = []
    in_list = False
    cur: dict | None = None
    nested_key: str | None = None
    nested_indent: int | None = None

    for raw in text.splitlines():
        line = raw.split("#", 1)[0].rstrip() if not ("'" in raw or '"' in raw) else raw.rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        content = line.strip()

        if not in_list:
            if content.startswith(f"{list_key}:"):
                in_list = True
            continue
        if indent == 0 and not content.startswith("- "):
            break

        if content.startswith("- "):
            if cur is not None:
                items.append(cur)
            cur = {}
            nested_key = None
            nested_indent = None
            rest = content[2:].strip()
            if rest and ":" in rest:
                key, value = rest.split(":", 1)
                if value.strip() == "":
                    cur[key.strip()] = {}
                    nested_key, nested_indent = key.strip(), indent
                else:
                    cur[key.strip()] = parse_scalar(value)
            continue

        if cur is None or ":" not in content:
            continue
        key, value = content.split(":", 1)
        key, value = key.strip(), value.strip()
        if nested_key and nested_indent is not None and indent > nested_indent:
            inner = cur.setdefault(nested_key, {})
            if isinstance(inner, dict):
                inner[key] = parse_scalar(value)
            continue
        if value == "":
            cur[key] = {}
            nested_key, nested_indent = key, indent
        else:
            cur[key] = parse_scalar(value)
            nested_key = nested_indent = None

    if cur is not None:
        items.append(cur)
    return items


def section(text: str, heading: str) -> str:
    lines = text.splitlines()
    out: list[str] = []
    capture = False
    wanted = heading.strip().lower()
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("## "):
            if capture:
                break
            capture = stripped.lower() == wanted
            continue
        if capture:
            out.append(line)
    return "\n".join(out)


def case_model_conditions(case_text: str) -> list[str]:
    """Parse the declared model_conditions list from a case.md frontmatter.

    Handles both a block list and an inline `[a, b]` form. Returns [] when no
    model_conditions key is present.
    """
    lines = case_text.splitlines()
    if not lines or lines[0].strip() != "---":
        return []
    fm_end = None
    for idx, raw in enumerate(lines[1:], start=1):
        if raw.strip() == "---":
            fm_end = idx
            break
    if fm_end is None:
        return []

    conds: list[str] = []
    collecting = False
    for raw in lines[1:fm_end]:
        stripped = raw.strip()
        indented = raw[:1] in (" ", "\t")
        if not collecting:
            if not indented and stripped.startswith("model_conditions:"):
                inline = stripped.split(":", 1)[1].strip()
                if inline:
                    inline = inline.strip("[]")
                    return [c.strip().strip("'\"") for c in inline.split(",") if c.strip()]
                collecting = True
            continue
        if indented and stripped.startswith("- "):
            conds.append(stripped[2:].strip().strip("'\""))
        elif not indented and stripped:
            break
    return conds


def result_status(score_sheet: Path) -> str | None:
    lines = read_text(score_sheet).splitlines()
    for i, raw in enumerate(lines):
        if raw.strip() == "## Result":
            for follow in lines[i + 1:]:
                if follow.strip():
                    return follow.strip().split()[0].strip("`*—-")
    return None


def output_is_real(fm: dict[str, str]) -> bool:
    """True only when a model-output receipt clearly records a real model run."""
    notes = (fm.get("operator_notes") or "").lower()
    if any(p in notes for p in ("real local-model run", "real external model run",
                                "real model run", "genuine local-model output")):
        return True
    if (fm.get("runtime") or "").strip() and "simulation" not in notes and "simulated" not in notes:
        return True
    return False


LONG_PROMPT_MARKERS = ("vanilla_long_prompt", "long_prompt", "long-prompt",
                       "equal_length", "equal-length")

# A judge_independence value affirms an independent judge ONLY when it matches
# one of these controlled values exactly (after lowercasing and treating '-'
# and ' ' as '_'). A loose 'independent' or 'human' inside arbitrary prose does
# not affirm, and any negation/limitation disqualifies the value outright.
JUDGE_INDEPENDENCE_AFFIRMATIVE = frozenset({
    "true", "yes",
    "independent", "independent_judge", "third_party",
    "human_independent", "independent_human",
    "two_judge", "independent_third_party",
    # Canonical phrase used by the v3 hosted-judge receipt; "orchestrating"
    # does not match the "orchestrator" negation marker (different stems), so
    # this exact allowlist entry affirms without conflict.
    "independent_of_the_orchestrating_agent",
})
# Whole-token negations, checked against the '_'-split value.
JUDGE_INDEPENDENCE_NEGATION_TOKENS = frozenset({"no", "not", "non"})
# Substring negations / limitations, checked against the normalized value.
JUDGE_INDEPENDENCE_NEGATION_MARKERS = (
    "false", "without", "same_agent", "orchestrator",
    "model_family_separated", "family_separated",
)


def is_long_prompt_condition(name: str) -> bool:
    """True if a condition name marks the equal-length / long-prompt control."""
    lowered = name.lower()
    return any(marker in lowered for marker in LONG_PROMPT_MARKERS)


def value_affirms_independence(value: str | None) -> bool:
    """True only for an exact, controlled affirmative judge_independence value.

    The value affirms an independent judge only when, after lowercasing and
    treating '-' and ' ' as '_', it matches one of JUDGE_INDEPENDENCE_AFFIRMATIVE
    exactly. Negations and limitations — 'no independent judge', 'non-independent',
    'without independent judge', 'model-family-separated only', 'same agent',
    'orchestrator' — never affirm, even when an affirmative word also appears.
    A loose 'independent' or 'human' inside arbitrary prose never affirms.
    Absence of a value is not an affirmation.
    """
    raw = (value or "").strip().lower()
    if not raw:
        return False
    normalized = raw.replace("-", "_").replace(" ", "_").replace("/", "_")
    while "__" in normalized:
        normalized = normalized.replace("__", "_")
    normalized = normalized.strip("_")
    if not normalized:
        return False
    tokens = normalized.split("_")
    if any(tok in JUDGE_INDEPENDENCE_NEGATION_TOKENS for tok in tokens):
        return False
    if any(marker in normalized for marker in JUDGE_INDEPENDENCE_NEGATION_MARKERS):
        return False
    return normalized in JUDGE_INDEPENDENCE_AFFIRMATIVE


def judge_independence_affirmed(model_dir: Path, score_sheet: Path) -> bool:
    """True only when an explicit judge_independence record (in the score sheet
    or a model-output receipt) affirms an independent / human / two-judge setup.
    Absence of the record is not an affirmation."""
    if score_sheet.exists():
        sfm = read_frontmatter(score_sheet)
        for key in ("judge_independence", "judge_independent"):
            if value_affirms_independence(sfm.get(key)):
                return True
    if model_dir.exists():
        for path in sorted(model_dir.glob("*.md")):
            if path.name.startswith("."):
                continue
            ofm = read_frontmatter(path)
            for key in ("judge_independence", "judge_independent"):
                if value_affirms_independence(ofm.get(key)):
                    return True
    return False


def run_packet_is_frozen(fm: dict[str, str]) -> bool:
    status = (fm.get("status") or "").strip().lower()
    if status.startswith("frozen") or "frozen_run" in status:
        return True
    return bool((fm.get("frozen") or "").strip())


def run_packet_uses_calibration_anchors(run_packet: Path) -> bool:
    text = read_text(run_packet)
    return (
        "calibration-anchors.md" in text
        or (run_packet.parent / "judge-packet" / "calibration-anchors.md").exists()
    )


def run_self_test() -> int:
    """Deterministic self-test for value_affirms_independence(). Stdlib only.

    Run with `python3 scripts/artifact_preflight.py --self-test`. Exits nonzero
    on any regression — so a future loosening of the judge-independence guard
    is caught before a benchmark_supported Result could slip past --strict.
    """
    affirmative = [
        "true", "yes", "independent", "independent_judge",
        "third_party", "third-party", "two_judge", "two-judge",
        "human_independent", "independent_human", "independent_third_party",
        "  Independent_Judge  ",  # case/whitespace-insensitive
        # The canonical phrase used by the v3 hosted-judge receipts:
        "independent of the orchestrating agent",
        "Independent of the orchestrating agent",
    ]
    negative = [
        "", "   ", "false", "not independent", "non-independent",
        "no independent judge", "no human judge", "without independent judge",
        "model-family-separated only", "model_family_separated",
        "same agent", "orchestrator", "same agent/orchestrator",
        "human", "judge", "the judge was independent of the generator",
        "no", "not", "non",
        # Negated / limited values that must never affirm even though they
        # contain the substring "independent":
        "not_independent_orchestrator_judge",
        "same_agent_independent",
        "no_independent_judge", "without_independent_judge",
        "non_independent",
    ]
    failures: list[str] = []
    for v in affirmative:
        if not value_affirms_independence(v):
            failures.append(f"expected affirmative, got False: {v!r}")
    for v in negative:
        if value_affirms_independence(v):
            failures.append(f"expected non-affirmative, got True: {v!r}")

    print("== artifact_preflight self-test: value_affirms_independence ==")
    print(f"Affirmative cases: {len(affirmative)}    Negative cases: {len(negative)}")
    if failures:
        for line in failures:
            print(f"  FAIL {line}")
        print(f"Self-test FAILED ({len(failures)} failure(s)).")
        return 1
    print("All cases passed. Self-test OK.")
    return 0


def book_map_line_is_evidence(line: str) -> bool:
    lowered = line.lower()
    if "book map" not in lowered and "book-map" not in lowered and "corpus/book-maps" not in lowered:
        return False
    allowed_phrases = (
        "no book map",
        "no book maps",
        "book maps named only as discovery",
        "discovery aid",
        "discovery hint",
        "discovery-only",
        "not evidence",
        "never evidence",
    )
    return not any(phrase in lowered for phrase in allowed_phrases)


def source_card_inventory() -> dict[str, tuple[Path, str | None]]:
    cards: dict[str, tuple[Path, str | None]] = {}
    for path in sorted(SOURCE_CARDS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        fm = read_frontmatter(path)
        card_id = fm.get("card_id") or path.stem
        cards[card_id] = (path, fm.get("operator_review_status"))
    return cards


def claim_card_inventory() -> dict[str, tuple[Path, str | None]]:
    cards: dict[str, tuple[Path, str | None]] = {}
    for path in sorted(CLAIM_CARDS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        fm = read_frontmatter(path)
        card_id = fm.get("card_id") or path.stem
        cards[card_id] = (path, fm.get("operator_review_status"))
    return cards


def check_source_cards(findings: list[Finding]) -> None:
    for path in sorted(SOURCE_CARDS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        text = read_text(path)
        for heading in ("## Claim", "## Evidence locator", "## Paraphrase"):
            body = section(text, heading)
            for line in body.splitlines():
                if book_map_line_is_evidence(line):
                    findings.append(Finding(
                        "BLOCKER",
                        path,
                        f"{heading} appears to use a book map as evidence: {line.strip()[:160]}",
                    ))
        supports = section(text, "## Supports")
        for line in supports.splitlines():
            if book_map_line_is_evidence(line):
                findings.append(Finding(
                    "WARN",
                    path,
                    f"Supports mentions a book map without clear discovery-only language: {line.strip()[:160]}",
                ))


def check_claim_cards(
    findings: list[Finding],
    source_cards: dict[str, tuple[Path, str | None]],
) -> None:
    for path in sorted(CLAIM_CARDS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        text = read_text(path)
        refs = sorted(set(CARD_ID_RE.findall(text)))
        if not refs:
            findings.append(Finding("WARN", path, "no source-card IDs found"))
        for ref in refs:
            if ref not in source_cards:
                findings.append(Finding("BLOCKER", path, f"cites missing source card {ref}"))
                continue
            ref_path, status = source_cards[ref]
            if status != "reviewed":
                findings.append(Finding(
                    "BLOCKER",
                    path,
                    f"cites unreviewed source card {ref} ({rel(ref_path)} has operator_review_status={status})",
                ))
        for heading in ("## Source cards for Claim A", "## Source cards for Claim B"):
            body = section(text, heading)
            for line in body.splitlines():
                if book_map_line_is_evidence(line):
                    findings.append(Finding(
                        "BLOCKER",
                        path,
                        f"{heading} appears to cite a book map as evidence: {line.strip()[:160]}",
                    ))


def check_eval_cases(
    findings: list[Finding],
    source_cards: dict[str, tuple[Path, str | None]],
    claim_cards: dict[str, tuple[Path, str | None]],
) -> None:
    for case_path in sorted(EVALS_DIR.glob("*/*/case.md")):
        case_dir = case_path.parent
        score_sheet = case_dir / "score-sheet.md"
        model_dir = case_dir / "model-outputs"
        case_text = read_text(case_path)
        case_fm = read_frontmatter(case_path)
        score_fm = read_frontmatter(score_sheet) if score_sheet.exists() else {}

        if not score_sheet.exists():
            findings.append(Finding("BLOCKER", case_path, "missing score-sheet.md"))
            continue

        case_status = case_fm.get("scoring_status")
        score_status = score_fm.get("scoring_status")
        if case_status != score_status:
            findings.append(Finding(
                "BLOCKER",
                case_path,
                f"case scoring_status={case_status} but score-sheet scoring_status={score_status}",
            ))

        result = result_status(score_sheet)
        if result and result not in RESULT_STATUSES:
            findings.append(Finding("BLOCKER", score_sheet, f"unknown Result status {result!r}"))
        score_section = section(case_text, "## Score sheet")
        if result and result not in score_section:
            findings.append(Finding(
                "WARN",
                case_path,
                f"Score sheet section does not mention recorded Result {result!r}",
            ))

        listed = set(re.findall(r"model-outputs/([A-Za-z0-9_.-]+\.md)", case_text))
        actual = set()
        if model_dir.exists():
            actual = {
                p.name for p in model_dir.glob("*.md")
                if not p.name.startswith(".")
            }
        for missing in sorted(listed - actual):
            findings.append(Finding("BLOCKER", case_path, f"lists missing model output {missing}"))
        for unlisted in sorted(actual - listed):
            findings.append(Finding("BLOCKER", case_path, f"model output exists but is not listed: {unlisted}"))
        if actual and case_status == "unscored":
            findings.append(Finding("WARN", case_path, "model outputs exist but case scoring_status is unscored"))
        if not actual and case_status == "scored":
            findings.append(Finding("BLOCKER", case_path, "case is scored but no model-output files exist"))

        # A benchmark_supported Result must rest on real outputs for *every
        # declared* condition (>= MIN_BENCHMARK_RUNS real runs each, not just
        # whichever conditions happen to have files), carry an equal-length
        # control among the declared conditions, and have an affirmatively
        # independent judge (docs/eval-benchmark-upgrade.md, eval-lab-protocol.md).
        if result == "benchmark_supported":
            declared = case_model_conditions(case_text)
            real_by_cond: dict[str, int] = {}
            non_real = 0
            for name in sorted(actual):
                ofm = read_frontmatter(model_dir / name)
                cond = (ofm.get("model_condition")
                        or re.sub(r"-\d+$", "", Path(name).stem)).strip()
                if output_is_real(ofm):
                    real_by_cond[cond] = real_by_cond.get(cond, 0) + 1
                else:
                    non_real += 1
            if non_real:
                findings.append(Finding(
                    "BLOCKER", case_path,
                    f"Result is benchmark_supported but {non_real} model output(s) "
                    "are simulated or not classifiable as real runs",
                ))
            if not declared:
                findings.append(Finding(
                    "BLOCKER", case_path,
                    "Result is benchmark_supported but case.md declares no "
                    "model_conditions to verify real-run coverage against",
                ))
            thin = [c for c in declared if real_by_cond.get(c, 0) < MIN_BENCHMARK_RUNS]
            if thin:
                detail = ", ".join(f"{c} ({real_by_cond.get(c, 0)} real)" for c in thin)
                findings.append(Finding(
                    "BLOCKER", case_path,
                    f"Result is benchmark_supported but declared conditions with fewer "
                    f"than {MIN_BENCHMARK_RUNS} real runs: {detail}",
                ))
            if not any(is_long_prompt_condition(c) for c in declared):
                findings.append(Finding(
                    "BLOCKER", case_path,
                    "Result is benchmark_supported but no equal-length "
                    "(vanilla_long_prompt) control is among the declared conditions",
                ))
            if not judge_independence_affirmed(model_dir, score_sheet):
                findings.append(Finding(
                    "BLOCKER", case_path,
                    "Result is benchmark_supported but judge independence is not "
                    "affirmatively recorded in the model-output receipts or score sheet",
                ))

        lineage = section(case_text, "## Lineage")
        for line in lineage.splitlines():
            if book_map_line_is_evidence(line):
                findings.append(Finding(
                    "BLOCKER",
                    case_path,
                    f"Lineage appears to cite a book map: {line.strip()[:160]}",
                ))
        for ref in sorted(set(CARD_ID_RE.findall(lineage))):
            if ref not in source_cards:
                findings.append(Finding("BLOCKER", case_path, f"Lineage cites missing source card {ref}"))
                continue
            ref_path, status = source_cards[ref]
            if status != "reviewed":
                findings.append(Finding(
                    "BLOCKER",
                    case_path,
                    f"Lineage cites unreviewed source card {ref} ({rel(ref_path)} has operator_review_status={status})",
                ))
        for card_id, (card_path, status) in claim_cards.items():
            if card_id in lineage and status != "reviewed":
                findings.append(Finding(
                    "BLOCKER",
                    case_path,
                    f"Lineage cites unreviewed claim/tension card {card_id} ({rel(card_path)})",
                ))


def check_eval_run_packets(findings: list[Finding]) -> None:
    """Guard the pre-run calibration gate for evals that use anchor files."""
    for run_packet in sorted(EVALS_DIR.glob("*/*/run-packet.md")):
        fm = read_frontmatter(run_packet)
        if not run_packet_is_frozen(fm):
            continue
        if not run_packet_uses_calibration_anchors(run_packet):
            continue

        anchors = run_packet.parent / "judge-packet" / "calibration-anchors.md"
        if not anchors.exists():
            findings.append(Finding(
                "BLOCKER",
                run_packet,
                "run packet is frozen but references calibration anchors and "
                "judge-packet/calibration-anchors.md is missing",
            ))
            continue
        anchor_status = read_frontmatter(anchors).get("status")
        if anchor_status != "filled_pre_run":
            findings.append(Finding(
                "BLOCKER",
                run_packet,
                "run packet is frozen but calibration anchors are not "
                f"operator-accepted (status={anchor_status})",
            ))


def check_public_sweep(findings: list[Finding]) -> None:
    for base in PUBLIC_SWEEP_DIRS:
        if not base.exists():
            continue
        for path in sorted(p for p in base.rglob("*") if p.is_file()):
            if path.name.startswith("."):
                continue
            text = read_text(path)
            for marker in PRIVATE_MARKERS:
                if marker in text:
                    findings.append(Finding("BLOCKER", path, f"contains private marker {marker!r}"))
            match = RAW_SOURCE_EXT_RE.search(text)
            if match:
                findings.append(Finding("BLOCKER", path, f"contains raw-source extension marker {match.group(0)!r}"))


def count_unreviewed_markdown(directory: Path) -> int:
    if not directory.exists():
        return 0
    total = 0
    for path in directory.glob("*.md"):
        if path.name.startswith("_"):
            continue
        if read_frontmatter(path).get("operator_review_status") == "unreviewed":
            total += 1
    return total


def wip_report() -> list[tuple[str, int, int]]:
    mapped_sources = {
        p.stem for p in BOOK_MAPS_DIR.glob("*.md")
        if not p.name.startswith("_")
    }
    acquired_unmapped = 0
    if ACQ_REGISTRY.exists():
        for entry in parse_yaml_list(read_text(ACQ_REGISTRY), "entries"):
            if entry.get("acquisition_status") == "sourced" and entry.get("source_id") not in mapped_sources:
                acquired_unmapped += 1
    return [
        ("acquired_unmapped", acquired_unmapped, WIP_CAPS["acquired_unmapped"]),
        (
            "book_maps_awaiting_review",
            count_unreviewed_markdown(BOOK_MAPS_DIR),
            WIP_CAPS["book_maps_awaiting_review"],
        ),
        (
            "source_cards_awaiting_review",
            count_unreviewed_markdown(SOURCE_CARDS_DIR),
            WIP_CAPS["source_cards_awaiting_review"],
        ),
        (
            "claim_tension_awaiting_review",
            count_unreviewed_markdown(CLAIM_CARDS_DIR),
            WIP_CAPS["claim_tension_awaiting_review"],
        ),
        (
            "canon_candidates_awaiting_decision",
            count_unreviewed_markdown(CANON_CANDIDATES_DIR),
            WIP_CAPS["canon_candidates_awaiting_decision"],
        ),
    ]


def main() -> int:
    argv = sys.argv[1:]
    if "--self-test" in argv:
        return run_self_test()
    strict = "--strict" in argv
    findings: list[Finding] = []
    source_cards = source_card_inventory()
    claim_cards = claim_card_inventory()

    check_source_cards(findings)
    check_claim_cards(findings, source_cards)
    check_eval_cases(findings, source_cards, claim_cards)
    check_eval_run_packets(findings)
    check_public_sweep(findings)

    print("== Anti-Slop artifact preflight ==")
    if strict:
        print("Read-only report (--strict). Changes nothing; exits nonzero only when "
              "blockers are found — warnings never fail.")
    else:
        print("Read-only report. Changes nothing and always exits 0.")
    print("Scope: lineage, receipt consistency, WIP counts, and public-safety markers.")
    print()

    print("-- WIP counts --")
    for label, count, cap in wip_report():
        status = "OK" if count <= cap else "OVER CAP"
        print(f"{label:36} {count:3} / {cap:<3} {status}")
        if count > cap:
            findings.append(Finding("WARN", None, f"WIP cap exceeded: {label} is {count}/{cap}"))
    print()

    print("-- Findings --")
    if not findings:
        print("No findings.")
    else:
        for finding in findings:
            print(finding.render())
    print()

    blockers = sum(1 for finding in findings if finding.severity == "BLOCKER")
    warnings = sum(1 for finding in findings if finding.severity == "WARN")
    print("-- Summary --")
    print(f"Blockers: {blockers}")
    print(f"Warnings: {warnings}")
    if strict:
        exit_code = 1 if blockers else 0
        print("Mode: --strict (blockers fail; WIP and other warnings do not)")
        print(f"Exit status: {exit_code}")
        return exit_code
    print("Exit status: 0 (report-only; not a hard gate)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
