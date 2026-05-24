#!/usr/bin/env python3
"""Artifact-packet status dashboard for the books-kb control plane.

Read-only. Reads the public manifests and the local-only operator-approval
packets prepared for first-50 metadata/locator verification, and reports whether
each packet is reviewable, how it compares to current public-manifest state, and
who is in the operator review queue.

It is a bridge for operator review. It applies nothing: no metadata is written to
any public manifest, no status is lifted, no artifact is created. Applying a
packet remains a separate, operator-approved Workflow 2 action.

- Standard library only. No model/API calls, no embeddings, no graph DB.
- Reads operator-approval packet metadata only; never reads raw source files.
- Public-safe output: prints source_ids, field names, and bibliographic metadata
  that is already destined for the public manifest — never raw source text,
  never private filesystem paths, never raw filenames.
- Always exits 0. This is a dashboard, not a gate.
"""

from __future__ import annotations

from pathlib import Path
import re
import sys

from artifact_status import parse_yaml_list

ROOT = Path(__file__).resolve().parents[1]

BOOKS = ROOT / "corpus" / "manifests" / "books-200.yaml"
ACQ = ROOT / "corpus" / "manifests" / "acquisition-registry.yaml"
ID_REGISTRY = ROOT / "corpus" / "manifests" / "source-id-registry.yaml"
PACKET_ROOT = ROOT / "local-only" / "phase-2-verification"

PACKET_FILES = (
    "approval-summary.md",
    "proposed-public-update.yaml",
    "operator-checklist.md",
    "quality-audit.md",
)

# Books_200 metadata/locator fields a packet proposes and the manifest carries.
COMPARE_FIELDS = ("edition", "year", "publisher", "isbn", "owned_format", "locator_system")
BLANK_FIELDS = ("edition", "year", "publisher", "isbn", "locator_system")

GUARD_RE = re.compile(r"edition_verified:\s*false")
GUARD_COMMENT = "set true only after operator approval"


# --- packet YAML parsing ---------------------------------------------------

def strip_inline_comment(line: str) -> str:
    in_s = in_d = esc = False
    for i, ch in enumerate(line):
        if esc:
            esc = False
            continue
        if ch == "\\":
            esc = True
            continue
        if ch == "'" and not in_d:
            in_s = not in_s
        elif ch == '"' and not in_s:
            in_d = not in_d
        elif ch == "#" and not in_s and not in_d:
            return line[:i]
    return line


def parse_scalar(value: str):
    value = value.strip()
    if value in {"", "null", "Null", "NULL", "~"}:
        return None
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_packet_yaml(text: str) -> dict:
    """Parse a proposed-public-update.yaml into a nested dict (indentation-based)."""
    root: dict = {}
    stack: list[tuple[int, dict]] = [(-1, root)]
    for raw in text.splitlines():
        line = strip_inline_comment(raw).rstrip()
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        content = line.strip()
        if content.startswith("- ") or ":" not in content:
            continue
        key, _, val = content.partition(":")
        key, val = key.strip(), val.strip()
        while stack and stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1] if stack else root
        if val == "":
            child: dict = {}
            parent[key] = child
            stack.append((indent, child))
        else:
            parent[key] = parse_scalar(val)
    return root


# --- packet model ----------------------------------------------------------

class Packet:
    def __init__(self, source_id: str, path: Path) -> None:
        self.source_id = source_id
        self.path = path
        self.files_present: list[str] = []
        self.shape_ok = False
        self.parse_ok = False
        self.parsed: dict = {}
        self.has_guard = False
        self.parse_error: str | None = None

    @property
    def books_block(self) -> dict:
        block = self.parsed.get("books_200_yaml")
        return block if isinstance(block, dict) else {}

    @property
    def acq_block(self) -> dict:
        block = self.parsed.get("acquisition_registry_yaml")
        return block if isinstance(block, dict) else {}


def load_packets() -> list[Packet]:
    packets: list[Packet] = []
    if not PACKET_ROOT.exists():
        return packets
    for source_dir in sorted(PACKET_ROOT.glob("BK-*")):
        approval_dir = source_dir / "operator-approval"
        if not approval_dir.is_dir():
            continue
        pkt = Packet(source_dir.name, approval_dir)
        pkt.files_present = sorted(p.name for p in approval_dir.iterdir() if p.is_file())
        pkt.shape_ok = set(pkt.files_present) == set(PACKET_FILES)
        proposed = approval_dir / "proposed-public-update.yaml"
        if proposed.is_file():
            text = proposed.read_text(encoding="utf-8")
            try:
                pkt.parsed = parse_packet_yaml(text)
                pkt.parse_ok = bool(
                    pkt.parsed.get("source_id")
                    and isinstance(pkt.parsed.get("books_200_yaml"), dict)
                    and isinstance(pkt.parsed.get("acquisition_registry_yaml"), dict)
                )
            except Exception as exc:  # noqa: BLE001 - dashboard must not crash
                pkt.parse_error = type(exc).__name__
            for raw in text.splitlines():
                if GUARD_RE.search(raw) and GUARD_COMMENT in raw:
                    pkt.has_guard = True
                    break
        packets.append(pkt)
    return packets


