#!/usr/bin/env python3
"""Create a gate log from the public template."""

from __future__ import annotations

from datetime import date
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "runs" / "gate-logs" / "_template.yaml"
OUT_DIR = ROOT / "runs" / "gate-logs"
SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def usage() -> int:
    print("Usage: python3 scripts/new_gate_log.py <run_id>")
    return 2


def main() -> int:
    if len(sys.argv) != 2:
        return usage()
    run_id = sys.argv[1].strip()
    if not SAFE_ID.match(run_id):
        print("run_id must use letters, numbers, dots, underscores, or hyphens.")
        return 2

    destination = OUT_DIR / f"{run_id}.yaml"
    if destination.exists():
        print(f"Refusing to overwrite existing file: {destination.relative_to(ROOT)}")
        return 1

    text = TEMPLATE.read_text(encoding="utf-8")
    text = text.replace("run_id:\n", f"run_id: {run_id}\n", 1)
    text = text.replace("created:\n", f"created: {date.today().isoformat()}\n", 1)
    destination.write_text(text, encoding="utf-8")
    print(f"Created {destination.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
