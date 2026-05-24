---
run_id: strategy-diagnosis-vs-structural-positioning-substrate-workflow-01
created: 2026-05-21
eval_type: contradiction-preservation
case_id: strategy-diagnosis-vs-structural-positioning
model_condition: substrate_workflow
model_name: qwen3.5:latest
model_id: qwen3.5:latest
runtime: Ollama (local HTTP server at http://localhost:11434), server version 0.24.0
provider: local
temperature: 0.7
top_p: 0.9
seed: 103
prompt_source: case.md — ## Advisor prompt, plus the substrate packet
prompt_sha256: 1a462aef8cb5e7dd7315530870829df5c6c937623126a82e5c2ed439f0af02dd
source_packet: the reviewed claim/tension card strategy-diagnosis-vs-structural-positioning and the reviewed source cards BK-0001-card-001 and BK-0023-card-001, supplied verbatim with a preamble naming their authority levels. See run-packet.md for the packet recipe.
source_packet_sha256: 89425b11beb871304fa5229124609718a8778595567261222d8daf58bbf90e84
output_file: model-outputs/substrate_workflow.md
judge_model_id: claude-opus-4-7
operator_notes: Real local-model run, not an in-session simulation. qwen3.5:latest was executed locally via Ollama (server 0.24.0) on the Advisor prompt plus the three reviewed substrate artifacts; generation 147.2s, prompt_eval 7593 tokens, 6072 output tokens, done_reason stop. The model also emitted a separate reasoning/thinking block, captured in the git-ignored local-only run receipts; the verbatim final answer is reproduced below and is what the rubric scores. A model output is a test artifact — never an authority, never citable as a source; the substrate artifacts it draws on are evidence-level (source cards) and synthesis-level (the claim/tension card), not canon. Packet frozen 2026-05-21T14:30:37Z; see run-packet.md.
raw_model_output_public_safe: true
---

# Model Output — substrate_workflow

## Condition

Substrate condition under test. Answered from the `case.md` Advisor prompt plus the substrate packet: the reviewed claim/tension card `strategy-diagnosis-vs-structural-positioning` and the reviewed source cards `BK-0001-card-001` and `BK-0023-card-001`, supplied verbatim. Real local-model run: `qwen3.5:latest` via Ollama. The answer below is the model's verbatim output.

## Output

Based on the provided artifacts, specifically the open tension between diagnosing a specific organizational challenge and analyzing industry structure, here is the advice for your situation.

### The Tension
Your board’s view and your view represent the two sides of an open tension documented in the knowledge base.
*   **Your View:** Aligns with `BK-0001-card-001` (Rumelt), which argues that strategy begins with a **diagnosis** of the specific critical challenge facing the organization.
*   **Your Board’s View:** Aligns with `BK-0023-card-001` (Porter), which argues that strategy begins with an analysis of **industry structure** (the five forces) to understand the arena's profit potential.

The `strategy-diagnosis-vs-structural-positioning` tension card clarifies that these are not contradictory claims, but rather address different levels of analysis and different starting points. It explicitly states that this tension is **open** and not resolved into a single canon. However, it provides **Deciding Conditions** for when to foreground one or the other.

### Where to Start
**Start with Diagnosis.**

According to the tension card’s **Deciding Conditions**, you should foreground diagnosis when "the case is a specific organization facing an identifiable critical difficulty." Your margin slide from 14% to 6% is a specific, identifiable critical difficulty. The question you are asking—"What should *this* organization do, here?"—is the exact condition under which Rumelt’s diagnosis-first posture fits.

Your board’s argument regarding the industry structure is valid; it addresses the question "Is this arena worth being in?" (Industry Selection). However, the tension card advises against flattening these into one undifferentiated step. To avoid discarding the question of *which* comes first, you must sequence them.

### Why This Sequence?
The `BK-0001-card-001` source card describes the **kernel** of a real strategy, which has three elements: Diagnosis, Guiding Policy, and Coherent Action.
1.  **Diagnosis First:** A guiding policy is defined as "a chosen line of response to the challenge the diagnosis isolated." You cannot formulate a guiding policy (whether to fix internally or reposition externally) without first diagnosing the specific challenge.
2.  **Structure as Input:** The tension card’s "Input Reading" condition states: "When a structural pass surfaces the force that *is* the organization's critical challenge... five-forces analysis is functioning as an input that feeds the diagnosis rather than as a rival to it."
    *   Do not run a Five Forces analysis as a separate, competing track.
    *   Instead, use the Five Forces framework to **inform the Diagnosis**. Ask: "Is the margin erosion caused by a structural force (e.g., buyer power, rivalry) or an internal execution gap?"
3.  **The Guiding Policy:** Once the diagnosis is complete, the Guiding Policy will emerge. If the diagnosis reveals the challenge is structural (e.g., "Buyer power has structurally crushed mid-range margins"), the Guiding Policy becomes "Reposition" (answering the Board). If the diagnosis reveals the challenge is internal (e.g., "We are inefficient despite the industry"), the Guiding Policy becomes "Fix" (answering you).

### Six-Week Plan
To commit to a direction in six weeks without flattening the tension:

*   **Weeks 1–2 (Diagnosis):** Conduct a deep dive into the 14% → 6% margin slide. Use the Five Forces (Porter) not as a template, but as a lens to identify the *specific* load-bearing factors. Is it the distributors (Buyer Power)? Is it the imports (Substitutes)? Or is it your internal design capacity (Coherent Action)?
*   **Weeks 3–4 (Guiding Policy):** Formulate the Guiding Policy based on the diagnosis. If the structural forces are the primary driver, the policy is "Reposition." If internal execution is the driver, the policy is "Fix."
*   **Weeks 5–6 (Coherent Action):** Define the concrete steps. This could be product refresh, quote turnaround improvements, or a strategic pivot.

### Conclusion
Do not default to a single starting point without testing the other. However, for a specific organization facing a specific difficulty, the **Diagnosis-first posture** is the correct starting point. This allows the structural context (your board’s concern) to feed the diagnosis, rather than competing with it. The resulting Guiding Policy will then tell you whether the arena is worth being in or if the fix must be internal. This approach honors the structural reality of your industry while ensuring your strategy is built on the specific challenge of your organization.
