#!/usr/bin/env python3
"""Create a claim/tension card from the public template."""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "corpus" / "claim-tension-cards" / "_template.md"
OUT_DIR = ROOT / "corpus" / "claim-tension-cards"
SAFE_SLUG = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def usage() -> int:
    print("Usage: python3 scripts/new_claim_tension_card.py <slug>")
    return 2


def main() -> int:
    if len(sys.argv) != 2:
        return usage()
    slug = sys.argv[1].strip()
    if not SAFE_SLUG.match(slug):
        print("slug must use letters, numbers, dots, underscores, or hyphens.")
        return 2

    destination = OUT_DIR / f"{slug}.md"
    if destination.exists():
        print(f"Refusing to overwrite existing file: {destination.relative_to(ROOT)}")
        return 1

    text = TEMPLATE.read_text(encoding="utf-8")
    destination.write_text(text, encoding="utf-8")
    print(f"Created {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
