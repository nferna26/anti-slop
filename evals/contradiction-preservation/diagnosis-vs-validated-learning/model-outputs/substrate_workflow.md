---
run_id: diagnosis-vs-validated-learning-substrate-workflow-01
created: 2026-05-20
eval_type: contradiction-preservation
case_id: diagnosis-vs-validated-learning
model_condition: substrate_workflow
model_name: claude-opus-4-7
prompt_source: case.md — ## Advisor prompt
output_file: model-outputs/substrate_workflow.md
source_packet: substrate — the Advisor prompt plus the reviewed claim/tension card strategy-diagnosis-vs-validated-learning and the reviewed source cards BK-0001-card-001 and BK-0007-card-001 (the artifacts named in case.md Lineage)
operator_notes: First evaluation pass. Output produced in-session as a good-faith simulation of the substrate_workflow condition — answered from the Advisor prompt plus the reviewed claim/tension card and the two reviewed source cards. A test artifact, never an authority and never citable as a source.
raw_model_output_public_safe: true
---

# Model Output — substrate_workflow

## Condition

Substrate workflow: answered from the Advisor prompt in `case.md` plus the substrate named in case.md Lineage — the reviewed claim/tension card `strategy-diagnosis-vs-validated-learning` and the two reviewed source cards `BK-0001-card-001` and `BK-0007-card-001`.

## Output

Your two colleagues are each invoking a real and well-grounded discipline, and the substrate I am working from holds them as a genuine, unresolved tension rather than letting one win by default. Let me lay the tension out, then locate your specific situation in it.

**The two postures.** One says a real strategy is built on a diagnosis: before you design or build, you name what is critical about the challenge, and a guiding policy and coherent action follow from that. This is the evidence in the source card `BK-0001-card-001`, on Rumelt's strategy kernel — an evidence-level claim, not a universal law. The other says that under deep uncertainty, where you do not yet know the customer or what they value, progress is *validated learning*: you find out by testing assumptions against real customer behaviour, because there is nothing solid yet to diagnose. That is the source card `BK-0007-card-001`, on Ries's validated learning — also evidence-level. The claim/tension card `strategy-diagnosis-vs-validated-learning` holds these two in tension and, deliberately, does not resolve it in general. What it offers instead is deciding conditions: how legible the challenge is, and how costly an experiment is.

**Your situation is not one problem — it is two,** and they sit on opposite sides of those deciding conditions.

The *legible part* is your clinics. You have four years of support tickets, churn interviews, and usage data on the clinic customer; the clinic's workflow pains are about as legible as a challenge gets. Here the diagnosis posture applies straightforwardly — you can and should name what is actually broken in clinic workflows from the evidence you already hold. Your head of product's instinct is right *for this part*.

The *unknown part* is your patients. The portal serves patients — a customer you have never sold to or studied — and its success depends on patients adopting self-service and clinics promoting it. No amount of analysis of your clinic data resolves that; the facts a diagnosis would need do not exist yet. Here the validated-learning posture applies — the founding engineer's instinct is right *for this part*. Your own deciding condition reinforces it: an experiment here is cheap and fast (two to three weeks, low cost, nothing built). When the load-bearing uncertainty is both unknown and cheap to test, testing it first is strongly favoured.

So the honest synthesis is neither "diagnose, then build" nor "just experiment." It is closer to a third reading the tension card names — treat the diagnosis of the bet itself as a hypothesis, and let a cheap experiment test it. Concretely, for the quarter:

- **Weeks 1–3: run the patient-demand experiment.** A fake-door landing page or a concierge pilot with several friendly clinics and their patients. This tests the load-bearing assumption — will patients adopt, will clinics promote — before any build capacity is committed.
- **In parallel: diagnose the clinic-workflow part** from your existing four years of data. This costs little engineering capacity and is legitimate diagnosis work on the legible part; it is what your head of product wants, done where it can actually be done.
- **At the three-week mark, regroup.** If patient demand shows real signal, the rest of the quarter goes to designing and building the portal — now grounded in both a clinic-workflow diagnosis and patient-behaviour evidence. If the signal is weak, you have spent three weeks rather than thirteen, and the workflow diagnosis still has value for your existing product.

Two cautions on what this is *not*. First, this recommendation is for *your* specifics — a legible clinic side, an unknown patient side, cheap experiments. Change those — if experiments were slow and expensive, or if patient demand were already well evidenced — and the balance shifts. Neither posture is a universal rule. Second, the underlying claims here are evidence-level source cards and a synthesis-level tension card, not canon. The tension between diagnosis-first and experiment-first is genuinely unresolved in general; what is decidable is only where *your* situation sits on the deciding conditions.
