---
case_id: halo-evidence-vs-diagnosis-validation-v11
benchmark_version: halo-evidence-vs-diagnosis-validation-v11-v1
artifact: judge-score
judge_model_id: claude-opus-4-7
judge_model_snapshot: claude-opus-4-7
judge_model_family: Claude Opus (Anthropic)
judge_provider: Anthropic API
judge_runtime: Anthropic API via Codex local-only script using operator-provided API key
generator_model_id: gemma-4-31b-it-mlx:2
judge_status: eligible blind judge pass - calibration passed; operator route acceptance recorded
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated pre-registered judge route; passed v11 smoke-2 before generation
calibration_result: passed - 0 C4-C6 eligibility differences, 0 C1/C2/C3 differences, no dependency or total mismatch
outputs_scored: 48
judge_date: 2026-05-24
condition_blinded: true
result_status: partial
note: Pre-registered blind judge route judged the v11 anonymised OUT-NN answers. No OUT-NN to condition mapping.
---

# Anthropic API Blind Judge Score - claude-opus-4-7

This is a condition-blind judge receipt for `halo-evidence-vs-diagnosis-validation-v11`, benchmark
version `halo-evidence-vs-diagnosis-validation-v11-v1`. It records C1-C6 scores only. It is not a Result
lift, not a condition reconciliation, and not benchmark promotion.

## Judge identity and independence

- Judge model: `claude-opus-4-7` (`claude-opus-4-7`), Claude Opus (Anthropic).
- Provider / runtime: Anthropic API via Codex local-only script using operator-provided API key.
- API settings: no explicit temperature parameter; max_tokens 2000 calibration / 12000 scoring.
- Response IDs: calibration `msg_01GCHo2oPGe2xpfhXF7j71yw`, scoring `msg_01YDmio453zr4MYGqkfqCMsp`.
- Input hashes: calibration packet sha256 `a88d2e4f115a8284ba398dacacd84e2c5a312f3abff6383eee81c7af6e2a63c9`, scoring packet sha256 `111ef33c2a4860fea909f9aac347fe5f27d1b89e25e11fc91c241313907cc487`.
- Raw output hashes: calibration response sha256 `3f338acc6557b22d75f6c4f8e439168c261bd95c05ab0e2052c019ce68b1d916`, scoring response sha256 `09c7321062ea8e048a089a9e631ef583da4ac901046244199f653dd03fc50ab2`. Raw transcripts remain local-only and are not committed.
- API usage for scoring: input tokens `49518`, output tokens `5222`.
- Judge route is pre-registered before generation. Hosted API judge calls are real external API runs; the local backstop is a real local non-generator model run. Neither is a simulated output or an in-session self-score.
- Route eligibility: the v11 run packet named hosted OpenAI, hosted Anthropic, and local gpt-oss backstop routes before generation. The OpenAI and Anthropic routes passed the `smoke-2` C4-C6 calibration gate before any v11 output generation. This receipt records the agent-operated route honestly.
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
C4-C6 eligibility differences: 0; C1/C2/C3 differences: 0; dependency violations: 0; total mismatches: 0. Calibration
eligibility: `True` under `C4-C6 exact on anchors A-G; C1/C2/C3 non-promotional; H illustrative-only`.

## Method

Each OUT-NN was scored against the six frozen criteria C1-C6 in the rubric, with
the dependency rule applied. Parsed rows were checked for dependency-rule
violations and TOTAL arithmetic. No arithmetic total normalization was needed.

## Score sheet

