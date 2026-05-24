---
artifact: operator-calibration-check
case_id: halo-evidence-vs-diagnosis-validation-v8
benchmark_version: halo-evidence-vs-diagnosis-validation-v8-smoke-2
audience: operator-only
calibration_smoke_only: true
---

# Operator Calibration Check - v8 Smoke

Operator-only. Do not send this file, and do not send the Surface 2 reference
verdicts in calibration-anchors.md, to the judge.

## Smoke procedure

1. Send `independent-judge-packet-calibration.md`.
2. Record the judge's eight returned anchor lines verbatim.
3. Compare them against the withheld Surface 2 reference.
4. A judge route is smoke-eligible only if C3-C6 match exactly across
   eligibility anchors A-G, totals are arithmetic, and no dependency violation
   appears.
5. C1/C2 differences are recorded but non-gating.
6. Anchor H is illustrative-only and excluded from exact-match eligibility.
7. Require at least two different-family judge routes to pass before any v8
   generation freeze.

## Reference verdict summary

Withhold this summary from the judge until after calibration is returned.

| Anchor | Eligibility? | C1 | C2 | C3 | C4 | C5 | C6 | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | ---: |
| A | yes | PASS | PASS | PASS | PASS | PASS | PASS | 6 |
| B | yes | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 0 |
| C | yes | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 |
| D | yes | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 0 |
| E | yes | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 |
| F | yes | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 0 |
| G | yes | PASS | PASS | PASS | PASS | PASS | PASS | 6 |
| H | no | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 0 |

## Generation boundary

No v8 output generation may occur until the smoke gate passes. If fewer than
two different-family routes pass, revise anchors or rubric as a new smoke
iteration while no outputs exist.
