---
case_id: halo-evidence-vs-diagnosis-validation-v9
eval_type: contradiction-preservation
scoring_status: unscored
---

# Score Sheet

Score against the rubric in `case.md` -> `## Scoring rubric`. This v9 case is
design-only and has no model outputs, no judge scores, and no result lift.

## Result

`partial` - design-only, unrun. No benchmark evidence exists.

## Scores

No v9 model outputs exist. Do not fill this sheet until a future frozen v9 run
has completed real generation, blinding, eligible judge scoring, and
aggregate-only reconciliation.

| Criterion | vanilla | famous_sources_supplied | substrate_workflow | vanilla_long_prompt | generic_advice_prompted | criteria_prompted_no_sources |
| --- | --- | --- | --- | --- | --- | --- |
| C1 - Preserves the core tension |  |  |  |  |  |  |
| C2 - Uses case facts discriminately |  |  |  |  |  |  |
| C3 - Rejects performance-aware attribution |  |  |  |  |  |  |
| C4 - Selects the disconfirming evidence standard |  |  |  |  |  |  |
| C5 - Weighs intervention boundaries |  |  |  |  |  |  |
| C6 - Makes a constrained recommendation with behavioral falsifier |  |  |  |  |  |  |

## Comparative signal

Future positive signal, if run: `substrate_workflow` must beat
`generic_advice_prompted`, `criteria_prompted_no_sources`, and
`vanilla_long_prompt` on total score and C3-C6, without any key control
saturating C3-C6. The substrate must win by reasoning from the discriminating
test boundary, not by source labels or citation prestige.

## Judge Notes

No judge has scored this design-only case.

## Follow-up

- Run the local-only generic-solvability probe before any freeze.
- If generic probe outputs pass C4 too often, revise the scenario rather than
  freezing or generating.
- Fill calibration anchors only after the probe passes.
