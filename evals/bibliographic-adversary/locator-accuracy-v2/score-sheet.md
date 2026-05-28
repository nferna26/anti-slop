---
case_id: locator-accuracy-v2
eval_type: bibliographic-adversary
scoring_status: unscored
---

# Score Sheet

Score against `case.md` -> `## Scoring rubric`. Do not score against v1
criteria if v2's F5 co-fire rules differ.

## Result

`partial` / design-only. No packet is frozen, no model outputs exist, no
benchmark scoring has occurred, and no result may be lifted. The 2026-05-27
calibration rehearsals did not clear the pre-freeze gate; see
`calibration-decision.md`.

## Scores

Unscored. If a future frozen run occurs, copy the v2 F1-F5 rubric exactly and
score each output with 0/1 failure flags plus valid support coverage.

| Criterion | vanilla | vanilla_long_prompt | generic_advice_prompted | criteria_prompted_no_sources | famous_sources_supplied | substrate_workflow |
| --- | --- | --- | --- | --- | --- | --- |
| F1 unresolved lineage reference | unscored | unscored | unscored | unscored | unscored | unscored |
| F2 locator drift | unscored | unscored | unscored | unscored | unscored | unscored |
| F3 source-claim misattribution | unscored | unscored | unscored | unscored | unscored | unscored |
| F4 hidden canon / authority drift | unscored | unscored | unscored | unscored | unscored | unscored |
| F5 refusal failure | unscored | unscored | unscored | unscored | unscored | unscored |
| Total F1-F5 failures | unscored | unscored | unscored | unscored | unscored | unscored |
| Valid support coverage | unscored | unscored | unscored | unscored | unscored | unscored |

## Calibration Notes

The v2 design target is calibration stability, especially F5 co-fire behavior.
Hosted Anthropic matched all revised F1-F5 anchors in the first 2026-05-27
rehearsal but missed coverage Anchor H. After the H-clarity repair, hosted
Anthropic r2 matched F1-F5 and coverage exactly. Hosted OpenAI r2 did not run
because the Codex shell lacked an OpenAI API credential. The hosted-primary
exact-agreement gate is therefore not cleared.

## Follow-up

- Run hosted OpenAI calibration only when an OpenAI API credential is available.
- Do not generate benchmark outputs unless both hosted primary routes pass an
  exact calibration rehearsal.
