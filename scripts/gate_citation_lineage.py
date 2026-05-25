#!/usr/bin/env python3
"""Check that public card/source references resolve to known KB artifacts.

This is a narrow implementation of the citation-lineage gate. It does not try
to decide whether every material claim is sufficiently supported. It checks the
lower-level failure that should be deterministic: when an output names a source
ID, source-card ID, claim/tension-card ID, or local card path, that reference
must resolve inside the public KB.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import argparse
import re
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SOURCE_CARDS_DIR = ROOT / "corpus" / "source-cards"
CLAIM_CARDS_DIR = ROOT / "corpus" / "claim-tension-cards"
BOOKS_MANIFEST = ROOT / "corpus" / "manifests" / "books-200.yaml"

SOURCE_ID_RE = re.compile(r"\bBK-\d{4}\b(?!-card-\d{3})")
SOURCE_CARD_RE = re.compile(r"\bBK-\d{4}-card-\d{3}\b")
BACKTICK_RE = re.compile(r"`([^`]+)`")
TENSION_IDISH_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*-vs-[a-z0-9]+(?:-[a-z0-9]+)*$")
CARD_PATH_RE = re.compile(
    r"\bcorpus/(source-cards|claim-tension-cards)/([A-Za-z0-9._-]+\.md)\b"
)


@dataclass(frozen=True)
class Reference:
    kind: str
    value: str
    line: int


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


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


def source_ids() -> set[str]:
    text = read_text(BOOKS_MANIFEST)
    return set(re.findall(r"\bsource_id:\s*(BK-\d{4})\b", text))


def source_card_ids() -> set[str]:
    ids: set[str] = set()
    for path in SOURCE_CARDS_DIR.glob("BK-*-card-*.md"):
        fields = read_frontmatter(path)
        card_id = fields.get("card_id")
        if card_id:
            ids.add(card_id)
        ids.add(path.stem)
    return ids


def claim_card_ids() -> set[str]:
    ids: set[str] = set()
    for path in CLAIM_CARDS_DIR.glob("*.md"):
        if path.name.startswith("_"):
            continue
        fields = read_frontmatter(path)
        card_id = fields.get("card_id")
        if card_id:
            ids.add(card_id)
        ids.add(path.stem)
    return ids


def line_refs(path: Path) -> list[Reference]:
    refs: list[Reference] = []
    for number, line in enumerate(read_text(path).splitlines(), start=1):
        for match in SOURCE_CARD_RE.finditer(line):
            refs.append(Reference("source_card", match.group(0), number))
        for match in SOURCE_ID_RE.finditer(line):
            refs.append(Reference("source_id", match.group(0), number))
        for match in CARD_PATH_RE.finditer(line):
            refs.append(Reference("card_path", f"corpus/{match.group(1)}/{match.group(2)}", number))
        for match in BACKTICK_RE.finditer(line):
            token = match.group(1).strip()
            if "/" in token or "\\" in token or len(token) > 96:
                continue
            if SOURCE_CARD_RE.fullmatch(token) or TENSION_IDISH_RE.fullmatch(token):
                refs.append(Reference("card_id", token, number))
    return refs


def resolve_card_path(value: str) -> bool:
    target = ROOT / value
    if not target.exists():
        return False
    try:
        target.relative_to(ROOT)
    except ValueError:
        return False
    return target.parent in {SOURCE_CARDS_DIR, CLAIM_CARDS_DIR}


def check_paths(paths: list[Path]) -> tuple[list[str], int]:
    known_sources = source_ids()
    known_source_cards = source_card_ids()
    known_claim_cards = claim_card_ids()
    all_card_ids = known_source_cards | known_claim_cards

    findings: list[str] = []
    ref_count = 0
    for path in paths:
        for ref in line_refs(path):
            ref_count += 1
            ok = True
            if ref.kind == "source_id":
                ok = ref.value in known_sources
            elif ref.kind == "source_card":
                ok = ref.value in known_source_cards
            elif ref.kind == "card_id":
                ok = ref.value in all_card_ids
            elif ref.kind == "card_path":
                ok = resolve_card_path(ref.value)
            if not ok:
                findings.append(
                    f"{path}:{ref.line}: unresolved {ref.kind} reference: {ref.value}"
                )
    return findings, ref_count


def self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        good = tmp_path / "good.md"
        bad = tmp_path / "bad.md"
        good.write_text(
            "Use `BK-0048-card-001` and source BK-0048 as lineage.\n",
            encoding="utf-8",
        )
        bad.write_text(
            "This cites `BK-9999-card-999` and source BK-9999.\n",
            encoding="utf-8",
        )
        good_findings, good_refs = check_paths([good])
        bad_findings, bad_refs = check_paths([bad])
        if good_refs < 2 or good_findings:
            print("Self-test failed: valid references did not pass.")
            for finding in good_findings:
                print(f"  - {finding}")
            return 1
        if bad_refs < 2 or len(bad_findings) < 2:
            print("Self-test failed: invalid references were not caught.")
            for finding in bad_findings:
                print(f"  - {finding}")
            return 1
    print("citation-lineage self-test passed.")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="Markdown files to check")
    parser.add_argument("--self-test", action="store_true", help="run deterministic self-test")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.self_test:
        return self_test()
    if not args.paths:
        print("Usage: python3 scripts/gate_citation_lineage.py <file.md> [more.md]")
        return 2

    paths = [path.resolve() for path in args.paths]
    missing = [path for path in paths if not path.exists()]
    if missing:
        for path in missing:
            print(f"Missing input: {path}")
        return 2

    findings, ref_count = check_paths(paths)
    print("== citation-lineage gate ==")
    print(f"Files checked: {len(paths)}")
    print(f"References checked: {ref_count}")
    if findings:
        print("Result: FAIL")
        for finding in findings:
            print(f"  - {finding}")
        return 1
    print("Result: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
