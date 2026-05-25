---
case_id: halo-evidence-vs-diagnosis-validation-v8
benchmark_version: halo-evidence-vs-diagnosis-validation-v8-v1
artifact: judge-score
judge_model_id: gpt-5.4-mini
judge_model_snapshot: gpt-5.4-mini-2026-03-17
judge_model_family: GPT-5 (OpenAI)
judge_provider: OpenAI API
judge_runtime: OpenAI API via Codex local-only script using operator-provided API key
generator_model_id: gemma4:31b
judge_status: eligible blind judge pass - calibration passed; operator route acceptance recorded
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated pre-registered judge route; passed v8 smoke-2 before generation
calibration_result: passed - 0 C3-C6 eligibility differences, 0 C1/C2 differences, no dependency or total mismatch
outputs_scored: 40
judge_date: 2026-05-24
condition_blinded: true
result_status: partial
note: Pre-registered blind judge route judged the v8 anonymised OUT-NN answers. No OUT-NN to condition mapping.
---

# OpenAI API Blind Judge Score - gpt-5.4-mini

This is a condition-blind judge receipt for `halo-evidence-vs-diagnosis-validation-v8`, benchmark
version `halo-evidence-vs-diagnosis-validation-v8-v1`. It records C1-C6 scores only. It is not a Result
lift, not a condition reconciliation, and not benchmark promotion.

## Judge identity and independence

