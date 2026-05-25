---
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
artifact: judge-score
judge_model_id: claude-opus-4-7
judge_model_snapshot: claude-opus-4-7
judge_model_family: Claude Opus (Anthropic)
judge_provider: Anthropic API
judge_runtime: Anthropic API via Codex local-only script using operator-provided API key
generator_model_id: gemma-4-31b-it-mlx:2
judge_status: eligible blind judge pass - calibration passed; operator route acceptance recorded
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated pre-registered judge route; passed v12 calibration and disagreement smoke before generation
calibration_result: passed - 0 C4-C6 eligibility differences, 0 C1/C2/C3 differences, no dependency or total mismatch
outputs_scored: 48
judge_date: 2026-05-24
condition_blinded: true
result_status: partial
note: Pre-registered blind judge route judged the v12 anonymised OUT-NN answers. No OUT-NN to condition mapping.
---

# Anthropic API Blind Judge Score - claude-opus-4-7

This is a condition-blind judge receipt for `halo-evidence-vs-diagnosis-validation-v12`, benchmark
version `halo-evidence-vs-diagnosis-validation-v12-v1`. It records C1-C6 scores only. It is not a Result
lift, not a condition reconciliation, and not benchmark promotion.

## Judge identity and independence

- Judge model: `claude-opus-4-7` (`claude-opus-4-7`), Claude Opus (Anthropic).
- Provider / runtime: Anthropic API via Codex local-only script using operator-provided API key.
- API settings: no explicit temperature parameter; max_tokens 2000 calibration / 12000 scoring.
- Response IDs: calibration `msg_012Qee7AuTqj22DPFKoJWA5r`, scoring `msg_01Xwb1bWj6mkQSscVuuDu6bc`.
- Input hashes: calibration packet sha256 `f310feb5b1cb828662b9f7d73591a906de6152e411f11bcd43cec3b761c1f523`, scoring packet sha256 `d78d2d3cd39d4e1efefdae387b133baeedb80eef904397d6694cc0124f16ace3`.
- Raw output hashes: calibration response sha256 `6ca68ca05ef79e38ed19201ba47b8b0c8ccd920d00fae5ba7db47c7e4e093978`, scoring response sha256 `fe04636e1e18675ea08a2ec5bec0e45f02fe60d1ee62aea345d44ad8b749efb6`. Raw transcripts remain local-only and are not committed.
- API usage for scoring: input tokens `51206`, output tokens `4244`.
- Judge route is pre-registered before generation. Hosted API judge calls are real external API runs; the local backstop is a real local non-generator model run. Neither is a simulated output or an in-session self-score.
- Route eligibility: the v12 run packet named hosted OpenAI, hosted Anthropic, and local gpt-oss backstop routes before generation. All three routes passed the C4-C6 calibration gate and judge-disagreement smoke before any v12 output generation. This receipt records the agent-operated route honestly.
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
```

Against the withheld reference: 0 total recorded differences;
C4-C6 eligibility differences: 0; C1/C2/C3 differences: 0; dependency violations: 0; total mismatches: 0. Calibration
eligibility: `True` under `C4-C6 exact on anchors A-G; C1/C2/C3 non-promotional; H illustrative-only; judge totals optional and parser-computed`.

## Method

Each OUT-NN was scored against the six frozen criteria C1-C6 in the rubric, with
the dependency rule applied. Parsed rows were checked for dependency-rule
violations and TOTAL arithmetic. No arithmetic total normalization was needed.

## Score sheet

| Output | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
|---|---|---|---|---|---|---|---|---|
| OUT-01 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Picks Case Evidence Review and explicitly dismisses Demand Cleanroom as already-answered; this is the workflow-truth shortcut. C5 fails by dependency; C6's change-my-mind is plausible but C5/C4 gate. |
| OUT-02 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Chooses Case Evidence Review; treats it as the disconfirming test rather than recognizing Demand Cleanroom isolates the commercial confounds. Fails C4 and dependent criteria. |
| OUT-03 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Selects Demand Cleanroom, ties it to removing bundle pricing and roadmap framing, names the short-term revenue risk and a concrete behavioral falsifier. |
| OUT-04 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Workflow-truth shortcut; dismisses Cleanroom as testing only sellability. Fails C4 and dependents. |
| OUT-05 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Picks Case Evidence Review without recognizing it cannot disconfirm the commercial attribution. Fails C4. |
| OUT-06 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review chosen; treats Cleanroom as pricing-only. Fails C4 and dependents. |
| OUT-07 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review recommendation; misses that it samples already-renewed accounts and cannot test the revenue attribution. Fails C4. |
| OUT-08 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; treats it as causal value test. Fails C4 standard. |
| OUT-09 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Chooses Case Evidence Review and dismisses Cleanroom because renewals are already in hand—exactly the workflow-truth shortcut. Fails C4. |
| OUT-10 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Selects Demand Cleanroom, frames it as the disconfirming test for revenue attribution under contamination, names short-term revenue risk, and gives behavioral falsifier. |
| OUT-11 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; treats Cleanroom as lagging indicator. Fails C4. |
| OUT-12 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Demand Cleanroom selected, explicitly cites bundle and roadmap contamination, notes already-renewed sample bias in Case Evidence Review, names revenue risk and behavioral falsifier. |
| OUT-13 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; misses commercial attribution test. Fails C4. |
| OUT-14 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review with modification; explicitly says Cleanroom is "too late." Fails C4. |
| OUT-15 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review chosen, displacing Cleanroom. Fails C4. |
| OUT-16 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Selects Demand Cleanroom and ties to removing bundle and roadmap framing. C5 weak: doesn't analyze what rejected packages forfeit/hide under the twelve-day window beyond a brief mention. Fails C5. |
| OUT-17 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Demand Cleanroom chosen, names contamination mechanisms, weighs short-term revenue tradeoff against twelve-day window, provides concrete behavioral falsifier. |
| OUT-18 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-19 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-20 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-21 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-22 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-23 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; does note survivorship bias but still selects it as primary test rather than Cleanroom. Fails C4. |
| OUT-24 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-25 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Demand Cleanroom selected, contamination mechanisms identified, twelve-day commercial risk weighed, behavioral falsifier given. |
| OUT-26 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-27 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Demand Cleanroom chosen; explains diagnostic vs commercial attribution distinction, names revenue risk, provides falsifier. |
| OUT-28 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Demand Cleanroom with clear contamination mechanism analysis, twelve-day revenue risk weighed, concrete behavioral falsifier. |
| OUT-29 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-30 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-31 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-32 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-33 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Demand Cleanroom selected with clear contamination analysis, short-term revenue risk acknowledged, behavioral falsifier specified. |
| OUT-34 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-35 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Demand Cleanroom with contamination mechanisms, revenue risk weighed, behavioral falsifier provided. |
| OUT-36 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Demand Cleanroom selected, but C5 analysis of what rejected packages learn/forfeit under twelve-day window is thin—only names short-term risk for chosen path. Fails C5. |
| OUT-37 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-38 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Demand Cleanroom, names contamination mechanisms including manager-rehearsal and support retagging, weighs revenue risk, gives falsifier. |
| OUT-39 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-40 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Demand Cleanroom chosen with clear contamination mechanism, sales-friction risk acknowledged, behavioral falsifier supplied. |
| OUT-41 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-42 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-43 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-44 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Demand Cleanroom selected, contamination mechanisms named, revenue/momentum risk weighed against twelve-day window, behavioral falsifier given. |
| OUT-45 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-46 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Demand Cleanroom chosen; explicitly notes Case Evidence Review can't prove demand without bundle, support-retagging contamination called out, revenue risk weighed, falsifier provided. |
| OUT-47 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Case Evidence Review; fails C4. |
| OUT-48 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Demand Cleanroom selected, contamination mechanisms named, short-term revenue risk weighed, behavioral falsifier specified. ``` |

Score distribution across the 48 blinded answers: {'3': 32, '4': 2, '6': 14}.
This distribution is over OUT-NN labels only; it is not a per-condition
aggregate, and no OUT-NN to condition mapping is recorded here.

## What this receipt is not

This is one blind judge receipt. It is not an eval Result, not a condition
reconciliation, and not a promotion. Reconciliation and any do-not-promote or
benchmark-supported decision are separate later steps.

A model output and a judge score are test artifacts, never authorities.
