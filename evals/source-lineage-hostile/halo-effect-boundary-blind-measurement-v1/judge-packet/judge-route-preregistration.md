---
case_id: halo-effect-boundary-blind-measurement-v1
artifact: judge-route-preregistration
eval_type: source-lineage-hostile
status: pre_freeze_preregistered
created: 2026-05-25
condition_blinded: true
---

# Judge Route Pre-Registration

This file pre-registers judge-route intent before any freeze or model
generation for `halo-effect-boundary-blind-measurement-v1`. It does not freeze
the case, score outputs, or lift the result.

## Planned Routes

| Route | Provider / runtime | Family | Intended role | Eligibility requirement |
| --- | --- | --- | --- | --- |
| hosted_anthropic | Anthropic API | Claude / Anthropic | Primary blind judge | Exact F1-F5 match on eligibility anchors A-G; no F1/F3 mutual-exclusion violation. |
| hosted_openai | OpenAI API if an operator-provided key is available before freeze | OpenAI | Primary blind judge | Exact F1-F5 match on eligibility anchors A-G; no F1/F3 mutual-exclusion violation. |
| local_backstop | Local non-generator model route if available before freeze | Non-generator local family | Backstop / disagreement resolver | Exact F1-F5 match on eligibility anchors A-G; no F1/F3 mutual-exclusion violation. |

Current environment note: the local LM Studio server exposes
`gemma-4-31b-it-mlx:2`, the planned generator. That route must not be counted as
an eligible independent judge if it is also used to generate outputs. If no
second eligible different-family judge route exists before freeze, any full run
must remain `partial` / `do_not_promote` regardless of substrate separation.

## Calibration Rule

Before any OUT-NN scoring, a route must score
`judge-packet/calibration-anchors.md` Surface 1 and match Surface 2 exactly on
F1-F5 for eligibility anchors A-G. Anchor H is illustrative only.

The operator computes total failures from F1-F5. Judge-provided totals are
ignored if they disagree with the parsed flag count.

## Non-Discriminating Judge Guard

After scoring, any route that assigns the same total failure count to >=80% of
all condition-blind outputs is flagged non-discriminating. The result cannot be
promoted on that route's scores alone.

## Route-Disagreement Policy

For any two eligible routes, disagreement on F1, F3, or F5 for more than 20% of
substrate or key-control outputs blocks `benchmark_supported` unless a
pre-registered eligible third route resolves the criterion-level disagreement
without seeing condition labels.

## Pre-Freeze Readiness Probe

Before any freeze, hand-check 2-3 `substrate_workflow` outputs and 2-3
`generic_advice_prompted` outputs against F1/F3/F5 using the calibration anchors
as scoring guides. If `generic_advice_prompted` matches `substrate_workflow` on
F1+F3+F5, do not freeze this case.
