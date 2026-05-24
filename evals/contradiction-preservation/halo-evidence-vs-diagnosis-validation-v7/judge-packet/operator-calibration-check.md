---
artifact: operator-calibration-check
case_id: halo-evidence-vs-diagnosis-validation-v7
benchmark_version: halo-evidence-vs-diagnosis-validation-v7-v1
audience: operator-only
---

# Operator Calibration Check - v7 Independent Judge

Operator-only. Do not send this file, and do not send the Surface 2 reference
verdicts in calibration-anchors.md, to the judge. The judge receives only
independent-judge-packet-calibration.md and, if calibration clears,
independent-judge-packet-scoring.md.

## Procedure

1. Send Part 1 only.
2. Record the judge's seven returned anchor lines verbatim.
3. Compare them against the withheld Surface 2 reference in calibration-anchors.md.
4. A judge is eligible only if C3-C6 match exactly across all seven anchors,
   C1/C2 differ by at most one criterion total, totals are arithmetic, and no
   dependency violation appears.
5. Eligible judges may score OUT-01 through OUT-40. Non-eligible judges get a
   calibration-only receipt and score zero real outputs.

## Reference verdict summary

Withhold this summary from the judge until after calibration is returned.

| Anchor | C1 | C2 | C3 | C4 | C5 | C6 | Total |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| Anchor A | pass | pass | pass | pass | pass | pass | 6 |
| Anchor B | fail | pass | fail | fail | fail | fail | 1 |
| Anchor C | pass | pass | pass | pass | fail | fail | 4 |
| Anchor D | pass | pass | pass | fail | fail | fail | 3 |
| Anchor E | fail | pass | pass | pass | fail | fail | 3 |
| Anchor F | fail | pass | fail | fail | fail | fail | 1 |
| Anchor G | pass | pass | pass | pass | pass | pass | 6 |

## Reconciliation is separate

This note covers calibration and scoring only. Mapping OUT-NN back to conditions
and computing condition aggregates is a separate step after blind scoring. The
answer key is local-only and is never sent to the judge or committed.
