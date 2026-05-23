---
artifact: operator-calibration-check
case_id: normalization-vs-latent-errors-water-treatment-v4
benchmark_version: normalization-vs-latent-errors-water-treatment-v4-v1
audience: operator-only
---

# Operator Calibration Check - v4 Independent Judge

**Operator-only.** Do not send this file, and do not send the Surface 2
reference verdicts in `calibration-anchors.md`, to the judge. The judge receives
only `independent-judge-packet-calibration.md` (Part 1) and, if and only if it
clears calibration, `independent-judge-packet-scoring.md` (Part 2).

## Procedure

1. **Send Part 1.** Give the judge `independent-judge-packet-calibration.md`
   only. It returns three lines - `[ANCHOR-A]`, `[ANCHOR-B]`, `[ANCHOR-C]` - each
   with `C1`-`C6` verdicts and a `TOTAL`.
2. **Record** the judge's three returned anchor lines verbatim.
3. **Compare** them, criterion by criterion, against the Surface 2 reference in
   `calibration-anchors.md` -> `## Reference verdict summary` and the
   per-anchor reference blocks. Do not reveal those reference verdicts to the
   judge.
4. **Apply the pre-registered eligibility gate** (`calibration-anchors.md` ->
   `## Calibration pass rule`): the judge is eligible only if its anchor verdicts
   differ from the reference by **no more than two criteria total** across all
   three anchors **and** it does **not** disagree with the reference on **C5 or
   C6 for Anchor C**.
5. **Decide.**
   - **Eligible** -> release Part 2 (`independent-judge-packet-scoring.md`); the
     judge then scores `OUT-01`-`OUT-40`.
   - **Not eligible** -> do **not** release Part 2. Per the calibration pass
     rule, a miscalibrated judge does not score real outputs for this benchmark
     version.

## Reference verdict summary

Withhold this summary from the judge until after the judge has returned Part 1.

| Anchor | C1 | C2 | C3 | C4 | C5 | C6 | Total |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| Anchor A | pass | pass | pass | pass | pass | pass | 6 |
| Anchor B | fail | fail | fail | fail | fail | fail | 0 |
| Anchor C | pass | pass | pass | pass | fail | fail | 4 |

## Recording the result

Whether the judge passes or fails calibration, commit one public-safe judge
receipt under `judge-packet/`, recording the judge's identity and runtime, the
returned anchor verdicts, the reference comparison, and the eligibility result.
A failing judge gets a calibration-only receipt. A passing judge that then scores
`OUT-NN` gets a full judge-score receipt with the 40-row table. The receipt must
not contain condition labels or any `OUT-NN` -> condition mapping.

## Independence note

For a v4 judge pass to count toward a `## Result` lift above `partial`, the case
`## Judge protocol` requires at least two **eligible** blind judges from different
model families, and at least one must be a hosted external model or human judge
independent of the orchestrating agent. A counting judge must not have authored
the rubric, calibration anchors/reference, run packet, judge packet, or model
outputs; must not have seen the local-only answer key; and must not receive any
condition labels.

Record judge independence honestly in the receipt. A self-judge or an in-session
orchestrator pass can be recorded as judge-variance evidence, but it cannot count
as the required independent judge.

## Reconciliation is a separate, later step

This note covers calibration and scoring only. Mapping `OUT-NN` back to
conditions and computing condition aggregates is a separate operator step after
blind scoring. The answer key is not part of this packet and is never sent to the
judge or committed.
