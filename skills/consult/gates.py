#!/usr/bin/env python3
"""Deterministic gates for the `consult` Skill.

Runs after synthesis, before output reaches the user. Each gate returns
(pass: bool, reason: str). The Skill retries the synthesis once on failure
with explicit guidance; second failure falls back to `## Gap` output.

Gates implemented (Day 4 set):
  1. gate_citations            — at least one [page-id] present
  2. gate_caveats              — a ## Caveats or ## Gap section present
  3. gate_banned_phrases       — no marketing words or LLM-tells
  4. gate_number_verification  — cited figures appear in retrieved cards
  5. gate_no_fabricated_citations — every [page-id] is in the retrieval set

Exit codes:
  0 — all gates pass
  1 — one or more gates failed (failures summarized on stderr)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


# ---------------------------------------------------------------- regex helpers

# Page-id pattern: prefix-followed-by-hyphens, lowercase + digits.
# Covers src-book-*, src-doc-*, paper-*, repo-*, pat-*, guard-*, tech-*,
# concept-*, cap-*, sys-*, playbook-*, adr-*, prd-*, epic-*, iss-*, risk-*,
# rev-*, q-YYYYMMDD-*, wb-*, etc.
CITATION_RE = re.compile(r"\[([a-z][a-z0-9]*(?:-[a-z0-9]+)+)\]")

# Numeric figure patterns — conservative; tolerates false negatives over false
# positives. Each pattern's group(0) is the raw match.
NUMERIC_PATTERNS = [
    re.compile(r"\d+(?:\.\d+)?\s*%"),                      # percentages
    re.compile(r"\$\s*\d+(?:[,.]\d+)*[KMB]?"),             # currency
    re.compile(r"\d{1,3}(?:,\d{3})+(?:\.\d+)?"),           # comma-numbers
    re.compile(r"(?<![\w.])\d+\.\d+(?![\w.])"),            # bare decimals
    re.compile(r"(?<![\w.\-])\d{2,}(?![\w.\-])"),          # bare integers (≥2)
]


def _digit_core(s: str) -> str:
    """Return just the digits and decimal point from a numeric match."""
    return re.sub(r"[^\d.]", "", s)


def _whole_word_present(haystack_lower: str, needle_lower: str) -> bool:
    """Whole-word substring check that handles hyphens, apostrophes, spaces."""
    idx = 0
    n = len(haystack_lower)
    needle_len = len(needle_lower)
    while idx <= n - needle_len:
        pos = haystack_lower.find(needle_lower, idx)
        if pos == -1:
            return False
        before_ok = pos == 0 or not (
            haystack_lower[pos - 1].isalnum() or haystack_lower[pos - 1] == "_"
        )
        end = pos + needle_len
        after_ok = end == n or not (
            haystack_lower[end].isalnum() or haystack_lower[end] == "_"
        )
        if before_ok and after_ok:
            return True
        idx = pos + 1
    return False


# ---------------------------------------------------------------- gates

BANNED_PHRASES: list[str] = [
    # Marketing words
    "comprehensive", "powerful", "robust", "seamless", "deep dive",
    "game-changing", "essential", "easy", "revolutionary",
    "cutting-edge", "world-class",
    # LLM-tells
    "as an AI", "as a language model", "I'm just", "in conclusion", "it depends",
]


def gate_citations(synthesis: str) -> tuple[bool, str]:
    matches = CITATION_RE.findall(synthesis)
    if not matches:
        return False, "no [page-id] citations found in synthesis"
    return True, ""


def gate_caveats(synthesis: str) -> tuple[bool, str]:
    """Pass if a ## Caveats or ## Gap H2 heading is present."""
    if re.search(r"(?m)^##\s+Caveats\b", synthesis):
        return True, ""
    if re.search(r"(?m)^##\s+Gap\b", synthesis):
        return True, ""
    return False, "neither '## Caveats' nor '## Gap' section present"


def gate_banned_phrases(synthesis: str) -> tuple[bool, str]:
    lower = synthesis.lower()
    hits: list[str] = []
    for phrase in BANNED_PHRASES:
        if _whole_word_present(lower, phrase.lower()):
            hits.append(phrase)
    if hits:
        return False, f"banned phrases found: {hits}"
    return True, ""


