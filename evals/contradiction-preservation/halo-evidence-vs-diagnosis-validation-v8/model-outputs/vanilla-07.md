---
run_id: halo-evidence-vs-diagnosis-validation-v8-vanilla-07
created: 2026-05-24
eval_type: contradiction-preservation
case_id: halo-evidence-vs-diagnosis-validation-v8
benchmark_version: halo-evidence-vs-diagnosis-validation-v8-v1
model_condition: vanilla
run_number: 7
model_name: gemma4:31b
model_id: gemma4:31b
model_snapshot: Ollama model ID 6316f0629137
runtime: Ollama local HTTP server; version 0.24.0
provider: local
temperature: 0.7
top_p: 0.9
num_ctx: 32768
seed: 701
prompt_source: condition packet (vanilla) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 5a42e17859b4a23ae36d2682474f8d0369ffc492c200375fd79a14bf3b322262
source_packet: the frozen Advisor prompt alone, with no added material - see run-packet.md
source_packet_sha256: 5a42e17859b4a23ae36d2682474f8d0369ffc492c200375fd79a14bf3b322262
condition_packet_sha256: 5a42e17859b4a23ae36d2682474f8d0369ffc492c200375fd79a14bf3b322262
output_file: model-outputs/vanilla-07.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - vanilla (run 07)

## Condition

Benchmark version `halo-evidence-vs-diagnosis-validation-v8-v1`, condition `vanilla`, run 7 of 8. Real local-model run: `gemma4:31b` via Ollama, seed 701, on the frozen condition packet.

## Output

**Recommendation: Run the targeted evidence pass.**

**Why:**
Your current growth is an accounting artifact, not a product success. 72% of your expansion revenue is tied to short-term discounts that incentivized early renewals; this is a "pull-forward" of revenue, not a sustainable increase in ACV. More critically, the product is failing the "front-line test": a 31% week-one retention rate for the actual users (reviewers) is a catastrophic signal.

Scaling now (Option 1) would be scaling a leaky bucket, leading to a massive churn event once the six-month discounts expire and the "champion" users realize the front-line staff aren't using the tool. Narrowing to regulated insurance (Option 3) is premature because you haven't yet determined if the low retention is a general UX/value problem or a specific "auditor explainability" problem. You must decouple the sales tactics (discounts and champion-lobbying) from the product value to see if a viable business actually exists.

**The strongest reason against this:**
It creates immediate political friction with Sales and potentially the CEO. By pausing discounts and instrumenting behavior, you are effectively "stopping the music" during a period where the board is being told a success story. Sales leadership will argue that you are killing momentum and "over-analyzing" a win, potentially risking the budget lock by appearing hesitant or pessimistic.

**Observable evidence that would change my mind:**
I would pivot to "Scale Broadly" (Option 1) only if the data from the evidence pass reveals that the 31% retention rate is skewed by a specific, easily fixable onboarding friction, and that the "non-renewal" letters were isolated incidents unrelated to Review Assist. Specifically, if you find that users who *do* survive the first week have a 90%+ retention rate and high NPS, the problem is "top of the funnel" enablement rather than "core value" deficiency, making aggressive scaling a viable bet.
