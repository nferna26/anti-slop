---
run_id: normalization-vs-latent-errors-print-vault-v6-generic-advice-prompted-03
created: 2026-05-23
eval_type: contradiction-preservation
case_id: normalization-vs-latent-errors-print-vault-v6
benchmark_version: normalization-vs-latent-errors-print-vault-v6-v1
model_condition: generic_advice_prompted
run_number: 3
model_name: gemma4:31b
model_id: gemma4:31b
model_snapshot: Ollama model ID 6316f0629137
runtime: Ollama local HTTP server; version 0.24.0
provider: local
temperature: 0.7
top_p: 0.9
num_ctx: 32768
seed: 305
prompt_source: condition packet (generic_advice_prompted) - frozen added material plus frozen Advisor prompt; see run-packet.md
prompt_sha256: 47e70d50741535d08f44f13a5a4d15abdbe7d15b552678359c585331cabff5c6
source_packet: a short generic advice-quality request, then the frozen Advisor prompt; no rubric and no sources - see run-packet.md
source_packet_sha256: c86420e546f8f0094fa8751fe984a1e420ee23251d0d6fa80216df4133941093
condition_packet_sha256: c86420e546f8f0094fa8751fe984a1e420ee23251d0d6fa80216df4133941093
output_file: model-outputs/generic_advice_prompted-03.md
judge_model_id: pending - judge receipts recorded separately under judge-packet
judge_prompt_sha256: pending - judge receipts recorded separately under judge-packet
judge_independence: pending - judge receipts recorded separately under judge-packet
raw_model_output_public_safe: true
---

# Model Output - generic_advice_prompted (run 03)

## Condition

Benchmark version `normalization-vs-latent-errors-print-vault-v6-v1`, condition `generic_advice_prompted`, run 3 of 8. Real local-model run: `gemma4:31b` via Ollama, seed 305, on the frozen condition packet.

## Output

**Recommendation: Decline the surge until after the rainy season.**

### Reasoning
The evidence suggests that Vault 3 is currently experiencing "environmental volatility" that is being masked by administrative reporting. You are seeing a divergence between **averaged data** (which looks stable) and **raw data/physical evidence** (which indicates instability).

1.  **The "Averaging" Trap:** The Facilities Manager is relying on the "green tile" (one-hour average). In archival preservation, averages are dangerous. A one-hour average can remain "within range" even if the RH spiked violently for ten minutes. The fact that ten-minute raw readings have become *sharper* since the March actuator replacement indicates that the system is reacting more aggressively to shocks, even if it recovers quickly enough to keep the hourly average stable.
2.  **Physical Warnings:** The "faint rippling" on packing tissue is the most critical piece of evidence. Tissue is often more hygroscopic and reactive than the prints themselves; it acts as a "canary in the coal mine." Dismissing this as "handling marks" is a red flag that the current operational culture is prioritizing the closure of work orders over conservation warnings.
3.  **Systemic Fragility:** The "pressure sensor flip" during brief door openings suggests the vestibule air curtain is not effectively buffering the vault from the rest of the building. A 35% increase in cart entries will increase the frequency of these pressure flips and RH spikes.
4.  **Procedural Failure:** The missing handheld hygrometer readings (6 of 21) and the reliance on "normalized by morning" notes suggest that the staff is treating the RH slope notices as a nuisance to be cleared rather than a technical failure to be solved.

Accepting the surge would be betting the safety of the collection on a "green tile" that is mathematically designed to hide the very spikes that cause mechanical stress (cockling, warping) in unframed 19th-century paper.

### The Strongest Reason Against This Recommendation
**The risk of institutional and financial damage.** Declining the surge causes immediate, quantifiable losses: cancellation fees, a public-program failure, and a strained relationship with a partner museum. This is a "political" and "financial" cost, whereas the risk to the prints is a "probabilistic" cost. In a corporate or administrative setting, the certainty of a fee often outweighs the possibility of a conservation issue.

### Observable Evidence That Would Change My Mind
I would reverse this recommendation only if the following two conditions were met during the overnight window:
1.  **Wet-Load Success:** The condensate pump passes a full wet-load test (not just a dry bench test), proving the dehumidifier can actually remove water from the air under load during a rainy season.
2.  **Peak Dampening:** The ten-minute raw readings show a *decrease* in peak amplitude during a simulated door-open event, proving that the new damper actuator is actually stabilizing the environment rather than just accelerating the recovery time.

**Note on the "Overnight Window":** Do not use the window for the dashboard rule. Suppressing notices is an administrative "band-aid" that reduces visibility exactly when you need it most. If you have the window, use it for the technical audit (Option B), but do so with the understanding that unless the results are flawless, the surge must still be declined.
