---
artifact: operator-calibration-check
case_id: diagnosis-vs-validated-learning-benefits-renewal-v3
benchmark_version: diagnosis-vs-validated-learning-benefits-renewal-v3-v1
audience: operator-only
---

# Operator Calibration Check — v3 Independent Judge

**Operator-only.** Do not send this file, and do not send the Surface 2
reference verdicts in `calibration-anchors.md`, to the judge. The judge receives
only `independent-judge-packet-calibration.md` (Part 1) and, if and only if it
clears calibration, `independent-judge-packet-scoring.md` (Part 2).

## Procedure

1. **Send Part 1.** Give the judge `independent-judge-packet-calibration.md`
   only. It returns three lines — `[ANCHOR-A]`, `[ANCHOR-B]`, `[ANCHOR-C]` — each
   with `C1`–`C6` verdicts and a `TOTAL`.
2. **Record** the judge's three returned anchor lines verbatim.
3. **Compare** them, criterion by criterion, against the Surface 2 reference in
   `calibration-anchors.md` → `## Reference verdict summary` and the per-anchor
   reference blocks. Do not reveal those reference verdicts to the judge.
4. **Apply the pre-registered eligibility gate** (`calibration-anchors.md` →
   `## Judge eligibility rule`): the judge is eligible only if its anchor
   verdicts differ from the reference by **no more than two criteria total**
   across all three anchors **and** it does **not** disagree with the reference
   on **C5 or C6** for any anchor.
5. **Decide.**
   - **Eligible** → release Part 2 (`independent-judge-packet-scoring.md`); the
     judge then scores `OUT-01`–`OUT-40`.
   - **Not eligible** → do **not** release Part 2. Per the case `## Judge
     protocol`, a miscalibrated judge does not score the real outputs and does
     not count toward the two-judge minimum unless the operator explicitly
     accepts it with a recorded limitation.

## Recording the result

Whether the judge passes or fails calibration, commit one public-safe judge
receipt under `judge-packet/`, recording the judge's identity and runtime, the
returned anchor verdicts, the reference comparison, and the eligibility result.
A failing judge gets a calibration-only receipt (see
`judge-calibration-gpt-oss-20b.md` for the shape); a passing judge that then
scores `OUT-NN` gets a full judge-score receipt with the 40-row table (see
`judge-score-claude-opus.md` for the shape). The receipt must not contain
condition labels or any `OUT-NN` → condition mapping.

## Independence note

For a v3 judge pass to count toward a `## Result` lift above `partial`, the case
`## Judge protocol` requires at least one **eligible** judge that is
**independent of the orchestrating agent** and that did **not** author the
rubric or the calibration anchors/reference. A hosted-API or human judge sourced
through this packet is intended to meet that bar — record its identity and its
independence honestly in the receipt. The two judge attempts already on record
(`judge-calibration-gpt-oss-20b.md`, `judge-score-claude-opus.md`) do **not**
meet it: the first failed calibration, and the second is the orchestrating agent
with a circular calibration.

## Reconciliation is a separate, later step

This note covers calibration and scoring only. Mapping `OUT-NN` back to
conditions and computing condition aggregates is a separate operator step done
after blind scoring, using the local-only answer key; it is not part of this
packet and the answer key is never sent to the judge or committed.
