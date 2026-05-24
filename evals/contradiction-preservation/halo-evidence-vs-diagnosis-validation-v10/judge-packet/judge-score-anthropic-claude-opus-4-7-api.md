---
case_id: halo-evidence-vs-diagnosis-validation-v10
benchmark_version: halo-evidence-vs-diagnosis-validation-v10-v1
artifact: judge-score
judge_model_id: claude-opus-4-7
judge_model_snapshot: claude-opus-4-7
judge_model_family: Claude Opus (Anthropic)
judge_provider: Anthropic API
judge_runtime: Anthropic API via Codex local-only script using operator-provided API key
generator_model_id: gemma-4-31b-it-mlx:2
judge_status: eligible blind judge pass - calibration passed; operator route acceptance recorded
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated pre-registered judge route; passed v10 smoke-2 before generation
calibration_result: passed - 0 C3-C6 eligibility differences, 0 C1/C2 differences, no dependency or total mismatch
outputs_scored: 48
judge_date: 2026-05-24
condition_blinded: true
result_status: partial
note: Pre-registered blind judge route judged the v10 anonymised OUT-NN answers. No OUT-NN to condition mapping.
---

# Anthropic API Blind Judge Score - claude-opus-4-7

This is a condition-blind judge receipt for `halo-evidence-vs-diagnosis-validation-v10`, benchmark
version `halo-evidence-vs-diagnosis-validation-v10-v1`. It records C1-C6 scores only. It is not a Result
lift, not a condition reconciliation, and not benchmark promotion.

## Judge identity and independence

- Judge model: `claude-opus-4-7` (`claude-opus-4-7`), Claude Opus (Anthropic).
- Provider / runtime: Anthropic API via Codex local-only script using operator-provided API key.
- API settings: no explicit temperature parameter; max_tokens 2000 calibration / 12000 scoring.
- Response IDs: calibration `msg_01Kh4TjQLBhs2XW7RJcRZZB1`, scoring `msg_01JQJyegPZtLftMPkJ8XwGr6`.
- Input hashes: calibration packet sha256 `8e782ab143fae035d1fd27b8f698a55ce6445af5fd9c8946474e20389a6135a6`, scoring packet sha256 `07c8adfa59735592ff72eaaa4e8783059edf4af0ecfe152c1c2bc210a41f42d8`.
- Raw output hashes: calibration response sha256 `e4ab7306ca8d40eed606a76ca8d126c72c01b2c98711ba3102e3827a9aa0efd2`, scoring response sha256 `bccb200a8005eb44c671f9042e13c08d8bb44900211cce1be55ffb083d651db6`. Raw transcripts remain local-only and are not committed.
- API usage for scoring: input tokens `48695`, output tokens `5653`.
- Judge route is pre-registered before generation. Hosted API judge calls are real external API runs; the local backstop is a real local non-generator model run. Neither is a simulated output or an in-session self-score.
- Route eligibility: the v10 run packet named hosted OpenAI, hosted Anthropic, and local gpt-oss backstop routes before generation. The OpenAI and Anthropic routes passed the `smoke-2` C3-C6 calibration gate before any v10 output generation. This receipt records the agent-operated route honestly.
- Condition-blind: the judge received only the independent calibration packet and, after calibration passed, the independent scoring packet. It did not receive model-outputs/, the local-only answer key, Surface 2 reference verdicts before calibration, or condition labels.

