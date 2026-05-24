---
case_id: halo-evidence-vs-diagnosis-validation-v12
artifact: run-packet
eval_type: contradiction-preservation
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
status: frozen_run_complete_scored
created: 2026-05-24
---

# Run Packet - halo-evidence-vs-diagnosis-validation-v12-v1

This is the frozen v12 packet for the Brightwell Benefits evidence-quality
eval. V11 stays frozen and unrescored as `partial` / `do_not_promote`; v12
kept the same C4-C6 critical composite, full reviewed source-card substrate,
hard controls, and aggregate-only reconciliation, but added a real
pre-generation judge-disagreement smoke gate and a third scored judge route.

This file is operator-facing. It names model conditions, readiness gates, and
run mechanics. It must not be shown to blind judges.

## Status

- Frozen case exists at `case.md`.
- Local-only substrate-feasibility probe passed before freeze.
- Calibration anchors and judge-disagreement smoke both passed before
  generation for hosted OpenAI `gpt-5.4`, hosted Anthropic
  `claude-opus-4-7`, and local `gpt-oss:20b`.
- Six condition packets were frozen locally under the v12 freeze candidate.
- 48 real LM Studio MLX model outputs exist, eight per condition, with 0
  simulated and 0 deferred outputs.
- Hash-blinded `OUT-NN` packet, three judge receipts, aggregate-only
  reconciliation, `score-sheet.md`, `eval-decision.md`, and `postmortem.md`
  exist.
- Result: `partial`; eval decision: `do_not_promote`.

## Declared Conditions

| Condition | Added material before the Advisor prompt |
| --- | --- |
| `vanilla` | None. Advisor prompt only. |
| `famous_sources_supplied` | Name-level list of relevant famous sources and decoys only; no claims or summaries. |
| `substrate_workflow` | Full public-safe text of reviewed source cards `BK-0048-card-001`, `BK-0001-card-001`, and `BK-0007-card-001`; no raw source text, no book maps, no unreviewed synthesis card, no canon language. |
| `vanilla_long_prompt` | Neutral unrelated filler length-matched to the substrate added material. |
| `generic_advice_prompted` | Short generic advice-quality request; no rubric or source content. |
| `criteria_prompted_no_sources` | Abstract criteria reminder about contaminated evidence, disconfirming tests, intervention boundaries, and falsifiers; no source names, source cards, or case-specific answer hint. |

## Required Readiness Gates

### 1. Substrate-feasibility probe

Before any full generation, the local-only probe had to show the scenario was
not generic-solvable but was substrate-feasible.

Probe summary:

- Completed probe outputs: 9/9.
- No-source C4 pass count: 0/6.
- Substrate C4 pass count: 3/3.
- Probe status: `probe_passed`.

Probe logs, raw outputs, and provisional scores stay local-only and are not
benchmark evidence.

### 2. Calibration smoke

All three pre-registered routes had to match the C4-C6 reference on eligibility
anchors A-G before generation. C1-C3 were scored and reported but non-gating;
judge-provided totals were optional and parser-computed.

Calibration summary:

- Hosted OpenAI `gpt-5.4`: passed, 0 C4-C6 eligibility differences; 2 C1/C2/C3 differences.
- Hosted Anthropic `claude-opus-4-7`: passed, 0 C4-C6 eligibility differences.
- Local `gpt-oss:20b`: passed, 0 C4-C6 eligibility differences; 4 C1/C2/C3 differences.

### 3. Judge-disagreement smoke

All three routes scored the same ten synthetic borderline answers before
generation. Pairwise C4-C6 disagreement had to be at or below 20 percent.

Smoke summary:

- OpenAI vs Anthropic: 0/10 C4-C6 disagreements.
- OpenAI vs local: 1/10 C4-C6 disagreements.
- Anthropic vs local: 1/10 C4-C6 disagreements.
- Overall readiness: `passed`.

## Frozen Inputs

