<!--
SAMPLE / PLACEHOLDER output for the holdout-transfer smoke. status:
holdout_smoke_not_benchmark. This is NOT a live model run and NOT a benchmark
artifact: it is a static, hand-written stand-in for a "brief-assisted" corrected
note, written as if the author had the holdout fixture brief in hand. It cites
only reviewed holdout cards at the locators those cards carry, anchors each
claim to a card, and refuses unsupported excess. The deterministic
citation-lineage gate (run with --root pointed at this packet) should PASS this
file in both default and --require-reviewed mode. Not canon, not source truth.
-->

# Brief-Assisted Note (placeholder; holdout corpus)

Corrected note, written against the holdout fixture brief:

- An observation log entry records what was seen; a motive is a separate
  inference. Supported by `BK-7901-card-001` (Chapter 2).
- Locality precision must match what was actually determined. Supported by
  `BK-7901-card-002` (Chapter 5, Section 3).
- A change in repeat plant counts is not a population change until the seasonal
  visibility confound is controlled. Supported by `BK-7902-card-001`
  (Chapter 3).

## Removed / unsupported (refused excess)

- A request for a precise grid reference for the locality discipline rule is
  refused: `BK-7901-card-002` carries only a coarse precision-discipline claim,
  so an exact grid reference is not supported.
- A request to report the repeat-count drop as a population decline is refused:
  `BK-7902-card-001` carries only the seasonal-confound warning, not a decline
  finding.
- The inter-observer-agreement draft is named only by its source ID `BK-7902`,
  because its draft card has not cleared review and must not be cited as
  reviewed lineage.

## Supported lineage

- `BK-7901-card-001`, Chapter 2 — observation vs. inferred cause.
- `BK-7901-card-002`, Chapter 5, Section 3 — locality locator discipline.
- `BK-7902-card-001`, Chapter 3 — seasonal confound in repeat counts.
