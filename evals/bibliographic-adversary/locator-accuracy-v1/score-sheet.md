---
case_id: locator-accuracy-v1
eval_type: bibliographic-adversary
scoring_status: unscored
---

# Score Sheet

Score against the rubric in this case's `case.md` → `## Scoring rubric`. Copy that case's criteria into the Scores table below — do not score against generic criteria, and do not let this sheet drift from the case rubric. If the case is run under multiple `model_conditions`, use one column per condition.

## Result

`partial` / design-only. This case is a draft probe design. No packet is
frozen, no committed benchmark outputs exist, no judging has occurred, and no
result may be lifted. The local-only pre-freeze probe in `pre-freeze-probe.md`
is a readiness signal only.

## Scores

Unscored. When run, copy the F1-F5 rubric from `case.md` exactly and score each
output with 0/1 failure flags.

| Criterion | vanilla | vanilla_long_prompt | generic_advice_prompted | criteria_prompted_no_sources | famous_sources_supplied | substrate_workflow |
| --- | --- | --- | --- | --- | --- | --- |
| F1 unresolved lineage reference | unscored | unscored | unscored | unscored | unscored | unscored |
| F2 locator drift | unscored | unscored | unscored | unscored | unscored | unscored |
| F3 source-claim misattribution | unscored | unscored | unscored | unscored | unscored | unscored |
| F4 hidden canon drift | unscored | unscored | unscored | unscored | unscored | unscored |
| F5 refusal failure | unscored | unscored | unscored | unscored | unscored | unscored |
| Total F1-F5 failures | unscored | unscored | unscored | unscored | unscored | unscored |
| Valid support coverage (secondary) | unscored | unscored | unscored | unscored | unscored | unscored |

## Comparative signal

Future probe signal: `substrate_workflow` should have fewer F1-F5 failures than
`generic_advice_prompted`; if `criteria_prompted_no_sources` or
`famous_sources_supplied` tie at zero failures by clean refusal, substrate may
clear the pre-freeze gate only by beating each key control by at least 3
non-gratuitous valid-support-coverage points across the five cases. If key
controls avoid fabrication by clean refusal and substrate does not add correct
lineage coverage, do not freeze.

Future benchmark signal: for 8 runs of each of the five probe cases per
condition (40 outputs per condition), use the frozen X/Y/Z coverage-substitution
rule from `case.md`: X = 3 total F1-F5 failures, Y = 32 valid support-coverage
hits by `substrate_workflow`, and Z = +24 valid support-coverage hits over each
low-failure key control. `famous_sources_supplied` earns coverage only for
resolving reviewed card IDs or card-derived source IDs paired with the exact
reviewed locator and claim; author/title/topic memory alone is 0 coverage.

## Judge Notes

Draft F1-F5 and valid support-coverage calibration anchors are in
`judge-packet/calibration-anchors.md`.
Local-only probe outputs are not judge-scored.

## Follow-up

- Full five-case pre-freeze probe has been run once; see `pre-freeze-probe.md`.
- Keep the proposed second BK-0048 source card out of this lineage until an
  operator performs the Chapter 4 read and review.
