---
artifact: operator-calibration-check
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
audience: operator-only
---

# Operator Calibration Check - v12 Independent Judge

Operator-only. Do not send this file, and do not send the Surface 2 reference
verdicts in calibration-anchors.md, to the judge. The judge receives only
independent-judge-packet-calibration.md and, if calibration clears,
independent-judge-packet-scoring.md.

## Procedure

1. Send Part 1 only.
2. Record the judge's returned anchor lines verbatim. Anchors A-G are required;
   Anchor H is optional and illustrative-only.
3. Compare them against the withheld Surface 2 reference in calibration-anchors.md.
4. A judge is eligible for the next readiness stage only if C4-C6 match exactly
   across eligibility anchors A-G and no dependency violation appears. C1/C2/C3
   are scored but non-gating. Judge-provided totals are optional and ignored;
   parser-computed totals are used.
5. Eligible judges must then pass the judge-disagreement smoke before scoring
   OUT-01 through OUT-48. Non-eligible judges get a
   calibration-only receipt and score zero real outputs.

## Reference verdict summary

Withhold this summary from the judge until after calibration is returned.

| Anchor | C1 | C2 | C3 | C4 | C5 | C6 | Total |
| --- | --- | --- | --- | --- | --- | --- | ---: |
| Anchor A | pass | pass | pass | pass | pass | pass | 6 |
| Anchor B | fail | fail | fail | fail | fail | fail | 0 |
| Anchor C | pass | pass | pass | pass | fail | fail | 4 |
| Anchor D | fail | fail | fail | fail | fail | fail | 0 |
| Anchor E | pass | pass | pass | pass | fail | fail | 4 |
| Anchor F | fail | fail | fail | fail | fail | fail | 0 |
| Anchor G | pass | pass | pass | pass | pass | pass | 6 |
| Anchor H | fail | fail | fail | fail | fail | fail | 0 |

## Reconciliation is separate

This note covers calibration and scoring only. Mapping OUT-NN back to conditions
and computing condition aggregates is a separate step after blind scoring. The
answer key is local-only and is never sent to the judge or committed.