# --- comparison ------------------------------------------------------------

def norm(value) -> str:
    return "" if value is None else str(value).strip()


def application_state(pkt: Packet, books_row: dict) -> tuple[str, list[str]]:
    """Classify a packet against current public books-200 state.

    Returns (state, detail_lines). state in {PENDING, APPLIED, STALE, UNKNOWN}.
    """
    if not pkt.parse_ok:
        return "UNKNOWN", ["packet did not parse"]
    public_blank = all(not norm(books_row.get(f)) for f in BLANK_FIELDS)
    if public_blank:
        return "PENDING", []
    mismatches: list[str] = []
    for field in COMPARE_FIELDS:
        proposed = norm(pkt.books_block.get(field))
        public = norm(books_row.get(field))
        if proposed and public and proposed != public:
            mismatches.append(f'{field}  public="{public}"  packet="{proposed}"')
    if mismatches:
        return "STALE", mismatches
    return "APPLIED", []


# --- report ----------------------------------------------------------------

def main() -> int:
    packets = load_packets()
    books = {r.get("source_id"): r for r in parse_yaml_list(
        BOOKS.read_text(encoding="utf-8"), "books")} if BOOKS.exists() else {}
    acq = {r.get("source_id"): r for r in parse_yaml_list(
        ACQ.read_text(encoding="utf-8"), "entries")} if ACQ.exists() else {}
    wave1 = parse_yaml_list(ID_REGISTRY.read_text(encoding="utf-8"), "wave_1") \
        if ID_REGISTRY.exists() else []
    wave1_by_id = {r.get("source_id"): r for r in wave1}

    book_map_ids = {p.stem for p in (ROOT / "corpus" / "book-maps").glob("BK-*.md")}

    out: list[str] = []
    out.append("== Anti-Slop artifact-packet status ==")
    out.append("Read-only dashboard. Reads public manifests + local-only operator-approval")
    out.append("packets. Changes nothing — applies no metadata, lifts no status.")
    out.append("")

    # -- inventory --
    shape_ok = sum(1 for p in packets if p.shape_ok)
    parse_ok = sum(1 for p in packets if p.parse_ok)
    guard_ok = sum(1 for p in packets if p.has_guard)
    out.append("-- Packet inventory --")
    out.append(f"Operator-approval packets found:      {len(packets)}")
    out.append(f"Packet shape valid (exactly 4 files):  {shape_ok} / {len(packets)}")
    out.append(f"proposed-public-update.yaml parses:    {parse_ok} / {len(packets)}")
    out.append(
        f"Guarded-proposal convention present:   {guard_ok} / {len(packets)}  "
        f'(edition_verified: false + "{GUARD_COMMENT}")'
    )
    for pkt in packets:
        if not pkt.shape_ok:
            out.append(f"  [shape] {pkt.source_id}: files present = {pkt.files_present}")
        if not pkt.parse_ok:
            reason = pkt.parse_error or "missing source_id / books_200_yaml / acquisition_registry_yaml"
            out.append(f"  [parse] {pkt.source_id}: {reason}")
    out.append("")

    # -- coverage --
    sourced_first50 = [
        sid for sid in wave1_by_id
        if norm((acq.get(sid) or {}).get("acquisition_status")
                or (books.get(sid) or {}).get("acquisition_status")) == "sourced"
    ]
    rights_blocked = sorted(
        sid for sid in wave1_by_id
        if norm((acq.get(sid) or {}).get("raw_source_status")
                or (books.get(sid) or {}).get("raw_source_status")) == "metadata_only"
    )
    packetable = sorted(set(sourced_first50) - set(rights_blocked))
    packet_ids = {p.source_id for p in packets}
    covered = sorted(sid for sid in packetable if sid in packet_ids)
    uncovered = sorted(sid for sid in packetable if sid not in packet_ids)
    extra = sorted(packet_ids - set(packetable) - set(rights_blocked))

    first30 = [sid for sid in packetable
               if bool(wave1_by_id.get(sid, {}).get("first_30_deep_card_candidate"))]
    first30_covered = sorted(sid for sid in first30 if sid in packet_ids)

    out.append("-- First-50 packet coverage --")
    out.append(f"Sourced first-50 books, packetable:    {len(packetable)}")
    out.append(f"  with an operator-approval packet:    {len(covered)} / {len(packetable)}")
    if uncovered:
        out.append(f"  MISSING a packet:                    {', '.join(uncovered)}")
    if extra:
        out.append(f"  packet present but not packetable:   {', '.join(extra)}")
    out.append(f"First-30 deep-card candidates (sourced): {len(first30)}")
    out.append(f"  with a packet:                       {len(first30_covered)} / {len(first30)}")
    out.append(f"Rights/access blocked (no packet by design): {', '.join(rights_blocked) or 'none'}")
    out.append("")

    # -- application state --
    pending, applied, stale, unknown = [], [], [], []
    stale_detail: dict[str, list[str]] = {}
    for pkt in packets:
        state, detail = application_state(pkt, books.get(pkt.source_id) or {})
        if state == "PENDING":
            pending.append(pkt.source_id)
        elif state == "APPLIED":
            applied.append(pkt.source_id)
        elif state == "STALE":
            stale.append(pkt.source_id)
            stale_detail[pkt.source_id] = detail
        else:
            unknown.append(pkt.source_id)

    out.append("-- Packet application state vs public manifests --")
    out.append(f"PENDING  (public fields still blank; not yet applied):  {len(pending)}")
    if pending:
        out.append("  " + ", ".join(sorted(pending)))
    out.append(f"APPLIED  (public manifest already matches the packet):  {len(applied)}")
    if applied:
        out.append("  " + ", ".join(sorted(applied)))
    out.append(f"STALE    (public manifest populated but DIFFERS):       {len(stale)}")
    for sid in sorted(stale):
        out.append(f"  {sid}:")
        for line in stale_detail[sid]:
            out.append(f"    {line}")
    if unknown:
        out.append(f"UNKNOWN  (packet did not parse):                        {len(unknown)}")
        out.append("  " + ", ".join(sorted(unknown)))
    out.append("")

    # -- operator review queue (state-driven; awaiting lanes are PENDING only) --
    # Awaiting-approval lanes carry ONLY pending packets. APPLIED packets are
    # done and STALE packets are superseded; neither belongs in an awaiting lane.
    q_map, q_first30, q_remaining = [], [], []
    for sid in sorted(pending):
        flags = wave1_by_id.get(sid, {})
        if bool(flags.get("first_30_deep_card_candidate")):
            q_first30.append(sid)
        elif bool(flags.get("map_candidate")):
            q_map.append(sid)
        else:
            q_remaining.append(sid)
    anchors = sorted(sid for sid in packet_ids if sid in book_map_ids)

    out.append("-- Operator review queue --")
    out.append(f"Awaiting operator approval — PENDING packets only ({len(pending)}), "
               "grouped by candidate type:")
    out.append(f"  Map candidates ({len(q_map)}):")
    out.append("    " + (", ".join(q_map) or "none"))
    out.append(f"  First-30 deep-card candidates ({len(q_first30)}):")
    out.append("    " + (", ".join(q_first30) or "none"))
    out.append(f"  Remaining sourced first-50 ({len(q_remaining)}):")
    out.append("    " + (", ".join(q_remaining) or "none"))
    out.append("Not awaiting approval:")
    out.append(f"  Applied — metadata/locator already in the public manifests ({len(applied)}):")
    out.append("    " + (", ".join(sorted(applied)) or "none"))
    out.append(f"  Superseded — STALE packets, do NOT apply ({len(stale)}):")
    out.append("    " + (", ".join(sorted(stale)) or "none"))
    if unknown:
        out.append(f"  Unparseable packets — needs inspection ({len(unknown)}):")
        out.append("    " + ", ".join(sorted(unknown)))
    out.append(f"  Rights/access blockers — separate workflow, no packet ({len(rights_blocked)}):")
    out.append("    " + (", ".join(rights_blocked) or "none"))
    out.append(f"  Note — artifact-bearing anchors ({len(anchors)}), already have a public book map:")
    out.append("    " + (", ".join(anchors) or "none"))
    out.append("    Their packets are APPLIED or STALE above; never apply an anchor packet blind.")
    out.append("")

    out.append("-- How to read this board --")
    out.append("Local-only packets are preparation, not approval. A packet in PENDING is a")
    out.append("proposal awaiting operator review; APPLIED means the public manifest already")
    out.append("carries those values; STALE means the public manifest was verified to")
    out.append("different values and the packet is superseded — do not apply it. Applying any")
    out.append("packet is a separate, operator-approved Workflow 2 action. This dashboard")
    out.append("changes nothing.")
    out.append("")
    out.append("Exit status: 0 (read-only dashboard)")

    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
