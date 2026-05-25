#!/usr/bin/env python3
"""Create an eval case folder with case, score sheet, and model-output folder."""

from __future__ import annotations

from datetime import date
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
EVALS_DIR = ROOT / "evals"
SCORE_TEMPLATE = ROOT / "runs" / "score-sheets" / "_template.md"
VALID_EVAL_TYPES = {
    "bibliographic-adversary",
    "contradiction-preservation",
    "canon-promotion-tournament",
    "long-tail-transfer",
    "source-lineage-hostile",
}
SAFE_ID = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def usage() -> int:
    print("Usage: python3 scripts/new_eval_case.py <eval_type> <case_id>")
    print("Valid eval types:")
    for eval_type in sorted(VALID_EVAL_TYPES):
        print(f"  - {eval_type}")
    return 2


def main() -> int:
    if len(sys.argv) != 3:
        return usage()
    eval_type = sys.argv[1].strip()
    case_id = sys.argv[2].strip()

    if eval_type not in VALID_EVAL_TYPES:
        print(f"Invalid eval_type: {eval_type}")
        return usage()
    if not SAFE_ID.match(case_id):
        print("case_id must use letters, numbers, dots, underscores, or hyphens.")
        return 2

    case_dir = EVALS_DIR / eval_type / case_id
    case_path = case_dir / "case.md"
    score_path = case_dir / "score-sheet.md"
    outputs_dir = case_dir / "model-outputs"

    if case_dir.exists():
        print(f"Refusing to overwrite existing case folder: {case_dir.relative_to(ROOT)}")
        return 1

    case_dir.mkdir(parents=True)
    outputs_dir.mkdir()
    (outputs_dir / ".gitkeep").write_text("keep\n", encoding="utf-8")

    case_template = (EVALS_DIR / eval_type / "_case-template.md").read_text(
        encoding="utf-8"
    )
    case_template = case_template.replace("case_id:\n", f"case_id: {case_id}\n", 1)
    case_template = case_template.replace(
        "created:\n", f"created: {date.today().isoformat()}\n", 1
    )
    case_path.write_text(case_template, encoding="utf-8")

    score_text = SCORE_TEMPLATE.read_text(encoding="utf-8")
    score_text = score_text.replace("case_id:\n", f"case_id: {case_id}\n", 1)
    score_text = score_text.replace("eval_type:\n", f"eval_type: {eval_type}\n", 1)
    score_path.write_text(score_text, encoding="utf-8")

    print(f"Created {case_dir.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
