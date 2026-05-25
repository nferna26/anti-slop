---
case_id: halo-evidence-vs-diagnosis-validation-v7
benchmark_version: halo-evidence-vs-diagnosis-validation-v7-v1
artifact: eval-decision
eval_decision: do_not_promote
decision_class: judge_calibration_failed
result_status: partial
decision_date: 2026-05-24
decision_summary: The v7 frozen run generated 40 real outputs and built the blind judge packet, but all three pre-registered judge routes failed the stricter v7 calibration gate; no OUT-NN answers were scored.
---

# Eval Decision - halo-evidence-vs-diagnosis-validation-v7

Public-safe decision record for the eval case in this folder. It sits on top of
`score-sheet.md` -> `## Result` and does not replace the Result status.

## Status

Result is `partial`. The v7-v1 case has forty real local generator outputs,
complete model-output receipts, a current `receipt-index.yaml`, a
condition-blind `OUT-NN` judge packet, and three calibration-only judge
receipts. No judge passed calibration, so no OUT-NN answers were scored and no
aggregate condition reconciliation was performed.

## Decision

`eval_decision: do_not_promote`.

## Reason

The v7 run followed the frozen run packet through generation and judge-packet
construction:

- five pre-registered conditions;
- eight real `gemma4:31b` runs per condition;
- zero simulated outputs;
- zero deferred outputs;
- zero seed+10 retries;
- reviewed-source-card-only substrate packet;
- equal-length filler matched to the substrate added material;
- anonymised `OUT-01` through `OUT-40` assignment by output-body hash;
- local-only answer key.

The judge layer failed the frozen v7 calibration gate:

| Judge route | Calibration differences | Critical C3-C6 differences | Noncritical C1/C2 differences | Eligible? |
| --- | ---: | ---: | ---: | --- |
| Hosted OpenAI `gpt-5.4-mini` | 6 | 1 | 5 | No |
| Hosted Anthropic `claude-opus-4-7` | 5 | 0 | 5 | No |
| Local `gpt-oss:20b` | 6 | 1 | 5 | No |

Under the pre-registered v7 rule, a failed judge scores zero outputs. Because
there are zero eligible scored judges, the positive result cannot be evaluated,
let alone met. The case cannot support `benchmark_supported`, a canon candidate,
or a public claim that the substrate improves advice.

## Reconciliation method

No aggregate reconciliation was performed. Reconciliation requires at least one
eligible scored judge receipt. This case has only calibration-only receipts.

The `OUT-NN` to condition/run answer key remains local-only and uncommitted.
Public artifacts do not reveal per-output condition mapping.

## What this result means

This is a real v7 execution result about readiness, not a substrate-performance
result. It shows that the v7 scenario, generation pipeline, receipt machinery,
blind packet, and judge-route pre-registration executed, but the calibration
design was too strict or too poorly aligned for all three planned judge routes.

The right next move is a new version with redesigned calibration anchors or
eligibility rules before generation. Do not revise v7 anchors after the fact,
do not score v7 outputs with a rescued judge route, and do not promote from v7.

## Discipline note

A model output is a test artifact - never an authority, never citable as a
source. A judge calibration result is likewise a test artifact: it is evidence
about how one judge handled one calibration surface under one rubric, not
evidence about the world and not an advice claim.
