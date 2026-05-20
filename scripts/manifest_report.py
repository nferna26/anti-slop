#!/usr/bin/env python3
"""Print a public-safe status report on the 200-book manifest and wave-1 progress.

No raw paths, no raw filenames. Counts only. Standard library only.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "corpus" / "manifests" / "books-200.yaml"
ACQ_REGISTRY = ROOT / "corpus" / "manifests" / "acquisition-registry.yaml"
ID_REGISTRY = ROOT / "corpus" / "manifests" / "source-id-registry.yaml"


def strip_comment(line: str) -> str:
    in_s = in_d = esc = False
    for i, c in enumerate(line):
        if esc:
            esc = False
            continue
        if c == "\\":
            esc = True
            continue
        if c == "'" and not in_d:
            in_s = not in_s
        elif c == '"' and not in_s:
            in_d = not in_d
        elif c == "#" and not in_s and not in_d:
            return line[:i]
    return line


def parse_scalar(v: str):
    v = v.strip()
    if v in {"", "null", "Null", "NULL", "~"}:
        return None
    if v.lower() == "true":
        return True
    if v.lower() == "false":
        return False
    if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
        return v[1:-1]
    return v


def parse_simple_books(path: Path) -> list[dict]:
    """Parse the manifest into a list of flat dicts with the top-level fields we report on."""
    text = path.read_text(encoding="utf-8")
    books: list[dict] = []
    cur: dict | None = None
    in_books = False
    for raw in text.splitlines():
        line = strip_comment(raw).rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        content = line.strip()
        if not in_books:
            if content.startswith("books:"):
                in_books = True
            continue
        if indent == 0 and not content.startswith("- "):
            break
        if content.startswith("- "):
            if cur is not None:
                books.append(cur)
            cur = {}
            rest = content[2:].strip()
            if rest and ":" in rest:
                k, v = rest.split(":", 1)
                cur[k.strip()] = parse_scalar(v.strip())
            continue
        if cur is None:
            continue
        if ":" not in content:
            continue
        k, v = content.split(":", 1)
        k = k.strip()
        v = v.strip()
        # We do not descend into eval_relevance for the top-level report.
        if v == "" or indent > 4:
            continue
        cur[k] = parse_scalar(v)
    if cur is not None:
        books.append(cur)
    return books


def parse_id_registry(path: Path) -> dict[str, dict]:
    """Return {source_id: {priority_rank, map_candidate, deep_card_candidate, first_30_deep_card_candidate}}."""
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8")
    result: dict[str, dict] = {}
    current: str | None = None
    for raw in text.splitlines():
        line = strip_comment(raw)
        m = re.match(r"\s*-\s*source_id:\s*(\S+)", line)
        if m:
            current = m.group(1)
            result[current] = {}
            continue
        if current is None:
            continue
        m = re.match(r"\s*(priority_rank|map_candidate|deep_card_candidate|first_30_deep_card_candidate):\s*(\S+)", line)
        if m:
            result[current][m.group(1)] = parse_scalar(m.group(2))
    return result


def count_acq_local_present(path: Path) -> int:
    if not path.exists():
        return 0
    text = path.read_text(encoding="utf-8")
    return sum(1 for line in text.splitlines()
               if re.match(r"\s*raw_source_exists_local:\s*true", line))


def main() -> int:
    if not MANIFEST.exists():
        print(f"Missing manifest: {MANIFEST}")
        return 1
    books = parse_simple_books(MANIFEST)
    print(f"== books-kb manifest report ==")
    print(f"Total books: {len(books)}")
    print()

    def count(field: str) -> Counter:
        c: Counter = Counter()
        for b in books:
            c[str(b.get(field, ""))] += 1
        return c

    for label, field in [
        ("Category", "category"),
        ("Availability tier", "availability_tier"),
        ("Status tag", "status_tag"),
        ("Acquisition status", "acquisition_status"),
        ("Publication status", "publication_status"),
        ("Raw source status", "raw_source_status"),
    ]:
        c = count(field)
        print(f"By {label.lower()}:")
        for k, n in sorted(c.items()):
            print(f"  {k or '(empty)'}: {n}")
        print()

    # Wave-1 detail
    id_reg = parse_id_registry(ID_REGISTRY)
    wave_1_ids = {sid for sid in id_reg}
    wave_1_books = [b for b in books if b.get("source_id") in wave_1_ids]

    print(f"== Wave-1 status (BK-0001 through BK-0050) ==")
    print(f"Wave-1 books found in manifest: {len(wave_1_books)}")
    wb_acq = Counter(str(b.get("acquisition_status", "")) for b in wave_1_books)
    wb_raw = Counter(str(b.get("raw_source_status", "")) for b in wave_1_books)
    print("Wave-1 acquisition_status:")
    for k, n in sorted(wb_acq.items()):
        print(f"  {k or '(empty)'}: {n}")
    print("Wave-1 raw_source_status:")
    for k, n in sorted(wb_raw.items()):
        print(f"  {k or '(empty)'}: {n}")

    map_candidates = sorted([sid for sid, v in id_reg.items() if v.get("map_candidate") is True])
    deep_cards = sorted([sid for sid, v in id_reg.items() if v.get("deep_card_candidate") is True])
    first_30 = sorted([sid for sid, v in id_reg.items() if v.get("first_30_deep_card_candidate") is True])
    print(f"Wave-1 map candidates ({len(map_candidates)}): {', '.join(map_candidates)}")
    print(f"Wave-1 deep-card candidates ({len(deep_cards)}): {', '.join(deep_cards)}")
    if first_30:
        print(f"Wave-1 first-30 deep-card candidates ({len(first_30)}): {', '.join(first_30)}")
    print()

    # Acquisition registry summary (if present)
    print(f"== Acquisition registry ==")
    if ACQ_REGISTRY.exists():
        local_present = count_acq_local_present(ACQ_REGISTRY)
        print(f"Entries present at: {ACQ_REGISTRY.relative_to(ROOT)}")
        print(f"Entries reporting raw_source_exists_local=true: {local_present}")
    else:
        print("Acquisition registry not present yet.")
    print()

    # Next suggested manual actions
    print("== Next suggested manual actions ==")
    print("- Review the five drafted first-five book maps (corpus/book-maps/BK-0001.md, BK-0003.md, BK-0007.md, BK-0042.md, BK-0048.md) and drain their Operator review notes.")
    print("- Begin source-card selection from the reviewed maps; do not start cards on maps that have not been operator-reviewed.")
    print("- Keep the BK-0020 (Shape Up) and BK-0046 (To Err Is Human) rights/access watchlist; both currently raw_source_status=metadata_only.")
    print("- Choose the next acquisition batch only after first-five map review and source-card WIP are under control (see docs/wip-limits.md).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
