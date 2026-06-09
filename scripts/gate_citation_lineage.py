#!/usr/bin/env python3
"""Check that public card/source references resolve to known KB artifacts.

This is a narrow, deterministic implementation of the citation-lineage gate. It
does not try to decide whether every material claim is sufficiently supported.
It checks the lower-level failure that should be deterministic: when an artifact
names a source ID, source-card ID, claim/tension-card ID, or local card path,
that reference must resolve inside the public KB.

Two levels:

- Default (existence): the referenced source / card / path exists in the KB.
- ``--require-reviewed`` (forward-reference / reviewed-lineage): in addition,
  every source-card reference (``BK-XXXX-card-NNN``) must resolve to a card whose
  ``operator_review_status`` is ``reviewed`` — except a file's reference to its
  own ``card_id`` (self-reference). This catches the failure where an artifact
  cites an unreviewed or nonexistent card as reviewed lineage. A planned/future
  comparison target that is not yet a reviewed card must be named by its source
  ID (``BK-XXXX``), never by a card ID, per the source-card discipline.

The KB root is injectable with ``--root`` so the same gate can run over a
fixture tree (used by ``--self-test``) or any checkout; it defaults to the repo
that contains this script.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import argparse
import re
import sys
import tempfile


DEFAULT_ROOT = Path(__file__).resolve().parents[1]

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


@dataclass(frozen=True)
class KBIndex:
    root: Path
    sources: frozenset[str]
    source_cards: frozenset[str]
    reviewed_source_cards: frozenset[str]
    claim_cards: frozenset[str]
    eval_labels: frozenset[str]

    @property
    def all_card_ids(self) -> frozenset[str]:
        return self.source_cards | self.claim_cards

    def resolves_idish(self, token: str) -> bool:
        """An ``x-vs-y`` backtick token resolves if it is a claim/tension card,
        or a known eval case label (case dir name), or a versioned/round variant
        of one (``<case>-v1``, ``<case>-smoke-2``, ...). Claim-tension card IDs
        and eval case IDs share the same ``x-vs-y`` shape, so the gate must know
        the eval-case namespace to avoid flagging real case IDs as dangling."""
        if token in self.claim_cards or token in self.eval_labels:
            return True
        return any(token.startswith(label + "-") for label in self.eval_labels)


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


def build_index(root: Path) -> KBIndex:
    root = root.resolve()
    source_cards_dir = root / "corpus" / "source-cards"
    claim_cards_dir = root / "corpus" / "claim-tension-cards"
    books_manifest = root / "corpus" / "manifests" / "books-200.yaml"

    sources: set[str] = set()
    if books_manifest.exists():
        sources = set(re.findall(r"\bsource_id:\s*(BK-\d{4})\b", read_text(books_manifest)))

    source_cards: set[str] = set()
    reviewed: set[str] = set()
    if source_cards_dir.is_dir():
        for path in source_cards_dir.glob("BK-*-card-*.md"):
            fields = read_frontmatter(path)
            card_id = fields.get("card_id") or path.stem
            source_cards.add(card_id)
            source_cards.add(path.stem)
            if fields.get("operator_review_status") == "reviewed":
                reviewed.add(card_id)
                reviewed.add(path.stem)

    claim_cards: set[str] = set()
    if claim_cards_dir.is_dir():
        for path in claim_cards_dir.glob("*.md"):
            if path.name.startswith("_"):
                continue
            fields = read_frontmatter(path)
            card_id = fields.get("card_id") or path.stem
            claim_cards.add(card_id)
            claim_cards.add(path.stem)

    # Eval case labels: immediate case directories under evals/<category>/.
    # These share the x-vs-y shape with claim-tension card IDs; collecting them
    # lets the gate tell a real case reference from a dangling claim-card ref.
    eval_labels: set[str] = set()
    evals_dir = root / "evals"
    if evals_dir.is_dir():
        for category in evals_dir.iterdir():
            if category.is_dir():
                eval_labels.update(d.name for d in category.iterdir() if d.is_dir())

    return KBIndex(root, frozenset(sources), frozenset(source_cards),
                   frozenset(reviewed), frozenset(claim_cards), frozenset(eval_labels))


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


def resolve_card_path(index: KBIndex, value: str) -> bool:
    target = index.root / value
    if not target.exists():
        return False
    try:
        target.relative_to(index.root)
    except ValueError:
        return False
    return target.parent in {index.root / "corpus" / "source-cards",
                             index.root / "corpus" / "claim-tension-cards"}


def check_paths(paths: list[Path], index: KBIndex | None = None,
                require_reviewed: bool = False) -> tuple[list[str], int]:
    if index is None:
        index = build_index(DEFAULT_ROOT)

    findings: list[str] = []
    ref_count = 0
    for path in paths:
        own_card_id = read_frontmatter(path).get("card_id")
        for ref in line_refs(path):
            ref_count += 1
            ok = True
            detail = ref.kind
            if ref.kind == "source_id":
                ok = ref.value in index.sources
            elif ref.kind == "source_card":
                if ref.value not in index.source_cards:
                    ok = False
                elif require_reviewed and ref.value != own_card_id \
                        and ref.value not in index.reviewed_source_cards:
                    ok = False
                    detail = "unreviewed source_card (cited as reviewed lineage)"
            elif ref.kind == "card_id":
                ok = ref.value in index.all_card_ids or index.resolves_idish(ref.value)
            elif ref.kind == "card_path":
                ok = resolve_card_path(index, ref.value)
            if not ok:
                findings.append(f"{path}:{ref.line}: unresolved {detail} reference: {ref.value}")
    return findings, ref_count


def _write_card(path: Path, card_id: str, reviewed: bool) -> None:
    status = "reviewed" if reviewed else "unreviewed"
    path.write_text(
        f"---\ncard_id: {card_id}\nsource_id: {card_id.split('-card-')[0]}\n"
        f"operator_review_status: {status}\n---\n\n# Source Card\n\nClaim.\n",
        encoding="utf-8",
    )


def self_test() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        cards = root / "corpus" / "source-cards"
        cards.mkdir(parents=True)
        (root / "corpus" / "claim-tension-cards").mkdir(parents=True)
        manifest = root / "corpus" / "manifests" / "books-200.yaml"
        manifest.parent.mkdir(parents=True)
        manifest.write_text("  - source_id: BK-0048\n  - source_id: BK-0003\n", encoding="utf-8")
        _write_card(cards / "BK-0048-card-001.md", "BK-0048-card-001", reviewed=True)
        _write_card(cards / "BK-0003-card-001.md", "BK-0003-card-001", reviewed=False)
        index = build_index(root)

        # 1. valid reviewed card ID + valid source ID -> pass (existence and reviewed)
        good = root / "good.md"
        good.write_text("Use `BK-0048-card-001` and source BK-0048 as lineage.\n", encoding="utf-8")
        # 2. nonexistent card ID + source ID -> fail (existence)
        bad = root / "bad.md"
        bad.write_text("This cites `BK-9999-card-999` and source BK-9999.\n", encoding="utf-8")
        # 3. forward-ref: an artifact cites an existing-but-UNREVIEWED card as lineage
        fwd = root / "forward.md"
        fwd.write_text("Anchored to `BK-0003-card-001` as reviewed lineage.\n", encoding="utf-8")
        # 4. self-reference: a card naming its own card_id is allowed even under reviewed mode
        self_ref = cards / "BK-0003-card-001.md"

        g_find, g_refs = check_paths([good], index)
        b_find, b_refs = check_paths([bad], index)
        # default mode: forward ref to existing unreviewed card passes (it exists)
        f_default, _ = check_paths([fwd], index, require_reviewed=False)
        # reviewed mode: forward ref to unreviewed card FAILS
        f_reviewed, _ = check_paths([fwd], index, require_reviewed=True)
        # reviewed mode: good (reviewed card) still passes
        g_reviewed, _ = check_paths([good], index, require_reviewed=True)
        # reviewed mode: a card's self-reference is NOT flagged
        s_reviewed, _ = check_paths([self_ref], index, require_reviewed=True)

        # 7. --root injection: build an index from a SECOND root where the same
        # filename (BK-0048-card-001) is UNREVIEWED, and confirm the SAME good.md
        # now FAILS under reviewed mode. Same input file, different injected root,
        # different result -> proves resolution comes from --root, not a hardcoded
        # path.
        root2 = root / "alt-root"
        cards2 = root2 / "corpus" / "source-cards"
        cards2.mkdir(parents=True)
        (root2 / "corpus" / "claim-tension-cards").mkdir(parents=True)
        m2 = root2 / "corpus" / "manifests" / "books-200.yaml"
        m2.parent.mkdir(parents=True)
        m2.write_text("  - source_id: BK-0048\n", encoding="utf-8")
        _write_card(cards2 / "BK-0048-card-001.md", "BK-0048-card-001", reviewed=False)
        index2 = build_index(root2)
        g_alt_root, _ = check_paths([good], index2, require_reviewed=True)

        checks = [
            ("valid reviewed card + source id pass", g_refs >= 2 and not g_find),
            ("nonexistent card + source id caught", b_refs >= 2 and len(b_find) >= 2),
            ("default mode: existing unreviewed card resolves", not f_default),
            ("reviewed mode: unreviewed-card forward-ref caught", len(f_reviewed) == 1),
            ("reviewed mode: reviewed card still passes", not g_reviewed),
            ("reviewed mode: self-reference allowed", not s_reviewed),
            ("--root injection: same file fails under a root where its card is unreviewed", len(g_alt_root) == 1),
        ]
        failed = [name for name, ok in checks if not ok]
        if failed:
            print("citation-lineage self-test FAILED:")
            for name in failed:
                print(f"  - {name}")
            return 1
    print("citation-lineage self-test passed (7 checks: existence, nonexistent-ref, default vs reviewed mode, unreviewed-forward-ref, self-reference, --root injection).")
    return 0


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, help="Markdown files to check")
    parser.add_argument("--root", type=Path, default=DEFAULT_ROOT,
                        help="KB root that holds corpus/ (default: this repo)")
    parser.add_argument("--require-reviewed", action="store_true",
                        help="also require every source-card reference to resolve to a reviewed card (self-references excepted)")
    parser.add_argument("--self-test", action="store_true", help="run deterministic self-test")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.self_test:
        return self_test()
    if not args.paths:
        print("Usage: python3 scripts/gate_citation_lineage.py [--root DIR] [--require-reviewed] <file.md> [more.md]")
        return 2

    paths = [path.resolve() for path in args.paths]
    missing = [path for path in paths if not path.exists()]
    if missing:
        for path in missing:
            print(f"Missing input: {path}")
        return 2

    index = build_index(args.root)
    findings, ref_count = check_paths(paths, index, require_reviewed=args.require_reviewed)
    print("== citation-lineage gate ==")
    print(f"Root: {index.root}")
    print(f"Mode: {'existence + reviewed-lineage' if args.require_reviewed else 'existence'}")
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
