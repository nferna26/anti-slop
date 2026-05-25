---
case_id: halo-evidence-vs-diagnosis-validation-v11
benchmark_version: halo-evidence-vs-diagnosis-validation-v11-v1
artifact: judge-score
judge_model_id: gpt-5.4
judge_model_snapshot: gpt-5.4-2026-03-05
judge_model_family: GPT-5 (OpenAI)
judge_provider: OpenAI API
judge_runtime: OpenAI API via Codex local-only script using operator-provided API key
generator_model_id: gemma-4-31b-it-mlx:2
judge_status: eligible blind judge pass - calibration passed; operator route acceptance recorded
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated pre-registered judge route; passed v11 smoke-2 before generation
calibration_result: passed - 0 C4-C6 eligibility differences, 2 C1/C2/C3 differences, no dependency or total mismatch
outputs_scored: 48
judge_date: 2026-05-24
condition_blinded: true
result_status: partial
note: Pre-registered blind judge route judged the v11 anonymised OUT-NN answers. No OUT-NN to condition mapping.
---

# OpenAI API Blind Judge Score - gpt-5.4

This is a condition-blind judge receipt for `halo-evidence-vs-diagnosis-validation-v11`, benchmark
version `halo-evidence-vs-diagnosis-validation-v11-v1`. It records C1-C6 scores only. It is not a Result
lift, not a condition reconciliation, and not benchmark promotion.

## Judge identity and independence

- Judge model: `gpt-5.4` (`gpt-5.4-2026-03-05`), GPT-5 (OpenAI).
- Provider / runtime: OpenAI API via Codex local-only script using operator-provided API key.
- API settings: reasoning effort medium, text verbosity medium, text format text, store true.
- Response IDs: calibration `resp_00079ca2604d5b14006a13630baad8819fac390733fcbc0ffb`, scoring `resp_0a26d99b4231eef1006a136c6779c881a1b3ee2dfdedf6971e`.
- Input hashes: calibration packet sha256 `a88d2e4f115a8284ba398dacacd84e2c5a312f3abff6383eee81c7af6e2a63c9`, scoring packet sha256 `111ef33c2a4860fea909f9aac347fe5f27d1b89e25e11fc91c241313907cc487`.
- Raw output hashes: calibration response sha256 `55fa54e02d346d36c53c8d54b0a1ad58bbe8a474bc6c4ac0496f335cbddbabaa`, scoring response sha256 `c56cfb963a91929e83187cebbd4341a7f0f614fb08c706dc45a77a1e289a1175`. Raw transcripts remain local-only and are not committed.
- Judge route is pre-registered before generation. Hosted API judge calls are real external API runs; the local backstop is a real local non-generator model run. Neither is a simulated output or an in-session self-score.
- Route eligibility: the v11 run packet named hosted OpenAI, hosted Anthropic, and local gpt-oss backstop routes before generation. The OpenAI and Anthropic routes passed the `smoke-2` C4-C6 calibration gate before any v11 output generation. This receipt records the agent-operated route honestly.
- Condition-blind: the judge received only the independent calibration packet and, after calibration passed, the independent scoring packet. It did not receive model-outputs/, the local-only answer key, Surface 2 reference verdicts before calibration, or condition labels.

