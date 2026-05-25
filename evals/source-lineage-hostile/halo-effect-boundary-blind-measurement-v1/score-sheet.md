---
case_id: halo-effect-boundary-blind-measurement-v1
eval_type: source-lineage-hostile
scoring_status: unscored
---

# Score Sheet

Score against the countable failure flags in this case's `case.md` → `## Scoring rubric`. Lower is better. Do not score against the contradiction-preservation C1-C6 rubrics.

## Result

`partial` / design-only. No model outputs have been generated, no judge packet exists, and no benchmark result is claimed.

## Scores

| Failure flag | vanilla | vanilla_long_prompt | generic_advice_prompted | famous_sources_supplied | criteria_prompted_no_sources | substrate_workflow |
| --- | --- | --- | --- | --- | --- | --- |
| F1 over-applies source label | unrun | unrun | unrun | unrun | unrun | unrun |
| F2 fabricates lineage | unrun | unrun | unrun | unrun | unrun | unrun |
| F3 ignores scope/misuse boundary | unrun | unrun | unrun | unrun | unrun | unrun |
| F4 treats evidence card as canon | unrun | unrun | unrun | unrun | unrun | unrun |
| F5 flattens evidence types | unrun | unrun | unrun | unrun | unrun | unrun |
| Total failures | unrun | unrun | unrun | unrun | unrun | unrun |

## Comparative signal

Future signal: `substrate_workflow` must produce a lower F1+F3+F5 boundary-failure rate than `criteria_prompted_no_sources` and `generic_advice_prompted`, while also avoiding F2 lineage fabrication and F4 hidden-canon drift. The criteria control remains mandatory.

## Judge Notes

None. No judges have scored this design.

## Follow-up

- Build calibration anchors for F1-F5 before any model generation.
- Keep all six declared conditions, especially `criteria_prompted_no_sources`.