## Calibration

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-C] C1=PASS C2=PASS C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=4
[ANCHOR-D] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-E] C1=PASS C2=PASS C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=4
[ANCHOR-F] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-G] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-H] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
```

Against the withheld reference: 0 total recorded differences;
C3-C6 eligibility differences: 0; C1/C2 differences: 0; dependency violations: 0; total mismatches: 0. Calibration
eligibility: `True` under `C3-C6 exact on anchors A-G; C1/C2 non-gating; H illustrative-only`.

## Method

Each OUT-NN was scored against the six frozen criteria C1-C6 in the rubric, with
the dependency rule applied. Parsed rows were checked for dependency-rule
violations and TOTAL arithmetic. Arithmetic total normalization: OUT-06 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-07 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-08 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-12 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-13 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-15 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-16 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-17 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-19 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-20 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-21 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-22 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-24 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-25 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-26 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-27 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-28 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-29 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-30 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-31 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-32 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-33 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-34 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-35 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-36 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-37 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-38 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-39 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-41 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-42 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-44 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-45 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-47 reported TOTAL=2 but C1-C6 PASS count is 3, OUT-48 reported TOTAL=2 but C1-C6 PASS count is 3. Aggregates use the PASS-count total required by the rubric.

## Score sheet

| Output | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
|---|---|---|---|---|---|---|---|---|
| OUT-01 | FAIL | FAIL | FAIL | FAIL | FAIL | FAIL | 0 | Picks Claim File Review without recognizing it samples already-renewed accounts; doesn't address commercial attribution. Change-my-mind condition is muddled and doesn't isolate disconfirming evidence standard. |
| OUT-02 | PASS | PASS | FAIL | FAIL | FAIL | FAIL | 2 | Workflow-truth shortcut; selects Claim File Review without recognizing the sampling bias from already-renewed accounts. Names contaminants but ultimately treats CFR as sufficient validation of commercial story. |
| OUT-03 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Correctly identifies Commercial Cleanroom as disconfirming test, names bundle/roadmap/manager-rerun contaminants, explains why other tests are diagnostic not commercial, and provides behavioral falsifier (independent adjuster return rate). |
| OUT-04 | PASS | PASS | FAIL | FAIL | FAIL | FAIL | 2 | Workflow-truth shortcut. Picks Claim File Review and explicitly frames Cleanroom as just "pricing elasticity," missing that it tests the disconfirming commercial attribution question. |
| OUT-05 | PASS | PASS | PASS | PASS | PASS | FAIL | 5 | Selects Cleanroom and names contaminants. Change-my-mind condition shifts to narrowing on health-liability, which is somewhat behavioral but not tightly tied to the commercial attribution falsifier. |
| OUT-06 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants well but picks Claim File Review as the diagnostic. Treats Cleanroom only as change-my-mind condition rather than the disconfirming commercial test. |
| OUT-07 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Identifies contamination but selects Claim File Review without acknowledging it samples already-renewed accounts. Fails to recognize Cleanroom as the disconfirming commercial test. |
| OUT-08 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but chooses Claim File Review, treating Cleanroom only as pricing elasticity. Fails to see CFR samples already-renewed accounts under contaminated commercial conditions. |
| OUT-09 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Selects Cleanroom as the test that removes bundle and roadmap contaminants. Names tradeoff (short-term revenue), and offers a concrete behavioral falsifier (high acceptance rates in CFR audit). |
| OUT-10 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Picks Cleanroom, displaces scaling, names multiple contaminants, explains why monitoring is illusory, and provides specific behavioral falsifier about why removal happened. |
| OUT-11 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Concisely picks Cleanroom, identifies bundle/roadmap/abandonment contaminants, explains why Sprint and CFR are insufficient, and gives a clear falsifier tied to health-liability regulatory blocker. |
| OUT-12 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Workflow-truth shortcut. Names contaminants but picks Claim File Review, dismissing Cleanroom as only "pricing elasticity" rather than the disconfirming commercial test. |
| OUT-13 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names halo and contaminated signals but selects Claim File Review. Treats Cleanroom only as sales elasticity test and doesn't see CFR's sampling problem. |
| OUT-14 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Selects Cleanroom, names halo and bundle/roadmap contaminants, displaces scaling, identifies tradeoff, and provides behavioral falsifier (independent adjuster return rate correlated with cycle time). |
| OUT-15 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Treats Cleanroom only as change-my-mind condition rather than the actual disconfirming test for commercial attribution. |
| OUT-16 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants and acknowledges CFR won't complete in time, but still selects it. Fails to recognize Cleanroom as the disconfirming commercial test. |
| OUT-17 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contamination but picks Claim File Review. Treats Cleanroom as only testing pricing, not the commercial attribution question. |
| OUT-18 | PASS | PASS | FAIL | FAIL | FAIL | FAIL | 2 | Mentions bundle-driven renewals but doesn't sharply identify contamination mechanisms. Picks CFR; treats Cleanroom only as pricing elasticity test. |
| OUT-19 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names halo effect and contaminants well but picks Claim File Review. Frames Cleanroom only as pricing test, not commercial attribution disconfirmation. |
| OUT-20 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review; doesn't recognize CFR samples already-renewed accounts. Treats Cleanroom as trailing indicator. |
| OUT-21 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants well but picks Claim File Review, framing Cleanroom only as sales tactics test rather than the commercial attribution disconfirmation. |
| OUT-22 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review without recognizing the sampling bias. Treats Cleanroom only as sales tactics test. |
| OUT-23 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Selects Cleanroom, displaces scaling, names halo and bundle/roadmap/manager-usage contaminants, identifies revenue-loss tradeoff, and provides behavioral falsifier about non-regulated adjuster adoption. |
| OUT-24 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review; explicitly says Cleanroom "tests the sales pitch, not the product," missing that it tests commercial attribution. |
| OUT-25 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants and ticket retagging well but picks Claim File Review. Recognizes Cleanroom in change-my-mind but doesn't select it. |
| OUT-26 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Treats Cleanroom as only revealing willingness to pay, not commercial attribution. |
| OUT-27 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review without recognizing the sampling problem in already-renewed accounts. |
| OUT-28 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Treats Cleanroom only as price/sales test, missing its role as the commercial attribution disconfirmation. |
| OUT-29 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Doesn't recognize CFR samples already-renewed accounts under the same commercial story. |
| OUT-30 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Treats Cleanroom only as sales test, doesn't see it as the commercial attribution disconfirmation. |
| OUT-31 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Frames Cleanroom only as pricing/sales narrative test. |
| OUT-32 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contamination but picks Claim File Review. Dismisses Cleanroom as testing only "pricing and sales psychology," missing the commercial attribution role. |
| OUT-33 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Change-my-mind misframes Cleanroom as pricing strategy rather than commercial attribution test. |
| OUT-34 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but selects Claim File Review. Doesn't recognize CFR's already-renewed sampling limitation; treats Cleanroom as only revenue signal. |
| OUT-35 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Treats Cleanroom only as willingness-to-pay test rather than the commercial attribution disconfirmation. |
| OUT-36 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Frames Cleanroom only as willingness-to-pay test, missing the commercial attribution role. |
| OUT-37 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Treats Cleanroom only as pricing/sales psychology test. |
| OUT-38 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Treats Cleanroom only as willingness-to-pay test. |
| OUT-39 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contamination clearly but picks Claim File Review. Doesn't engage Cleanroom as the disconfirming commercial test. |
| OUT-40 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Picks Cleanroom, displaces scaling, names halo and contaminants, identifies tradeoff with sales/revenue risk, and provides behavioral falsifier from CFR-style evidence of acceptance without rewrites. |
| OUT-41 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Frames Cleanroom only as pricing/sales positioning test rather than commercial attribution. |
| OUT-42 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Treats Cleanroom only as willingness-to-pay, missing commercial attribution role. |
| OUT-43 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Selects Cleanroom, displaces scaling, names halo and contaminants, identifies revenue/political risk tradeoff, and provides behavioral falsifier (independent adjuster acceptance in non-regulated segments). |
| OUT-44 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Dismisses Cleanroom as testing price not product, and doesn't see CFR's sampling problem. |
| OUT-45 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Frames Cleanroom only as sales data test rather than commercial attribution disconfirmation. |
| OUT-46 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Selects Cleanroom, displaces scaling, names halo effect and bundle/roadmap contaminants, identifies sales-conflict tradeoff, and provides concrete behavioral falsifier (CFR showing independent adjuster acceptance). |
| OUT-47 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Treats Cleanroom only as pricing test in change-my-mind condition. |
| OUT-48 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminants but picks Claim File Review. Explicitly dismisses Cleanroom as testing only sales tactics/pricing elasticity, missing its commercial attribution role. |

Score distribution across the 48 blinded answers: {'0': 1, '2': 3, '3': 34, '5': 1, '6': 9}.
This distribution is over OUT-NN labels only; it is not a per-condition
aggregate, and no OUT-NN to condition mapping is recorded here.

## What this receipt is not

This is one blind judge receipt. It is not an eval Result, not a condition
reconciliation, and not a promotion. Reconciliation and any do-not-promote or
benchmark-supported decision are separate later steps.

A model output and a judge score are test artifacts, never authorities.
