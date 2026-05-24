---
case_id: halo-evidence-vs-diagnosis-validation-v11
artifact: run-packet
eval_type: contradiction-preservation
benchmark_version: halo-evidence-vs-diagnosis-validation-v11-v1
status: frozen_run_complete_scored
created: 2026-05-24
---

# Run Packet - halo-evidence-vs-diagnosis-validation-v11-v1

This is the frozen v11 packet for the Harbor Claims evidence-quality eval. It
keeps the v10 substrate and two-sided feasibility probe, changes the company
and feature surface, and pre-registers C1-C3 as descriptive rather than
promotional. The load-bearing benchmark question is C4-C6: can the reviewed
source-card substrate move the generator to the disconfirming commercial test,
the intervention boundary, and a constrained recommendation with a behavioral
falsifier?

This file is operator-facing. It names model conditions, readiness gates, and
run mechanics. It must not be shown to blind judges.

## Status

- Frozen case exists at `case.md`.
- Substrate-feasibility probe passed before freeze.
- Calibration anchors are filled and status `smoke_passed_pre_generation`.
- Six condition packets were frozen locally under the v11 freeze candidate.
- 48 real model outputs exist, eight per condition, with 0 simulated and 0
  deferred outputs.
- Hash-blinded `OUT-NN` packet, hosted OpenAI and hosted Anthropic judge
  receipts, aggregate-only reconciliation, `score-sheet.md`,
  `eval-decision.md`, and `postmortem.md` exist.
- Result: `partial`; eval decision: `do_not_promote`.
- V10 remains frozen and unrescored as `partial` / `do_not_promote`.

## Design Change From v10

V10 showed large substrate lift on the intended C4-C6 mechanism but failed its
frozen rule because C3 was non-discriminating. Controls could reject
contaminated attribution without the substrate, so C3 was not a good
promotional margin criterion.

V11 therefore keeps C1-C3 on the score sheet but excludes them from
promotion-critical margins and saturation gates. The positive rule is pinned
to C4-C6 only: selecting the evidence standard that can disconfirm the
commercial success story, weighing what the intervention learns or hides under
the board-window constraint, and making one constrained recommendation with a
behavioral falsifier.

## Declared Conditions

Six conditions are declared in `case.md`:

| Condition | Added material before the Advisor prompt |
| --- | --- |
| `vanilla` | None. Advisor prompt only. |
| `famous_sources_supplied` | Name-level list of relevant famous sources and decoys only; no claims or summaries. |
| `substrate_workflow` | Full public-safe text of reviewed source cards `BK-0048-card-001`, `BK-0001-card-001`, and `BK-0007-card-001`; no raw source text, no book maps, no unreviewed synthesis card, no canon language. |
| `vanilla_long_prompt` | Neutral unrelated filler length-matched to the substrate added material. |
| `generic_advice_prompted` | Short generic advice-quality request; no rubric or source content. |
| `criteria_prompted_no_sources` | Abstract criteria reminder about contaminated evidence, disconfirming tests, intervention boundaries, and falsifiers; no source names, source cards, or case-specific answer hint. |

## Required Pre-Freeze Gates

### 1. Substrate-feasibility probe

Before any full generation:

- Run at least three `vanilla`, three `generic_advice_prompted`, and three
  `substrate_workflow` probe outputs.
- Score C4-C6 locally for design readiness only.
- No-source passes readiness only if at most one of the six no-source outputs
  passes C4.
- Substrate passes readiness only if at least two of the three
  `substrate_workflow` outputs pass C4.

Probe summary:

- Completed probe outputs: 9/9.
- No-source C4 pass count: 0/6.
- Substrate C4 pass count: 3/3.
- Probe status: `probe_passed`.

Probe logs, raw outputs, and provisional scores stay local-only and are not
benchmark evidence.

### 2. Calibration smoke

Only after the substrate-feasibility probe passes:

- Fill `judge-packet/calibration-anchors.md` with anchors that distinguish the
  right disconfirming test from the wrong monitoring/product-diagnostic tests.
- Pre-register at least three judge routes.
- Require at least two different-family routes to pass the C4-C6-only
  calibration gate before any full condition generation.
- Failed or unavailable routes are recorded honestly and score zero future
  outputs.

Calibration summary:

- Hosted OpenAI `gpt-5.4`: passed, 0 C4-C6 eligibility differences; 2
  C1/C2/C3 differences.
- Hosted Anthropic `claude-opus-4-7`: passed, 0 C4-C6 eligibility differences.
- Local `gpt-oss:20b`: did not clear the route gate. It returned no Anchor H
  line and reported an arithmetic total mismatch on Anchor G; it scored zero
  v11-v1 outputs.

