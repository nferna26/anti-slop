---
case_id: halo-evidence-vs-diagnosis-validation-v8
artifact: run-packet
eval_type: contradiction-preservation
benchmark_version: halo-evidence-vs-diagnosis-validation-v8-smoke-2
status: calibration_smoke_passed_no_generation
created: 2026-05-24
---

# Run Packet - halo-evidence-vs-diagnosis-validation-v8-smoke-2

This is a pre-generation calibration-smoke packet for the v8 HelioLedger
evidence-quality benchmark. It is not a frozen generation packet. The revised
rubric and anchors calibrated two different-family hosted judge routes before
any v8 model output was generated.

## Why v8 exists

v7 kept the right domain but failed at judge calibration. The failure pattern
was concentrated in debatable C1/C2 partial-credit calls and one ambiguous
Anchor-D C3 call. v8 keeps the domain and five standard conditions, leaves v7
frozen and unrescored, demotes C1/C2 from judge eligibility, and gates the
smoke test on the load-bearing C3-C6 ladder only.

## Generation freeze status

No v8 condition packet is frozen. No v8 model outputs have been generated. No
OUT-NN answer key exists.

The `smoke-2` calibration gate passed with hosted OpenAI and hosted Anthropic
eligible. Local `gpt-oss:20b` failed the smoke gate on one C3-C6 eligibility
criterion and remains a recorded failed backstop.

Before a future generation freeze:

1. Run the calibration-only smoke packet against the pre-registered judge
   routes.
2. Record calibration-only receipts.
3. Require at least two different-family routes to pass the C3-C6-only gate.
4. Only then freeze condition packets and generate outputs.

If fewer than two different-family routes pass, revise the anchors or rubric as
a new smoke iteration while no outputs exist. Do not generate outputs from a
failed smoke surface.

## Smoke iteration history

- `halo-evidence-vs-diagnosis-validation-v8-smoke-1` was run locally before any
  v8 output generation. Hosted Anthropic passed the C3-C6-only gate exactly,
  but hosted OpenAI and local `gpt-oss:20b` failed on remaining ambiguous
  partial anchors. No v8 model outputs existed, no scoring occurred, and no
  condition packet was frozen. The anchor set was revised into this
  `smoke-2` iteration by making the scaling/monitoring trap and experiment-only
  boundary trap less ambiguous.

## Planned standard conditions

A future generation pass, if smoke succeeds, uses the five standard conditions
only:

| Condition | Planned added material before the Advisor prompt |
| --- | --- |
| `vanilla` | None. Advisor prompt only. |
| `famous_sources_supplied` | Name-level list of relevant famous sources and decoys only; no claims or summaries. |
| `substrate_workflow` | Reviewed source-card packet only: `BK-0048-card-001`, `BK-0001-card-001`, `BK-0007-card-001`. |
| `vanilla_long_prompt` | Equal-length unrelated filler, clean of business/product/evidence terms. |
| `generic_advice_prompted` | Short generic advice-quality request; no rubric or source content. |

No `substrate_workflow_plus_synthesis` arm is included in this first v8 pass.
That keeps v8 focused on whether the reviewed source-card substrate beats the
standard controls, rather than asking a second question about a reviewed
synthesis card.

## Reviewed lineage for future substrate packet

| Artifact | Authority level |
| --- | --- |
| `corpus/source-cards/BK-0048-card-001.md` | reviewed source card; evidence-level |
| `corpus/source-cards/BK-0001-card-001.md` | reviewed source card; evidence-level |
| `corpus/source-cards/BK-0007-card-001.md` | reviewed source card; evidence-level |

No unreviewed claim/tension card, book map, raw source text, or canon artifact
is part of the v8 planned substrate packet.

## Calibration smoke rules

The calibration-smoke anchors are in
`judge-packet/calibration-anchors.md`. The rule is:

- eligibility anchors: A-G;
- illustrative-only anchor: H, scored but excluded from exact-match
  eligibility;
- C3-C6 must match the reference exactly across A-G;
- C1/C2 are scored but do not affect eligibility;
- all totals must equal the count of PASS criteria;
- no C5/C6 dependency violation may appear.

## Pre-registered judge routes for smoke

- Judge A: hosted OpenAI API route, planned model `gpt-5.4-mini`.
- Judge B: hosted Anthropic API route, planned model `claude-opus-4-7` if
  available through the operator-provided key.
- Judge C: local `gpt-oss:20b` through Ollama as a non-generator third-family
  backstop.

Each route is calibration-only during this smoke pass. A failed smoke route
scores zero model outputs because no v8 model outputs exist.

## Future positive result

A future generation pass must use the positive rule in `case.md`. The smoke
pass alone cannot support `benchmark_supported`, a canon candidate, or a public
advice claim.

## Current state

Calibration smoke passed with two different-family hosted judge routes:

| Judge route | Smoke eligible? | Receipt |
| --- | --- | --- |
| Hosted OpenAI `gpt-5.4-mini` | Yes | `judge-packet/judge-calibration-smoke-openai-gpt-5.4-mini.md` |
| Hosted Anthropic `claude-opus-4-7` | Yes | `judge-packet/judge-calibration-smoke-anthropic-claude-opus-4-7.md` |
| Local `gpt-oss:20b` | No | `judge-packet/judge-calibration-smoke-local-gpt-oss-20b.md` |

This authorizes a future freeze/generation step under the v8 rule, but does not
itself create a benchmark result, condition aggregate, canon candidate, public
advice claim, or model-output receipt.
