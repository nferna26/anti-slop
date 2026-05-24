---
case_id: halo-evidence-vs-diagnosis-validation-v9
benchmark_version: halo-evidence-vs-diagnosis-validation-v9-v1
artifact: judge-score
judge_model_id: claude-opus-4-7
judge_model_snapshot: claude-opus-4-7
judge_model_family: Claude Opus (Anthropic)
judge_provider: Anthropic API
judge_runtime: Anthropic API via Codex local-only script using operator-provided API key
generator_model_id: gemma-4-31b-it-mlx
judge_status: eligible blind judge pass - calibration passed; operator route acceptance recorded
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated pre-registered judge route; passed v9 smoke-2 before generation
calibration_result: passed - 0 C3-C6 eligibility differences, 0 C1/C2 differences, no dependency or total mismatch
outputs_scored: 48
judge_date: 2026-05-24
condition_blinded: true
result_status: partial
note: Pre-registered blind judge route judged the v9 anonymised OUT-NN answers. No OUT-NN to condition mapping.
---

# Anthropic API Blind Judge Score - claude-opus-4-7

This is a condition-blind judge receipt for `halo-evidence-vs-diagnosis-validation-v9`, benchmark
version `halo-evidence-vs-diagnosis-validation-v9-v1`. It records C1-C6 scores only. It is not a Result
lift, not a condition reconciliation, and not benchmark promotion.

## Judge identity and independence

- Judge model: `claude-opus-4-7` (`claude-opus-4-7`), Claude Opus (Anthropic).
- Provider / runtime: Anthropic API via Codex local-only script using operator-provided API key.
- API settings: no explicit temperature parameter; max_tokens 2000 calibration / 12000 scoring.
- Response IDs: calibration `msg_01DNUASRxhGszYFeM52wvE8a`, scoring `msg_01TdXR3LZHCT7XMYgLpp94D2`.
- Input hashes: calibration packet sha256 `d5bf3a2c7a97462e9669310bc1a9313d20d219c88fa96c849678faaa1aa9a469`, scoring packet sha256 `b5f396fcc200526ee234f828e8f0669f5d8328b54c3f6048252fddcad145b514`.
- Raw output hashes: calibration response sha256 `5678adbb1dae9b737208d3eba97a4b009a073c37ab2e5dcd5a7d9fbfa7d144db`, scoring response sha256 `31444fc2fbb8303b19bb04daef7bd2a3d8e888fa2c2c8fd1b593d267b0e3081c`. Raw transcripts remain local-only and are not committed.
- API usage for scoring: input tokens `49112`, output tokens `4984`.
- Judge route is pre-registered before generation. Hosted API judge calls are real external API runs; the local backstop is a real local non-generator model run. Neither is a simulated output or an in-session self-score.
- Route eligibility: the v9 run packet named hosted OpenAI, hosted Anthropic, and local gpt-oss backstop routes before generation. The OpenAI and Anthropic routes passed the `smoke-2` C3-C6 calibration gate before any v9 output generation. This receipt records the agent-operated route honestly.
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
violations and TOTAL arithmetic. No arithmetic total normalization was needed.

## Score sheet

