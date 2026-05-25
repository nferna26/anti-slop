---
case_id: halo-evidence-vs-diagnosis-validation-v10
benchmark_version: halo-evidence-vs-diagnosis-validation-v10-v1
artifact: judge-score
judge_model_id: gpt-5.4-mini
judge_model_snapshot: gpt-5.4-mini-2026-03-17
judge_model_family: GPT-5 (OpenAI)
judge_provider: OpenAI API
judge_runtime: OpenAI API via Codex local-only script using operator-provided API key
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

# OpenAI API Blind Judge Score - gpt-5.4-mini

This is a condition-blind judge receipt for `halo-evidence-vs-diagnosis-validation-v10`, benchmark
version `halo-evidence-vs-diagnosis-validation-v10-v1`. It records C1-C6 scores only. It is not a Result
lift, not a condition reconciliation, and not benchmark promotion.

## Judge identity and independence

- Judge model: `gpt-5.4-mini` (`gpt-5.4-mini-2026-03-17`), GPT-5 (OpenAI).
- Provider / runtime: OpenAI API via Codex local-only script using operator-provided API key.
- API settings: reasoning effort medium, text verbosity medium, text format text, store true.
- Response IDs: calibration `resp_0bb4755172d3bcb4006a134be3a08881a29d636a4befe24d47`, scoring `resp_006a32e456fc84fe006a1353e3024481979b5c9d8b3cf32e07`.
- Input hashes: calibration packet sha256 `8e782ab143fae035d1fd27b8f698a55ce6445af5fd9c8946474e20389a6135a6`, scoring packet sha256 `07c8adfa59735592ff72eaaa4e8783059edf4af0ecfe152c1c2bc210a41f42d8`.
- Raw output hashes: calibration response sha256 `5678adbb1dae9b737208d3eba97a4b009a073c37ab2e5dcd5a7d9fbfa7d144db`, scoring response sha256 `394be07218e14cdf047f5419279793a483f083dd3674acd6c69f3eecd17fe231`. Raw transcripts remain local-only and are not committed.
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
violations and TOTAL arithmetic. No arithmetic total normalization was needed.

## Score sheet