## Calibration

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-C] C1=PASS C2=FAIL C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=3
[ANCHOR-D] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-E] C1=PASS C2=FAIL C3=PASS C4=PASS C5=FAIL C6=FAIL TOTAL=3
[ANCHOR-F] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
[ANCHOR-G] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-H] C1=FAIL C2=FAIL C3=FAIL C4=FAIL C5=FAIL C6=FAIL TOTAL=0
```

Against the withheld reference: 2 total recorded differences;
C4-C6 eligibility differences: 0; C1/C2/C3 differences: 2; dependency violations: 0; total mismatches: 0. Calibration
eligibility: `True` under `C4-C6 exact on anchors A-G; C1/C2/C3 non-promotional; H illustrative-only`.

## Method

Each OUT-NN was scored against the six frozen criteria C1-C6 in the rubric, with
the dependency rule applied. Parsed rows were checked for dependency-rule
violations and TOTAL arithmetic. No arithmetic total normalization was needed.

## Score sheet

| Output | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
|---|---|---|---|---|---|---|---|---|
| OUT-01 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly treats the quarter as contaminated and cites concrete confounds like bundle pricing, roadmap-pitched praise, and manager-driven usage. But it chooses the Claim File Review as the main decision package, so it misses that the board’s budget question is commercial attribution under normal conditions; C5 and C6 therefore fail by dependency. |
| OUT-02 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer distinguishes noisy commercial and usage signals with multiple specific case facts and a clear downside to its own choice. It still selects the Claim File Review as sufficient validation, which does not disconfirm the discount-and-roadmap-framed revenue story; C5 and C6 fail by dependency. |
| OUT-03 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | This picks the Commercial Cleanroom and explicitly ties it to removing bundle pricing and roadmap framing, while explaining why Sprint/File Review do not answer the board’s attribution question. It also names the sacrificed short-term revenue optics, a concrete failure path, and observable evidence that would shift the recommendation. |
| OUT-04 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | It correctly identifies contaminated signals and selects the Commercial Cleanroom as the only disconfirming commercial test. However, it does not adequately weigh intervention boundaries for rejected packages under the twelve-day window, so C5 fails, and C6 fails by dependency. |
| OUT-05 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer is strong on contaminated evidence recognition and uses several concrete scenario facts, including a real downside to the File Review. But it treats product-ground-truth as the decisive test instead of isolating whether demand survives without discount and roadmap framing, so C4 fails and the ladder collapses. |
| OUT-06 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies multiple specific confounds by mechanism, including bundle pricing, manager-only usage, and support retagging. Still, it recommends the Claim File Review rather than the Commercial Cleanroom, so it does not select the required disconfirming commercial evidence standard. |
| OUT-07 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The response preserves the core evidence-quality tension and cites concrete contaminated signals from finance, sales, usage, and support. It fails the load-bearing criterion by choosing the Claim File Review as the main validation package instead of the Cleanroom. |
| OUT-08 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It discriminates well among distorted indicators and gives a concrete drawback to its recommendation. But it makes the workflow-truth shortcut by choosing the Claim File Review as sufficient for the board decision, leaving commercial attribution unresolved. |
| OUT-09 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | This answer clearly rejects contaminated signals like bundle-driven expansion, roadmap-primed comments, and manager-led usage. It still selects the Claim File Review rather than the Commercial Cleanroom, so it fails to test whether the success story survives normal commercial conditions. |
| OUT-10 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It correctly frames the issue as whether current success survives removal of pricing and pitch confounds, and it selects the Commercial Cleanroom on that basis. It also names the short-term revenue/political cost, contrasts Cleanroom with usage/file reviews, and gives observable evidence that would change the call. |
| OUT-11 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | This is a strong answer: it isolates bundle pricing and roadmap framing as the critical confounds and explains why Sprint/File Review answer different questions. It also states what is displaced, what is forfeited, the strongest reason against, and a concrete behavioral falsifier. |
| OUT-12 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer handles contaminated evidence well and uses several case facts, including the board-window downside to its choice. But it chooses the Claim File Review as the main package, which does not answer whether buyers still expand absent discount and roadmap framing. |
| OUT-13 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It properly calls out bundle-price revenue, roadmap-biased praise, and manager-generated usage as non-independent signals. The failure is selecting the Claim File Review as decisive validation rather than the Commercial Cleanroom as the disconfirming commercial test. |
| OUT-14 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | This response recognizes contaminated evidence and distinguishes between surface usage and actual work product. But it still recommends the Claim File Review, so it misses the board’s key attribution question and fails C4, with C5/C6 failing by dependency. |
| OUT-15 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It gives a coherent evidence-quality critique with concrete facts and a real tradeoff. However, it prioritizes user-level diagnosis over the required commercial disconfirmation test, so it fails C4. |
| OUT-16 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer correctly recommends the Commercial Cleanroom and explains that it alone removes bundle-pricing and roadmap-pitch confounds. It also states what is displaced, what short-term revenue is forfeited, and what observable front-line adoption evidence would overturn the recommendation. |
| OUT-17 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It accurately identifies specific contaminated signals and the mismatch between manager behavior and adjuster behavior. But it makes the workflow-truth shortcut by elevating the Claim File Review over the Commercial Cleanroom for the board decision. |
| OUT-18 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer uses many concrete case facts and clearly rejects several contaminated metrics. Its core miss is choosing the Claim File Review as the primary package, which cannot disconfirm the discount-and-roadmap-driven revenue narrative. |
| OUT-19 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It frames the issue as false positives and cites multiple confounded signals by mechanism. But it still treats user-level file truth as the decisive test, so it fails to select the Cleanroom as the board-relevant disconfirming evidence standard. |
| OUT-20 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The response discriminates well among contaminated commercial, usage, and support signals and gives a concrete downside to the recommendation. It nonetheless chooses the Claim File Review, leaving the main commercial attribution uncertainty unresolved. |
| OUT-21 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It recognizes that the current story may be a false positive and names specific confounds like bundling, manager audits, and ticket recategorization. But recommending the Claim File Review instead of the Commercial Cleanroom fails C4. |
| OUT-22 | PASS | FAIL | PASS | FAIL | FAIL | FAIL | 2 | It does identify specific contamination mechanisms, but it invents a material cash-runway condition not in the case, which breaks C2’s fact-discipline requirement. It also recommends the Claim File Review rather than the Cleanroom, so the intervention ladder fails. |
| OUT-23 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | This answer selects the Commercial Cleanroom for the right reason: it directly tests whether demand survives removal of bundle pricing and roadmap framing. It also acknowledges the main downside—deferring product-debugging detail—and gives concrete evidence that would switch priority to the Claim File Review. |
| OUT-24 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly distinguishes contaminated success signals from genuine workflow evidence and includes a concrete downside to its choice. But it still chooses the Claim File Review as sufficient validation, which does not answer the board’s commercial attribution question. |
| OUT-25 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The response handles the evidence contamination well and uses concrete case facts against its own recommendation. Its main error is preferring the Claim File Review over the Commercial Cleanroom for a one-package budget decision. |
| OUT-26 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It discriminates among revenue, usage, and segment signals and notes what is given up by not scaling. Still, it chooses the Claim File Review instead of the Commercial Cleanroom, so it does not isolate whether the growth story survives without the commercial confounds. |
| OUT-27 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer rightly treats pricing bundles and manager-driven usage as confounded signals and offers a real downside to its choice. But it falls into the workflow-truth shortcut by choosing the Claim File Review as the main validation package. |
| OUT-28 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies several contaminated signals and articulates a concrete risk of its own recommendation under the time window. However, it recommends the Claim File Review rather than the Cleanroom, so it misses the board’s key disconfirming test. |
| OUT-29 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | It correctly chooses the Commercial Cleanroom and ties it to removing bundle-price and roadmap-promise distortions. But it does not sufficiently analyze intervention boundaries for rejected packages under the twelve-day decision window, so C5 fails and C6 fails by dependency. |
| OUT-30 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | This is a complete answer: it selects the Commercial Cleanroom as the only test that can make the success story wrong, not just monitor it. It also explains what scaling would hide, what Cleanroom sacrifices, and gives a concrete condition that would redirect toward product diagnosis. |
| OUT-31 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The response carefully separates bookings, roadmap talk, manager usage, and health-liability explainability as different kinds of evidence. But it still chooses the Claim File Review instead of the Commercial Cleanroom, so it fails the central intervention criterion. |
| OUT-32 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It correctly identifies the board’s question as commercial validity under stripped-away discounts and roadmap framing, and it recommends the Commercial Cleanroom accordingly. It also weighs what is sacrificed, contrasts with Claim File Review evidence, and names observable adoption evidence that would change the recommendation. |
| OUT-33 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | The answer distinguishes contaminated success signals from validated commercial learning and selects the Commercial Cleanroom for the right reason. It also addresses the near-term revenue cost, contrasts with product-diagnostic evidence, and supplies a concrete behavioral falsifier. |
| OUT-34 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | It picks the Commercial Cleanroom and correctly centers the pricing-and-roadmap confounds. But the boundary analysis is too thin about what rejected packages learn or hide in the twelve-day window, so C5 fails and C6 cannot pass. |
| OUT-35 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It strongly rejects contaminated commercial and usage evidence and names multiple specific case facts. The decisive miss is recommending the Claim File Review as the main answer, which does not isolate whether demand survives without sales incentives and roadmap framing. |
| OUT-36 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | This preserves the core tension and discriminates among several contaminated signals, including bundle pricing and manager audit usage. But it still treats the Claim File Review as sufficient validation, so it fails C4 and therefore the dependency ladder. |
| OUT-37 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer uses concrete scenario facts well and sees the difference between buyer/manager enthusiasm and practitioner abandonment. It nonetheless chooses the Claim File Review instead of the Commercial Cleanroom, which is the wrong intervention standard for the board decision. |
| OUT-38 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies multiple confounds and a clear downside to its own recommendation. But it picks the Claim File Review as the key package, leaving the central commercial attribution question untested. |
| OUT-39 | PASS | FAIL | PASS | PASS | FAIL | FAIL | 3 | It chooses the Commercial Cleanroom for the right core reason and identifies key confounds. Still, it is too sparse and under-factored for C2, and it does not adequately weigh what rejected packages learn or hide under the budget window, so C5 fails and C6 fails by dependency. |
| OUT-40 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes that the issue is contaminated evidence and uses many concrete case facts, including a fact against its own recommendation. But it recommends the Claim File Review instead of the Commercial Cleanroom, so it misses the disconfirming commercial test the board needs. |
| OUT-41 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly spots the difference between buyer-level enthusiasm and front-line user abandonment, and it names several contamination mechanisms. The failure is selecting the Claim File Review rather than the Commercial Cleanroom as the one package to commit to. |
| OUT-42 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | This answer preserves the main tension and cites multiple specific confounds, plus a real board-timing downside. But it still makes the workflow-diagnostic shortcut by choosing the Claim File Review over the Commercial Cleanroom. |
| OUT-43 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It does a good job identifying contaminated commercial and usage signals and gives a concrete reason against its own choice. However, it recommends the Claim File Review as decisive validation, which does not answer whether the revenue story holds under normal commercial conditions. |
| OUT-44 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The response clearly separates contaminated signals from workflow evidence and weighs several options. It still chooses the Claim File Review instead of the Commercial Cleanroom, so it fails the load-bearing C4 criterion. |
| OUT-45 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It cites multiple concrete case facts and explicitly rejects bookings and usage volume as clean proof. But it treats the Claim File Review as the primary answer rather than the Commercial Cleanroom, so it does not isolate the board’s key uncertainty. |
| OUT-46 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer properly recognizes several contamination mechanisms and gives a concrete downside under the twelve-day board window. Its core miss is recommending the Claim File Review instead of the Commercial Cleanroom as the required disconfirming test. |
| OUT-47 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly flags bundle pricing, manager-only usage, support retagging, and explainability as non-independent or misleading evidence. But it makes the product-diagnostic shortcut by choosing the Claim File Review over the Commercial Cleanroom. |
| OUT-48 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | This answer preserves the core evidence-quality tension and uses several concrete facts, including a board-window downside. It still recommends the Claim File Review, so it does not select the only package that directly tests whether expansion demand survives without discount and roadmap framing. |

Score distribution across the 48 blinded answers: {'2': 1, '3': 36, '4': 3, '6': 8}.
This distribution is over OUT-NN labels only; it is not a per-condition
aggregate, and no OUT-NN to condition mapping is recorded here.

## What this receipt is not

This is one blind judge receipt. It is not an eval Result, not a condition
reconciliation, and not a promotion. Reconciliation and any do-not-promote or
benchmark-supported decision are separate later steps.

A model output and a judge score are test artifacts, never authorities.
