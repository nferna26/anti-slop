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
is frozen in `run-packet.md`, 240 real model-output receipts exist, and the
condition-blind OUT-NN packet has been scored by the two eligible hosted judge
routes. Public-safe route receipts are
`judge-packet/judge-score-hosted_anthropic_r2.md` and
`judge-packet/judge-score-hosted_openai_r3.md`. No benchmark score table,
aggregate reconciliation, eval decision, postmortem, receipt index, or Result
lift has occurred. The OUT-NN origin map remains local-only.

## Scores

Unscored by condition. Route-level judge-score receipts exist, but no OUT-NN
score has been reconciled to condition aggregates.

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

- Reconcile aggregate-only in a separate tranche from committed route receipts
  and the local-only answer key.
- Do not lift a Result until aggregate-only reconciliation is complete and the
  frozen positive rule has been applied without revision.
