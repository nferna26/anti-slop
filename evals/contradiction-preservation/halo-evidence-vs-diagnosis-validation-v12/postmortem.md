---
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
artifact: postmortem
result_status: partial
eval_decision: do_not_promote
decision_class: controls_matched_total_margin
created: 2026-05-24
---

# Postmortem - halo-evidence-vs-diagnosis-validation-v12

## Verdict

`do_not_promote` / `partial`. V12 is not `benchmark_supported`.

The machinery worked: substrate-feasibility probe, frozen packet, 48 real LM
Studio MLX outputs, hash-blinded `OUT-NN` packet, three pre-registered judges
that passed calibration and disagreement smoke before generation, public-safe
receipts, aggregate-only reconciliation from committed hashes, and gates.

## What v12 tested

V12 tested the v11 failure directly. V11 separated on C4-C6 but could not
promote because only two judges scored and their disagreement exceeded the
pre-registered trigger. V12 therefore pre-registered three routes before
generation and added a judge-disagreement smoke test on ten borderline answers.

The eval kept the same hard claim: the substrate must beat the usual controls
and the hard `criteria_prompted_no_sources` control on C4-C6, not merely beat
generic advice or equal-length filler.

## What Happened

The readiness gates all passed:

- no-source probe C4 passes: 0/6
- substrate probe C4 passes: 3/3
- OpenAI / Anthropic / local calibration: all C4-C6 eligible
- judge-disagreement smoke: pairwise C4-C6 disagreement rates 0.00, 0.10, 0.10

The full run then produced a mixed but non-promotional result.

Pooled condition means:

- `criteria_prompted_no_sources`: 5.250
- `substrate_workflow`: 5.000
- `vanilla`: 3.000
- `famous_sources_supplied`: 3.000
- `vanilla_long_prompt`: 3.000
- `generic_advice_prompted`: 3.000

Pooled C4-C6 pass rates:

- `substrate_workflow`: C4 0.67, C5 0.67, C6 0.67
- `criteria_prompted_no_sources`: C4 0.83, C5 0.75, C6 0.67
- `generic_advice_prompted`: C4 0.00, C5 0.00, C6 0.00
- `vanilla_long_prompt`: C4 0.00, C5 0.00, C6 0.00

Substrate still separated cleanly from `vanilla`, `famous_sources_supplied`,
`vanilla_long_prompt`, and `generic_advice_prompted`. It did not separate from
`criteria_prompted_no_sources`.

## Why It Did Not Promote

The hard criteria prompt taught enough of the key move to match or beat the
source-card substrate:

- substrate minus `criteria_prompted_no_sources` total margin: -0.250
- C4 margin: -0.167
- C5 margin: -0.083
- C6 margin: +0.000

The judge-disagreement trigger also fired:

- `substrate_workflow`: 7/8 outputs had C4-C6 disagreement across judges.
- `criteria_prompted_no_sources`: 6/8 outputs had C4-C6 disagreement.
- key controls pooled: 6/24 disagreement rate, 0.25, above the 0.20 trigger.

OpenAI `gpt-5.4` was flagged non-discriminating by the pre-registered guard
because it assigned total 3 to 43/48 outputs. Anthropic and local gpt-oss were
discriminating, but they disagreed enough on substrate and criteria-prompted
outputs that the no-unresolved-judge clause still failed.

## Lessons

- The v11 third-route gap was fixed procedurally. Local `gpt-oss:20b` passed
  calibration and disagreement smoke, scored all outputs, and was not added
  after the fact.
- The remaining failure is substantive: a criteria prompt with no sources can
  supply enough abstract evidence-quality instruction to match the substrate on
  the C4-C6 ladder.
- The disagreement-smoke set was too easy relative to real outputs. It found
  only one local disagreement in ten synthetic answers, but real substrate and
  criteria-control outputs created much higher C4-C6 disagreement.
- Generic advice and equal-length filler are no longer the live blockers in
  this case shape. The live blocker is whether source-card substrate adds
  anything beyond an explicit criteria prompt.

## Do Not Do

- Do not rescore v12 or revise its positive rule.
- Do not drop `criteria_prompted_no_sources`.
- Do not claim v12 is `benchmark_supported`.
- Do not use v12 as canon support or evidence that the business
  recommendation is correct.
- Do not treat the substrate's +2.000 margin over generic advice as enough;
  the hard control matched it.

## Suggested Next Step

Stop trying to promote this eval family by making the case surface subtler. The
hard control has now identified the real comparison: source-card substrate vs
an explicit criteria prompt. A next attempt should either:

1. Test a claim where the substrate contains a source-specific boundary that an
   abstract criteria prompt cannot name, or
2. Change the research question to a smaller, honest claim: the substrate helps
   versus generic and equal-length prompting, but not versus a well-written
   criteria prompt.

Either path is compatible with the KB discipline. Neither path supports canon
yet.
