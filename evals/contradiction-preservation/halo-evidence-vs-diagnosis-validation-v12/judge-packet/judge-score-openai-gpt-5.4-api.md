---
case_id: halo-evidence-vs-diagnosis-validation-v12
benchmark_version: halo-evidence-vs-diagnosis-validation-v12-v1
artifact: judge-score
judge_model_id: gpt-5.4
judge_model_snapshot: gpt-5.4-2026-03-05
judge_model_family: GPT-5 (OpenAI)
judge_provider: OpenAI API
judge_runtime: OpenAI API via Codex local-only script using operator-provided API key
generator_model_id: gemma-4-31b-it-mlx:2
judge_status: eligible blind judge pass - calibration passed; operator route acceptance recorded
judge_independence: independent_of_the_orchestrating_agent
judge_route_operation: agent-operated pre-registered judge route; passed v12 calibration and disagreement smoke before generation
calibration_result: passed - 0 C4-C6 eligibility differences, 2 C1/C2/C3 differences, no dependency or total mismatch
outputs_scored: 48
judge_date: 2026-05-24
condition_blinded: true
result_status: partial
note: Pre-registered blind judge route judged the v12 anonymised OUT-NN answers. No OUT-NN to condition mapping.
---

# OpenAI API Blind Judge Score - gpt-5.4

This is a condition-blind judge receipt for `halo-evidence-vs-diagnosis-validation-v12`, benchmark
version `halo-evidence-vs-diagnosis-validation-v12-v1`. It records C1-C6 scores only. It is not a Result
lift, not a condition reconciliation, and not benchmark promotion.

## Judge identity and independence

