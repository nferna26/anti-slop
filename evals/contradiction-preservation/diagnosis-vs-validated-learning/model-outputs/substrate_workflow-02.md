---
run_id: diagnosis-vs-validated-learning-substrate-workflow-02
created: 2026-05-20
eval_type: contradiction-preservation
case_id: diagnosis-vs-validated-learning
model_condition: substrate_workflow
model_name: claude-opus-4-7
prompt_source: case.md — ## Advisor prompt
output_file: model-outputs/substrate_workflow-02.md
source_packet: substrate — the Advisor prompt plus the reviewed claim/tension card strategy-diagnosis-vs-validated-learning and the reviewed source cards BK-0001-card-001 and BK-0007-card-001 (the artifacts named in case.md Lineage)
operator_notes: Repeat run (run 02) of the substrate_workflow condition. Output produced in-session as a good-faith simulation — answered from the Advisor prompt plus the reviewed claim/tension card and the two reviewed source cards. A test artifact, never an authority and never citable as a source.
raw_model_output_public_safe: true
---

# Model Output — substrate_workflow (run 02)

## Condition

Substrate workflow: answered from the Advisor prompt in `case.md` plus the substrate named in case.md Lineage — the reviewed claim/tension card `strategy-diagnosis-vs-validated-learning` and the two reviewed source cards `BK-0001-card-001` and `BK-0007-card-001`. This is a second run of the same condition.

## Output

Both of your colleagues are right — but right about different parts of your problem. The substrate I am using holds "diagnose first" and "experiment first" as a genuine, unresolved tension, and gives two conditions for telling which applies in a given situation: how legible the challenge is, and how cheaply you can test it. Your situation contains both kinds of challenge, so let me separate them.

The diagnosis posture comes from the source card `BK-0001-card-001`, on Rumelt's strategy kernel: a strategy's first element is a diagnosis that names what is critical — which presumes you have facts to interpret. The validated-learning posture comes from `BK-0007-card-001`, on Ries: when the customer and the value proposition are unknown, you cannot diagnose, you have to learn from real behaviour. These are evidence-level claims; the claim/tension card `strategy-diagnosis-vs-validated-learning` holds them in tension and crowns no winner. None of this is canon.

Your two parts:

**The clinics — the legible part.** Four years of tickets, churn interviews, and usage data. This challenge is legible: you can diagnose what is broken in clinic workflows from evidence you already hold. Diagnosis applies here, and your head of product should run it — cheaply, off existing data.

**The patients — the unknown part.** A customer you have never studied. Whether patients adopt a self-service portal, and whether clinics promote it, is not knowable from your clinic data; the facts a diagnosis needs do not exist yet. This is the validated-learning case. The second deciding condition points the same way: a test here is cheap and fast — two to three weeks, nothing built. When the load-bearing unknown is both unknowable in advance and cheap to probe, you probe it first.

So, the quarter:

- Weeks 1–3: run the patient-demand experiment — a fake-door or concierge pilot — and, in parallel, diagnose the clinic-workflow part from existing data. Little build capacity is spent.
- Then regroup. A positive demand signal means the rest of the quarter goes to building, now informed by both the workflow diagnosis and patient evidence. A weak signal means you have lost three weeks, not the quarter.

Two caveats. This is right for *your* specifics — a legible clinic side, an unknown patient side, cheap experiments. If experiments were slow and expensive, or if patient demand were already evidenced, the balance would move; neither posture is a universal rule. And the tension itself stays open — what is settled here is only where your situation sits, not the general question of whether diagnosis or experiment comes first.
