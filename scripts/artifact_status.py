#!/usr/bin/env python3
"""Artifact status scanner for the books-kb control plane.

Read-only. Derives current artifact state from files on disk and reports drift
against the manifests and the acquisition registry. It changes nothing — it does
not edit registry values, statuses, or any artifact. It is a dashboard.

Scans:
- corpus/book-maps/*.md
- corpus/source-cards/*.md
- corpus/claim-tension-cards/*.md
- evals/**/case.md and evals/**/score-sheet.md
- corpus/manifests/books-200.yaml
- corpus/manifests/acquisition-registry.yaml
- corpus/manifests/source-id-registry.yaml

Standard library only. No model/API calls, no embeddings, no local-only reads.
Public-safe output only. Always exits 0 — reporting drift is not a build failure.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

BOOK_MAPS_DIR = ROOT / "corpus" / "book-maps"
SOURCE_CARDS_DIR = ROOT / "corpus" / "source-cards"
CLAIM_CARDS_DIR = ROOT / "corpus" / "claim-tension-cards"
EVALS_DIR = ROOT / "evals"
MANIFEST = ROOT / "corpus" / "manifests" / "books-200.yaml"
ACQ_REGISTRY = ROOT / "corpus" / "manifests" / "acquisition-registry.yaml"
ID_REGISTRY = ROOT / "corpus" / "manifests" / "source-id-registry.yaml"

SOURCE_ID_RE = re.compile(r"\bBK-\d{4}\b")
CARD_ID_RE = re.compile(r"\bBK-\d{4}-card-\d{3}\b")


# --- parsing helpers -------------------------------------------------------

def strip_quotes(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_scalar(value: str):
    value = value.strip()
    if value in {"", "null", "Null", "NULL", "~"}:
        return None
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    return strip_quotes(value)


def read_frontmatter(path: Path) -> dict[str, str]:
    """Parse a leading --- ... --- YAML frontmatter block into a flat dict."""
    fields: dict[str, str] = {}
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return fields
    for raw in lines[1:]:
        if raw.strip() == "---":
            break
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw[:1] in (" ", "\t"):  # nested line; frontmatter here is flat
            continue
        if ":" not in raw:
            continue
        key, value = raw.split(":", 1)
        fields[key.strip()] = strip_quotes(value)
    return fields


def parse_yaml_list(text: str, list_key: str) -> list[dict]:
    """Parse a top-level `list_key:` list-of-dicts with up to one level of nesting."""
    items: list[dict] = []
    in_list = False
    cur: dict | None = None
    nested_key: str | None = None
    nested_indent: int | None = None

    for raw in text.splitlines():
        line = raw.split("#", 1)[0].rstrip() if not _has_quote(raw) else raw.rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        content = line.strip()

        if not in_list:
            if content.startswith(f"{list_key}:"):
                in_list = True
            continue

        if indent == 0 and not content.startswith("- "):
            break

        if content.startswith("- "):
            if cur is not None:
                items.append(cur)
            cur = {}
            nested_key = None
            nested_indent = None
            rest = content[2:].strip()
            if rest and ":" in rest:
                k, v = rest.split(":", 1)
                k, v = k.strip(), v.strip()
                if v == "":
                    cur[k] = {}
                    nested_key, nested_indent = k, indent
                else:
                    cur[k] = parse_scalar(v)
            continue

        if cur is None or ":" not in content:
            continue
        k, v = content.split(":", 1)
        k, v = k.strip(), v.strip()

        if nested_key and nested_indent is not None and indent > nested_indent:
            inner = cur.setdefault(nested_key, {})
            if isinstance(inner, dict):
                inner[k] = parse_scalar(v)
            continue

        if v == "":
            cur[k] = {}
            nested_key, nested_indent = k, indent
        else:
            cur[k] = parse_scalar(v)
            nested_key = nested_indent = None

    if cur is not None:
        items.append(cur)
    return items


def _has_quote(line: str) -> bool:
    return "'" in line or '"' in line


def result_status(score_sheet: Path) -> str | None:
    """Return the Result status word from a score-sheet.md ## Result section."""
    lines = score_sheet.read_text(encoding="utf-8").splitlines()
    for i, raw in enumerate(lines):
        if raw.strip() == "## Result":
            for follow in lines[i + 1:]:
                if follow.strip():
                    token = follow.strip().split()[0].strip("`*—-")
                    return token or None
    return None


# --- per-source state ------------------------------------------------------

