#!/usr/bin/env python3
"""Rank the first-50 source queue for the books-kb control plane.

Read-only. Produces an operator-facing queue from public manifests and public
artifacts only. It does not edit statuses, read local-only source files, call
models/APIs, or create artifacts.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re

from artifact_status import parse_yaml_list, read_frontmatter

ROOT = Path(__file__).resolve().parents[1]

BOOKS = ROOT / "corpus" / "manifests" / "books-200.yaml"
ACQ = ROOT / "corpus" / "manifests" / "acquisition-registry.yaml"
SOURCE_ID_REGISTRY = ROOT / "corpus" / "manifests" / "source-id-registry.yaml"
BOOK_MAPS_DIR = ROOT / "corpus" / "book-maps"
SOURCE_CARDS_DIR = ROOT / "corpus" / "source-cards"
CLAIM_CARDS_DIR = ROOT / "corpus" / "claim-tension-cards"
EVALS_DIR = ROOT / "evals"

CARD_ID_RE = re.compile(r"\bBK-\d{4}-card-\d{3}\b")


@dataclass
class SourceRow:
    source_id: str
    priority_rank: int
    title: str
    map_candidate: bool
    deep_card_candidate: bool
    first30_candidate: bool
    acquisition_status: str | None
    raw_source_status: str | None
    edition_verified: bool
    locator_scheme: str | None
    map_status: str | None
    source_cards_reviewed: int
    source_cards_unreviewed: int
    in_reviewed_tension: bool
    in_eval: bool
    registry_mapped: bool | None
    registry_source_cards_started: bool | None

    @property
    def source_cards_total(self) -> int:
        return self.source_cards_reviewed + self.source_cards_unreviewed

    @property
    def level(self) -> int:
        level = 0
        if self.acquisition_status == "sourced" and self.edition_verified and self.locator_scheme:
            level = max(level, 1)
        if self.map_status == "reviewed":
            level = max(level, 2)
        if self.source_cards_reviewed:
            level = max(level, 3)
        if self.in_reviewed_tension or self.in_eval:
            level = max(level, 4)
        return level

    @property
    def level_label(self) -> str:
        labels = {
            0: "L0 registered",
            1: "L1 verified/locatable",
            2: "L2 reviewed map",
            3: "L3 reviewed source card",
            4: "L4 tension/eval participant",
        }
        return labels[self.level]

    @property
    def recommended_map_class(self) -> str:
        """Return the map depth this source should receive next."""
        if self.map_candidate or self.deep_card_candidate:
            return "deep"
        return "lite"

    @property
    def recommended_map_label(self) -> str:
        if self.recommended_map_class == "deep":
            return "deep book map"
        return "map-lite"

    def blockers(self) -> list[str]:
        out: list[str] = []
        if self.raw_source_status == "metadata_only":
            out.append("rights/access verification required")
        elif self.acquisition_status != "sourced":
            out.append("not sourced")
        elif not self.edition_verified or not self.locator_scheme:
            out.append("edition/locator verification required")
        if self.map_status == "unreviewed":
            out.append("book map awaiting operator review")
        if self.registry_mapped is False and self.map_status:
            out.append("registry mapped flag drift")
        if self.registry_source_cards_started is False and self.source_cards_total:
            out.append("registry source-card flag drift")
        return out

    def next_action(self) -> str:
        blockers = self.blockers()
        if "registry mapped flag drift" in blockers or "registry source-card flag drift" in blockers:
            return "Run receipt/status reconciliation."
        if self.raw_source_status == "metadata_only":
            return "Prepare operator rights/access approval packet."
        if self.acquisition_status != "sourced":
            return "Acquire or explicitly defer before mapping."
        if not self.edition_verified or not self.locator_scheme:
            return "Run book-map Workflow 1/2 metadata + locator verification."
        if self.map_status is None:
            return f"Draft approval-ready {self.recommended_map_label}."
        if self.map_status == "unreviewed":
            return "Review and approve/send back book map."
        if self.source_cards_total == 0:
            return "Select and draft first approval-ready source card."
        if self.source_cards_unreviewed:
            return "Review pending source card before drafting more."
        if not self.in_reviewed_tension and self.source_cards_reviewed:
            return "Consider next source card or a reviewed-card tension pair."
        if self.in_reviewed_tension and not self.in_eval:
            return "Consider eval case if the tension needs proof-surface coverage."
        return "Coverage exists; use as support or move to benchmark/eval follow-up."

    def sort_key(self) -> tuple:
        blockers = self.blockers()
        if any("drift" in blocker for blocker in blockers):
            band = 0
        elif self.map_status == "reviewed" and self.source_cards_total == 0:
            band = 1
        elif self.acquisition_status == "sourced" and self.edition_verified and self.locator_scheme and self.map_status is None:
            band = 2
        elif self.acquisition_status == "sourced" and (not self.edition_verified or not self.locator_scheme):
            band = 3
        elif self.source_cards_reviewed and not self.in_reviewed_tension:
            band = 4
        elif self.raw_source_status == "metadata_only":
            band = 5
        elif self.acquisition_status != "sourced":
            band = 6
        else:
            band = 7
        return (
            band,
            self.recommended_map_class != "deep",
            not self.map_candidate,
            not self.deep_card_candidate,
            not self.first30_candidate,
            self.priority_rank,
        )


def read_yaml_list(path: Path, key: str) -> list[dict]:
    if not path.exists():
        return []
    return parse_yaml_list(path.read_text(encoding="utf-8"), key)


def source_card_index() -> tuple[dict[str, str], dict[str, tuple[int, int]]]:
    card_to_source: dict[str, str] = {}
    counts: dict[str, tuple[int, int]] = {}
    for path in sorted(SOURCE_CARDS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        fm = read_frontmatter(path)
        sid = fm.get("source_id")
        if not sid:
            continue
        card_id = fm.get("card_id") or path.stem
        card_to_source[card_id] = sid
        reviewed, unreviewed = counts.get(sid, (0, 0))
        if fm.get("operator_review_status") == "reviewed":
            reviewed += 1
        else:
            unreviewed += 1
        counts[sid] = (reviewed, unreviewed)
    return card_to_source, counts


def reviewed_tension_sources(card_to_source: dict[str, str]) -> set[str]:
    sources: set[str] = set()
    for path in sorted(CLAIM_CARDS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        fm = read_frontmatter(path)
        if fm.get("operator_review_status") != "reviewed":
            continue
        for card_id in set(CARD_ID_RE.findall(path.read_text(encoding="utf-8"))):
            sid = card_to_source.get(card_id)
            if sid:
                sources.add(sid)
    return sources


def eval_sources(card_to_source: dict[str, str]) -> set[str]:
    sources: set[str] = set()
    for path in sorted(EVALS_DIR.glob("*/*/case.md")):
        text = path.read_text(encoding="utf-8")
        for card_id in set(CARD_ID_RE.findall(text)):
            sid = card_to_source.get(card_id)
            if sid:
                sources.add(sid)
    return sources


def book_map_statuses() -> dict[str, str]:
    statuses: dict[str, str] = {}
    for path in sorted(BOOK_MAPS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        statuses[path.stem] = read_frontmatter(path).get("operator_review_status") or "unknown"
    return statuses


def build_rows() -> list[SourceRow]:
    wave = read_yaml_list(SOURCE_ID_REGISTRY, "wave_1")
    books = {row.get("source_id"): row for row in read_yaml_list(BOOKS, "books")}
    acq = {row.get("source_id"): row for row in read_yaml_list(ACQ, "entries")}
    maps = book_map_statuses()
    card_to_source, source_card_counts = source_card_index()
    tension_sources = reviewed_tension_sources(card_to_source)
    eval_source_ids = eval_sources(card_to_source)

    rows: list[SourceRow] = []
    for item in wave:
        sid = item.get("source_id")
        if not sid:
            continue
        book_row = books.get(sid, {})
        acq_row = acq.get(sid, {})
        processing = acq_row.get("processing_status") or {}
        reviewed, unreviewed = source_card_counts.get(sid, (0, 0))
        rows.append(SourceRow(
            source_id=sid,
            priority_rank=int(item.get("priority_rank") or 999),
            title=str(item.get("title") or book_row.get("title") or ""),
            map_candidate=bool(item.get("map_candidate")),
            deep_card_candidate=bool(item.get("deep_card_candidate")),
            first30_candidate=bool(item.get("first_30_deep_card_candidate")),
            acquisition_status=acq_row.get("acquisition_status") or book_row.get("acquisition_status"),
            raw_source_status=acq_row.get("raw_source_status") or book_row.get("raw_source_status"),
            edition_verified=bool(acq_row.get("edition_verified")),
            locator_scheme=acq_row.get("locator_scheme") or book_row.get("locator_system"),
            map_status=maps.get(sid),
            source_cards_reviewed=reviewed,
            source_cards_unreviewed=unreviewed,
            in_reviewed_tension=sid in tension_sources,
            in_eval=sid in eval_source_ids,
            registry_mapped=(processing or {}).get("mapped") if isinstance(processing, dict) else None,
            registry_source_cards_started=(
                (processing or {}).get("source_cards_started")
                if isinstance(processing, dict) else None
            ),
        ))
    return rows


def flags(row: SourceRow) -> str:
    out = []
    if row.map_candidate:
        out.append("map")
    if row.deep_card_candidate:
        out.append("deep")
    if row.first30_candidate:
        out.append("first30")
    return ",".join(out) if out else "-"


def print_table(rows: list[SourceRow], limit: int = 15) -> None:
    print(f"{'Rank':<4} {'Source':<7} {'Level':<4} {'Flags':<18} {'Map':<5} {'Next action'}")
    print(f"{'-' * 4} {'-' * 7} {'-' * 4} {'-' * 18} {'-' * 5} {'-' * 48}")
    for index, row in enumerate(rows[:limit], start=1):
        map_class = row.recommended_map_class if row.map_status is None and row.level == 1 else "-"
        print(
            f"{index:<4} {row.source_id:<7} L{row.level:<3} "
            f"{flags(row):<18} {map_class:<5} {row.next_action()}"
        )


def is_map_ready(row: SourceRow) -> bool:
    return (
        row.acquisition_status == "sourced"
        and row.edition_verified
        and bool(row.locator_scheme)
        and row.map_status is None
    )


def main() -> int:
    rows = build_rows()
    ranked = sorted(rows, key=lambda row: row.sort_key())

    print("== First-50 artifact queue ==")
    print("Read-only queue. Changes nothing.")
    print()

    print("-- Level summary --")
    for level in range(5):
        count = sum(1 for row in rows if row.level == level)
        label = {
            0: "L0 registered / blocked or not yet verified",
            1: "L1 verified and locatable",
            2: "L2 reviewed book map",
            3: "L3 reviewed source card",
            4: "L4 reviewed tension/eval participant",
        }[level]
        print(f"{label:<48} {count}")
    print()

    print("-- Top recommended next actions --")
    print_table(ranked, limit=15)
    print()

    print("-- Ready lanes --")
    source_card_ready = [
        row.source_id for row in rows
        if row.map_status == "reviewed" and row.source_cards_total == 0
    ]
    map_ready_deep = [
        row.source_id for row in rows
        if is_map_ready(row) and row.recommended_map_class == "deep"
    ]
    map_ready_lite = [
        row.source_id for row in rows
        if is_map_ready(row) and row.recommended_map_class == "lite"
    ]
    metadata_ready = [
        row.source_id for row in rows
        if row.acquisition_status == "sourced"
        and (not row.edition_verified or not row.locator_scheme)
    ]
    rights_blocked = [
        row.source_id for row in rows
        if row.raw_source_status == "metadata_only"
    ]
    not_sourced = [
        row.source_id for row in rows
        if row.acquisition_status != "sourced" and row.raw_source_status != "metadata_only"
    ]
    print(f"Reviewed maps with no source card: {', '.join(source_card_ready) or 'none'}")
    print(f"Verified and deep-map-ready, no map yet: {', '.join(map_ready_deep) or 'none'}")
    print(f"Verified and map-lite-ready, no map yet: {', '.join(map_ready_lite) or 'none'}")
    print(f"Sourced but needs metadata/locator packet: {', '.join(metadata_ready) or 'none'}")
    print(f"Rights/access blocked: {', '.join(rights_blocked) or 'none'}")
    print(f"Not sourced yet: {', '.join(not_sourced) or 'none'}")
    print()

    print("-- Suggested immediate move --")
    if source_card_ready:
        first = sorted(
            [row for row in rows if row.source_id in source_card_ready],
            key=lambda row: row.sort_key(),
        )[0]
        print(
            f"Draft the first source card for {first.source_id} ({first.title}) "
            "via anti-slop-source-card Workflow 5."
        )
    elif map_ready_deep:
        first = sorted([row for row in rows if row.source_id in map_ready_deep], key=lambda row: row.sort_key())[0]
        print(f"Draft a deep book map for {first.source_id} ({first.title}).")
    elif map_ready_lite:
        first = sorted([row for row in rows if row.source_id in map_ready_lite], key=lambda row: row.sort_key())[0]
        print(f"Draft a map-lite for {first.source_id} ({first.title}).")
    elif metadata_ready:
        first = sorted(
            [row for row in rows if row.source_id in metadata_ready],
            key=lambda row: row.sort_key(),
        )[0]
        print(f"Prepare metadata/locator packet for {first.source_id} ({first.title}).")
    else:
        print("No ready public artifact move found; resolve acquisition or rights blockers.")

    print()
    print("Exit status: 0 (read-only report)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