The v12-v1 freeze records:

- `case.md` sections from `## Scenario` through `## Falsifier`.
- The final declared `model_conditions`.
- The reviewed lineage packet and hashes:
  - `corpus/source-cards/BK-0048-card-001.md` sha256 `2f11b5e74182d50dbbff87d26f43dd9376e22a6d4aa316a264fd9e2ecf5b476d`.
  - `corpus/source-cards/BK-0001-card-001.md` sha256 `1535ee5be11481217f9731d0851b2ffe23f9f61ae1b8b978added09026a9730b`.
  - `corpus/source-cards/BK-0007-card-001.md` sha256 `8d7bb540f96f0cc51fd77173c8e02988bdf8ca500fa2507c8f25875bc466251f`.
- Advisor prompt sha256 `81621976eaf302301d88434e895bffe7f264ddbe9d86bbb0dd82120c2f65f2aa`.
- Condition packet hashes:
  - `vanilla`: `81621976eaf302301d88434e895bffe7f264ddbe9d86bbb0dd82120c2f65f2aa`
  - `famous_sources_supplied`: `fbda9621700ea5a031af698b8700a95ac925370d84a60c86c1d7bce543e8cc3b`
  - `substrate_workflow`: `b6cd135fd92e629c778a8282ec7993f44f89675e5f6dceea2232399cd10f2424`
  - `vanilla_long_prompt`: `98ca8c241ae7ac2a811e9012d1dcc7202739138b0b2a830b3ed8ef5ba847b45e`
  - `generic_advice_prompted`: `2d3cd0a66ac65ac18e241525d58fddd7447998bf4d887a6f8c7bfef16372a25d`
  - `criteria_prompted_no_sources`: `eedcb93e6e1ac3648b936a1b5b4926243f86d4779861ecb7569972e407df3b14`
- Equal-length filler: 4,323 words, sha256 `9a5c74bdf8c08a89a03d330c2a4146808a97bb61acfd06f0617ae82afd547e6e`, forbidden-vocabulary hits `{}`.

Any edit to scenario, prompt, rubric, positive rule, falsifier, conditions, or
lineage after freeze starts a new benchmark version.

## Generator

- Provider: LM Studio local OpenAI-compatible HTTP server; MLX runtime.
- Model id: `gemma-4-31b-it-mlx:2`.
- Model snapshot: `lmstudio-community/gemma-4-31B-it-MLX-8bit`, loaded context length 65,536.
- Decoding: `temperature: 0.7`, `top_p: 0.9`, `num_ctx: 65536`.
- Response budget: `max_tokens: 2048`.
- Runs: 8 real outputs per declared condition, 48 outputs total.
- Simulated outputs: 0.
- Deferred outputs: 0.

## Result Summary

V12 is not `benchmark_supported`.

Pooled means:

- `criteria_prompted_no_sources`: 5.250
- `substrate_workflow`: 5.000
- `vanilla`: 3.000
- `famous_sources_supplied`: 3.000
- `vanilla_long_prompt`: 3.000
- `generic_advice_prompted`: 3.000

The substrate separated from `vanilla`, `famous_sources_supplied`,
`vanilla_long_prompt`, and `generic_advice_prompted` by +2.000 total points.
It did not separate from `criteria_prompted_no_sources`; that control beat the
substrate by +0.250 total points pooled and had higher C4 and C5 pass rates.

The result stayed `partial` because multiple pre-registered clauses failed:
total-score margin, critical-criterion margin, judge-level stability, and the
no-unresolved-judge trigger. OpenAI was also flagged non-discriminating by the
80 percent same-total guard, although two other judges were discriminating.

## Canon Boundary

This v12 result creates no canon candidate and no public advice claim. It is
evidence that this frozen substrate did not beat a criteria-prompted no-source
control under the pre-registered rule. It cannot prove that any source claim is
true or that the recommendation is correct in the real world.
