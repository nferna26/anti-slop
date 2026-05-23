---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v2
benchmark_version: diagnosis-vs-validated-learning-benefits-renewal-v2-v1
artifact: judge-packet-judge-instructions
status: frozen
note: This is the frozen judge prompt for the pending independent blind judge pass. Its sha256 is recorded in README.md and is what a future receipt should carry as judge_prompt_sha256.
---

# Independent Judge Instructions — Blind Pass

You are an independent judge scoring a contradiction-preservation eval. Your
single job is to score forty blinded answers against a fixed six-criterion
rubric. You are not running a model, not writing advice, and not deciding
anything about the knowledgebase the eval supports.

## What independence means here

You must be a different party from the one that generated these answers and
from the one that orchestrated the eval. If you are the same model family, the
same agent, or the same person as either, you are **not** an independent judge
— stop, and record that this pass still lacks an independent judge. The case
requires **at least two** blind judges from **different model families**;
record your identity and family honestly on the score sheet.

## What you are given

- `case-context.md` — the eval scenario, the advisor prompt the answers
  responded to, the expected reasoning, and the failure modes. Verbatim,
  condition-neutral excerpts of the frozen case.
- `rubric.md` — the six scoring criteria C1–C6 and the pre-registered criterion
  dependency rule, condition-neutral.
- `outputs/OUT-01.md` … `OUT-40.md` — forty model answers, each with a stable
  anonymous label. The condition that produced each answer, its run number, and
  its seed are withheld by design.
- `blank-score-sheet.md` — the sheet you fill in.
- `output-manifest.yaml` — each label's output body sha256, for later
  reconciliation. You do not need it to score.

## How to score

1. Read `case-context.md` and `rubric.md` in full before scoring any answer.
2. Score each `OUT-NN` independently, criterion by criterion, against the six
   rubric criteria C1–C6. Mark every cell `pass` or `fail`.
3. Apply the **pre-registered criterion dependency rule** in `rubric.md`
   exactly: if C5 fails, C6 must fail; if C4 fails, C6 should fail (and if you
   pass C6 while failing C4, record an explicit reason); C3 may pass even if C6
   fails. Do not invent other dependencies.
4. The total is the count of `pass` (0–6).
5. Score only the six rubric criteria. Do not invent, split, re-weight, or
   re-interpret criteria after reading the answers.
6. Score each answer on its own merits. Do not rank the answers against each
   other and do not let one answer's score influence another's. The comparison
   across answers is done later, by someone else, from your per-answer scores.
7. Write one short paragraph of reasoning per answer, naming which criteria
   passed and failed and why, grounded in the rubric wording.

## Prohibitions — do not let these drive a score

- **Condition identity.** You are not told which condition produced an answer.
  Do not try to deduce it, and if you form a guess, do not let it affect any
  score. Score the text in front of you.
- **Source familiarity.** Naming a famous author, a famous book, a famous
  framework, or a reference card is not itself a pass on any criterion. An
  answer that name-drops a recognised source but flattens the tension still
  fails `No flattening`. An answer that reasons correctly without naming
  anyone can still pass. Score the reasoning, not the citations.
- **Output length.** A longer or more elaborately formatted answer is not for
  that reason better. A short answer that meets a criterion passes it; a long
  answer that does not, fails. Length is never evidence.
- **House style.** Headings, bullet structure, and confident tone are not
  scored. Only the six criteria are.

## What to produce

Fill in `blank-score-sheet.md`: every cell C1–C6 for every `OUT-NN`, the totals,
your judge identity and model family, the sha256 of this instructions file
(from README.md), the date, and one short reasoning paragraph per output.
Return the filled sheet. Do not change any model output, the rubric, the case
context, or any eval Result or status — a judge scores; it does not promote.

A model output is a test artifact, never an authority. Your scores are evidence
about how those answers met a rubric — nothing more.
