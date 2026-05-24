---
run_id: halo-evidence-vs-diagnosis-validation-v7-vanilla-01
created: 2026-05-23
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v7
benchmark_version: halo-evidence-vs-diagnosis-validation-v7-v1
model_condition: vanilla
run_number: 1
model_name: gemma4:31b
model_id: gemma4:31b
model_snapshot: Ollama model ID 6316f0629137
runtime: Ollama local HTTP server; version 0.24.0
provider: local
temperature: 0.7
top_p: 0.9
num_ctx: 32768
seed: 101
prompt_source: condition packet (vanilla) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 5a42e17859b4a23ae36d2682474f8d0369ffc492c200375fd79a14bf3b322262
source_packet: the frozen Advisor prompt alone, with no added material - see run-packet.md
source_packet_sha256: 5a42e17859b4a23ae36d2682474f8d0369ffc492c200375fd79a14bf3b322262
condition_packet_sha256: 5a42e17859b4a23ae36d2682474f8d0369ffc492c200375fd79a14bf3b322262
output_file: model-outputs/vanilla.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - vanilla (run 01)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v7-v1`, condition `vanilla`, run 1 of 8. Real local-model run: `gemma4:31b` via Ollama, seed 101, on the frozen condition packet.

## Output

**Recommendation: Run the targeted evidence pass.**

**Why:**
Your current growth is a "mirage" created by sales tactics, not product-market fit. 72% of your expansion revenue is derived from discounts tied to early renewals—this is a one-time pull-forward of revenue, not a sustainable growth engine. More critically, the "usage" metric is a vanity metric: the feature is being used by a few "champions" to prepare for meetings, while the actual front-line workers (the people whose daily workflow determines long-term retention) are abandoning the tool at a rate of 69% after one week.

Scaling this now would be "scaling a leak." You would be committing a year's budget to a product that front-line users find unusable and that insurance regulators find indefensible. If you scale broadly, you aren't expanding a wedge; you are accelerating the arrival of a massive churn event once the early-renewal discounts expire and the "training questions" (which are actually product failures) accumulate.

**The strongest reason against this:**
It kills the "upbeat story" for the board packet. By pausing discounts and instrumenting the truth, you are effectively telling the CEO and the Board that the recent revenue spike was a tactical illusion rather than a strategic breakthrough. In a high-pressure environment, this can be perceived as a lack of momentum or a failure of the product team to "capture the win," potentially risking a budget cut or a loss of confidence from sales leadership who are currently riding the high of the revenue bump.

**The observable evidence that would change my mind:**
I would pivot to "Scale Broadly" only if the reviewer-level behavior data showed that the 31% retention rate was a "false low" caused by the nature of the work (e.g., reviewers only *need* to use the tool once every two weeks, but the "first week" window is too narrow), AND if the non-renewal letters from the two customers were explicitly linked to budget cuts rather than product dissatisfaction. If the users are actually getting value but simply aren't logging in daily, the risk of scaling is significantly lower.
