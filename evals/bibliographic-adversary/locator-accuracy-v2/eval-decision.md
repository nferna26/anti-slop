---
case_id: locator-accuracy-v2
benchmark_version: locator-accuracy-v2-v1
artifact: eval-decision
eval_decision: do_not_promote
decision_class: non_discriminating_judge_and_famous_margin_failed
result_status: partial
decision_date: 2026-05-28
decision_summary: The substrate showed zero failures and high valid support coverage under both eligible judge routes, but the frozen Positive-result rule is not met because hosted_anthropic_r2 trips the non-discriminating-judge guard and misses the primary failure-rate margin against famous_sources_supplied.
---

# Eval Decision - locator-accuracy-v2-v1

Public-safe decision record for the eval case in this folder. It sits on top of
`score-sheet.md` -> `## Result` and does not replace the Result status.

## Status

Result is `partial`. The benchmark packet was frozen before generation, 240
real `gemma-4-31b-it-mlx` outputs were generated, the OUT-NN judge packet was
condition-blind, and the two pre-registered hosted judge routes both passed
exact calibration before scoring all 240 OUT rows. Aggregate-only
reconciliation is complete from the committed judge-score receipts and the
local-only OUT-NN answer key. No per-OUT-NN to condition/case/run mapping is
committed.

## Decision

`eval_decision: do_not_promote`.

The frozen Positive-result rule is not met. Do not lift `## Result` to
`benchmark_supported`, do not cite this eval as benchmark-supported evidence,
and do not use it to promote canon.

## Reason

The run produced the strongest mechanical-lineage signal so far: both eligible
judge routes scored `substrate_workflow` at zero F1-F5 failures, while assigning
valid support coverage only to the substrate condition. However, the frozen
rule required at least two different-family judge routes to clear the rule
independently. Only `hosted_openai_r3` clears it.

| Positive-rule clause | hosted_anthropic_r2 | hosted_openai_r3 |
| --- | --- | --- |
| Calibration passed before OUT scoring | pass | pass |
| OUT rows scored | 240 | 240 |
| Substrate total failures <= X=3 | pass: 0 | pass: 0 |
| Substrate valid support coverage >= Y=32 | pass: 43 | pass: 41 |
| Non-discriminating-judge guard | **fail**: 208/240 outputs (86.7%) have total failure count 0 | pass: max bucket 107/240 (44.6%) |
| `criteria_prompted_no_sources` branch | pass: low-failure coverage margin +43 | pass: high-failure primary margin +0.425 |
| `generic_advice_prompted` branch | pass: high-failure primary margin +0.250 | pass: high-failure primary margin +0.675 |
| `famous_sources_supplied` branch | **fail**: high-failure primary margin +0.225 < +0.250 | pass: high-failure primary margin +0.850 |
| Route can promote? | **No** | Route-local yes |

Because `hosted_anthropic_r2` cannot promote, the case has only one
different-family route-local positive result. Pooled coverage does not rescue
the case; the rule explicitly says pooled-only coverage cannot promote.

## Reconciliation Method

Reconciliation happened only after blind scoring completed. The committed route
receipts were parsed for OUT-NN F1-F5 totals and valid support coverage. The
local-only answer key at
`local-only/runs/locator-accuracy-v2-v1/out-nn-answer-key.yaml` was then read to
join OUT labels to condition aggregates. The public artifacts record only
condition-level aggregate tables.

No per-OUT-NN to condition/case/run mapping, run ID, seed table, raw judge
transcript, request JSON, API credential, or local-only artifact is committed.

## What This Result Means

This is a clean non-promotion with a useful signal. It does not support the old
claim that the substrate improves advice, and it does not prove source truth.
It also does not prove that the substrate prevents fabrication, because one
important control (`criteria_prompted_no_sources`) also avoided failures under
Anthropic. What it shows, descriptively, is that the substrate can add
inspectable reviewed public-KB lineage where the safe controls often refuse
silently.

That narrower mechanical-lineage claim still lacks a `benchmark_supported`
result because the pre-registered two-route rule did not clear. A future case
or benchmark version would need to make the judge-discrimination and
famous-source-margin criteria hold without revising this frozen run.

## Discipline Note

A model output is a test artifact, never an authority and never citable as a
source. A judge score is evidence about scoring behavior under a frozen rubric,
not evidence about the world and not an advice claim. This eval-decision
promotes no source card, claim/tension card, canon candidate, or public advice
claim.
