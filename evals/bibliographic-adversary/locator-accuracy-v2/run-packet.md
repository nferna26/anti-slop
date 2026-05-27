---
case_id: locator-accuracy-v2
artifact: run-packet
eval_type: bibliographic-adversary
benchmark_version: locator-accuracy-v2-v0-design
status: design_only_not_frozen_not_run
created: 2026-05-27
---

# Run Packet - locator-accuracy-v2-v0-design

This is a placeholder run packet for v2 calibration repair. It is not a frozen
benchmark packet and must not be used to generate model outputs.

## Status

Design-only, not frozen, not run as a benchmark. No condition packets are
hashed here. No substrate brief is recompiled here. No benchmark outputs exist.

The 2026-05-27 calibration rehearsal did not clear the pre-freeze gate:
`hosted_anthropic` matched F1-F5 but missed coverage Anchor H, and
`hosted_openai` did not run because no OpenAI API credential was available in
the Codex shell. See `calibration-decision.md`.

## Calibration Rehearsal Plan

Before any v2 freeze:

1. Build a calibration-only packet from `case.md` -> `## Scoring rubric` and
   `judge-packet/calibration-anchors.md` Surface 1 / Surface 1B.
2. Send only judge-facing surfaces to hosted Anthropic and hosted OpenAI.
3. Withhold Surface 2 / Surface 2B until after each route scores.
4. Compare each route to the reference key exactly:
   - F1-F5 anchors A-F must match exactly;
   - coverage anchors G-L must match exactly;
   - no F1/F3 mutual-exclusion violation;
   - parser-computed totals must equal flagged failure counts if totals are
     requested.
5. If either hosted primary route fails or is unavailable, leave v2 design-only
   and do not freeze.
6. If both hosted routes pass, a later tranche may freeze a real
   `locator-accuracy-v2-v1` benchmark packet with hashes, condition packets,
   generator settings, substrate-brief hash, and the unchanged X/Y/Z rule.

## Boundary

This file records intended calibration rehearsal only. It does not certify judge
eligibility, does not freeze a packet, does not authorize generation, and does
not lift any Result.