| Output | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
|---|---|---|---|---|---|---|---|---|
| OUT-01 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Selects Claim File Review and explicitly rejects the Commercial Cleanroom as merely a pricing test, missing that the Cleanroom is the disconfirming commercial test. C5 fails by dependency; C6 falsifier is plausible but C5 gating applies. |
| OUT-02 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Picks Claim File Review and dismisses the Cleanroom as only "willingness to pay," failing to recognize it as the disconfirming test for the commercial attribution question. |
| OUT-03 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Selects Commercial Cleanroom, correctly identifies bundle pricing and roadmap framing as contaminants, distinguishes diagnostic tests from commercial validation, names short-term revenue cost, and gives concrete falsifier. |
| OUT-04 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Selects Commercial Cleanroom on the right grounds—removing pricing and roadmap confounds—names contaminated signals, weighs the short-term revenue tradeoff, and provides a behavioral falsifier. |
| OUT-05 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Picks Claim File Review and frames the Cleanroom as merely a pricing-elasticity test, missing its role as the disconfirming commercial test. |
| OUT-06 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Workflow-truth shortcut: chooses Claim File Review without acknowledging it samples already-renewed accounts and cannot disconfirm the commercial attribution. |
| OUT-07 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Selects Claim File Review and treats the Cleanroom only as a hypothetical fallback rather than the correct disconfirming test for the board question. |
| OUT-08 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Workflow-truth shortcut; selects Claim File Review without noting it samples already-renewed accounts and cannot disconfirm the commercial story. |
| OUT-09 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Chooses Claim File Review; doesn't engage that the review is anchored in accounts selected by the current commercial motion. |
| OUT-10 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Selects Commercial Cleanroom, names bundle pricing and roadmap pitch as the variables to isolate, weighs short-term revenue risk, and provides a falsifier tied to behavioral evidence. |
| OUT-11 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Cleanroom selected on disconfirming grounds; correctly identifies why diagnostics don't answer the board question, names sacrifice, and gives a concrete behavioral falsifier. |
| OUT-12 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Chooses Claim File Review; treats Cleanroom as a follow-on rather than the primary disconfirming commercial test. |
| OUT-13 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Picks Claim File Review and mischaracterizes Cleanroom as only "willingness to pay," failing the disconfirming standard. |
| OUT-14 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Brief recommendation of Claim File Review; doesn't engage with the commercial attribution question or that the review samples already-renewed accounts. |
| OUT-15 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Claim File Review chosen; Cleanroom framed only as a pricing test rather than the disconfirming commercial standard. |
| OUT-16 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Selects Cleanroom for the right reason (isolates pricing and roadmap framing), names contamination concretely, engages the revenue risk under the twelve-day window, and provides a behavioral falsifier. |
| OUT-17 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Picks Claim File Review and dismisses Cleanroom as merely measuring willingness to pay. |
| OUT-18 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Claim File Review chosen; explicitly downgrades Cleanroom as just a sales experiment, missing its role as the disconfirming commercial test. |
| OUT-19 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Claim File Review chosen; treats Cleanroom only as lagging willingness-to-pay rather than the disconfirming standard. |
| OUT-20 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Workflow-truth shortcut; dismisses Cleanroom as a "sales elasticity" test. |
| OUT-21 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Picks Claim File Review; doesn't address the contamination of already-renewed sampling and treats Cleanroom only as a fallback for pricing. |
| OUT-22 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Claim File Review selected; Cleanroom characterized as testing only the sales pitch and revenue attribution, not as the necessary disconfirming standard. |
| OUT-23 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Selects Cleanroom as the isolating test for pricing and roadmap framing, acknowledges the product-utility tradeoff, and gives a behavioral falsifier. |
| OUT-24 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Chooses Claim File Review; reduces Cleanroom to "pricing/sales psychology" rather than the disconfirming commercial test. |
| OUT-25 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Claim File Review chosen with Cleanroom treated as merely a willingness-to-pay test. |
| OUT-26 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Picks Claim File Review and reduces Cleanroom to "sales psychology," failing the disconfirming standard despite otherwise rich analysis. |
| OUT-27 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Claim File Review chosen; Cleanroom dismissed as "sales psychology." |
| OUT-28 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Chooses Claim File Review without recognizing the Cleanroom as the disconfirming commercial test for the board question. |
| OUT-29 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Selects Cleanroom on disconfirming grounds (isolates pricing and roadmap), names revenue cost, and gives a concrete falsifier shifting to Claim File Review. |
| OUT-30 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Cleanroom selected for the right reasons; names contamination mechanisms, weighs the political/financial cost in the twelve-day window, and provides a behavioral falsifier. |
| OUT-31 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Claim File Review chosen; Cleanroom reduced to "if they buy it," missing disconfirming role. |
| OUT-32 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Selects Cleanroom as the test that isolates pricing/pitch noise, weighs board-window cost, and gives a behavioral falsifier. |
| OUT-33 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Cleanroom chosen on disconfirming grounds, contamination named concretely, revenue-window risk weighed, and falsifier given. |
| OUT-34 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Selects Cleanroom citing bundle pricing and roadmap framing as the variables to isolate; identifies short-term revenue risk and a concrete falsifier. |
| OUT-35 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Claim File Review chosen; Cleanroom characterized as testing only willingness to pay. |
| OUT-36 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Picks Claim File Review and reduces Cleanroom to a pricing test, missing the disconfirming commercial standard. |
| OUT-37 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Claim File Review chosen; Cleanroom positioned as fallback for pricing strategy rather than disconfirming test. |
| OUT-38 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Claim File Review chosen; Cleanroom mentioned only as testing price elasticity, not as the disconfirming commercial test. |
| OUT-39 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Selects Cleanroom because pricing incentives and roadmap promises contaminate signals; identifies revenue/momentum cost and a behavioral falsifier. |
| OUT-40 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Claim File Review chosen; explicitly dismisses Cleanroom as a packaging test rather than the disconfirming commercial standard. |
| OUT-41 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Picks Claim File Review while dismissing Cleanroom as testing only pricing/sales tactics. |
| OUT-42 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Claim File Review chosen; Cleanroom relegated to a pricing/packaging fallback. |
| OUT-43 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Picks Claim File Review; falsifier shifts to narrowing rather than recognizing Cleanroom as the disconfirming commercial test. |
| OUT-44 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Claim File Review chosen; reduces Cleanroom to "sales pitch" testing without the disconfirming role. |
| OUT-45 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Picks Claim File Review and treats Cleanroom only as a pricing/packaging tool, missing the disconfirming standard. |
| OUT-46 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Claim File Review chosen; Cleanroom mentioned only as a willingness-to-pay test for falsification. |
| OUT-47 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Picks Claim File Review; reduces Cleanroom to a price-elasticity test rather than the disconfirming commercial standard. |
| OUT-48 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Chooses Claim File Review; treats Cleanroom merely as "if they will pay," failing to recognize it as the disconfirming commercial test. |

Score distribution across the 48 blinded answers: {'3': 36, '6': 12}.
This distribution is over OUT-NN labels only; it is not a per-condition
aggregate, and no OUT-NN to condition mapping is recorded here.

## What this receipt is not

This is one blind judge receipt. It is not an eval Result, not a condition
reconciliation, and not a promotion. Reconciliation and any do-not-promote or
benchmark-supported decision are separate later steps.

A model output and a judge score are test artifacts, never authorities.
