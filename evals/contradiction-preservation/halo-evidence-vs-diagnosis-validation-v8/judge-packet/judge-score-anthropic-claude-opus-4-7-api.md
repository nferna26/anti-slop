---
case_id: halo-evidence-vs-diagnosis-validation-v8
benchmark_version: halo-evidence-vs-diagnosis-validation-v8-v1
artifact: judge-score
judge_model_id: claude-opus-4-7
judge_model_snapshot: claude-opus-4-7
judge_model_family: Claude Opus (Anthropic)
judge_provider: Anthropic API
judge_runtime: Anthropic API via Codex local-only script using operator-provided API key
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

# Anthropic API Blind Judge Score - claude-opus-4-7

This is a condition-blind judge receipt for `halo-evidence-vs-diagnosis-validation-v8`, benchmark
version `halo-evidence-vs-diagnosis-validation-v8-v1`. It records C1-C6 scores only. It is not a Result
lift, not a condition reconciliation, and not benchmark promotion.

## Judge identity and independence

- Judge model: `claude-opus-4-7` (`claude-opus-4-7`), Claude Opus (Anthropic).
- Provider / runtime: Anthropic API via Codex local-only script using operator-provided API key.
- API settings: no explicit temperature parameter; max_tokens 2000 calibration / 12000 scoring.
- Response IDs: calibration `msg_01T6QGp824Fv77fCdeEKtCZF`, scoring `msg_017kGB71AuQjSjmgYeqBhBY2`.
- Input hashes: calibration packet sha256 `12c5d225c1b66460ffab97a6bc300edfe522982c59cd5dd9c5bbbfda212575bb`, scoring packet sha256 `aab9cdb636d300206cfdbffc26ef8c506b61bf86cb19ec2eae8c0e26bdcba3a2`.
- Raw output hashes: calibration response sha256 `5678adbb1dae9b737208d3eba97a4b009a073c37ab2e5dcd5a7d9fbfa7d144db`, scoring response sha256 `d3a09fd8eec42653611692a2fde7a24f5c971494a5d193c6feeecb43445babb8`. Raw transcripts remain local-only and are not committed.
- API usage for scoring: input tokens `45033`, output tokens `5470`.
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
| OUT-01 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Identifies contamination (discounts, champion usage, sales-market fit framing), names disconfirming behavioral tests, weighs tradeoffs of each package under the timing constraint, and gives a concrete falsifier tied to champion-as-value-proxy. |
| OUT-02 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Names discount-driven revenue and training-reclassification as contaminated signals, identifies retention/explainability as the right evidence, weighs scaling vs narrowing tradeoffs, and gives a concrete falsifier about onboarding-bug-driven retention. |
| OUT-03 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Rejects discount and champion signals and names disconfirming evidence (non-pitched cohort retention), but does not analyze what each package would learn, hide, or make irreversible under the planning window, so C5 fails and C6 fails by dependency. |
| OUT-04 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Names contaminated signals and a concrete falsifier, but provides minimal intervention-boundary analysis comparing what scaling or narrowing would learn or hide; C5 fails and C6 fails by dependency. |
| OUT-05 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Names discount-borrowed revenue and champion mirage as contaminated, identifies front-line retention and explainability as right evidence, contrasts package tradeoffs, and offers a concrete behavioral falsifier of non-discounted cohorts with >60% retention. |
| OUT-06 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Explicitly rejects halo-style trait re-description and discount-driven NRR, names auditor-explainability and segmented retention tests, weighs the political tradeoff of pausing discounts, and gives an actionable falsifier requiring control-group retention uplift. |
| OUT-07 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Identifies discount-driven revenue and champion vanity usage, names retention and auditor acceptance as the right evidence, weighs tradeoffs and sacrifices, and provides specific behavioral evidence (organic non-discounted retention) that would flip the recommendation. |
| OUT-08 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Names discount-driven revenue and champion-prep usage as contaminated, identifies front-line retention as the disconfirming standard, contrasts what scaling and narrowing would hide, and gives a concrete falsifier about systemic value capture. |
| OUT-09 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Rejects discount-borrowed revenue and champion-vs-reviewer gap, names retention/auditability as the evidence standard, weighs the package tradeoffs under timing, and gives a buyer-vs-user value-distinction falsifier. |
| OUT-10 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Identifies discount-driven NRR and champion vanity as contaminated, names front-line retention and auditor acceptance as the right test, weighs what's sacrificed by the pass, and gives a concrete non-pitched cohort falsifier. |
| OUT-11 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Calls out halo-style trait redescription and discount contamination, identifies non-pitched retention and auditor explainability as the right evidence, names political tradeoff under twelve-day window, and gives a concrete behavioral falsifier. |
| OUT-12 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Names contaminated signals and a falsifier but provides little intervention-boundary analysis comparing what each package learns, hides, or forecloses under the planning window; C5 fails and C6 fails by dependency. |
| OUT-13 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Explicitly identifies halo trait redescription and discount-driven NRR contamination, names organic non-discounted expansion as the disconfirming test, weighs what each option would commit, and gives a concrete behavioral falsifier. |
| OUT-14 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Rejects discount-tied revenue and champion-driven usage, names segment-level retention and explainability as the standard, contrasts scaling and narrowing under the window, and gives a concrete falsifier about segment-isolated low retention. |
| OUT-15 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Names discount-driven revenue and ops-champion vanity usage as contaminated, identifies front-line retention as the disconfirming test, weighs political tradeoff, and gives a concrete ACV-tied auditor-approved falsifier. |
| OUT-16 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Identifies discount-driven revenue, hidden procurement-delayed churn, and champion vanity usage; names non-pitched cohort retention as the falsifier; weighs scaling vs narrowing under the window. |
| OUT-17 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Rejects discount-driven NRR and support reclassification as contaminated, identifies front-line retention independent of pitch as the right test, weighs tradeoffs of all three options, and gives a concrete behavioral falsifier. |
| OUT-18 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Names discount-driven revenue and the champion-vs-user gap, identifies front-line retention as the right standard, weighs political tradeoff, and gives a concrete onboarding-intervention falsifier. |
| OUT-19 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Names halo effect, discount-driven NRR, and champion-driven usage as contaminated, identifies front-line behavior as the standard, contrasts package tradeoffs, and gives a concrete management-value falsifier. |
| OUT-20 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Rejects discount-driven NRR and champion vanity usage, identifies non-pitched cohort retention as the test, weighs sacrificed momentum under the budget window, and gives a concrete behavioral falsifier. |
| OUT-21 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Identifies contaminated signals and a falsifier but doesn't compare what each package would learn, hide, or foreclose under the twelve-day window beyond noting political friction; C5 fails and C6 fails by dependency. |
| OUT-22 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Names halo-driven trait redescription, discount-driven revenue, and champion vanity usage as contaminated, identifies pitch-free retention as the right test, weighs the budget-window tradeoff, and gives a concrete behavioral falsifier. |
| OUT-23 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Names contaminated signals and a concrete falsifier, but does little to compare what each package would learn, hide, or foreclose under the planning window; C5 fails and C6 fails by dependency. |
| OUT-24 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Explicitly invokes halo trait redescription, discount-driven revenue, and support reclassification as contaminated signals, names non-pitched retention as the right standard, weighs budget-window tradeoff, and gives a behavioral falsifier. |
| OUT-25 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Names halo trait redescription and discount-driven NRR, identifies pitch-free reviewer retention as the disconfirming test, weighs the budget-window tradeoff, and gives a concrete behavioral falsifier. |
| OUT-26 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Identifies discount-driven revenue, champion vanity usage, and support reclassification as contaminated, names front-line retention as the right standard, weighs tradeoffs, and provides a concrete behavioral falsifier. |
| OUT-27 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Calls out halo trait redescription and discount-driven NRR explicitly, names front-line behavior and the pitched-vs-unpitched comparison as the right standard, weighs board-clock tradeoff, and gives a concrete champion-led falsifier. |
| OUT-28 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Identifies contaminated signals and a falsifier but provides little comparative boundary analysis of what each package would learn or foreclose under the twelve-day window; C5 fails and C6 fails by dependency. |
| OUT-29 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Rejects contaminated signals and gives a concrete falsifier, but is too brief on what each rejected package would learn or hide under the planning window; C5 fails and C6 fails by dependency. |
| OUT-30 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Names discount-driven NRR, halo effect, and champion-vs-reviewer gap as contaminated, identifies reviewer retention and non-renewal-cause testing as the standard, weighs political tradeoffs, and gives a concrete training-intervention falsifier. |
| OUT-31 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Identifies discount-borrowed revenue, support reclassification, and champion-vs-reviewer split as contaminated, names front-line retention as the standard, weighs tradeoffs, and gives a concrete SOP-mandated adoption falsifier. |
| OUT-32 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Names discount-driven NRR and the champion-vs-reviewer split as contaminated, identifies non-pitched cohort retention as the disconfirming test, weighs budget-window tradeoff, and gives a concrete behavioral falsifier. |
| OUT-33 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Calls out halo-driven discounting and account-manager influence, identifies front-line retention and auditor-defensibility as the standard, weighs all three options' tradeoffs, and gives concrete falsifiers for both pivot directions. |
| OUT-34 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Names discount pull-forward revenue and champion-lobbying as contaminated, identifies front-line retention as the standard, weighs scaling vs narrowing tradeoff, and gives a concrete onboarding-friction falsifier. |
| OUT-35 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Names discount-borrowed revenue and champion vanity usage as contaminated, identifies front-line retention trend as the right test, weighs tradeoffs of all three options under the budget window, and gives a specific retention-trend falsifier. |
| OUT-36 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Identifies discount-inflated revenue, pitch-biased quotes, and champion-driven usage as contaminated, names front-line retention as the standard, weighs the narrative-collapse tradeoff, and gives a concrete champion-as-buyer falsifier. |
| OUT-37 | PASS | PASS | PASS | FAIL | FAIL | FAIL | 3 | Names contaminated signals but the disconfirming "evidence" is a Crossing-the-Chasm narrative about SOP mandates rather than a behavioral test tied to the critical uncertainty; framework-label-heavy reasoning weakens C4, and the ladder collapses. |
| OUT-38 | PASS | PASS | PASS | PASS | PASS | PASS | 6 | Names halo trait redescription, discount-inflated revenue, pitch-biased quotes, and support reclassification as contaminated, identifies behavioral evidence as the standard, weighs budget-window tradeoffs, and gives a concrete champion-as-audit-tool falsifier. |
| OUT-39 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Identifies contaminated signals and a falsifier, but says little about what each rejected package would specifically learn, hide, or foreclose under the twelve-day window beyond political risk; C5 fails and C6 fails by dependency. |
| OUT-40 | PASS | PASS | PASS | PASS | FAIL | FAIL | 4 | Names discount-driven revenue, pitch-signaling, and support reclassification as contaminated and gives a pitch-free retention falsifier, but provides minimal boundary analysis of what each rejected package would learn or foreclose; C5 fails and C6 fails by dependency. |

Score distribution across the forty blinded answers: {'3': 1, '4': 9, '6': 30}.
This distribution is over OUT-NN labels only; it is not a per-condition
aggregate, and no OUT-NN to condition mapping is recorded here.

## What this receipt is not

This is one blind judge receipt. It is not an eval Result, not a condition
reconciliation, and not a promotion. Reconciliation and any do-not-promote or
benchmark-supported decision are separate later steps.

A model output and a judge score are test artifacts, never authorities.