- Judge model: `gpt-5.4-mini` (`gpt-5.4-mini-2026-03-17`), GPT-5 (OpenAI).
- Provider / runtime: OpenAI API via Codex local-only script using operator-provided API key.
- API settings: reasoning effort medium, text verbosity medium, text format text, store true.
- Response IDs: calibration `resp_09f090887e86bd64006a1267b1805881a0be2fc70aa9fcbe5d`, scoring `resp_033d26ff7ed15b9a006a1281220f648195b15c838c9a94ef2c`.
- Input hashes: calibration packet sha256 `12c5d225c1b66460ffab97a6bc300edfe522982c59cd5dd9c5bbbfda212575bb`, scoring packet sha256 `aab9cdb636d300206cfdbffc26ef8c506b61bf86cb19ec2eae8c0e26bdcba3a2`.
- Raw output hashes: calibration response sha256 `16aedb3d2baaa888e426f9318c691ba37cad56d7bf369dcc24b68f7f1e0a2c71`, scoring response sha256 `a85b4c1d2c7884ab4dfd6b9ab4598c50618fc3a55c563aa5d80beb0d8f8c4283`. Raw transcripts remain local-only and are not committed.
- Judge route is pre-registered before generation. Hosted API judge calls are real external API runs; the local backstop is a real local non-generator model run. Neither is a simulated output or an in-session self-score.
- Route eligibility: the v8 run packet named hosted OpenAI, hosted Anthropic, and local gpt-oss backstop routes before generation. The OpenAI and Anthropic routes passed the `smoke-2` C3-C6 calibration gate before any v8 output generation. This receipt records the agent-operated route honestly.
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
[ANCHOR-H] C1=FAIL C2=FAIL C3=PASS C4=FAIL C5=FAIL C6=FAIL TOTAL=1
```

Against the withheld reference: 1 total recorded differences;
C3-C6 eligibility differences: 0; C1/C2 differences: 0; dependency violations: 0; total mismatches: 0. Calibration
eligibility: `True` under `C3-C6 exact on anchors A-G; C1/C2 non-gating; H illustrative-only`.

## Method

Each OUT-NN was scored against the six frozen criteria C1-C6 in the rubric, with
the dependency rule applied. Parsed rows were checked for dependency-rule
violations and TOTAL arithmetic. No arithmetic total normalization was needed.

## Score sheet

| Output | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
|---|---|---|---|---|---|---|---|---|
| OUT-01 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Recognizes the choice is about separating signal from contaminated growth, not simply “scale or don’t.” It names discount-tied revenue and champion-driven usage as non-independent evidence, gives a segment-level falsifier, and explains the sacrifice of momentum under the twelve-day window. |
| OUT-02 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Clearly rejects the revenue story as independent proof and separates discount-driven growth from end-user adoption. It gives a behavioral test that would shift the recommendation and spells out the board/sales tradeoff. |
| OUT-03 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Uses the case facts well and frames the decision as evidence quality versus scaling. It identifies contaminated growth signals, names a disconfirming cohort test, and states the cost of losing momentum. |
| OUT-04 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Distinguishes the board story from reviewer-level behavior and the insurance segment failure. It explains what the evidence pass learns versus what scaling would prematurely lock in, and gives a concrete adoption-based falsifier. |
| OUT-05 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Separates borrowed revenue, champion usage, and explainability failure from genuine product value. It names the risk of scaling a leaky bucket and gives a concrete behavioral standard that would change the call. |
| OUT-06 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Applies the halo and strategy-kernel ideas directly to the case facts rather than just naming frameworks. It identifies multiple contaminated signals, specifies the control-group test, and explains the board-timing sacrifice. |
| OUT-07 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Cleanly separates discount-fueled revenue and champion usage from end-user value. It weighs the evidence pass against scaling and narrowing, then gives a concrete user-level falsifier tied to the critical uncertainty. |
| OUT-08 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Uses the case facts discriminately and treats the headline numbers as lagging, contaminated signals. It explains what scaling and narrowing would irreversibly commit or leave unresolved, and gives a clear adoption-based change-my-mind condition. |
| OUT-09 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Separates financial engineering, champion behavior, and regulated-segment failure from independent validation. It states what the evidence pass would uncover versus what scaling would hide, and gives an observable cohort test. |
| OUT-10 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Recognizes the core tension is whether the growth is organic or discount-driven. It identifies the contaminated signals, gives a non-discounted adoption falsifier, and explains the momentum cost of pausing. |
| OUT-11 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Applies the halo effect to the leadership adjectives and the revenue bump, not just as a label. It names the contaminated metrics, the right disconfirming test, and the budget-lock tradeoff. |
| OUT-12 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Recognizes the decision is about evidence quality before strategy lock-in. It distinguishes the board narrative from champion behavior and explainability testing, and gives a concrete behavioral shift that would justify scaling. |
| OUT-13 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Uses multiple case facts to show the current story is performance-colored rather than independently validated. It names the contaminated revenue and usage signals, explains the planning-window sacrifice, and gives a clean falsifier. |
| OUT-14 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Separates discount-driven growth, champion-driven usage, and segment-specific explainability failure from real validation. It clearly explains what the evidence pass learns versus what scaling would lock in, and gives an adoption-based trigger to change course. |
| OUT-15 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Treats the revenue bump as synthetic and uses reviewer behavior as the real test. It states the downside of slowing momentum and gives a concrete cohort-based threshold that would justify scaling. |
| OUT-16 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Clear on the evidence-versus-scale tension and discriminates between financial and functional success. It names the contaminated signals, the unresolved diagnosis, and the behavioral evidence that would reverse the recommendation. |
| OUT-17 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Distinguishes artificial revenue from actual product utility and explains why the narrow-focus option is premature. It gives a segment-level retention falsifier and spells out the political cost of pausing. |
| OUT-18 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Separates champion usage from reviewer rejection and discount-driven revenue from true fit. It clearly weighs what the evidence pass reveals against what scaling would hide, and gives a concrete onboarding-based reversal condition. |
| OUT-19 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Recognizes the key issue is whether the apparent success is a tactical sales win or a product win. It names contaminated signals, states the boundary between evidence gathering and scaling, and gives a business-outcome falsifier. |
| OUT-20 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Uses several concrete facts to show why the growth story is unstable. It identifies the critical user-level test, explains the cost of pausing the revenue-led plan, and gives a non-pitched cohort falsifier. |
| OUT-21 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Separates discount-driven expansion and low reviewer retention from real market pull. It states the budget-lock tradeoff and gives a concrete adoption benchmark tied to the critical uncertainty. |
| OUT-22 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Directly addresses the contaminated leadership narrative and the difference between execution targets and validated learning. It includes the right segment-level test and explains what the evidence pass protects against. |
| OUT-23 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Clearly rejects the sales-shaped story and grounds the decision in reviewer behavior and audited utility. It explains the board-timing sacrifice and gives a concrete non-pitch/non-discount falsifier. |
| OUT-24 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Identifies the halo effect in the leadership adjectives and the discount-driven revenue bump, then connects that to the strategy-kernel problem. It gives a behavioral threshold that would validate scaling and makes the twelve-day tradeoff explicit. |
| OUT-25 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Uses the case facts to distinguish validated learning from execution theater. It names the contaminated signals, explains the planning-window sacrifice, and provides a direct non-discounted retention test. |
| OUT-26 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Frames the situation as a sales-driven mirage and ties the evidence pass to actual user utility. It clearly states what scaling would accelerate and gives a concrete retention-and-buyer linkage that would change the answer. |
| OUT-27 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Separates the performance-colored narrative from the underlying user failure and strategy gap. It explains the irreversibility of scaling now versus the learning value of the evidence pass, and gives a champion-led falsifier. |
| OUT-28 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Recognizes the revenue bump is shaped by discounts and champion skew, not clean product validation. It explains the momentum cost of pausing and gives concrete segment-level evidence that would justify scaling. |
| OUT-29 | PASS | FAIL | FAIL | PASS | FAIL | FAIL | 2 | The recommendation is directionally right, but the answer is too thin on distinct case facts and only clearly names one contaminated signal. It does give a useful falsifier, but the dependency rule blocks the higher criteria because C2 and C3 do not clear. |
| OUT-30 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Connects the case to vanity metrics, halo effects, and a chasm-like user gap without collapsing into labels alone. It names contaminated signals, explains the cost of scaling or pivoting too early, and gives a concrete organic-adoption test. |
| OUT-31 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Clearly separates bought revenue and champion behavior from actual reviewer adoption. It spells out what the evidence pass learns versus what scaling would lock in, and provides a behavioral falsifier tied to workflow change. |
| OUT-32 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Uses concrete facts to show a selection-bias and financial-engineering problem, then explains why narrowing is premature. It names the irreversible scaling risk and gives a clean cohort-based retention test. |
| OUT-33 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Separates sales tactics from genuine utility and distinguishes vanity metrics from actionable behavior. It explains the board-clock risk and provides specific evidence that would support either broad scaling or a narrower pivot. |
| OUT-34 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Treats the growth as an accounting artifact and the reviewer failure as the key signal. It explains what scaling now would make irreversible and gives a practical onboarding-focused falsifier. |
| OUT-35 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Separates borrowed revenue, low reviewer retention, and segment-specific explainability risk from real PMF. It explains what the evidence pass would clarify versus what scaling would hide, and gives a specific trend-line trigger to change the recommendation. |
| OUT-36 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Identifies multiple contaminated signals and treats the board story as a false positive. It clearly states what scaling would commit and gives a buyer-and-discount-independent evidence standard. |
| OUT-37 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Good discrimination between discounts, biased feedback, and actual user rejection. It explains the learning-versus-scaling boundary and gives a concrete process-mandate falsifier. |
| OUT-38 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Clearly frames the decision as evidence quality versus premature strategy lock-in. It identifies the contaminated signals, explains what scaling or pivoting would leave unresolved, and gives a behavior-based condition that would justify narrowing. |
| OUT-39 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Separates sales-tactic growth from user-level utility and explicitly treats scaling as premature. It gives the right disconfirming behavioral test and explains the tradeoff of pausing for evidence. |
| OUT-40 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Recognizes the decision turns on whether the revenue bump is a mirage or real product pull. It names the contaminated signals, explains the scale-versus-evidence boundary, and gives a concrete retention-based falsifier. |

Score distribution across the forty blinded answers: {'2': 1, '6': 39}.
This distribution is over OUT-NN labels only; it is not a per-condition
aggregate, and no OUT-NN to condition mapping is recorded here.

## What this receipt is not

This is one blind judge receipt. It is not an eval Result, not a condition
reconciliation, and not a promotion. Reconciliation and any do-not-promote or
benchmark-supported decision are separate later steps.

A model output and a judge score are test artifacts, never authorities.