class SourceState:
    def __init__(self, source_id: str) -> None:
        self.source_id = source_id
        self.has_book_map = False
        self.book_map_review = None  # operator_review_status of the map, if any
        self.reviewed_source_cards = 0
        self.unreviewed_source_cards = 0
        self.claim_tension_refs = 0
        self.eval_refs = 0
        self.reg_mapped = None
        self.reg_source_cards_started = None
        self.acquisition_status = None
        self.edition_verified = None
        self.locator_scheme = None
        self.in_reviewed_claim_card = False
        self.in_eval = False

    @property
    def source_card_count(self) -> int:
        return self.reviewed_source_cards + self.unreviewed_source_cards

    @property
    def has_reviewed_map(self) -> bool:
        return self.has_book_map and self.book_map_review == "reviewed"

    @property
    def has_reviewed_source_card(self) -> bool:
        return self.reviewed_source_cards > 0

    @property
    def has_any_artifact(self) -> bool:
        return (
            self.has_book_map
            or self.source_card_count > 0
            or self.claim_tension_refs > 0
            or self.eval_refs > 0
        )

    def level(self) -> int:
        lvl = 0  # L0 registered
        if self.acquisition_status == "sourced" and self.edition_verified is True \
                and bool(self.locator_scheme):
            lvl = max(lvl, 1)
        if self.has_reviewed_map:
            lvl = max(lvl, 2)
        if self.has_reviewed_source_card:
            lvl = max(lvl, 3)
        if self.in_reviewed_claim_card or self.in_eval:
            lvl = max(lvl, 4)
        return lvl

    def drift(self) -> list[str]:
        flags: list[str] = []
        if self.has_book_map and self.reg_mapped is False:
            flags.append("book map exists but registry processing_status.mapped is false")
        if self.has_book_map is False and self.reg_mapped is True:
            flags.append("registry processing_status.mapped is true but no book map exists")
        if self.source_card_count > 0 and self.reg_source_cards_started is False:
            flags.append(
                "source card exists but registry processing_status.source_cards_started is false"
            )
        if self.source_card_count == 0 and self.reg_source_cards_started is True:
            flags.append(
                "registry processing_status.source_cards_started is true but no source card exists"
            )
        if self.has_reviewed_source_card and not self.has_reviewed_map:
            flags.append("reviewed source card exists but no reviewed book map exists")
        return flags


# --- scan ------------------------------------------------------------------

