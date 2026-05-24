---
case_id: halo-evidence-vs-diagnosis-validation-v10
artifact: run-packet
eval_type: contradiction-preservation
benchmark_version: halo-evidence-vs-diagnosis-validation-v10-v1
status: frozen_run_complete_scored
created: 2026-05-24
---

# Run Packet - halo-evidence-vs-diagnosis-validation-v10-v1

This is the frozen v10 packet for the Northstar evidence-quality eval family.
It preserves the v9 case boundary but changes the readiness discipline: v10 may
not run unless a two-sided local-only substrate-feasibility probe shows that
no-source outputs fail C4 while substrate outputs pass C4.

This file is operator-facing. It names model conditions, readiness gates, and
run mechanics. It must not be shown to blind judges.

## Status

- Frozen case exists at `case.md`.
- Substrate-feasibility probe passed before freeze.
- Calibration anchors are filled and status `smoke_passed_pre_generation`.
- Six condition packets were frozen locally under the v10 freeze candidate.
- 48 real model outputs exist, eight per condition, with 0 simulated and 0
  deferred outputs.
- Hash-blinded `OUT-NN` packet, hosted OpenAI and hosted Anthropic judge
  receipts, aggregate-only reconciliation, `score-sheet.md`, `eval-decision.md`,
  and `postmortem.md` exist.
- Result: `partial`; eval decision: `do_not_promote`.
- V9 remains frozen and unrescored as `partial` / `do_not_promote`.

## Design Change From v9

V9 made no-source advice fail C4, but substrate failed C4 too. The compact
three-card packet did not move the generator from the workflow-product decoy
to the commercial-attribution boundary. V10 therefore uses the full public-safe
text of the three reviewed source cards rather than compact card summaries,
now that the LM Studio MLX generator is loaded with a 65,536-token context.

The load-bearing question remains C4: can the answer select the Commercial
Cleanroom as the evidence standard that can disconfirm the revenue /
product-market-fit story by removing bundle pricing and roadmap framing, while
explaining why the Usage Quality Sprint and Claim File Review are product
diagnostics or monitoring tests rather than commercial attribution tests?

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
- Score C3-C6 locally for design readiness only.
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
- Require at least two different-family routes to pass the C3-C6-only
  calibration gate before any full condition generation.
- Failed or unavailable routes are recorded honestly and score zero future
  outputs.

Calibration summary:

- Hosted OpenAI `gpt-5.4-mini`: passed, 0 C3-C6 eligibility differences.
- Hosted Anthropic `claude-opus-4-7`: passed, 0 C3-C6 eligibility differences.
- Local `gpt-oss:20b`: incomplete calibration surface; scores zero outputs.

## Frozen Inputs

The v10-v1 freeze records:

- `case.md` sections from `## Scenario` through `## Falsifier`.
- The final declared `model_conditions`.
- The reviewed lineage packet and hashes:
  - `corpus/source-cards/BK-0048-card-001.md` sha256 `2f11b5e74182d50dbbff87d26f43dd9376e22a6d4aa316a264fd9e2ecf5b476d`.
  - `corpus/source-cards/BK-0001-card-001.md` sha256 `1535ee5be11481217f9731d0851b2ffe23f9f61ae1b8b978added09026a9730b`.
  - `corpus/source-cards/BK-0007-card-001.md` sha256 `8d7bb540f96f0cc51fd77173c8e02988bdf8ca500fa2507c8f25875bc466251f`.
- Advisor prompt sha256 `61d771e2bff7fd2e18be1d2999d0f601760656e3e69b4622989ca7bffd3aff8e`.
- Calibration packet sha256 `8e782ab143fae035d1fd27b8f698a55ce6445af5fd9c8946474e20389a6135a6`.
- Condition packet hashes:
  - `vanilla`: `61d771e2bff7fd2e18be1d2999d0f601760656e3e69b4622989ca7bffd3aff8e`
  - `famous_sources_supplied`: `d057ad83d3f7bf7e5568fa060310fc46d54ebd76e09ae17c88d4f64128eb21dd`
  - `substrate_workflow`: `4d41d81d7d66e84b069bc8791aaca914e70d8ca6b29484d4b11bcf704c5f9046`
  - `vanilla_long_prompt`: `725394e5c302c1e30265374a9742db053b2cd62aaaaf76c7381b6fcdd8c7558b`
  - `generic_advice_prompted`: `372fe6128e2e633706cc66d44caf0e7dfaf2bba60181854165887aa7ed453ea9`
  - `criteria_prompted_no_sources`: `99e91b34c6105209d4266fed0bcb0ab798bcedfae3a4ab5516c3c91fc972adaa`
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

V10 is not `benchmark_supported`. The substrate finally separated strongly on
the C4-C6 boundary: pooled `substrate_workflow` mean total was 6.000, while
`generic_advice_prompted` was 3.000, `vanilla_long_prompt` was 2.938, and
`criteria_prompted_no_sources` was 3.500. The pre-registered total-score
margins and judge-level stability clauses passed.

The positive rule still failed because:

- `critical_criterion_margin` was false: controls also passed C3, so substrate
  did not beat key controls by the required +0.25 on every C3-C6 criterion.
- `no_critical_saturation` was false: `generic_advice_prompted` saturated C3
  at 1.00, while `vanilla_long_prompt` and `criteria_prompted_no_sources`
  reached 0.94 on C3.
- `no_unresolved_judge_trigger` was false because the two hosted judges
  disagreed on C3-C6 for 25 percent of `criteria_prompted_no_sources` outputs.

The result is therefore `partial` / `do_not_promote`, decision class
`critical_margin_failed`. This is a positive design signal for C4-C6 substrate
lift, but not a benchmark promotion.

## Positive Rule Additions

Relative to v9, v10 adds:

- A two-sided substrate-feasibility probe: no-source must fail C4 while
  substrate must pass C4 before full generation.
- Full public-safe reviewed source cards in the substrate condition.

The v9 `criteria_prompted_no_sources` control, non-discriminating judge guard,
and anti-saturation guard remain.

## Local-Only Probe Script

The local-only probe entry point is:

```sh
python3 local-only/eval-runs/halo-evidence-vs-diagnosis-validation-v10/substrate_feasibility_probe.py prepare
python3 local-only/eval-runs/halo-evidence-vs-diagnosis-validation-v10/substrate_feasibility_probe.py run
python3 local-only/eval-runs/halo-evidence-vs-diagnosis-validation-v10/substrate_feasibility_probe.py report
```

The script writes only under `local-only/`. Probe outputs and local scoring are
not public artifacts and do not constitute a benchmark result.

## Canon Boundary

This v10 design creates no canon candidate and no public advice claim. A future
`benchmark_supported` result, if one ever exists, may support only a claim about
model behavior under this frozen eval condition. It cannot prove that the
source claims are true or that the recommendation is correct in the real world.
