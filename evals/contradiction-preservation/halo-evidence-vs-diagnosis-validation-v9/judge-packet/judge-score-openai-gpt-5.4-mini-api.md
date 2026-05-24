---
case_id: halo-evidence-vs-diagnosis-validation-v9
benchmark_version: halo-evidence-vs-diagnosis-validation-v9-v1
artifact: judge-score
judge_model_id: gpt-5.4-mini
judge_model_snapshot: gpt-5.4-mini-2026-03-17
judge_model_family: GPT-5 (OpenAI)
judge_provider: OpenAI API
judge_runtime: OpenAI API via Codex local-only script using operator-provided API key
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

# OpenAI API Blind Judge Score - gpt-5.4-mini

This is a condition-blind judge receipt for `halo-evidence-vs-diagnosis-validation-v9`, benchmark
version `halo-evidence-vs-diagnosis-validation-v9-v1`. It records C1-C6 scores only. It is not a Result
lift, not a condition reconciliation, and not benchmark promotion.

## Judge identity and independence

- Judge model: `gpt-5.4-mini` (`gpt-5.4-mini-2026-03-17`), GPT-5 (OpenAI).
- Provider / runtime: OpenAI API via Codex local-only script using operator-provided API key.
- API settings: reasoning effort medium, text verbosity medium, text format text, store true.
- Response IDs: calibration `resp_0d507ad003a97bd4006a132890739081a19108fac9ee48d8f7`, scoring `resp_08b86a87331d187e006a133795cf8c8195a7ee4b8cf795116f`.
- Input hashes: calibration packet sha256 `d5bf3a2c7a97462e9669310bc1a9313d20d219c88fa96c849678faaa1aa9a469`, scoring packet sha256 `b5f396fcc200526ee234f828e8f0669f5d8328b54c3f6048252fddcad145b514`.
- Raw output hashes: calibration response sha256 `5678adbb1dae9b737208d3eba97a4b009a073c37ab2e5dcd5a7d9fbfa7d144db`, scoring response sha256 `51a8872a86be4b73279fbddb55c16138f5ffc3445d588f383084d1c033f731a8`. Raw transcripts remain local-only and are not committed.
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
| OUT-01 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It clearly recognizes the false-positive / evidence-quality problem and cites contaminated signals like bundle pricing, roadmap-pitch praise, manager-led usage, and support retagging. But it recommends Claim File Review rather than the Commercial Cleanroom disconfirming commercial test, so C4 and downstream criteria fail. |
| OUT-02 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It separates value signals from contaminated ones, naming bundle-priced expansion, roadmap-shaped feedback, and manager audits as non-independent evidence. The recommendation is still Claim File Review, not the Commercial Cleanroom that would actually test the board’s attribution question. |
| OUT-03 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It does a good job identifying performance-aware attribution, manager-run usage, and support retagging as biased signals. However, it chooses the product-diagnostic file review instead of the commercial disconfirmation test, so the ladder stops at C4. |
| OUT-04 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly frames the quarter as a mirage built on pricing bundles, manager audits, and explainability problems. But it still selects Claim File Review, so it never makes the Commercial Cleanroom the decisive evidence standard. |
| OUT-05 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It distinguishes the contaminated growth story from actual product utility and cites several concrete case facts. Still, it recommends the wrong package under this rubric, so C4 fails and C5/C6 cannot pass. |
| OUT-06 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It names the key confounds well: temporary pricing incentives, manager audits, adjuster abandonment, and health-liability explainability. But because it lands on Claim File Review rather than the Commercial Cleanroom, the commercial attribution question remains untested. |
| OUT-07 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It recognizes that the reported growth is distorted by bundle pricing and manager-led activity, with clear case-specific details. The answer still stops at a workflow audit instead of the disconfirming commercial cleanroom, so downstream criteria fail. |
| OUT-08 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It separates pricing-driven bookings, roadmap-elicited sentiment, and manager reruns from true product utility. But it picks Claim File Review, which diagnoses utility without isolating the discount/roadmap confounds the board must resolve. |
| OUT-09 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It cleanly identifies contaminated leadership praise, misclassified support data, and manager-driven usage. The recommendation remains the file review, so it does not select the Commercial Cleanroom as the disconfirming test. |
| OUT-10 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It uses the case facts discriminately and distinguishes product utility from sales optics, with a clear strongest reason against. But the chosen package is still Claim File Review, so the commercial attribution uncertainty is left unresolved. |
| OUT-11 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies several contaminated signals, including bundle pricing, roadmap pitching, manager-driven usage, and retagged support. Yet it does not make the Commercial Cleanroom the recommendation, so C4 and the dependent criteria fail. |
| OUT-12 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly notes the false-positive pattern and the product-versus-buyer uncertainty. Still, it recommends the Claim File Review instead of the cleanroom that would test whether the success story survives normal commercial conditions. |
| OUT-13 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It distinguishes contaminated commercial signals from actual user utility and uses multiple case facts well. But the answer remains anchored on Claim File Review, not the board-relevant commercial disconfirmation test. |
| OUT-14 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It recognizes the pricing bundle, roadmap promises, manager audits, and explainability gap as distinct confounds. The answer still chooses Claim File Review, so it fails the criterion that requires the Commercial Cleanroom. |
| OUT-15 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It clearly identifies the evidence contamination, including bundle pricing, roadmap promises, manager audits, and health-liability abandonment. But it recommends file review rather than the cleanroom that would directly test willingness to expand without those confounds. |
| OUT-16 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It weighs the twelve-day budget window and explains what would be lost by choosing a slower diagnostic test. However, because it still selects Claim File Review, it does not satisfy the criterion for the disconfirming commercial test. |
| OUT-17 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly contrasts usage volume with actual workflow value and points to the explainability gap. But the recommendation is still a product diagnostic, so it does not isolate the commercial attribution question. |
| OUT-18 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It clearly spots contaminated bookings, manager use, and regulated-segment abandonment, and it explains the tradeoff. The choice is still Claim File Review rather than Commercial Cleanroom, so the rubric’s key commercial criterion is not met. |
| OUT-19 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies bundle pricing, managerial vanity use, and the black-box problem with the product. Still, it stops at product auditing, so it doesn’t make the board’s commercial confound the explicit test. |
| OUT-20 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It cleanly separates buyer enthusiasm from user utility and notes the twelve-day constraint. But because the recommendation is Claim File Review, it never chooses the commercial disconfirmation package. |
| OUT-21 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly treats bookings, roadmap promises, and manager usage as contaminated signals and weighs the risks under the time window. The answer still recommends Claim File Review, so C4 fails. |
| OUT-22 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies the entangled bookings, manager auditing, invisible churn, and explainability gap with good specificity. But it does not pick the Commercial Cleanroom, so it cannot satisfy the disconfirming-evidence criterion. |
| OUT-23 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It distinguishes pricing incentives, roadmap-prompted praise, and manager auditing from genuine product value. Nonetheless, it recommends the file review, which is product diagnosis rather than the commercial attribution test the rubric asks for. |
| OUT-24 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly names performance-aware attribution, broad activity metrics, and the load-bearing diagnosis problem. But the answer still chooses Claim File Review, so the commercial disconfirmation standard is not met. |
| OUT-25 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It uses several concrete case facts well, including bundle pricing, manager use, health-liability justification gaps, and the time limit. However, it still settles on Claim File Review rather than the cleanroom that would falsify the success story. |
| OUT-26 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It cleanly identifies the false-positive pattern, manager audits, and regulated-segment failure. But because it chooses Claim File Review, it does not select the board’s key commercial test. |
| OUT-27 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It clearly distinguishes commercial pressure from product utility and explains what the different tests would learn. Still, the recommendation is not the Commercial Cleanroom, so the rubric’s load-bearing criterion fails. |
| OUT-28 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It separates perceived value from actual utility using multiple concrete case facts. But it chooses the file review, which diagnoses product truth without removing the discount and roadmap confounds. |
| OUT-29 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It lays out the contaminated leadership narrative, activity metrics, and pricing distortions very well. Yet it still recommends Claim File Review instead of the commercial test that could disconfirm the growth story. |
| OUT-30 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It explicitly calls out performance-aware attribution, bundle pricing, and manager-driven usage as independent confounds. But the recommended action is still product diagnosis, not the Commercial Cleanroom that would answer the budget question. |
| OUT-31 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies the false-positive pattern and the value gap between buyers and users. The answer remains on Claim File Review, so it does not select the disconfirming commercial package. |
| OUT-32 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It gives a detailed, fact-based explanation of the contaminated signals and tradeoffs. But it still lands on Claim File Review, so it fails the rubric’s commercial-attribution requirement. |
| OUT-33 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It clearly distinguishes bundle pricing, manager audits, and explainability failures from real utility. However, the chosen package is still the file review, not the Commercial Cleanroom. |
| OUT-34 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It recognizes the contaminated revenue and usage proxies and uses the twelve-day window appropriately. Still, it recommends Claim File Review rather than the commercial disconfirmation test. |
| OUT-35 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies lagging indicators, vanity usage, and the health-liability explainability problem with good specificity. But because it chooses Claim File Review, it does not satisfy the key criterion requiring the Commercial Cleanroom. |
| OUT-36 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It separates halo effects, manager audits, and the explainability failure from real value very well. The recommendation remains a diagnostic file audit, so the disconfirming commercial test is not selected. |
| OUT-37 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It clearly names the contaminated signals and explains the tradeoff between product usefulness and marketability. But it still chooses Claim File Review, which leaves the board’s commercial uncertainty untested. |
| OUT-38 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It discriminates well between pricing incentives, roadmap praise, and reporting artifacts versus actual utility. Still, the answer is not the Commercial Cleanroom, so C4 and the dependent criteria fail. |
| OUT-39 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies the noisy financials, manager audits, and health-liability abandonment cleanly. But it recommends the claim-file audit rather than the disconfirming commercial experiment. |
| OUT-40 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It clearly frames the false-positive signal and the need to understand ground truth. However, it still picks Claim File Review, so it does not meet the criterion for the commercial cleanroom test. |
| OUT-41 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It uses the case facts discriminately and names the load-bearing diagnosis problem well. But the recommendation is still the file review, not the Commercial Cleanroom that the rubric treats as decisive. |
| OUT-42 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It clearly explains the buyer-user gap, the contaminated growth signals, and the twelve-day tradeoff. The answer nonetheless recommends Claim File Review, so it fails the commercial disconfirmation criterion. |
| OUT-43 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies incentive misalignment, survivor bias, and the explainability failure with solid case grounding. But it stays with the file review instead of selecting the Commercial Cleanroom. |
| OUT-44 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It cleanly identifies the contaminated positives, silent churn, and the limitation of the usage sprint. Still, the chosen package is Claim File Review, so the key commercial test is not selected. |
| OUT-45 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It nicely distinguishes usage, willingness-to-pay, and the explainability gap while handling the board timing tradeoff. But it recommends Claim File Review rather than the Commercial Cleanroom. |
| OUT-46 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies financial noise, behavioral noise, and operational noise with good specificity. However, because it still selects the file review, it does not satisfy the rubric’s disconfirming commercial standard. |
| OUT-47 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It distinguishes pricing incentives, roadmap promises, and manager audits from actual utility and explains the tradeoff clearly. But the recommendation is still Claim File Review, so C4 and everything downstream fail. |
| OUT-48 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It strongly identifies the contaminated growth story, manager usage, support-tag migration, and the explainability gap. Still, it recommends the file review instead of the Commercial Cleanroom, so the load-bearing commercial criterion is not met. |

Score distribution across the 48 blinded answers: {'3': 48}.
This distribution is over OUT-NN labels only; it is not a per-condition
aggregate, and no OUT-NN to condition mapping is recorded here.

## What this receipt is not

This is one blind judge receipt. It is not an eval Result, not a condition
reconciliation, and not a promotion. Reconciliation and any do-not-promote or
benchmark-supported decision are separate later steps.

A model output and a judge score are test artifacts, never authorities.
