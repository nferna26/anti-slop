<!--
SAMPLE / PLACEHOLDER negative fixture for the holdout-transfer smoke. status:
holdout_smoke_not_benchmark. This is NOT a live model run and NOT a benchmark
artifact: it is a static, hand-written stand-in for a "source-free" note,
written as if the author answered from memory with no fixture brief. It
deliberately breaks lineage so the deterministic citation-lineage gate (run with
--root pointed at this packet) has distinct findings to catch. The gate should
FAIL this file in both default and --require-reviewed mode. Not canon, not
source truth.

What the gate catches deterministically (lineage only):
  - fabricated card ID BK-7999-card-001 -> unresolved in BOTH modes
  - fabricated source ID BK-7999        -> unresolved in BOTH modes
  - unreviewed card BK-7902-card-002 cited as reviewed lineage -> caught under
    --require-reviewed
What a HUMAN reviewer additionally sees (the gate does NOT check these): the
invented precise grid reference and the population-decline over-claim are
locator/claim-anchoring failures, not lineage-resolution failures.
-->

# Source-Free Note (placeholder; intentionally fails the gate)

Note written without the fixture brief:

- The kernel of good observation is supported by `BK-7999-card-001` (Chapter 4).
- Locality should be recorded to a precise grid reference; see `BK-7901-card-002`
  at grid square 31U-DQ-9182 (a precise reference the card does not carry).
- Repeat counts dropped, so the population declined; per `BK-7902-card-002`
  (cited here as if it were reviewed lineage).
- General background drawn from source `BK-7999`.

This note cites a card ID and a source ID that do not resolve in the holdout
corpus (`BK-7999-card-001`, `BK-7999`), invents a locator precision that
`BK-7901-card-002` never carried, over-reads a confound warning as a decline,
and cites the unreviewed draft `BK-7902-card-002` as reviewed lineage.
