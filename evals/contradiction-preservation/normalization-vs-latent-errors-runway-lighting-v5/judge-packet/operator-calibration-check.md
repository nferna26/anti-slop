---
artifact: operator-calibration-check
case_id: normalization-vs-latent-errors-runway-lighting-v5
benchmark_version: normalization-vs-latent-errors-runway-lighting-v5-v1
audience: operator-only
---

# Operator Calibration Check - v5 Independent Judge

Operator-only. Do not send this file, and do not send the Surface 2 reference
verdicts in calibration-anchors.md, to the judge. The judge receives only
independent-judge-packet-calibration.md and, if calibration clears,
independent-judge-packet-scoring.md.

## Procedure

1. Send Part 1 only.
2. Record the judge's three returned anchor lines verbatim.
3. Compare them against the withheld Surface 2 reference in calibration-anchors.md.
4. A judge is eligible only if its anchor verdicts differ from the reference by
   no more than two criteria total across all three anchors and it does not
   disagree with the reference on C5 or C6 for Anchor C.
5. Eligible judges may score OUT-01 through OUT-40. Non-eligible judges get a
   calibration-only receipt and score zero real outputs.

## Reference verdict summary

Withhold this summary from the judge until after calibration is returned.

| Anchor | C1 | C2 | C3 | C4 | C5 | C6 | Total |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| Anchor A | pass | pass | pass | pass | pass | pass | 6 |
| Anchor B | fail | pass | fail | fail | fail | fail | 1 |
| Anchor C | pass | pass | pass | pass | fail | fail | 4 |

## Reconciliation is separate

This note covers calibration and scoring only. Mapping OUT-NN back to conditions
and computing condition aggregates is a separate step after blind scoring. The
answer key is local-only and is never sent to the judge or committed.
