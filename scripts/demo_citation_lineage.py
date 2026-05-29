#!/usr/bin/env python3
"""Stranger-reproducible demo of the mechanical-lineage primitive.

Pipeline, with no API key, no network, no model runtime, and no raw book:

  1. compile_brief.py   -> compile a non-canon decision brief from reviewed
                           public-KB source cards (public paraphrases + locators).
  2. (placeholder)      -> a static, committed sample "corrected note" stands in
                           for a model output (proof/citation-lineage-demo/).
  3. gate_citation_lineage.py --require-reviewed
                        -> deterministically check that every card/source the
                           note cites resolves to a REVIEWED public-KB artifact.
  4. receipt            -> write a public-safe receipt of what was checked.

The demo asserts the gate PASSES the good sample and FAILS the slop sample
(which cites a nonexistent card), so it both shows the tool working and proves
it catches a fabricated citation. Exit 0 only when the gate behaves correctly.

Transient outputs (compiled brief, receipt) go to a fresh temp dir so a clean
checkout is never mutated; the temp paths are printed at the end.
"""

from __future__ import annotations

import hashlib
import pathlib
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEMO = ROOT / "proof" / "citation-lineage-demo"
GATE = ROOT / "scripts" / "gate_citation_lineage.py"
COMPILE = ROOT / "scripts" / "compile_brief.py"
CARDS = ["BK-0048-card-001", "BK-0001-card-001", "BK-0002-card-001",
         "BK-0042-card-001", "BK-0044-card-002"]


def run(argv: list[str]) -> tuple[int, str]:
    proc = subprocess.run([sys.executable, *argv], capture_output=True, text=True)
    return proc.returncode, proc.stdout + proc.stderr


def main() -> int:
    out_dir = pathlib.Path(tempfile.mkdtemp(prefix="citation-lineage-demo-"))
    brief = out_dir / "compiled-brief.md"
    receipt = out_dir / "demo-receipt.md"

    print("== Anti-Slop citation-lineage demo ==")
    print(f"Working dir (transient): {out_dir}")

    # 1. compile a brief from reviewed source cards (public paraphrases only).
    rc, log = run([str(COMPILE), "citation-lineage-demo", *CARDS,
                   "--no-related-tensions",
                   "--question", "Demo: cite only reviewed public-KB lineage.",
                   "--output", str(brief)])
    if rc != 0 or not brief.exists():
        print("FAIL: compile_brief did not produce a brief.\n" + log)
        return 1
    brief_sha = hashlib.sha256(brief.read_bytes()).hexdigest()
    print(f"[1/3] compiled brief from {len(CARDS)} reviewed cards -> {brief.name} (sha256 {brief_sha[:16]}...)")

    # 2/3. gate the good and slop samples.
    good = DEMO / "sample-corrected-note.md"
    slop = DEMO / "sample-slop-note.md"
    good_rc, good_log = run([str(GATE), "--require-reviewed", str(good)])
    slop_rc, slop_log = run([str(GATE), "--require-reviewed", str(slop)])
    print(f"[2/3] gate on good sample  -> exit {good_rc} (expect 0 / PASS)")
    print(f"[3/3] gate on slop sample  -> exit {slop_rc} (expect 1 / FAIL)")

    receipt.write_text(
        "# Citation-Lineage Demo Receipt\n\n"
        "Deterministic, offline demo of the mechanical-lineage primitive. No API\n"
        "key, network, model runtime, or raw book is used.\n\n"
        "## Pipeline\n\n"
        f"1. compile_brief from {len(CARDS)} reviewed source cards "
        f"({', '.join(CARDS)}); brief sha256 `{brief_sha}`.\n"
        "2. static sample corrected note (placeholder model output) under "
        "`proof/citation-lineage-demo/`.\n"
        "3. gate_citation_lineage.py --require-reviewed.\n\n"
        "## Results\n\n"
        f"- good sample (`sample-corrected-note.md`): gate exit {good_rc} "
        f"({'PASS' if good_rc == 0 else 'FAIL'}); cites only reviewed cards at reviewed locators.\n"
        f"- slop sample (`sample-slop-note.md`): gate exit {slop_rc} "
        f"({'FAIL — unresolved reference caught' if slop_rc == 1 else 'unexpected'}); "
        "cites a nonexistent card `BK-9999-card-001`.\n\n"
        "A model output is a test artifact, never an authority. This receipt "
        "records a deterministic citation check, not source truth or canon.\n",
        encoding="utf-8",
    )

    ok = good_rc == 0 and slop_rc == 1
    print(f"\nReceipt: {receipt}")
    if ok:
        print("DEMO PASSED: gate accepted reviewed lineage and rejected the fabricated citation.")
        return 0
    print("DEMO FAILED: gate did not behave as expected.")
    print("--- good log ---\n" + good_log)
    print("--- slop log ---\n" + slop_log)
    return 1


if __name__ == "__main__":
    sys.exit(main())