def gate_number_verification(
    synthesis: str, card_texts: list[str]
) -> tuple[bool, str]:
    """Every numeric figure in the synthesis must appear in at least one card.

    Tolerates trivial format variations: "63%" matches "63 percent"; comma
    differences ("23,000" vs "23000") are normalized.
    """
    if not card_texts:
        # No cards to verify against — let other gates handle this case.
        return True, ""

    joined = " ".join(card_texts)
    joined_lower = joined.lower()
    joined_nocomma = re.sub(r"(\d),(\d)", r"\1\2", joined)
    joined_nocomma_lower = joined_nocomma.lower()

    figures: list[str] = []
    seen: set[str] = set()
    for pat in NUMERIC_PATTERNS:
        for m in pat.finditer(synthesis):
            raw = m.group(0).strip()
            if raw in seen:
                continue
            seen.add(raw)
            figures.append(raw)

    unverified: list[str] = []
    for raw in figures:
        # 1. Verbatim substring.
        if raw in joined:
            continue
        # 2. Normalized (commas stripped).
        raw_nocomma = raw.replace(",", "")
        if raw_nocomma in joined_nocomma:
            continue
        # 3. Percent-vs-spelled.
        if raw.rstrip().endswith("%"):
            core = _digit_core(raw)
            spelled = f"{core} percent"
            if spelled in joined_lower:
                continue
            # Also try "core%" without surrounding whitespace
            if f"{core}%" in joined:
                continue
        # 4. Digit core fallback (case-insensitive).
        core = _digit_core(raw)
        if core and core in joined_nocomma_lower:
            continue
        unverified.append(raw)

    if unverified:
        return False, f"numeric figures not found in retrieved cards: {unverified}"
    return True, ""


def gate_no_fabricated_citations(
    synthesis: str, card_ids: list[str]
) -> tuple[bool, str]:
    if not card_ids:
        return True, ""
    valid = set(card_ids)
    cited = set(CITATION_RE.findall(synthesis))
    invented = sorted(cited - valid)
    if invented:
        return False, f"citations not in retrieval set: {invented}"
    return True, ""


# ---------------------------------------------------------------- CLI

def _read_text(p: Path) -> str:
    try:
        return p.read_text(encoding="utf-8")
    except Exception as e:
        print(f"error reading {p}: {e}", file=sys.stderr)
        sys.exit(2)


def _card_id_from_path(p: Path) -> str:
    return p.stem


def run_all_gates(
    synthesis: str, card_texts: list[str], card_ids: list[str]
) -> list[tuple[str, bool, str]]:
    return [
        ("citations", *gate_citations(synthesis)),
        ("caveats", *gate_caveats(synthesis)),
        ("banned_phrases", *gate_banned_phrases(synthesis)),
        ("number_verification", *gate_number_verification(synthesis, card_texts)),
        ("no_fabricated_citations", *gate_no_fabricated_citations(synthesis, card_ids)),
    ]


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--synthesis", required=True, type=Path,
                    help="path to the synthesis markdown file")
    ap.add_argument("--cards", nargs="*", default=[], type=Path,
                    help="paths to retrieved card files (one per top-N page)")
    ap.add_argument("--quiet", action="store_true",
                    help="suppress per-gate output on success")
    args = ap.parse_args(argv)

    synthesis = _read_text(args.synthesis)
    card_texts = [_read_text(p) for p in args.cards]
    card_ids = [_card_id_from_path(p) for p in args.cards]

    results = run_all_gates(synthesis, card_texts, card_ids)

    passed = [r for r in results if r[1]]
    failed = [r for r in results if not r[1]]

    if failed:
        print(f"FAIL — {len(failed)}/{len(results)} gates failed:", file=sys.stderr)
        for name, _, reason in failed:
            print(f"  - {name}: {reason}", file=sys.stderr)
        if passed and not args.quiet:
            print("\npassed gates:", file=sys.stderr)
            for name, _, _ in passed:
                print(f"  - {name}", file=sys.stderr)
        return 1

    if not args.quiet:
        print(f"PASS — {len(passed)}/{len(results)} gates passed")
        for name, _, _ in passed:
            print(f"  - {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
