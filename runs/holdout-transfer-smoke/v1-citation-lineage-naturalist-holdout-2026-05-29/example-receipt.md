# Holdout-Transfer Smoke Receipt (example)

`status: holdout_smoke_not_benchmark` — not canon, not source truth. Example of
the receipt `python3 scripts/holdout_smoke.py` writes to a transient temp dir.
The compiled-brief sha256 varies between runs (the brief carries no date here,
but the value is shown abbreviated); the gate results are deterministic.

## Pipeline

1. compile-brief-equivalent over the holdout root from 3 reviewed cards
   (BK-7901-card-001, BK-7901-card-002, BK-7902-card-001); the deliberately
   unreviewed BK-7902-card-002 is excluded.
2. static stand-in notes under `outputs/` (placeholder model outputs; no model
   is run).
3. gate_citation_lineage.py --root <packet> in default + --require-reviewed.

## Gate results (mechanical lineage only)

- brief-assisted note: default exit 0, --require-reviewed exit 0 (PASS / PASS) —
  every cited card resolves to a reviewed holdout card; no unreviewed-as-reviewed
  reference.
- source-free note: default exit 1 (8 unresolved: fabricated BK-7999-card-001 /
  BK-7999), --require-reviewed exit 1 (11 unresolved: + 3 unreviewed-as-reviewed
  BK-7902-card-002) — FAIL / FAIL.

The gate enforces card-ID/source-ID resolution and reviewed-lineage discipline.
Locator correctness, claim anchoring, and refusal of excess are human-inspected,
not gate-enforced. A model output is a test artifact, never an authority.
