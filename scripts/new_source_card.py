#!/usr/bin/env python3
"""Create the next numbered source card for a source_id."""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "corpus" / "source-cards" / "_template.md"
OUT_DIR = ROOT / "corpus" / "source-cards"
SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def usage() -> int:
    print("Usage: python3 scripts/new_source_card.py <source_id>")
    return 2


def next_card_path(source_id: str) -> tuple[Path, str]:
    for number in range(1, 1000):
        card_id = f"{source_id}-card-{number:03d}"
        path = OUT_DIR / f"{card_id}.md"
        if not path.exists():
            return path, card_id
    raise RuntimeError(f"Too many cards for {source_id}")


def main() -> int:
    if len(sys.argv) != 2:
        return usage()
    source_id = sys.argv[1].strip()
    if not SAFE_ID.match(source_id):
        print("source_id must use letters, numbers, dots, underscores, or hyphens.")
        return 2

    destination, card_id = next_card_path(source_id)
    text = TEMPLATE.read_text(encoding="utf-8")
    text = text.replace("card_id:\n", f"card_id: {card_id}\n", 1)
    text = text.replace("source_id:\n", f"source_id: {source_id}\n", 1)
    destination.write_text(text, encoding="utf-8")
    print(f"Created {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
