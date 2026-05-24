---
case_id: halo-evidence-vs-diagnosis-validation-v8
artifact: run-packet
eval_type: contradiction-preservation
benchmark_version: halo-evidence-vs-diagnosis-validation-v8-v1
status: frozen_run_complete_scored_do_not_promote
created: 2026-05-24
---

# Run Packet - halo-evidence-vs-diagnosis-validation-v8-v1

This is the frozen generation packet for the v8 HelioLedger evidence-quality
benchmark. It freezes the `smoke-2` calibration surface that passed with hosted
OpenAI and hosted Anthropic before any v8 model output was generated.

This file is operator-facing. It names model conditions and run mechanics. It
must not be shown to blind judges.

## Freeze Prerequisites

- `judge-packet/calibration-anchors.md` is status
  `smoke_passed_pre_generation`.
- Hosted OpenAI `gpt-5.4-mini` passed the C3-C6-only smoke gate on eligibility
  anchors A-G.
- Hosted Anthropic `claude-opus-4-7` passed the same C3-C6-only smoke gate.
- Local `gpt-oss:20b` failed the smoke gate and is recorded as an ineligible
  backstop route for v8-v1.
- The `vanilla_long_prompt` filler is generated, scanned, length-matched to
  the `substrate_workflow` added material, and frozen by hash.
- All five condition packets are assembled and frozen by hash.

## Frozen Inputs

The frozen pass covers `case.md` from `## Scenario` through `## Falsifier`, the
declared `model_conditions`, the reviewed lineage artifacts below, and the
filled `smoke-2` calibration anchors.

Lineage artifacts hashed at freeze:

| Artifact | sha256 |
| --- | --- |
| `corpus/source-cards/BK-0048-card-001.md` | `2f11b5e74182d50dbbff87d26f43dd9376e22a6d4aa316a264fd9e2ecf5b476d` |
| `corpus/source-cards/BK-0001-card-001.md` | `1535ee5be11481217f9731d0851b2ffe23f9f61ae1b8b978added09026a9730b` |
| `corpus/source-cards/BK-0007-card-001.md` | `8d7bb540f96f0cc51fd77173c8e02988bdf8ca500fa2507c8f25875bc466251f` |

No unreviewed claim/tension card, book map, raw source text, or canon artifact
is part of the frozen substrate packet.

## Advisor Prompt

The Advisor prompt is derived deterministically from `case.md` -> `## Advisor
prompt`: take the block-quote lines, remove a leading `> ` from each line, turn
a line that is exactly `>` into an empty line, join with newlines, strip
leading/trailing whitespace, and append one trailing newline.

Frozen Advisor prompt: 391 words, 2636 characters, sha256
`5a42e17859b4a23ae36d2682474f8d0369ffc492c200375fd79a14bf3b322262`.

## Condition Packets

Five conditions are declared in `case.md`. Each packet is the named added
material followed by one blank line and the verbatim Advisor prompt. The Advisor
prompt is byte-identical across conditions.

| Condition | Added material before the Advisor prompt |
| --- | --- |
| `vanilla` | None. Advisor prompt only. |
| `famous_sources_supplied` | Name-level list of relevant famous sources and decoys only; no claims or summaries. |
| `substrate_workflow` | Reviewed source-card packet only: `BK-0048-card-001`, `BK-0001-card-001`, `BK-0007-card-001`. |
| `vanilla_long_prompt` | Neutral unrelated filler length-matched to the substrate added material. |
| `generic_advice_prompted` | Short generic advice-quality request; no rubric or source content. |

No `substrate_workflow_plus_synthesis` arm is included in v8-v1.

## Frozen Packet Hashes

