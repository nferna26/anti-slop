#!/usr/bin/env python3
"""Heuristically flag suspicious raw or long text files in public folders."""

from __future__ import annotations

from pathlib import Path
import os
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_THRESHOLD_BYTES = 75_000
THRESHOLD_BYTES = int(os.environ.get("RAW_TEXT_THRESHOLD_BYTES", DEFAULT_THRESHOLD_BYTES))
SUSPICIOUS_NAME_PARTS = ("raw", "ocr", "extracted", "chapter", "fulltext")
TEXT_EXTENSIONS = {
    ".md",
    ".txt",
    ".yaml",
    ".yml",
    ".json",
    ".csv",
    ".tsv",
    ".rst",
}
EXCLUDED_DIRS = {
    ".git",
    "_archive",
    "local-only",
    "raw",
    "_raw",
    "extracted-text",
    "ocr-output",
    "__pycache__",
}
ALLOWLIST = {
    Path("scripts/check_no_raw_text.py"),
    Path(".gitignore"),
    Path("local-only.README.md"),
}

# Structured manifest paths that legitimately exceed the size heuristic.
# These still warn (the warning is informational), but the warning message
# is clearer so reviewers know the file is curated metadata, not raw text.
STRUCTURED_MANIFESTS = {
    Path("corpus/manifests/books-200.yaml"),
    Path("corpus/manifests/acquisition-registry.yaml"),
}


def is_excluded(path: Path) -> bool:
    try:
        relative = path.relative_to(ROOT)
    except ValueError:
        return True
    return any(part in EXCLUDED_DIRS for part in relative.parts)


def is_text_candidate(path: Path) -> bool:
    return path.suffix.lower() in TEXT_EXTENSIONS or path.name in {"README", "Makefile"}


def main() -> int:
    print("This is a defensive heuristic, not a legal guarantee.")
    warnings: list[str] = []

    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        if is_excluded(path):
            continue
        relative = path.relative_to(ROOT)
        if relative in ALLOWLIST:
            continue

        lower_name = path.name.lower()
        if any(part in lower_name for part in SUSPICIOUS_NAME_PARTS):
            warnings.append(f"{relative}: suspicious filename")

        if is_text_candidate(path):
            try:
                size = path.stat().st_size
            except OSError as exc:
                warnings.append(f"{relative}: could not stat file: {exc}")
                continue
            if size > THRESHOLD_BYTES:
                if relative in STRUCTURED_MANIFESTS:
                    warnings.append(
                        f"{relative}: structured manifest is {size} bytes (above {THRESHOLD_BYTES} threshold); "
                        f"informational only — this file is curated metadata, not raw source text"
                    )
                else:
                    warnings.append(
                        f"{relative}: text-like file is {size} bytes, above {THRESHOLD_BYTES}"
                    )

    if warnings:
        print("Warnings:")
        for warning in warnings:
            print(f"  - {warning}")
    else:
        print("No suspicious public raw-text files found.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
