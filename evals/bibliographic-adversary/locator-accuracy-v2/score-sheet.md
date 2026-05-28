---
case_id: locator-accuracy-v2
eval_type: bibliographic-adversary
scoring_status: unscored
---

# Score Sheet

Score against `case.md` -> `## Scoring rubric`. Do not score against v1
criteria if v2's F5 co-fire rules differ.

## Result

`partial` / generated-not-scored. Benchmark version `locator-accuracy-v2-v1`
is frozen in `run-packet.md` and 240 real model-output receipts now exist, but
no OUT-NN anonymisation, judge scoring, benchmark scoring, aggregate
reconciliation, or Result lift has occurred. The hosted-primary calibration
gate cleared after the H-clarity repair; see `calibration-decision.md`.

## Scores

Unscored. In a future judging tranche, copy the v2 F1-F5 rubric exactly and
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
because the Codex shell lacked an OpenAI API credential. Hosted OpenAI r3 then
matched F1-F5 and coverage exactly after a local credential was loaded safely.
The hosted-primary exact-agreement gate is therefore cleared.

## Follow-up

- Build the condition-blind OUT-NN packet only in a separate anonymisation
  tranche.
- Do not judge, score, reconcile, or lift a Result from the generated receipts
  until the OUT-NN packet is built and eligible judge routes score it blind.
