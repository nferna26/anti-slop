---
case_id: locator-accuracy-v1
benchmark_version: locator-accuracy-v1-v1
artifact: eval-decision
eval_decision: do_not_promote
decision_class: judge_calibration_failed_before_generation
result_status: partial
decision_date: 2026-05-27
decision_summary: The locator-accuracy-v1-v1 packet froze cleanly, but both hosted primary judge routes failed the exact calibration gate before any benchmark output generation. No eligible judge routes remain, so generation stops before outputs and the case stays partial.
---

# Eval Decision - locator-accuracy-v1-v1

Public-safe decision record for the eval case in this folder. It sits on top of
`score-sheet.md` -> `## Result` and does not replace the Result status.

## Status

Result is `partial`. The benchmark packet is frozen, and calibration was run
against the pre-registered judge-facing anchor surfaces. No benchmark model
outputs were generated, no OUT-NN packet exists, no anonymisation occurred, no
output judging occurred, and no aggregate reconciliation was performed.

## Decision

`eval_decision: do_not_promote`.

The run is **blocked before generation**. Do not generate benchmark outputs for
`locator-accuracy-v1-v1` under the current frozen judge-calibration surface.

## Reason

The frozen judge-route rule requires at least two eligible different-family
judge routes before any benchmark generation. The two hosted primary routes both
failed exact calibration:

| Judge route | Model | Calibration result | Differences | Eligible? |
| --- | --- | --- | --- | --- |
| `hosted_anthropic` | `claude-opus-4-7` | failed | Anchor D F5 missed; Anchor E F5 missed | No |
| `hosted_openai` | `gpt-5.4` | failed | Anchor D F5 missed; Anchor E F1 over-fired | No |
| `local_backstop` | — | not run | LM Studio exposed only the Gemma generator family plus an embedding model; no pre-registered non-Gemma LM Studio backstop was available | No |

Both hosted judges matched the coverage anchors G-L exactly, but exact coverage
agreement is not sufficient. F1-F5 anchors A-F must also match exactly, and both
hosted routes missed the withheld reference key. Under the pre-registered rule,
a failed calibration route scores zero benchmark outputs.

Because there are zero eligible judge routes, the positive result cannot be
evaluated, let alone met. The case cannot support `benchmark_supported`, a canon
candidate, or any public claim that the substrate improves provenance behavior.

## Reconciliation Method

No aggregate reconciliation was performed. Reconciliation requires generated
benchmark outputs and at least two eligible scored judge receipts. This case has
only calibration-only receipts and no OUT-NN outputs.

No OUT-NN -> condition/run/case answer key exists for this benchmark version.
No per-output condition mapping was committed.

## What This Result Means

This is a real calibration-stage result, not a substrate-performance result. It
shows that the frozen locator-accuracy scenario, packet, route pre-registration,
and calibration machinery reached the intended pre-generation gate, and that the
gate correctly prevented an under-calibrated run from spending 240 outputs.

The immediate methodological lesson is that the F5 refusal-failure boundary is
not yet judge-stable when paired with F3 misattribution and F4/F1 evidence
laundering anchors. A future version may revise the calibration surface or
judge instructions before generation, but `locator-accuracy-v1-v1` itself
should not be rescued after the fact.

## Discipline Note

A judge calibration result is a test artifact: it is evidence about how one
planned judge route handled one frozen calibration surface. It is not source
truth, model-output evidence, advice, or canon.
