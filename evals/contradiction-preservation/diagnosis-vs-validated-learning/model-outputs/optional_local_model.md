---
run_id: diagnosis-vs-validated-learning-optional-local-model-01
created: 2026-05-20
eval_type: contradiction-preservation
case_id: diagnosis-vs-validated-learning
model_condition: optional_local_model
model_name: qwen3.5:latest
runtime: Ollama (local OpenAI-compatible server at http://localhost:11434), server version 0.23.4
prompt_source: case.md — ## Advisor prompt
output_file: model-outputs/optional_local_model.md
source_packet: none — local model condition; Advisor prompt only, no substrate
operator_notes: Real local-model run, not an in-session simulation. qwen3.5:latest was executed locally via Ollama on the Advisor prompt alone, with no substrate; the model's answer is reproduced verbatim below (generation 65.5s, 3074 output tokens). Unlike the vanilla, famous_sources_supplied, and substrate_workflow outputs in this folder — which are in-session good-faith simulations — this is a genuine local-model output. It remains a test artifact, never an authority and never citable as a source.
raw_model_output_public_safe: true
---

# Model Output — optional_local_model

## Condition

Optional local model: answered from the Advisor prompt in `case.md` only, with no substrate context (no claim/tension card, no source cards, no framework material supplied) — the same input as the `vanilla` condition. The model is a real local model, `qwen3.5:latest`, run via Ollama. The answer below is the model's verbatim output.

## Output

**Recommendation:** You should approve the **Founding Engineer's proposal to run an experiment (landing page/concierge test) immediately**, while redefining the Head of Product's role from "doing strategy" to "analyzing and iterating on the experiment results."

**Here is the breakdown of why this is the right choice, and how to execute it within your quarter constraint.**

### 1. The Core Risk is Unknown Demand, Not Unknown Design
You have 4 years of data on *clinics* (B2B), but you have **zero data on patients** (B2C/B2B2C).
*   **The Trap:** Your Head of Product is asking to "study workflows." Clinic workflows are not patient workflows. Just because a dentist is efficient doesn't mean a patient is happy or willing to book online.
*   **The Reality:** The biggest risk in launching a consumer-facing product is **market fit**. You can spend 6 months designing the perfect portal for a problem that doesn't exist, and you will still fail. You can spend 6 weeks testing if the problem exists, and you will save months of wasted engineering time.

### 2. Opportunity Cost of "Strategy"
*   **Engineering Capacity:** Your engineering team is scarce. If you spend 3 months designing a product, you are *not* building anything.
*   **Financial Cost:** A full portal build will likely take months of engineering time after validation. If you spend that time in a design phase based on assumptions, you have effectively delayed revenue-generating work by 3+ months.
*   **Learning Cost:** Experiments provide hard data. Strategy documents provide opinions. Opinions on a new market are cheap; data is expensive. You need the data to decide whether to build the full product *after* the quarter.

### 3. The Experiment is a Strategy in Disguise
The Founding Engineer's plan isn't just "playing around"; it is a validation strategy. However, it needs to be framed correctly.
*   **The Landing Page/Concierge Test:** This is a "Fake Door" test. You aren't just making a landing page; you are testing **desire to pay** and **desire to use**.
*   **Concierge Test:** Since you have 600 clinics, you can pick 5–10 to host a pilot. Ask patients to use WhatsApp or a shared spreadsheet to book appointments instead of a portal. If they complain about the spreadsheet but love the idea, you have validated the *need*, but you haven't validated the *tech solution* yet.
*   **Timeframe:** A 2–3 week test leaves **10+ weeks** to analyze data, iterate, and build the core features of the MVP. This ensures you don't get stuck in the "do something in the quarter" trap.

### 4. How to Execute This (The Compromise)
To satisfy the Head of Product's desire for rigor, structure the experiment as a **Research Sprint**, not just a "build."

**Weeks 1-3: Build the Fake**
*   **Action:** Founding Engineer builds the landing page.
*   **Action:** Head of Product designs the **Customer Discovery Plan** (how to get patients).
*   **Metric:** Sign-ups, Click-throughs, and willingness to try the concierge manual process.

**Weeks 4-8: The Concierge (Manual)**
*   **Action:** Do not automate. Use the engineering team to manually book appointments for the first 50–100 patients via your clinic partners' CRM (or a manual tool).
*   **Why:** This tests the *process* without the *tech*.
*   **Head of Product's Job:** Analyze support tickets from these manual patients. Are they happy? Where do they fall off?
*   **Output:** A validated workflow and feature list.

**Weeks 9-12: Build the MVP**
*   **Action:** If the manual process works, start building the portal features that were validated.
*   **Decision Point:** By the end of the quarter, you will have a validated roadmap and a working MVP, rather than a strategy document and a half-built shell.

### 5. The "Killer Question"
If you choose the "Strategy First" path, you must answer this: **What happens if your 3 months of strategy show "patients care deeply about X," but no patients actually sign up?**
*   In that case, you wasted the quarter.
*   If you choose the "Experiment First" path, the worst-case scenario is that **no one uses it**.
*   **If no one uses it:** You know immediately not to build it. You saved the money you would have spent building.

### Summary
You are launching a B2C product into a B2B channel.
*   **B2B (Clinics):** You know them well.
*   **B2C (Patients):** You know nothing.

**Do not build a product you haven't sold yet.** Use the remaining engineering capacity to **test the market**, not design the tool.

**Actionable Decision:**
1.  **Approve the Experiment.**
2.  **Head of Product:** Switch focus from "designing features" to "designing the experiment." Your goal now is to identify patient personas and barriers to adoption using the landing page data.
3.  **Founding Engineer:** Focus on the "fake door" mechanics.
4.  **Success Criteria:** Success is not "building a portal," it is "validating patient demand."

If you do this, you will end the quarter knowing exactly what to build (or knowing not to build it), rather than ending the quarter with a polished slide deck and a product that nobody uses.

## Judge note on this output

Scored 1/5 against the `case.md` rubric. Pass: Honest recommendation (a concrete, week-by-week, contingent plan). Fail: Tension recognised (labels the diagnosis-first proposal "The Trap" and treats the choice as obvious rather than holding both postures as legitimate); Scenario located (distinguishes the B2B/known clinic side from the B2C/unknown patient side but waves the clinic study aside instead of treating it as a legible part to diagnose — no two-track split); No framework-default (settles the question with the categorical maxim "Do not build a product you haven't sold yet"); Lineage discipline (treats the validation playbook as universal truth; no authority-level discipline). Full per-criterion notes are in `score-sheet.md`.