def main() -> int:
    states: dict[str, SourceState] = {}

    def state(source_id: str) -> SourceState:
        return states.setdefault(source_id, SourceState(source_id))

    # Manifests
    manifest_ids: list[str] = []
    if MANIFEST.exists():
        for entry in parse_yaml_list(MANIFEST.read_text(encoding="utf-8"), "books"):
            sid = entry.get("source_id")
            if not sid:
                continue
            manifest_ids.append(sid)
            st = state(sid)
            st.acquisition_status = entry.get("acquisition_status")
            st.locator_scheme = entry.get("locator_system") or st.locator_scheme

    if ACQ_REGISTRY.exists():
        for entry in parse_yaml_list(ACQ_REGISTRY.read_text(encoding="utf-8"), "entries"):
            sid = entry.get("source_id")
            if not sid:
                continue
            st = state(sid)
            if st.acquisition_status is None:
                st.acquisition_status = entry.get("acquisition_status")
            st.edition_verified = entry.get("edition_verified")
            if entry.get("locator_scheme"):
                st.locator_scheme = entry.get("locator_scheme")
            proc = entry.get("processing_status")
            if isinstance(proc, dict):
                st.reg_mapped = proc.get("mapped")
                st.reg_source_cards_started = proc.get("source_cards_started")

    wave1_ids: list[str] = []
    if ID_REGISTRY.exists():
        for entry in parse_yaml_list(ID_REGISTRY.read_text(encoding="utf-8"), "wave_1"):
            sid = entry.get("source_id")
            if sid:
                wave1_ids.append(sid)
    wave1_ids.sort()

    # Book maps
    book_maps = 0
    maps_awaiting_review = 0
    for path in sorted(BOOK_MAPS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        fm = read_frontmatter(path)
        sid = fm.get("source_id")
        if not sid:
            continue
        book_maps += 1
        review = fm.get("operator_review_status")
        st = state(sid)
        st.has_book_map = True
        st.book_map_review = review
        if review != "reviewed":
            maps_awaiting_review += 1

    # Source cards
    source_cards = 0
    cards_awaiting_review = 0
    for path in sorted(SOURCE_CARDS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        fm = read_frontmatter(path)
        sid = fm.get("source_id")
        if not sid:
            continue
        source_cards += 1
        st = state(sid)
        if fm.get("operator_review_status") == "reviewed":
            st.reviewed_source_cards += 1
        else:
            st.unreviewed_source_cards += 1
            cards_awaiting_review += 1

    # Claim/tension cards
    claim_cards = 0
    claim_cards_awaiting_review = 0
    for path in sorted(CLAIM_CARDS_DIR.glob("*.md")):
        if path.name.startswith("_"):
            continue
        fm = read_frontmatter(path)
        if not fm.get("card_id"):
            continue
        claim_cards += 1
        reviewed = fm.get("operator_review_status") == "reviewed"
        if not reviewed:
            claim_cards_awaiting_review += 1
        body = path.read_text(encoding="utf-8")
        ref_sids = {cid[:7] for cid in CARD_ID_RE.findall(body)}
        for sid in ref_sids:
            st = state(sid)
            st.claim_tension_refs += 1
            if reviewed:
                st.in_reviewed_claim_card = True

    # Evals
    eval_cases = 0
    eval_unscored = 0
    eval_scored = 0
    eval_other_scoring: dict[str, int] = {}
    for path in sorted(EVALS_DIR.rglob("case.md")):
        fm = read_frontmatter(path)
        if not fm.get("case_id"):
            continue
        eval_cases += 1
        scoring = fm.get("scoring_status")
        if scoring == "unscored":
            eval_unscored += 1
        elif scoring == "scored":
            eval_scored += 1
        else:
            eval_other_scoring[scoring or "(missing)"] = (
                eval_other_scoring.get(scoring or "(missing)", 0) + 1
            )
        body = path.read_text(encoding="utf-8")
        ref_sids = {cid[:7] for cid in CARD_ID_RE.findall(body)}
        for sid in ref_sids:
            st = state(sid)
            st.eval_refs += 1
            st.in_eval = True

    result_counts: dict[str, int] = {}
    for path in sorted(EVALS_DIR.rglob("score-sheet.md")):
        status = result_status(path)
        key = status or "(none)"
        result_counts[key] = result_counts.get(key, 0) + 1

    # --- report ------------------------------------------------------------
    out: list[str] = []
    out.append("== Anti-Slop artifact status ==")
    out.append("Read-only scanner (scripts/artifact_status.py). Changes nothing.")
    out.append(
        f"Scanned: {len(manifest_ids)} manifest source_ids, {book_maps} book maps, "
        f"{source_cards} source cards, {claim_cards} claim/tension cards, "
        f"{eval_cases} eval cases."
    )
    out.append("")

    detail_ids = sorted(sid for sid, st in states.items() if st.has_any_artifact)
    out.append(f"-- Per-source artifact detail ({len(detail_ids)} sources with artifacts) --")
    if not detail_ids:
        out.append("(no source has an artifact yet)")
    for sid in detail_ids:
        st = states[sid]
        out.append(f"{sid}  level L{st.level()}")
        if st.has_book_map:
            out.append(f"  book map:            present, operator_review_status={st.book_map_review}")
        else:
            out.append("  book map:            none")
        out.append(
            f"  source cards:        {st.reviewed_source_cards} reviewed, "
            f"{st.unreviewed_source_cards} unreviewed"
        )
        out.append(f"  claim/tension refs:  {st.claim_tension_refs}")
        out.append(f"  eval case refs:      {st.eval_refs}")
        out.append(
            f"  registry:            mapped={fmt(st.reg_mapped)}  "
            f"source_cards_started={fmt(st.reg_source_cards_started)}"
        )
        for flag in st.drift():
            out.append(f"  DRIFT: {flag}")
    out.append("")

    out.append("-- Aggregate WIP --")
    out.append(f"Book maps awaiting review:            {maps_awaiting_review}")
    out.append(f"Source cards awaiting review:         {cards_awaiting_review}")
    out.append(f"Claim/tension cards awaiting review:  {claim_cards_awaiting_review}")
    scoring_line = f"Evals: scoring_status unscored={eval_unscored} scored={eval_scored}"
    for key, count in sorted(eval_other_scoring.items()):
        scoring_line += f" {key}={count}"
    out.append(scoring_line)
    if result_counts:
        parts = " ".join(f"{k}={v}" for k, v in sorted(result_counts.items()))
        out.append(f"Evals by Result status:               {parts}")
    else:
        out.append("Evals by Result status:               (no score sheets found)")
    out.append("")

    out.append(f"-- First-50 level summary (wave-1, {len(wave1_ids)} source_ids) --")
    out.append("Each source counted once, at its highest level reached.")
    level_labels = {
        0: "L0 registered",
        1: "L1 sourced + locator/edition verified",
        2: "L2 reviewed book map",
        3: "L3 at least one reviewed source card",
        4: "L4 in a reviewed claim/tension card or an eval case",
    }
    level_counts = {n: 0 for n in range(5)}
    for sid in wave1_ids:
        level_counts[state(sid).level()] += 1
    for n in range(5):
        out.append(f"  {level_labels[n]:<52} {level_counts[n]}")
    advanced = sorted(sid for sid in wave1_ids if state(sid).level() >= 2)
    if advanced:
        out.append("  L2+ sources: " + ", ".join(advanced))
    out.append("")

    out.append("-- Drift summary (source_ids needing registry reconciliation) --")
    drifting = [(sid, states[sid].drift()) for sid in sorted(states) if states[sid].drift()]
    if not drifting:
        out.append("No drift detected.")
    else:
        out.append(
            "These source_ids have on-disk artifact state that disagrees with the "
            "acquisition registry. This scanner does not reconcile them — it reports only."
        )
        for sid, flags in drifting:
            out.append(f"  {sid}:")
            for flag in flags:
                out.append(f"    - {flag}")
    out.append("")
    out.append("Read-only scan complete. No files were modified.")

    print("\n".join(out))
    return 0


def fmt(value) -> str:
    if value is True:
        return "true"
    if value is False:
        return "false"
    return "unknown"


if __name__ == "__main__":
    sys.exit(main())
