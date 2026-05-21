---
case_id: managerial-output-vs-industry-structure
benchmark_version: managerial-output-vs-industry-structure-v1
artifact: judge-packet-judge-instructions
status: frozen
note: This is the frozen judge prompt for the pending independent blind judge pass. Its sha256 is recorded in README.md and is what a future receipt should carry as judge_prompt_sha256.
---

# Independent Judge Instructions — Blind Pass

You are an independent judge scoring a contradiction-preservation eval. Your
single job is to score fifteen blinded answers against a fixed rubric. You are
not running a model, not writing advice, and not deciding anything about the
knowledgebase the eval supports.

## What independence means here

You must be a different party from the one that generated these answers and
from the one that orchestrated the eval. If you are the same model family,
the same agent, or the same person as either, you are **not** an independent
judge — stop, and record that this pass still lacks an independent judge.
Record your identity honestly on the score sheet (`judge identity`): a model
ID and family, a human, or a two-judge panel. Do not describe a non-independent
judge as independent.

## What you are given

- `case-context.md` — the eval scenario, the advisor prompt the answers
  responded to, the expected reasoning, and the failure modes. Verbatim,
  condition-neutral excerpts of the frozen case.
- `rubric.md` — the five scoring criteria, verbatim from the frozen case.
- `outputs/OUT-01.md` … `OUT-15.md` — fifteen model answers, each with a
  stable anonymous label. The condition that produced each answer, its run
  number, and its seed are withheld by design.
- `blank-score-sheet.md` — the sheet you fill in.
- `output-manifest.yaml` — each label's output body sha256, for later
  reconciliation. You do not need it to score.

## How to score

1. Read `case-context.md` and `rubric.md` in full before scoring any answer.
2. Score each `OUT-NN` independently, criterion by criterion, against the five
   rubric criteria. Mark every cell `pass` or `fail`. The total is the count
   of `pass` (0–5).
3. Score only the five rubric criteria. Do not invent, split, or add criteria.
   Do not change a criterion's meaning after reading the answers.
4. Score each answer on its own merits against the rubric. Do not rank the
   answers against each other and do not let one answer's score influence
   another's. The comparison across conditions is done later, by someone else,
   from your per-answer scores.
5. Write one short paragraph of reasoning per answer, naming which criteria
   passed and failed and why, grounded in the rubric wording.

## Prohibitions — do not let these drive a score

- **Condition identity.** You are not told which condition produced an answer.
  Do not try to deduce it, and if you form a guess, do not let it affect any
  score. Score the text in front of you.
- **Source familiarity.** Naming a famous author, a famous framework, or a
  card or artifact is not itself a pass. An answer that cites a recognised
  name but flattens the attribution still fails `No flattening`. An answer that
  reasons correctly without naming anyone can still pass. Score the reasoning,
  not the citations. Note: `Lineage and authority discipline` is about whether
  ideas are attributed at the right level and not wielded as a question-ending
  authority — it is not a reward for name-dropping.
- **Output length.** A longer or more elaborately formatted answer is not for
  that reason better. A short answer that meets a criterion passes it; a long
  answer that does not, fails. Length is never evidence.
- **House style.** Headings, bullet structure, and confident tone are not
  scored. Only the five criteria are.

## What to produce

Fill in `blank-score-sheet.md`: every cell, the per-output totals, your
judge identity, the sha256 of this instructions file (from README.md), the
date, and the per-output reasoning. Return the filled sheet. Do not change any
model output, the rubric, the case context, or any eval Result or status — a
judge scores; it does not promote.

A model output is a test artifact, never an authority. Your scores are evidence
about how those answers met a rubric — nothing more.
