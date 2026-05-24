#!/usr/bin/env python3
"""Create a book map from the public template."""

from __future__ import annotations

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "corpus" / "book-maps" / "_template.md"
OUT_DIR = ROOT / "corpus" / "book-maps"
SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def usage() -> int:
    print("Usage: python3 scripts/new_book_map.py <source_id>")
    return 2


def main() -> int:
    if len(sys.argv) != 2:
        return usage()
    source_id = sys.argv[1].strip()
    if not SAFE_ID.match(source_id):
        print("source_id must use letters, numbers, dots, underscores, or hyphens.")
        return 2

    destination = OUT_DIR / f"{source_id}.md"
    if destination.exists():
        print(f"Refusing to overwrite existing file: {destination.relative_to(ROOT)}")
        return 1

    text = TEMPLATE.read_text(encoding="utf-8")
    text = text.replace("source_id:\n", f"source_id: {source_id}\n", 1)
    destination.write_text(text, encoding="utf-8")
    print(f"Created {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