## Frozen Inputs

The v11-v1 freeze records:

- `case.md` sections from `## Scenario` through `## Falsifier`.
- The final declared `model_conditions`.
- The reviewed lineage packet and hashes:
  - `corpus/source-cards/BK-0048-card-001.md` sha256 `2f11b5e74182d50dbbff87d26f43dd9376e22a6d4aa316a264fd9e2ecf5b476d`.
  - `corpus/source-cards/BK-0001-card-001.md` sha256 `1535ee5be11481217f9731d0851b2ffe23f9f61ae1b8b978added09026a9730b`.
  - `corpus/source-cards/BK-0007-card-001.md` sha256 `8d7bb540f96f0cc51fd77173c8e02988bdf8ca500fa2507c8f25875bc466251f`.
- Advisor prompt sha256 `18fa1d51f6167dbbf1f7ece676734d5cdb459384bca25e1508dd96cd4745e42d`.
- Calibration packet sha256 `20e9a18503ec1f3ed89543b52f9ce60c475b8d0a5a728f6798e0ddf427f1d17e`.
- Condition packet hashes:
  - `vanilla`: `18fa1d51f6167dbbf1f7ece676734d5cdb459384bca25e1508dd96cd4745e42d`
  - `famous_sources_supplied`: `5f0d18f3e982d60319cdf56d83f5bfcb60ca486dc8eccd9dfcda42bea551750c`
  - `substrate_workflow`: `e9e525835ff94d5abdccdcdbcfa4f178337e1c9310550dacd9c20d6f9b3d28f4`
  - `vanilla_long_prompt`: `b2788902c52d3bd202aee721889f5170e506802736ec9b70be6e014d6c8ff138`
  - `generic_advice_prompted`: `31fa87bc7ee0d210ab5e0070b5421b72beac068fc006b3bc3be78b3dd242d5e7`
  - `criteria_prompted_no_sources`: `50fbf7f03eb7162af1196144f49fb4b1f5366ec098b65051c926600c569a4fe7`
- Equal-length filler: 4,323 words, sha256 `9a5c74bdf8c08a89a03d330c2a4146808a97bb61acfd06f0617ae82afd547e6e`, forbidden-vocabulary hits `{}`.
- Generator model, runtime, decoding parameters, timeout, seeds, and retry rule.

Any edit to scenario, prompt, rubric, positive rule, falsifier, conditions, or
lineage after freeze starts a new benchmark version.

## Generator

- Provider: LM Studio local OpenAI-compatible HTTP server; MLX runtime.
- Model id: `gemma-4-31b-it-mlx:2`.
- Model snapshot: `lmstudio-community/gemma-4-31B-it-MLX-8bit`, loaded context length 65,536.
- Decoding: `temperature: 0.7`, `top_p: 0.9`, `num_ctx: 65536`.
- Response budget: `max_tokens: 1024`.
- Runs: 8 real outputs per declared condition, 48 outputs total.
- Simulated outputs: 0.
- Deferred outputs: 0.

## Result Summary

V11 is not `benchmark_supported`. It produced the strongest substrate/control
separation in this family, but the pre-registered judge-disagreement trigger
blocked promotion.

Pooled means:

- `substrate_workflow`: 5.875
- `criteria_prompted_no_sources`: 4.062
- `vanilla`: 3.000
- `famous_sources_supplied`: 3.000
- `vanilla_long_prompt`: 3.000
- `generic_advice_prompted`: 2.938

The C4-C6 margins all cleared. The substrate beat:

- `generic_advice_prompted` by +2.938 total and +0.958 on the C4-C6 composite.
- `vanilla_long_prompt` by +2.875 total and +0.958 on the C4-C6 composite.
- `criteria_prompted_no_sources` by +1.812 total and +0.583 on the C4-C6 composite.

No key control saturated C4-C6. Both hosted judges were discriminating: OpenAI
assigned 36/48 outputs total 3 and 8/48 total 6; Anthropic assigned 36/48 total
3 and 12/48 total 6, below the 80 percent non-discrimination threshold.

The result still stayed `partial` because the two eligible judges disagreed on
C4-C6 for 3/8 `criteria_prompted_no_sources` outputs, above the 20 percent
per-condition trigger. No pre-registered eligible third route was available to
resolve the disagreement by criterion.

## Canon Boundary

This v11 result creates no canon candidate and no public advice claim. A future
`benchmark_supported` result, if one ever exists, may support only a claim about
model behavior under that frozen eval condition. It cannot prove that the
source claims are true or that the recommendation is correct in the real world.