| Output | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
|---|---|---|---|---|---|---|---|---|
| OUT-01 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly sees the signal contamination and uses several concrete facts, including bundle pricing, roadmap-pitch praise, manager-led samples, and health-liability explainability. But it recommends Claim File Review rather than the Commercial Cleanroom, so it does not choose the board-level disconfirming commercial test. |
| OUT-02 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It distinguishes bundle incentives, manager-run samples, and health-liability explainability gaps from real value, and it names a concrete drawback of the chosen test. But it still picks Claim File Review, which leaves the commercial attribution question unresolved. |
| OUT-03 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It chooses the Commercial Cleanroom and explicitly frames it as the way to remove pricing and roadmap confounds to test whether expansion survives normal conditions. It also contrasts the usage sprint and file review as weaker diagnostics, weighs the twelve-day risk, and gives a behavioral change-my-mind standard. |
| OUT-04 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It uses several case facts and correctly identifies bundle pricing, roadmap praise, and manager-driven usage as contaminated signals. But it recommends Claim File Review, which is diagnostic rather than the commercial disconfirmation test the rubric wants. |
| OUT-05 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It selects the Commercial Cleanroom and ties it to stripping out bundle pricing and roadmap framing to test independent commercial pull. It also states the revenue-speed tradeoff and gives observable evidence that would move the answer. |
| OUT-06 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It recognizes the contaminated booking, usage, and support signals and gives a sensible downside of the chosen test. But the answer still commits to Claim File Review instead of the commercial cleanroom that would actually disconfirm the success story. |
| OUT-07 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies multiple contaminated signals, including bundle pricing, roadmap narratives, and manager audits. But it picks Claim File Review, so it does not select the only package that directly tests whether the growth story survives normal commercial conditions. |
| OUT-08 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It uses many scenario details and correctly calls out pricing and manager-mediated usage contamination. However, it recommends Claim File Review, which is a product diagnostic rather than the board’s commercial attribution test. |
| OUT-09 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It directly names the halo contamination and explains that removing bundle pricing and roadmap hype is the clean test of whether expansion persists. It also weighs the short-term revenue risk and gives a concrete behavioral falsifier. |
| OUT-10 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It recommends the Commercial Cleanroom and clearly treats it as the validated-learning test that strips out bundle pricing and roadmap promises. It also explains the cost of not scaling now and gives specific evidence that would change the recommendation. |
| OUT-11 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It distinguishes usage tracking, claim-file snapshots, and commercial attribution, and selects the Commercial Cleanroom as the only way to isolate standalone value. It also addresses board-timing risk and gives a concrete change-my-mind condition. |
| OUT-12 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It uses the relevant facts well and correctly flags the incentive and behavior contamination. But it recommends Claim File Review, so it never makes the commercial success story itself falsifiable. |
| OUT-13 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It clearly identifies bundle pricing, roadmap promises, manager usage, and explainability failure as distinct signals. But the chosen package is still Claim File Review, not the commercial cleanroom the rubric requires. |
| OUT-14 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It chooses the Commercial Cleanroom and explains that removing bundle-price and roadmap incentives is the way to test if the product has independent value. It also notes the revenue risk and names behavioral evidence that would move it away from cleanroom. |
| OUT-15 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly separates bundle-price distortion, manager-led audits, and health-liability explainability issues. But it still picks Claim File Review, so it does not isolate the commercial attribution problem the board must solve. |
| OUT-16 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It uses the right contaminated facts and even notes the twelve-day constraint. Yet it recommends Claim File Review, which leaves the commercial demand question open. |
| OUT-17 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies the contaminated bookings, manager audits, and explainability gap with good specificity. But Claim File Review is still the wrong package for disconfirming the revenue story. |
| OUT-18 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly contrasts perceived value with actual utility and cites manager reruns plus bundle-driven renewals. But by recommending Claim File Review, it chooses diagnosis over the commercial test the board needs. |
| OUT-19 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies several specific contamination mechanisms, including bundle discounts, roadmap promises, and manager training usage. But it still recommends Claim File Review, so it does not select the disconfirming commercial standard. |
| OUT-20 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It gives a strong account of the contaminated metrics and the explainability risk in regulated segments. But it chooses Claim File Review, which does not answer whether the growth story survives without pricing and roadmap framing. |
| OUT-21 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It cleanly separates bookings, support tags, and manager activity from real utility, and it uses several concrete facts. But the answer still lands on Claim File Review rather than the commercial cleanroom. |
| OUT-22 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It explicitly calls out bundle pricing, roadmap promises, manager audits, and health-liability explainability as contamination. But it chooses Claim File Review, so it remains a product audit instead of a commercial disconfirmation. |
| OUT-23 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It recommends Commercial Cleanroom and clearly states that removing bundle pricing and roadmap pitch isolates the product’s true market pull. It also explains the short-term downside and gives a concrete alternative signal that would change the recommendation. |
| OUT-24 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It uses several case facts and recognizes the bundled renewals, roadmap pitches, and manager-driven usage as confounded. But it selects Claim File Review, which does not directly test whether the commercial story survives normal conditions. |
| OUT-25 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It clearly distinguishes the contaminated revenue story from the underlying product question and cites multiple facts. But it recommends Claim File Review, so it fails the commercial disconfirmation criterion. |
| OUT-26 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly identifies the financial incentives, manager-led samples, and explainability gap. However, Claim File Review is still a diagnosis tool, not the disconfirming commercial test required here. |
| OUT-27 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It names several contaminated signals by mechanism, including bundle pricing, manager audits, and health-liability abandonment. But it recommends Claim File Review, so it does not settle the board’s commercial attribution question. |
| OUT-28 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It distinguishes buyer signals, manager behavior, and commercial testing reasonably well. But because it chooses Claim File Review, it stops at product diagnosis rather than the clean disconfirmation of the revenue story. |
| OUT-29 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It uses the case facts discriminately and correctly identifies bundle pricing, manager audits, and explainability as the real issues. But the recommendation remains Claim File Review instead of Commercial Cleanroom. |
| OUT-30 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It gives a strong signal-versus-noise analysis with several concrete contaminated facts. But it still recommends Claim File Review, which leaves the commercial attribution question unanswered. |
| OUT-31 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It uses multiple concrete facts and gives a solid boundary analysis around the twelve-day window. But Claim File Review is still the wrong package for testing whether the success story survives without price and pitch support. |
| OUT-32 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies the contaminated revenue, usage, and segment-failure signals with good specificity. But by choosing Claim File Review, it does not select the commercial test that can actually falsify the growth story. |
| OUT-33 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It recognizes the bundle-price, manager-enthusiasm, and health-liability issues and gives a plausible downside. But the recommendation is still Claim File Review, not the cleanroom the rubric requires. |
| OUT-34 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It clearly distinguishes buyer signals from user utility and identifies the contaminated evidence mechanisms. Yet it recommends Claim File Review, so it fails the board-level commercial attribution test. |
| OUT-35 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It uses several concrete facts and explains the buyer/user split well. But because it selects Claim File Review, it does not choose the disconfirming commercial package. |
| OUT-36 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It distinguishes bundle incentives, manager audits, and explainability failure from real utility. But it still lands on Claim File Review, which is diagnostic rather than commercial validation. |
| OUT-37 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It makes the tradeoff between lagging commercial indicators and leading user red flags very clear. Still, Claim File Review is the answer, so it does not isolate whether demand survives without bundle pricing and roadmap framing. |
| OUT-38 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It uses concrete facts about bundled renewals, manager audits, and regulated-segment abandonment. But it recommends Claim File Review, not the commercial cleanroom that would disconfirm the growth story. |
| OUT-39 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It clearly rejects the contaminated signals and uses multiple case facts, including bundle pricing, roadmap pitches, and manager reruns. But the answer still chooses Claim File Review, so it does not answer the commercial attribution question. |
| OUT-40 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It recommends the Commercial Cleanroom and explicitly frames it as the validated-learning test that removes the confounding incentives. It also weighs the board-window risk and provides a concrete evidence threshold that would shift the choice. |
| OUT-41 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It sharply distinguishes lagging commercial metrics from leading product failures and uses several concrete contaminated signals. But it recommends Claim File Review, which is not the commercial falsification package. |
| OUT-42 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly identifies the bundle-price, roadmap, manager-audit, and explainability confounds. But Claim File Review is still a product diagnostic, not the board’s commercial disconfirmation test. |
| OUT-43 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It recommends Commercial Cleanroom and clearly explains that removing bundle pricing and roadmap framing is how to test whether growth is real. It also states the short-term revenue sacrifice and gives a concrete alternative signal that would change the decision. |
| OUT-44 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It gives a strong false-positive diagnosis with multiple concrete contaminated signals and a sensible downside. But it still chooses Claim File Review, so it misses the commercial test the board needs. |
| OUT-45 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies the contaminated growth story and explainability failure well. However, it recommends Claim File Review rather than the commercial cleanroom that would directly test whether the success story survives normal conditions. |
| OUT-46 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It selects Commercial Cleanroom and explains that removing bundle pricing and roadmap pitches is the validated-learning test. It also addresses the sales conflict and gives an observable behavioral scenario that would change the recommendation. |
| OUT-47 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It clearly distinguishes sales incentives, superficial usage metrics, and user-level trust failure. But Claim File Review is still the recommendation, so it does not choose the board-level commercial disconfirmation. |
| OUT-48 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It uses several concrete facts to separate contaminated revenue, manager auditing, and user abandonment. But it recommends Claim File Review, which leaves the commercial attribution question unresolved. |

Score distribution across the 48 blinded answers: {'3': 38, '6': 10}.
This distribution is over OUT-NN labels only; it is not a per-condition
aggregate, and no OUT-NN to condition mapping is recorded here.

## What this receipt is not

This is one blind judge receipt. It is not an eval Result, not a condition
reconciliation, and not a promotion. Reconciliation and any do-not-promote or
benchmark-supported decision are separate later steps.

A model output and a judge score are test artifacts, never authorities.
