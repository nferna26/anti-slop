#!/usr/bin/env python3
"""Holdout-transfer smoke for the deterministic citation-lineage primitive.

status: holdout_smoke_not_benchmark. This is NOT a benchmark and NOT canon. It
does not measure any model and does not claim advice/slop/reasoning improvement.

Question it probes: does the *mechanical* citation-lineage primitive (a cited
card ID resolves to a reviewed card in the corpus, and fabricated /
unreviewed-as-reviewed citations are caught) transfer to a corpus that is NOT
the business-strategy corpus the locator-accuracy-v4 benchmark was run over?

It does this fully offline (no API key, no network, no model runtime, no raw
book) over a self-contained holdout fixture corpus in a different domain
(synthetic field-naturalism cards, reserved BK-79## band):

  1. compile an *equivalent* fixture brief from the holdout corpus's REVIEWED
     cards (compile_brief.py has no --root and reads the real corpus, so this
     reproduces its shape over the holdout root) -> temp file.
  2. two static, committed stand-in notes under outputs/ play the role of a
     model output (NO model is run): a brief-assisted note that cites only
     resolving reviewed cards and refuses unsupported excess, and a source-free
     note that fabricates an ID and cites an unreviewed card as reviewed lineage.
  3. gate_citation_lineage.py --root <packet> checks each note in BOTH default
     (existence) and --require-reviewed modes.

The smoke asserts the gate's mechanical behaviour transfers: PASS the
brief-assisted note in both modes, FAIL the source-free note in both modes. Exit
0 only when all four gate behaviours hold. A model output is a test artifact,
never an authority.

What the gate enforces (deterministic): card-ID / source-ID resolution and
reviewed-lineage discipline. What it does NOT enforce: locator-text correctness,
claim-anchoring, or whether a refusal happened — those are human-inspected
properties of the two notes, illustrative only.

Deterministic rerun:  python3 scripts/holdout_smoke.py
Self-test alias:      python3 scripts/holdout_smoke.py --self-test
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
PACKET = ROOT / "runs" / "holdout-transfer-smoke" / \
    "v1-citation-lineage-naturalist-holdout-2026-05-29"
GATE = ROOT / "scripts" / "gate_citation_lineage.py"
CARDS_DIR = PACKET / "corpus" / "source-cards"
OUTPUTS = PACKET / "outputs"

REVIEWED_INPUT_CARDS = ["BK-7901-card-001", "BK-7901-card-002", "BK-7902-card-001"]
UNREVIEWED_CARD = "BK-7902-card-002"


def _frontmatter(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    lines = text.splitlines()
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
        fields[key.strip()] = value.strip()
    return fields


def _section(text: str, heading: str) -> str:
    out: list[str] = []
    capture = False
    wanted = heading.strip().lower()
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("## "):
            if capture:
                break
            capture = stripped[3:].strip().lower() == wanted
            continue
        if capture:
            out.append(line)
    return "\n".join(out).strip()


def build_fixture_brief() -> str:
    """compile_brief-equivalent over the holdout root (reviewed cards only)."""
    lines = [
        "---",
        "brief_id: holdout-transfer-smoke",
        "status: machine_compiled_not_canon",
        "smoke_status: holdout_smoke_not_benchmark",
        "include_unreviewed: false",
        "input_cards:",
    ]
    lines += [f"  - {cid}" for cid in REVIEWED_INPUT_CARDS]
    lines += [
        "---",
        "",
        "# Holdout Fixture Brief (compiled, not canon, not source truth)",
        "",
        "Equivalent of compile_brief.py compiled over the HOLDOUT corpus root.",
        "Reviewed fixture cards only; the deliberately-unreviewed "
        f"`{UNREVIEWED_CARD}` is excluded (mirrors include_unreviewed=false).",
        "",
        "## Included Cards",
        "",
    ]
    lines += [f"- `{cid}`" for cid in REVIEWED_INPUT_CARDS]
    lines += ["", "## Source Cards", ""]
    for cid in REVIEWED_INPUT_CARDS:
        path = CARDS_DIR / f"{cid}.md"
        text = path.read_text(encoding="utf-8")
        fm = _frontmatter(text)
        lines += [
            f"### {cid} - {fm.get('title', cid)}",
            f"- Source: `{fm.get('source_id', 'unknown')}`",
            f"- Locator: {fm.get('locator', 'unknown')}",
            f"- Review status: `{fm.get('operator_review_status', 'unknown')}`",
            "",
            "#### Claim",
            _section(text, "Claim") or "None recorded.",
            "",
            "#### Scope Conditions",
            _section(text, "Scope conditions") or "None recorded.",
            "",
            "#### Misuse Risk",
            _section(text, "Misuse risk") or "None recorded.",
            "",
        ]
    return "\n".join(lines)


def gate(note: pathlib.Path, require_reviewed: bool) -> int:
    argv = [sys.executable, str(GATE), "--root", str(PACKET)]
    if require_reviewed:
        argv.append("--require-reviewed")
    argv.append(str(note))
    return subprocess.run(argv, capture_output=True, text=True).returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true",
                        help="alias for the default deterministic rerun")
    parser.parse_args()

    out_dir = pathlib.Path(tempfile.mkdtemp(prefix="holdout-transfer-smoke-"))
    print("== Anti-Slop holdout-transfer smoke (holdout_smoke_not_benchmark) ==")
    print(f"Packet: {PACKET.relative_to(ROOT)}")
    print(f"Working dir (transient): {out_dir}")

    # 1. compile-brief-equivalent over the holdout root.
    brief_text = build_fixture_brief()
    brief = out_dir / "holdout-brief.compiled.md"
    brief.write_text(brief_text, encoding="utf-8")
    brief_sha = hashlib.sha256(brief.read_bytes()).hexdigest()
    # reviewed cards are rendered as ### blocks and listed; the unreviewed card
    # may be NAMED in explanatory prose but must not be rendered/listed as input.
    brief_ok = (all(f"### {cid}" in brief_text for cid in REVIEWED_INPUT_CARDS)
                and f"### {UNREVIEWED_CARD}" not in brief_text
                and f"- `{UNREVIEWED_CARD}`" not in brief_text)
    print(f"[1/3] compiled fixture brief from {len(REVIEWED_INPUT_CARDS)} "
          f"reviewed holdout cards -> {brief.name} (sha256 {brief_sha[:16]}...); "
          f"reviewed-only={'ok' if brief_ok else 'FAIL'}")

    # 2/3. gate the two static notes in both modes against the holdout --root.
    good = OUTPUTS / "brief-assisted-note.md"
    slop = OUTPUTS / "source-free-note.md"
    good_def, good_rev = gate(good, False), gate(good, True)
    slop_def, slop_rev = gate(slop, False), gate(slop, True)
    print(f"[2/3] brief-assisted note: default exit {good_def} (expect 0), "
          f"--require-reviewed exit {good_rev} (expect 0)")
    print(f"[3/3] source-free note:    default exit {slop_def} (expect 1), "
          f"--require-reviewed exit {slop_rev} (expect 1)")

    checks = {
        "brief reviewed-only compile": brief_ok,
        "brief-assisted PASS (default)": good_def == 0,
        "brief-assisted PASS (--require-reviewed)": good_rev == 0,
        "source-free FAIL (default)": slop_def == 1,
        "source-free FAIL (--require-reviewed)": slop_rev == 1,
    }
    failed = [name for name, ok in checks.items() if not ok]

    receipt = out_dir / "holdout-smoke-receipt.md"
    receipt.write_text(
        "# Holdout-Transfer Smoke Receipt (holdout_smoke_not_benchmark)\n\n"
        "Deterministic, offline. No API key, network, model runtime, or raw "
        "book. Not a benchmark, not canon, not source truth. The static notes "
        "are placeholders, not model runs.\n\n"
        "## Pipeline\n\n"
        f"1. compile-brief-equivalent over the holdout root from "
        f"{len(REVIEWED_INPUT_CARDS)} reviewed cards "
        f"({', '.join(REVIEWED_INPUT_CARDS)}); brief sha256 `{brief_sha}`.\n"
        f"2. static stand-in notes under `{OUTPUTS.relative_to(ROOT)}`.\n"
        "3. gate_citation_lineage.py --root <packet> in default + "
        "--require-reviewed.\n\n"
        "## Gate results (mechanical lineage only)\n\n"
        f"- brief-assisted note: default exit {good_def}, "
        f"--require-reviewed exit {good_rev} (expect 0 / 0 = PASS).\n"
        f"- source-free note: default exit {slop_def}, "
        f"--require-reviewed exit {slop_rev} (expect 1 / 1 = FAIL).\n\n"
        "The gate enforces card-ID/source-ID resolution and reviewed-lineage "
        "discipline. Locator correctness, claim anchoring, and refusal are "
        "human-inspected, not gate-enforced.\n",
        encoding="utf-8",
    )
    print(f"\nReceipt: {receipt}")

    if not failed:
        print("HOLDOUT SMOKE PASSED: the deterministic citation-lineage primitive "
              "transfers to the holdout corpus (resolved reviewed lineage, "
              "rejected fabricated + unreviewed-as-reviewed citations).")
        return 0
    print("HOLDOUT SMOKE FAILED:")
    for name in failed:
        print(f"  - {name}")
    return 1


if __name__ == "__main__":
    sys.exit(main())