| Output | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
|---|---|---|---|---|---|---|---|---|
| OUT-01 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Identifies contamination (bundle pricing, manager usage, ticket retagging) but selects Claim File Review, missing that it samples already-renewed accounts and cannot disconfirm the commercial attribution. C5/C6 fail by dependency. |
| OUT-02 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Workflow-truth shortcut. Names contamination signals well but picks Claim File Review without recognizing it samples renewed accounts under contaminated commercial conditions. |
| OUT-03 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Identifies performance-aware attribution and contaminated signals but selects Claim File Review, treating it as load-bearing diagnosis without acknowledging it cannot test commercial attribution. |
| OUT-04 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Workflow-truth shortcut. Notes pricing/manager-usage contamination but picks Claim File Review and dismisses Cleanroom as "only sales pitch." |
| OUT-05 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Identifies entangled signals but picks Claim File Review without engaging that it samples already-renewed accounts; brief boundary analysis. |
| OUT-06 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Workflow-truth shortcut. Recognizes contamination but selects Claim File Review as "ground truth" without addressing the renewed-account sampling problem. |
| OUT-07 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names bundle pricing, roadmap pitch, manager usage contamination but picks Claim File Review. Does not isolate the disconfirming commercial test. |
| OUT-08 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Good contamination analysis but selects Claim File Review; dismisses Cleanroom as "tests pricing elasticity rather than product viability," missing it's the disconfirming commercial test. |
| OUT-09 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Workflow-truth shortcut with framework label references. Picks Claim File Review without addressing renewed-account sampling limitation. |
| OUT-10 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Identifies contamination but selects Claim File Review; treats Cleanroom as merely about willingness to pay rather than the disconfirming test. |
| OUT-11 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contamination via framework labels but selects Claim File Review; dismisses Cleanroom inadequately. |
| OUT-12 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Identifies contamination but workflow-truth shortcut; picks Claim File Review without addressing renewed-account anchoring. |
| OUT-13 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Recognizes contaminated signals but selects Claim File Review, framing Cleanroom merely as pricing test. |
| OUT-14 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Workflow-truth shortcut. Identifies contamination clearly but picks Claim File Review; dismisses Cleanroom as willingness-to-pay test. |
| OUT-15 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Strong contamination analysis and explicitly notes Cleanroom is what's displaced, but still picks Claim File Review. Sacrifices the disconfirming commercial test. |
| OUT-16 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Workflow-truth shortcut. Names contamination well but selects Claim File Review and characterizes Cleanroom as merely willingness-to-pay. |
| OUT-17 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Identifies entangled signals but selects Claim File Review without addressing that it cannot disconfirm commercial attribution. |
| OUT-18 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Notes displacement of Cleanroom and what is given up, but still picks Claim File Review. Misses that Cleanroom is the disconfirming commercial test. |
| OUT-19 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Workflow-truth shortcut. Contamination recognized but Claim File Review chosen over the disconfirming commercial test. |
| OUT-20 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Identifies contamination but workflow-truth shortcut to Claim File Review. |
| OUT-21 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Strong contamination diagnosis with displacement analysis but still picks Claim File Review, treating Cleanroom as merely sales experiment. |
| OUT-22 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Identifies contamination but picks Claim File Review; brief reasoning, doesn't acknowledge renewed-account limitation. |
| OUT-23 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Workflow-truth shortcut. Notes pricing/roadmap/manager contamination but picks Claim File Review. |
| OUT-24 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Heavy framework label usage but applies to facts. Picks Claim File Review over disconfirming commercial test. |
| OUT-25 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Identifies contamination but workflow-truth shortcut; characterizes Cleanroom narrowly. |
| OUT-26 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Recognizes false-positive contamination but selects Claim File Review without addressing its sampling limitation. |
| OUT-27 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Framework-label heavy but applied. Picks Claim File Review; mind-change pivot to Cleanroom suggests partial recognition but recommendation still wrong. |
| OUT-28 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names halo effect and contamination but workflow-truth shortcut to Claim File Review. |
| OUT-29 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Strong contamination diagnosis via framework labels applied to facts, but picks Claim File Review over the disconfirming commercial test. |
| OUT-30 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Identifies performance-aware attribution and contamination but picks Claim File Review. |
| OUT-31 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Workflow-truth shortcut with strong contamination analysis but still picks Claim File Review. |
| OUT-32 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Discusses displacement and tradeoffs well, picks Claim File Review modified; treats Cleanroom narrowly as sales experiment rather than disconfirming test. |
| OUT-33 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Identifies contamination but workflow-truth shortcut to Claim File Review. |
| OUT-34 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Brief but identifies contamination; picks Claim File Review without addressing renewed-account sampling. |
| OUT-35 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Strong contamination and tradeoff discussion but still picks Claim File Review over the disconfirming commercial test. |
| OUT-36 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names halo effect and contamination but workflow-truth shortcut. |
| OUT-37 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Brief; identifies contamination and partially recognizes commercial risk but still picks Claim File Review. |
| OUT-38 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Identifies contamination clearly but selects Claim File Review and dismisses Cleanroom as merely sales tactics. |
| OUT-39 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Brief contamination identification, workflow-truth shortcut to Claim File Review. |
| OUT-40 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Recognizes false-positive and contamination but selects Claim File Review. |
| OUT-41 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Framework label heavy but applied to facts. Picks Claim File Review over disconfirming commercial test. |
| OUT-42 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Discusses displacement explicitly but selects Claim File Review; dismisses Cleanroom as "dangerous gamble," missing it's the disconfirming test. |
| OUT-43 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Identifies contamination but workflow-truth shortcut; treats Cleanroom as merely revenue/pricing test. |
| OUT-44 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Strong contamination analysis but picks Claim File Review; mind-change criterion partially acknowledges Cleanroom value. |
| OUT-45 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Identifies contamination but workflow-truth shortcut to Claim File Review. |
| OUT-46 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names noise types well but workflow-truth shortcut; dismisses Cleanroom as merely pricing positioning. |
| OUT-47 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Identifies contamination but selects Claim File Review and frames Cleanroom narrowly. |
| OUT-48 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Strong contamination diagnosis but workflow-truth shortcut to Claim File Review; misses that Cleanroom is the disconfirming commercial test. ``` |

Score distribution across the 48 blinded answers: {'3': 48}.
This distribution is over OUT-NN labels only; it is not a per-condition
aggregate, and no OUT-NN to condition mapping is recorded here.

## What this receipt is not

This is one blind judge receipt. It is not an eval Result, not a condition
reconciliation, and not a promotion. Reconciliation and any do-not-promote or
benchmark-supported decision are separate later steps.

A model output and a judge score are test artifacts, never authorities.
