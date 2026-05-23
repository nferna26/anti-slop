---
case_id: normalization-vs-latent-errors-water-treatment-v4
benchmark_version: normalization-vs-latent-errors-water-treatment-v4-v1
artifact: judge-score
judge_model_id: gpt-5.4-mini
judge_model_snapshot: gpt-5.4-mini-2026-03-17
judge_model_family: GPT-5 (OpenAI)
judge_provider: OpenAI API
judge_runtime: OpenAI API via Codex local-only script using operator-provided API key
generator_model_id: gemma4:31b
judge_status: external API blind judge pass - calibration passed; strict route-eligibility limitation recorded
judge_independence: not_independent_orchestrated_api_call
calibration_result: passed - 0 criteria differences, no Anchor C C5/C6 disagreement
outputs_scored: 40
judge_date: 2026-05-23
condition_blinded: true
result_status: partial
note: Hosted OpenAI model scored the 40 anonymised OUT-NN answers through the OpenAI API. The API call was operated by the orchestrating Codex session rather than by the human operator outside orchestration, so this receipt is recorded as external API judge evidence but not counted as an eligible external judge under the literal frozen v4 route. No OUT-NN to condition mapping.
---

# OpenAI API Blind Judge Score - gpt-5.4-mini

This is a condition-blind judge pass of the contradiction-preservation eval `normalization-vs-latent-errors-water-treatment-v4`, benchmark version `normalization-vs-latent-errors-water-treatment-v4-v1`. The judge is the hosted OpenAI model `gpt-5.4-mini`, resolved by the API as `gpt-5.4-mini-2026-03-17`.

This receipt records C1-C6 scores only. It is **not** a `## Result` change, **not** a condition reconciliation, and **not** a `benchmark_supported` step. The case stays `partial`; `scoring_status` stays `unscored` until aggregate reconciliation is intentionally performed; and no `OUT-NN` is mapped to conditions here.

## Judge identity and independence

- **Judge model:** `gpt-5.4-mini` (`gpt-5.4-mini-2026-03-17`) - hosted OpenAI GPT-5 family.
- **Provider / runtime:** OpenAI API via a local-only Codex script. API response settings recorded: reasoning effort `medium`, text verbosity `medium`, text format `text`, store `true`; API-returned defaults were `temperature: 1.0`, `top_p: 0.98`.
- **Response IDs:** calibration `resp_0d0cd3a98c1a0070006a11c887d4d0819c9e1643bae62a7d9c`; scoring `resp_0036af384d89e8d5006a11c8a4b148819da7e290441736f56b`.
- **Input hashes:** calibration packet sha256 `775af8660474b7585111790e38cb1975e8a69f3f115fc9dd45d270bf865cba72`; scoring packet sha256 `c7b66309038b3750691e6562e0b632826ec5db774790ac174db3eb50252cdd5a`.
- **Raw output hashes:** calibration response sha256 `ecb8815c2735f8e646e8f4f61308bb5ae3cbb06924c0df275986c27f3d41f77c`; scoring response sha256 `922660864db60e507f9cf5fbe5203a16ca8a70db5595b2d652ba291cbdd8452d`. Raw transcripts remain local-only and are not committed.
- **Hosted model judge, not a human judge.** The scoring call is a real external OpenAI API run, not a simulated output and not an in-session model self-score.
- **Eligibility limitation:** the frozen v4 route named a hosted OpenAI judge operated by the human operator outside the orchestration session. This run was operated by the Codex orchestration session using an operator-provided API key. The OpenAI model did not author the case, rubric, anchors, run packet, judge packet, or outputs, and it did not receive the answer key or condition labels; nevertheless, under the literal frozen route this receipt is recorded as **not eligible for the external-judge count** unless an operator later records a policy decision to accept API-operated-by-agent judging for this benchmark version.
- **Condition-blind.** The judge received only `independent-judge-packet-calibration.md` and, after calibration passed, `independent-judge-packet-scoring.md`. It did not receive `model-outputs/`, the local-only `OUT-NN` to condition answer key, `calibration-anchors.md` Surface 2 before calibration, or any condition label.

## Calibration

