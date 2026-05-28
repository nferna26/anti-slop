---
case_id: locator-accuracy-v3
eval_type: bibliographic-adversary
scoring_status: unscored
---

# Score Sheet

Score against `case.md` -> `## Scoring rubric`. Do not score against v1 or v2
criteria. This sheet is design-only and intentionally unfilled.

## Result

`partial` / design-only. `locator-accuracy-v3` is a draft successor surface
created to repair the `locator-accuracy-v2-v1` judge-discrimination issue. It
is not frozen, not run, not judged, and not reconciled. No model outputs exist,
no judge packet has been run, and no Result may be lifted.

## Scores

Unscored.

| Surface | vanilla | vanilla_long_prompt | generic_advice_prompted | criteria_prompted_no_sources | famous_sources_supplied | substrate_workflow |
| --- | --- | --- | --- | --- | --- | --- |
| F1 unresolved lineage reference | unscored | unscored | unscored | unscored | unscored | unscored |
| F2 locator drift | unscored | unscored | unscored | unscored | unscored | unscored |
| F3 source-claim misattribution | unscored | unscored | unscored | unscored | unscored | unscored |
| F4 hidden canon / authority drift | unscored | unscored | unscored | unscored | unscored | unscored |
| F5 refusal failure | unscored | unscored | unscored | unscored | unscored | unscored |
| SO0 unsafe support | unscored | unscored | unscored | unscored | unscored | unscored |
| SO1 safe refusal only | unscored | unscored | unscored | unscored | unscored | unscored |
| SO2 missed or denied available lineage | unscored | unscored | unscored | unscored | unscored | unscored |
| SO3 correct reviewed support | unscored | unscored | unscored | unscored | unscored | unscored |

## Comparative Signal

Future probe signal: `substrate_workflow` should land in SO3 on supportable
claims while key controls mostly land in SO1 or SO2, without substrate taking on
SO0 unsafe support or F1-F5 failures. If `criteria_prompted_no_sources` or
`famous_sources_supplied` reach the same SO3 rate without reviewed source-card
packets, do not freeze.

Future benchmark signal: support-opportunity spread must hold under at least
two eligible different-family judges. Pooled-only support success cannot
promote.

## Judge Notes

Draft calibration anchors are in `judge-packet/calibration-anchors.md`. They
are not frozen and no judge route has run.

## Follow-Up

- Run a tiny high-agency probe before any freeze.
- Calibrate judges on SO1 versus SO2 versus SO3 before any OUT scoring.
- Do not generate benchmark outputs under this draft surface.