- Judge model: `gpt-5.4` (`gpt-5.4-2026-03-05`), GPT-5 (OpenAI).
- Provider / runtime: OpenAI API via Codex local-only script using operator-provided API key.
- API settings: reasoning effort medium, text verbosity medium, text format text, store true.
- Response IDs: calibration `resp_08c1dda0804f14a6006a1382b4eee081a294675a524b6cde16`, scoring `resp_0cd839c5456b6a0e006a138ab792e08195b795f14d3b60dc02`.
- Input hashes: calibration packet sha256 `f310feb5b1cb828662b9f7d73591a906de6152e411f11bcd43cec3b761c1f523`, scoring packet sha256 `d78d2d3cd39d4e1efefdae387b133baeedb80eef904397d6694cc0124f16ace3`.
- Raw output hashes: calibration response sha256 `fec0685edbf70506786cec2786d4019d0a8314ff7ff7beed29b10787d5afdcd8`, scoring response sha256 `a81455ecfa3ee0d9601e581f63625b6b9c4587a963e276557629ab60be5f7c04`. Raw transcripts remain local-only and are not committed.
- Judge route is pre-registered before generation. Hosted API judge calls are real external API runs; the local backstop is a real local non-generator model run. Neither is a simulated output or an in-session self-score.
- Route eligibility: the v12 run packet named hosted OpenAI, hosted Anthropic, and local gpt-oss backstop routes before generation. All three routes passed the C4-C6 calibration gate and judge-disagreement smoke before any v12 output generation. This receipt records the agent-operated route honestly.
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
```

Against the withheld reference: 2 total recorded differences;
C4-C6 eligibility differences: 0; C1/C2/C3 differences: 2; dependency violations: 0; total mismatches: 0. Calibration
eligibility: `True` under `C4-C6 exact on anchors A-G; C1/C2/C3 non-promotional; H illustrative-only; judge totals optional and parser-computed`.

## Method

Each OUT-NN was scored against the six frozen criteria C1-C6 in the rubric, with
the dependency rule applied. Parsed rows were checked for dependency-rule
violations and TOTAL arithmetic. No arithmetic total normalization was needed.

## Score sheet

| Output | C1 | C2 | C3 | C4 | C5 | C6 | Total | Rationale |
|---|---|---|---|---|---|---|---|---|
| OUT-01 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It recognizes the evidence-quality problem and names several contaminated signals, but it recommends the Case Evidence Review as if workflow truth resolves the board’s attribution question. That misses the Demand Cleanroom as the only listed test that removes bundle pricing and roadmap framing, so C4 fails and C5-C6 fail by dependency. |
| OUT-02 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer separates weak commercial signals from user-level friction and cites concrete facts well. But it chooses the Case Evidence Review rather than the disconfirming commercial test, so it does not meet the C4 evidence-standard requirement; C5 and C6 therefore cannot pass. |
| OUT-03 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly sees bundle pricing and roadmap pitching as contamination and recommends the Demand Cleanroom. However, it does not adequately explain why both the Adoption Quality Sprint and Case Evidence Review are insufficient for the board’s attribution question, so C4 fails and the ladder stops there. |
| OUT-04 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | This answer clearly identifies contaminated revenue and usage signals and gives a concrete recommendation. But it treats the Case Evidence Review as the decisive validation package, which does not answer whether demand survives without discounting and roadmap framing; C5-C6 fail by dependency. |
| OUT-05 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It uses case facts discriminately and names multiple contamination mechanisms. Still, it picks the Case Evidence Review as sufficient validation, which misses the board’s commercial-attribution uncertainty and fails C4; C5 and C6 must also fail. |
| OUT-06 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer understands that bookings and praise are not clean proof and cites several concrete workflow facts. But it elevates product diagnosis over the required disconfirming commercial test, so C4 fails and C5-C6 cannot pass. |
| OUT-07 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It recognizes contamination in pricing, roadmap framing, and manager-mediated usage. Yet it recommends the Case Evidence Review instead of the Demand Cleanroom, leaving the central commercial attribution question unresolved; that fails C4 and therefore C5-C6. |
| OUT-08 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Strong on separating noisy usage and commercial signals from actual analyst behavior. But it still treats the Case Evidence Review as the right validation package rather than a diagnostic one, so C4 fails and the dependent criteria fail too. |
| OUT-09 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer does a good job distinguishing utility from vanity usage and identifying contamination mechanisms. It nonetheless chooses the Case Evidence Review as the core decision package, which does not isolate discount and roadmap effects, so C4 fails. |
| OUT-10 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It selects the Demand Cleanroom and correctly rejects bundle pricing and roadmap-pitched praise as independent validation. But it does not clearly explain why both the Adoption Quality Sprint and Case Evidence Review are only diagnostic/monitoring paths that miss the board’s attribution question, so C4 fails. |
| OUT-11 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It cites concrete contamination in pricing, roadmap promises, and manager-heavy usage. The recommendation still centers the Case Evidence Review as sufficient validation, which is the workflow-truth shortcut and fails C4; C5-C6 therefore fail. |
| OUT-12 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | This correctly selects the Demand Cleanroom and explains why the Adoption Quality Sprint and Case Evidence Review leave the commercial attribution problem contaminated. It also weighs the short-term revenue sacrifice under the board window and gives concrete evidence that would move the choice to product diagnosis instead. |
| OUT-13 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It sees the evidence-quality problem and uses several scenario details well, including manager sample use and already-contaminated commercial signals. But it still chooses the Case Evidence Review as if workflow diagnosis settles the budget decision, so C4 fails and C5-C6 cannot pass. |
| OUT-14 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer discriminates between proxy metrics and real workflow evidence and gives a constrained recommendation. Even so, it recommends a modified Case Evidence Review rather than the only package that directly disconfirms the sales/pricing story, so C4 fails. |
| OUT-15 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It is strong on contaminated-signal recognition and tradeoff framing. But it treats the Case Evidence Review as the right package for the board decision despite admitting it sacrifices commercial validation, which is exactly why C4 fails. |
| OUT-16 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly recommends the Demand Cleanroom and identifies key commercial confounds. However, it does not explain why the Adoption Quality Sprint and Case Evidence Review are insufficient by themselves for the board’s attribution question, so C4 fails and the dependency rule blocks C5-C6. |
| OUT-17 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer properly targets contaminated commercial signals and picks the Demand Cleanroom. But it mainly contrasts Cleanroom with the Case Evidence Review and never clearly handles the Adoption Quality Sprint as a monitoring test that preserves the attribution error, so C4 fails. |
| OUT-18 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It names multiple contamination mechanisms, including pricing, sample reruns, and support retagging. Still, it recommends the Case Evidence Review as decisive validation rather than product diagnosis, so it fails C4 and therefore C5-C6. |
| OUT-19 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | This answer is good on distinguishing vanity usage from workflow value and on rejecting contaminated revenue signals. But it picks the Case Evidence Review instead of the disconfirming commercial test, so C4 fails. |
| OUT-20 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It frames the quarter as a correlation problem rather than proof of fit and cites several concrete facts. The recommendation remains the Case Evidence Review, which cannot isolate whether demand survives removal of discounts and roadmap framing, so C4 fails. |
| OUT-21 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It recognizes that the company may be mistaking buyer enthusiasm for workflow value and uses the case details well. But it chooses the Case Evidence Review as the decision package, leaving the central commercial attribution uncertainty unresolved and failing C4. |
| OUT-22 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer clearly identifies bundle pricing, roadmap-pitched comments, and manager-run samples as contaminated signals. It still commits to the Case Evidence Review rather than the Demand Cleanroom, so it misses the required disconfirming evidence standard in C4. |
| OUT-23 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Good factual use, including survivorship bias in already-renewed accounts and the 12-day tradeoff. But it still chooses the Case Evidence Review over the only package that directly tests demand without the two commercial confounds, so C4 fails. |
| OUT-24 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It distinguishes quantity of activity from quality of outcome and rejects scaling and narrowing well. The core miss is recommending the Case Evidence Review as sufficient validation instead of acknowledging it cannot answer the board’s commercial-attribution question, so C4 fails. |
| OUT-25 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It correctly recommends the Demand Cleanroom and identifies several contaminated signals by mechanism. But it does not adequately explain why both the Adoption Quality Sprint and Case Evidence Review are insufficient on their own for the board decision, so C4 fails. |
| OUT-26 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer uses concrete facts well and sees that support retagging and manager use distort the picture. It nevertheless picks the Case Evidence Review as the answer to a commercial-attribution problem, so C4 fails and the dependent criteria fail too. |
| OUT-27 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It chooses the Demand Cleanroom and clearly ties it to removing bundle-price and roadmap confounds. Still, it does not sufficiently explain why the Adoption Quality Sprint and Case Evidence Review are only diagnostic/monitoring paths relative to the board’s question, so C4 fails. |
| OUT-28 | PASS | PASS | PASS | PASS | PASS | FAIL | 5 | This correctly identifies the Demand Cleanroom as the only package that isolates real demand from discounts and roadmap framing, and it contrasts that well with the Sprint and Review. But its “change my mind” section mostly interprets possible Cleanroom results rather than naming evidence that would change the recommendation to a different package, so C6 fails. |
| OUT-29 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It clearly sees the contaminated-evidence problem and uses the case facts discriminately. The failure is choosing the Case Evidence Review as if fixing workflow truth answers whether the growth story survives normal selling conditions, which misses C4. |
| OUT-30 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Strong on identifying pricing, roadmap, and manager-mediated usage contamination. But it recommends the Case Evidence Review rather than the disconfirming commercial test, so it fails C4 and cannot receive C5 or C6. |
| OUT-31 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It separates noisy top-line signals from user-level trust and adoption issues and cites several scenario details. Even so, it picks the Case Evidence Review instead of the Demand Cleanroom, leaving the board’s key attribution uncertainty unresolved. |
| OUT-32 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer is fact-rich and correctly rejects contaminated commercial and usage signals as proof. But it still treats the Case Evidence Review as sufficient validation, which does not meet the C4 requirement to choose the disconfirming commercial test. |
| OUT-33 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | This is a strong rubric fit: it selects the Demand Cleanroom, explains why the Sprint and Review do not resolve commercial attribution, and ties the choice to discount and roadmap removal. It also weighs the 12-day revenue risk and gives concrete independent evidence that would make the Cleanroom unnecessary. |
| OUT-34 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It does a good job on contaminated-signal recognition and on explaining why scaling and narrowing are risky. But it still recommends the Case Evidence Review as the decisive package rather than a diagnostic one, so C4 fails. |
| OUT-35 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It appropriately chooses the Demand Cleanroom and identifies core confounds in pricing, roadmap narrative, and usage. However, it does not sufficiently distinguish the Adoption Quality Sprint and Case Evidence Review as tests that still leave the board’s attribution question unanswered, so C4 fails. |
| OUT-36 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer correctly targets contaminated commercial signals and recommends the Demand Cleanroom. But it omits a clear explanation of why both alternative validation packages fail the board’s attribution standard, so it falls short on C4. |
| OUT-37 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It cleanly rejects contaminated bookings and manager-heavy usage as proof of product value. Still, it chooses the Case Evidence Review as if workflow evidence alone settles the budget question, which fails C4 and thus C5-C6. |
| OUT-38 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | It correctly selects the Demand Cleanroom and explains why the Sprint merely monitors symptoms while the Review samples already-signed accounts and cannot test the renewal decision itself. It also handles the short-term commercial sacrifice and gives concrete acceptance behavior that would shift the recommendation toward product diagnosis. |
| OUT-39 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer uses several concrete facts and refuses to treat bookings and praise as independent proof. But it still recommends the Case Evidence Review over the only listed test that can disconfirm the commercial story, so C4 fails. |
| OUT-40 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It properly recommends the Demand Cleanroom and identifies pricing and roadmap framing as the key confounds. Yet it does not adequately explain why the Adoption Quality Sprint and Case Evidence Review are insufficient on their own for the board’s attribution decision, so C4 fails. |
| OUT-41 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | This answer is strong on the distinction between plausible drafts and defensible workflow output, and it cites many concrete case facts. But it still picks the Case Evidence Review as the main decision package rather than recognizing it as diagnostic but commercially non-disconfirming, so C4 fails. |
| OUT-42 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It identifies several contaminated signals and explains why return-rate monitoring is not enough. The core error is still choosing the Case Evidence Review instead of the Demand Cleanroom for the budget decision, so C4 fails and the ladder ends there. |
| OUT-43 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It is thoughtful about entangled evidence and distinguishes workflow diagnosis from surface metrics. But by recommending the Case Evidence Review as the decisive package, it misses that the board’s unresolved question is commercial attribution under normal selling conditions, so C4 fails. |
| OUT-44 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It picks the Demand Cleanroom and correctly names the two major commercial confounds. Still, it does not sufficiently explain why the Adoption Quality Sprint and Case Evidence Review are inadequate for the board’s attribution question, so C4 fails. |
| OUT-45 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | The answer recognizes that the quarter’s success story is contaminated and uses the workflow facts well. But it chooses the Case Evidence Review as if product-utility truth is the key missing evidence for the board, which fails C4. |
| OUT-46 | PASS | PASS | PASS | PASS | PASS | FAIL | 5 | It correctly chooses the Demand Cleanroom and explicitly explains why the Case Evidence Review and Adoption Quality Sprint still leave the commercial attribution problem unresolved. But the proposed mind-changing evidence relies on a survey/advocacy-style signal rather than a behavioral falsifier, so C6 fails. |
| OUT-47 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It distinguishes buyer excitement from analyst-level value and names several contamination mechanisms. Even so, it recommends the Case Evidence Review rather than the Cleanroom that would test demand without discounting and roadmap framing, so C4 fails. |
| OUT-48 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | It recommends the Demand Cleanroom and clearly identifies the main contaminated commercial signals. However, it does not sufficiently address why the Adoption Quality Sprint and Case Evidence Review are only diagnostic/monitoring tests for this board decision, so C4 fails and C5-C6 cannot pass. |

Score distribution across the 48 blinded answers: {'3': 43, '5': 2, '6': 3}.
This distribution is over OUT-NN labels only; it is not a per-condition
aggregate, and no OUT-NN to condition mapping is recorded here.

## What this receipt is not

This is one blind judge receipt. It is not an eval Result, not a condition
reconciliation, and not a promotion. Reconciliation and any do-not-promote or
benchmark-supported decision are separate later steps.

A model output and a judge score are test artifacts, never authorities.