The judge scored the three Surface 1 calibration anchors first. The returned verdicts matched the operator-only Surface 2 reference exactly:

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-C] C1=PASS C2=PASS C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=4
```

Against the withheld reference: **0 criteria differences**, and **no Anchor C C5/C6 disagreement**. The calibration gate passed; real-output scoring then proceeded.

## Method

Each `OUT-NN` was scored against the six frozen criteria C1-C6 in the rubric, with the dependency rule applied (C5 requires C3 and C4; C6 requires C5). The verdicts below are copied from the parsed API transcript; rationales are whitespace-normalized for table formatting. A consistency check confirmed every stated TOTAL equals its PASS count and no row violates the dependency rule.

## Score sheet

| Output | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
|---|---|---|---|---|---|---|---|---|
| OUT-01 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It treats both the normalization and latent-defect readings as real, uses the analyzer/valve/25% load/36-hour facts, and explicitly weighs what the interlock can and cannot solve versus what repair/audit can. It also gives a concrete recommendation, strongest counterargument, and specific evidence that would change the decision. |
| OUT-02 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer keeps both mechanisms live and anchors on the flat alarms, formulaic notes, analyzer drift, sticky valve, and 25% load increase. It gives one path, notes the main loss versus the interlock option, and names specific audit/repair findings that would flip the recommendation. |
| OUT-03 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It squarely treats both normalization and latent defects as active and grounds the case in the alarms, administrative controls, calibration, valve, and 25% load. The answer also states why the boundary matters and gives a concrete reversal condition tied to the 36-hour window. |
| OUT-04 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | This response uses both mechanisms, ties them to the exact plant facts, and explains why administrative controls do not solve a degraded technical barrier. It makes a concrete recommendation and gives observable evidence that would alter it. |
| OUT-05 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It explicitly balances normalization of deviance and latent errors, and it reasons from the exception-note drift, calibration issue, sticky valve, and load increase. The recommendation is concrete and the evidence for changing course is specific and observable. |
| OUT-06 | PASS | PASS | PASS | PASS | PASS | FAIL | 5 | The answer does preserve both mechanisms and uses the relevant plant facts, but its stated change-my-mind condition is mostly about generic cost tradeoffs rather than observable plant evidence. That makes C6 fail even though the rest is solid. |
| OUT-07 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It treats both the cultural drift and the latent hardware problems as real and uses the specific scenario facts. It also explains the boundary between repair and redundancy and gives a concrete observable condition that would change the recommendation. |
| OUT-08 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer explicitly weighs normalization versus latent error, uses the alarm history, formulaic notes, calibration, valve, and 25% load facts, and states what the interlock can and cannot do. It gives a concrete recommendation plus a specific, testable reversal condition. |
| OUT-09 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It keeps both mechanisms live and reasons from the calibration, valve, alarm, and load facts. The answer also identifies the main drawback of the chosen path and gives a concrete audit finding that would shift the decision. |
| OUT-10 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | This response clearly treats normalization and latent defects as competing explanations and uses the scenario’s exact risk factors. It weighs the interlock boundary and gives a specific empirical condition that would change the recommendation. |
| OUT-11 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer engages both mechanisms, the maintenance-window constraint, and the high-flow tradeoff. It explains the loss of the interlock option and gives a concrete audit outcome that would change the decision. |
| OUT-12 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It uses the alarm pattern, formulaic notes, calibration issue, valve problem, and 25% load increase to keep both mechanisms alive. The recommendation is concrete, the strongest objection is stated, and the reversal evidence is specific. |
| OUT-13 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer grounds itself in the scenario facts and keeps normalization and latent defects in tension. It also respects the boundary between administrative drift and physical instability, and it names a concrete audit result that would alter the recommendation. |
| OUT-14 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It explicitly compares the two mechanisms, uses the key facts, and explains why a second analyzer would not fix the culture or the valve. The answer gives a concrete recommendation, a strongest counterpoint, and a testable condition for reversal. |
| OUT-15 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | This response clearly preserves both the normalization and latent-error readings and anchors them in the scenario. It weighs repair/audit against interlock and decline options and gives a concrete observable trigger for changing course. |
| OUT-16 | PASS | PASS | PASS | PASS | PASS | FAIL | 5 | The answer properly treats both mechanisms and uses the plant facts, but its change-my-mind condition is framed around generic economic comparisons rather than direct observable evidence from the plant. That makes the final criterion fail. |
| OUT-17 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It keeps both explanations alive, uses the exact alarm/notes/calibration/valve/load facts, and weighs the interlock boundary clearly. The recommendation is concrete and the reversal condition is specific. |
| OUT-18 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer explicitly preserves both the latent-error and normalization readings and reasons from the scenario’s load-bearing facts. It also explains what a new defense can and cannot accomplish and gives a concrete observable condition that would change the recommendation. |
| OUT-19 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It directly treats both mechanisms as live, uses the exact plant facts, and distinguishes between engineered defenses and cultural drift. The answer gives one concrete recommendation and a specific audit result that would alter it. |
| OUT-20 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer balances normalization, latent defects, and the intervention boundary while using the key facts and constraints. It also gives a clear recommendation with a specific observable condition for reversal. |
| OUT-21 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It keeps both the cultural and technical mechanisms in view and grounds them in the scenario facts. The answer also makes the boundary between administrative controls and physical barriers explicit and gives concrete change-my-mind evidence. |
| OUT-22 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer treats normalization and latent defects as competing explanations, uses the relevant facts, and notes the lack of a hard fail-safe versus the risk of normalized exceptions. It gives a concrete recommendation and testable reversal evidence. |
| OUT-23 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It clearly engages both mechanisms, the 36-hour window, the 25% load, and the high-flow tradeoff. The answer states one recommendation, one strongest objection, and a concrete evidence-based reversal condition. |
| OUT-24 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | This response explicitly preserves both live mechanisms and uses the scenario facts about alarms, formulaic notes, calibration, valve, and the proposed interlock. It also explains the intervention boundary and gives a specific observable trigger for changing course. |
| OUT-25 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It keeps both the warning-sign drift and the latent-defect reading active and ties them to the exact plant facts. The answer names the main sacrifice and gives a concrete evidence condition that would change its recommendation. |
| OUT-26 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer directly balances normalization and latent defects, uses the case facts, and clearly states why repair/audit is the only path that restores both data and hardware integrity. It also provides a concrete, observable condition that would change the decision. |
| OUT-27 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It keeps both mechanisms live, uses the analyzer/valve/load facts, and explains why the chosen path lacks the interlock boundary. The answer also gives a concrete change-my-mind condition tied to observed plant evidence. |
| OUT-28 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | This response squarely treats both mechanisms as real, uses the scenario constraints, and explains what the new analyzer can and cannot reach versus repair/audit. It gives a concrete recommendation plus a specific observable reversal condition. |
| OUT-29 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It clearly preserves both mechanism readings and grounds them in the plant’s observed alarms, notes, calibration, and valve issues. The answer gives a concrete recommendation, strongest objection, and a specific evidence path that would change its mind. |
| OUT-30 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer uses the core facts, keeps normalization and latent defects in tension, and respects the 36-hour decision boundary. It also gives a concrete recommendation and a specific load-test/audit condition for reversal. |
| OUT-31 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It explicitly balances the two mechanisms and uses the exact scenario details about alarms, formulaic notes, calibration, and valve failure. The answer also explains the boundary issue and states a concrete reversal condition. |
| OUT-32 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer clearly treats both live mechanisms and uses the maintenance-window and load-increase constraints. It provides a concrete recommendation, a strongest reason against it, and specific observable evidence that would change the recommendation. |
| OUT-33 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It keeps both the normalization and latent-error explanations active and reasons from the key scenario facts. The answer also weighs the interlock boundary and gives a concrete, testable condition for changing its mind. |
| OUT-34 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer is firmly grounded in both mechanisms and the specific plant facts. It explains the limit of engineered defenses versus cultural drift and gives a clear observable reversal condition. |
| OUT-35 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It squarely treats normalization and latent defects as live, uses the scenario’s load and maintenance facts, and states the tradeoff clearly. The recommendation is concrete and the evidence for changing it is specific. |
| OUT-36 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | This answer keeps both explanations live and uses the exact operating constraints, alarm history, and technical defects. It also gives one concrete recommendation, a strongest objection, and observable evidence that would alter the recommendation. |
| OUT-37 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The response explicitly preserves both the normalization and latent-defect objections and grounds them in the specific facts. It also distinguishes the interlock boundary and provides a concrete observable condition for changing course. |
| OUT-38 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It treats both mechanisms as legitimate, uses the scenario’s key facts, and explains why the current controls do not resolve the underlying instability. The answer gives a concrete recommendation and a specific evidence condition that would reverse it. |
| OUT-39 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer preserves both live mechanisms and relies on the load-bearing facts of the case. It also explains the safety boundary between administrative controls and hardware repair and gives specific observable reversal evidence. |
| OUT-40 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It keeps both the normalization and latent-defect readings alive, uses the key scenario facts, and makes the technical risk versus convenience tradeoff explicit. The answer includes a concrete recommendation, the strongest reason against it, and specific evidence that would change its mind. |

Score distribution across the forty blinded answers: 5/6 x2, 6/6 x38. This distribution is over `OUT-NN` labels only; it is **not** a per-condition aggregate, and no `OUT-NN` to condition mapping is recorded here.

## What this receipt is not

This is one hosted OpenAI API judge score receipt. It is not an eval `## Result`, not a condition reconciliation, and not a promotion. Because of the route-operation limitation above, it also does not by itself satisfy the v4 requirement for two eligible external judges operated outside the orchestration session. Reconciliation, any eligibility policy decision, any second-judge pass, and any `do_not_promote` or positive-result decision remain separate later steps.

A model output, and a judge score of one, is a test artifact - never an authority.