| Item | Value |
| --- | --- |
| Calibration-anchor status | `smoke_passed_pre_generation` |
| Calibration-anchor `sha256` | `ce3e0bc5d2e40713d97e6cdd16a73e7eb9316933e9f660dacfba6ecda438842d` |
| Case `sha256` at freeze | `4b98f3821beeba4497f6bb31149354903807eea4cbf90cba9075d788b4803037` |
| Advisor prompt words / characters / `sha256` | 391 / 2636 / `5a42e17859b4a23ae36d2682474f8d0369ffc492c200375fd79a14bf3b322262` |
| Generator model and snapshot | `gemma4:31b`; Ollama model ID `6316f0629137`; Ollama server `0.24.0` |
| Judge route A | hosted OpenAI API judge, `gpt-5.4-mini`, smoke eligible |
| Judge route B | hosted Anthropic API judge, `claude-opus-4-7`, smoke eligible |
| Judge route C | local `gpt-oss:20b`, smoke ineligible |
| `vanilla` packet words / `sha256` | 391 / `5a42e17859b4a23ae36d2682474f8d0369ffc492c200375fd79a14bf3b322262` |
| `famous_sources_supplied` packet words / `sha256` | 520 / `a8f837584b6b87efa42fb92f178885d67f9a6373379ee1ede9671b0a54d4d2f8` |
| `substrate_workflow` packet words / `sha256` | 4725 / `3cb2b1bbe627b1bc559da202163e4e65f7b4fe039ccf90688ace1e1316829fa4` |
| `vanilla_long_prompt` packet words / `sha256` | 4768 / `4534e171b8d6f32b6e7785827b181c32158796a35e8ccccf057086ac0f0e43d5` |
| `generic_advice_prompted` packet words / `sha256` | 415 / `5e94f3c66f0dff57d38dd5c747b6fa04e65a3365ab875d68633add0ce68b4ce2` |
| Filler word count and ratio | 4334 words; ratio 1.000 to `substrate_workflow` added material |
| Filler forbidden-vocabulary scan | `{}`; zero forbidden-stem hits |

## Run Parameters

- Run count: eight real runs per condition minimum, five conditions x 8 = 40
  outputs.
- Seeds: condition index follows the declared `model_conditions` order:
  `vanilla` (1), `famous_sources_supplied` (2), `substrate_workflow` (3),
  `vanilla_long_prompt` (4), `generic_advice_prompted` (5). Run `r`,
  condition `i` -> seed `r*100 + i`; a timeout retry uses `seed + 10` and is
  recorded.
- Decoding: generation `temperature 0.7`, `top_p 0.9`, `num_ctx 32768`,
  timeout 600 s, held constant across all conditions and runs.
- Frozen generator: `gemma4:31b`, Ollama model ID `6316f0629137`, local Ollama
  server version `0.24.0`.

## Judge Routes

The v8-v1 pass uses two eligible scored judges only:

- Judge A: hosted OpenAI `gpt-5.4-mini`, passed smoke-2.
- Judge B: hosted Anthropic `claude-opus-4-7`, passed smoke-2.

Local `gpt-oss:20b` remains recorded as a failed smoke route and scores zero
v8-v1 outputs. No after-the-fact route may be added.

## Output, Anonymisation, And Answer Key

- One public-safe model-output receipt per run under `model-outputs/`, with
  benchmark provenance.
- Real outputs only; no simulations in the comparison set.
- After all outputs exist and before any judge sees them, hash each output body
  with `sha256`, sort ascending, and assign `OUT-01` through `OUT-NN`.
- The `OUT-NN` to condition answer key stays local-only and git-ignored.
- Committed reconciliation is aggregate-only; no per-`OUT-NN` to condition
  mapping is committed.

## Current State

The v8-v1 generation and scoring pass is complete:

- Forty real `gemma4:31b` outputs were generated: eight per declared condition,
  zero simulated outputs, zero deferred outputs, and zero retry seeds.
- Public-safe model-output receipts were written under `model-outputs/`, and
  `receipt-index.yaml` indexes all forty receipts.
- Output bodies were hashed, sorted by `sha256`, and assigned `OUT-01` through
  `OUT-40` before judging.
- The `OUT-NN` to condition/run answer key remains local-only and git-ignored.
- Hosted OpenAI `gpt-5.4-mini` and hosted Anthropic `claude-opus-4-7` scored
  all forty blinded outputs. Local `gpt-oss:20b` scored zero outputs because it
  failed the smoke gate.
- Aggregate-only reconciliation joined committed output hashes to committed
  model-output receipt bodies. The local-only answer key was not read.

The pre-registered positive result did not pass. `score-sheet.md` records
`Result: partial`; `eval-decision.md` records `eval_decision: do_not_promote`
with decision class `controls_matched_total_margin`. Generic advice matched
the substrate total mean and saturated C3-C6; the equal-length control also
saturated C3/C4. This v8 result must not be cited as `benchmark_supported`.
