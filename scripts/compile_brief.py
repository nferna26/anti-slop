#!/usr/bin/env python3
"""Compile a non-canon decision brief from reviewed source/tension cards.

The brief is not advice and not canon. It is a public-safe, inspectable packet
of the reviewed card content that should constrain a later model answer:
claims, locators, scope conditions, misuse risks, and related tensions.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date
from pathlib import Path
import argparse
import re
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SOURCE_CARDS_DIR = ROOT / "corpus" / "source-cards"
CLAIM_CARDS_DIR = ROOT / "corpus" / "claim-tension-cards"


@dataclass(frozen=True)
class Card:
    card_id: str
    path: Path
    kind: str
    fields: dict[str, str]
    text: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def read_frontmatter(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    lines = text.splitlines()
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
            capture = stripped[3:].strip().lower() == wanted
            continue
        if capture:
            out.append(line)
    return "\n".join(out).strip()


def all_cards() -> dict[str, Card]:
    cards: dict[str, Card] = {}
    for path in sorted(SOURCE_CARDS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        text = read_text(path)
        fields = read_frontmatter(text)
        card_id = fields.get("card_id", path.stem)
        cards[card_id] = Card(card_id, path, "source_card", fields, text)
    for path in sorted(CLAIM_CARDS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        text = read_text(path)
        fields = read_frontmatter(text)
        card_id = fields.get("card_id", path.stem)
        cards[card_id] = Card(card_id, path, "claim_tension_card", fields, text)
        cards.setdefault(path.stem, cards[card_id])
    return cards


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def require_cards(ids: list[str], include_unreviewed: bool) -> list[Card]:
    known = all_cards()
    cards: list[Card] = []
    missing: list[str] = []
    blocked: list[str] = []
    for card_id in ids:
        card = known.get(card_id)
        if card is None:
            missing.append(card_id)
            continue
        status = card.fields.get("operator_review_status", "")
        if status != "reviewed" and not include_unreviewed:
            blocked.append(f"{card_id} ({status or 'missing review status'})")
            continue
        cards.append(card)
    if missing or blocked:
        if missing:
            print("Unknown card IDs:", ", ".join(missing), file=sys.stderr)
        if blocked:
            print(
                "Unreviewed cards excluded by default:",
                ", ".join(blocked),
                file=sys.stderr,
            )
            print("Pass --include-unreviewed to include them with warnings.", file=sys.stderr)
        raise SystemExit(2)
    return cards


def related_reviewed_tensions(selected: list[Card]) -> list[Card]:
    selected_ids = {card.card_id for card in selected}
    already = set(selected_ids)
    related: list[Card] = []
    for path in sorted(CLAIM_CARDS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        text = read_text(path)
        fields = read_frontmatter(text)
        card_id = fields.get("card_id", path.stem)
        if card_id in already:
            continue
        if fields.get("operator_review_status") != "reviewed":
            continue
        if any(selected_id in text for selected_id in selected_ids):
            related.append(Card(card_id, path, "claim_tension_card", fields, text))
    return related


def compact(text: str) -> str:
    if not text:
        return "None recorded."
    return text.strip()


def render_source_card(card: Card) -> str:
    claim = compact(section(card.text, "Claim"))
    locator = compact(section(card.text, "Evidence locator"))
    scope = compact(section(card.text, "Scope conditions"))
    misuse = compact(section(card.text, "Misuse risk"))
    title = card.fields.get("title", card.card_id)
    review = card.fields.get("operator_review_status", "unknown")
    return "\n".join(
        [
            f"### {card.card_id} - {title}",
            "",
            f"- Path: `{rel(card.path)}`",
            f"- Source: `{card.fields.get('source_id', 'unknown')}`",
            f"- Locator: {card.fields.get('locator', 'unknown')}",
            f"- Review status: `{review}`",
            "",
            "#### Claim",
            "",
            claim,
            "",
            "#### Evidence Locator",
            "",
            locator,
            "",
            "#### Scope Conditions",
            "",
            scope,
            "",
            "#### Misuse Risk",
            "",
            misuse,
            "",
        ]
    )


def render_tension_card(card: Card, related: bool = False) -> str:
    tension = compact(section(card.text, "Tension"))
    deciding = compact(section(card.text, "Deciding conditions"))
    scope = compact(section(card.text, "Scope conditions"))
    preserved = compact(section(card.text, "Tension preserved"))
    title = card.fields.get("title", card.card_id)
    review = card.fields.get("operator_review_status", "unknown")
    prefix = "Related reviewed tension" if related else "Tension"
    return "\n".join(
        [
            f"### {prefix}: {card.card_id} - {title}",
            "",
            f"- Path: `{rel(card.path)}`",
            f"- Review status: `{review}`",
            f"- Tension status: `{card.fields.get('tension_status', 'unknown')}`",
            "",
            "#### Tension",
            "",
            tension,
            "",
            "#### Deciding Conditions",
            "",
            deciding,
            "",
            "#### Scope Conditions",
            "",
            scope,
            "",
            "#### Tension Preserved",
            "",
            preserved,
            "",
        ]
    )


def render_brief(
    decision_slug: str,
    cards: list[Card],
    question: str | None,
    include_unreviewed: bool,
    include_related: bool,
) -> str:
    related = related_reviewed_tensions(cards) if include_related else []
    input_ids = [card.card_id for card in cards]
    all_ids = input_ids + [card.card_id for card in related]
    lines: list[str] = [
        "---",
        f"brief_id: {decision_slug}",
        "status: machine_compiled_not_canon",
        f"created: {date.today().isoformat()}",
        f"include_unreviewed: {str(include_unreviewed).lower()}",
        "input_cards:",
    ]
    lines.extend(f"  - {card_id}" for card_id in input_ids)
    lines.extend(
        [
            "---",
            "",
            "# Compiled Decision Brief",
            "",
            "This brief is machine-compiled from public-safe KB cards. It is not",
            "canon, not advice, and not proof that any source claim is true. It is",
            "a constraint packet for later operator review.",
            "",
            "## Decision Question",
            "",
            question or decision_slug,
            "",
            "## Authority Boundary",
            "",
            "- Source cards are evidence units, not canon.",
            "- Claim/tension cards are synthesis units, not canon.",
            "- This compiled brief is `machine_compiled_not_canon`.",
            "- A later model answer must not treat card labels as proof.",
            "",
            "## Included Cards",
            "",
        ]
    )
    lines.extend(f"- `{card_id}`" for card_id in all_ids)
    lines.extend(["", "## Source Cards", ""])
    source_cards = [card for card in cards if card.kind == "source_card"]
    if source_cards:
        for card in source_cards:
            lines.append(render_source_card(card))
    else:
        lines.append("None selected.")
        lines.append("")

    tension_cards = [card for card in cards if card.kind == "claim_tension_card"]
    if tension_cards:
        lines.extend(["## Selected Tension Cards", ""])
        for card in tension_cards:
            lines.append(render_tension_card(card))

    lines.extend(["## Related Reviewed Tension Cards", ""])
    if related:
        for card in related:
            lines.append(render_tension_card(card, related=True))
    else:
        lines.append("None found from selected card references.")
        lines.append("")

    lines.extend(
        [
            "## Rejected / Out Of Scope",
            "",
            "- Raw source text and local-only paths are excluded.",
            "- Unreviewed cards are excluded unless `--include-unreviewed` is passed.",
            "- Book maps are discovery aids and are not compiled as evidence.",
            "- Canon claims are not created by this brief.",
            "",
        ]
    )
    return "\n".join(lines)


def self_test() -> int:
    cards = require_cards(["BK-0048-card-001"], include_unreviewed=False)
    text = render_brief("self-test", cards, "Should this trait evidence be trusted?", False, True)
    checks = [
        "status: machine_compiled_not_canon",
        "BK-0048-card-001",
        "## Source Cards",
        "## Rejected / Out Of Scope",
    ]
    missing = [check for check in checks if check not in text]
    if missing:
        print("compile-brief self-test failed; missing:", ", ".join(missing))
        return 1
    with tempfile.TemporaryDirectory() as tmp:
        out = Path(tmp) / "brief.md"
        out.write_text(text, encoding="utf-8")
        if not out.read_text(encoding="utf-8").startswith("---"):
            print("compile-brief self-test failed; output not markdown/frontmatter.")
            return 1
    print("compile-brief self-test passed.")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("decision_slug", nargs="?", help="brief slug or short decision label")
    parser.add_argument("card_ids", nargs="*", help="source-card or claim/tension-card IDs")
    parser.add_argument("--question", help="operator decision question to include")
    parser.add_argument("--output", type=Path, help="write brief to this path instead of stdout")
    parser.add_argument("--include-unreviewed", action="store_true", help="include unreviewed cards with warning")
    parser.add_argument("--no-related-tensions", action="store_true", help="do not auto-include related reviewed tension cards")
    parser.add_argument("--self-test", action="store_true", help="run deterministic self-test")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.self_test:
        return self_test()
    if not args.decision_slug or not args.card_ids:
        print("Usage: python3 scripts/compile_brief.py <decision_slug> <card_id...>")
        return 2

    cards = require_cards(args.card_ids, include_unreviewed=args.include_unreviewed)
    text = render_brief(
        args.decision_slug,
        cards,
        args.question,
        args.include_unreviewed,
        not args.no_related_tensions,
    )
    if args.output:
        args.output.write_text(text, encoding="utf-8")
        print(f"Wrote {args.output}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())

