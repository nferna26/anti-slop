---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v2
benchmark_version: diagnosis-vs-validated-learning-benefits-renewal-v2-v1
artifact: judge-packet-readme
judge_status: prepared_not_judged
frozen_judge_prompt_sha256: 512a889d1a7e208e4085053c2fd2e7beeea50cb6a7bda1008090f99e3fffa142
---

# Independent-Judge Packet — diagnosis-vs-validated-learning-benefits-renewal-v2

This is the condition-blinded packet for an **independent blind judge pass** of
the contradiction-preservation eval in the parent folder, benchmark version
`diagnosis-vs-validated-learning-benefits-renewal-v2-v1`. It is prepared but
**not yet judged**: no judge has scored it, and nothing here changes the case's
`## Result`, which is `partial`.

The case has forty real `gemma4:31b` model outputs — eight runs each of five
conditions. This packet lets a genuinely independent judge score those forty
answers without knowing which condition produced which answer.

## What is in the packet

- `judge-instructions.md` — the frozen judge prompt: the judge's role, the
  scoring procedure, the criterion dependency rule, and the prohibitions.
  Frozen; sha256
  `512a889d1a7e208e4085053c2fd2e7beeea50cb6a7bda1008090f99e3fffa142` (recorded
  in this file's frontmatter as `frozen_judge_prompt_sha256`). A receipt for an
  independent pass should carry this hash as `judge_prompt_sha256`.
- `case-context.md` — verbatim, condition-neutral excerpts of the frozen
  `case.md`: the scenario, the advisor prompt, the expected reasoning, and the
  failure modes. The case's `What this eval tests`, `Lineage`, and
  `Expected source behavior` sections are withheld — they describe the
  conditions and would defeat the blinding.
- `rubric.md` — the six scoring criteria C1–C6 and the pre-registered criterion
  dependency rule, as a condition-neutral excerpt of the frozen `case.md` (the
  six criteria are verbatim; run-mechanics sentences are trimmed so the copy
  carries no condition labels).
- `outputs/OUT-01.md` … `OUT-40.md` — the forty model answers, each behind a
  stable anonymous label. The output bodies are verbatim and unaltered; the
  generating condition, run number, and seed are withheld. Labels are assigned
  in ascending order of each answer's body sha256, so the order carries no
  condition information.
- `output-manifest.yaml` — `OUT-NN` → output body sha256. Public-safe; carries
  no condition identity.
- `blank-score-sheet.md` — the sheet the independent judge fills in.

## Blinding and reconciliation

The blinding is procedural: no file in this packet labels an answer with its
condition, and `judge-instructions.md` forbids the judge from using a guessed
condition, source-name familiarity, or output length as grounds for a score.
The output bodies are unaltered, so a reader who consults `../model-outputs/`
could de-anonymise them — the judge is trusted not to, exactly as a blind
review depends on the reviewer not breaking the seal.

After an independent judge returns `blank-score-sheet.md`, reconcile each
`OUT-NN` back to its condition with the **answer key**, which is kept
local-only (git-ignored) and is not part of this packet. The `output_sha256`
in `output-manifest.yaml` is the bridge: re-hash any `../model-outputs/` answer
body and match it to a label.

## Status

Prepared, not judged. The case's `## Judge protocol` requires at least two
blind judges from different model families (none of them the agent that
orchestrated this eval, and none of them the generator's family — the
generator was `gemma4:31b`, so the judges must be non-Gemma), criterion-level
scoring with the pre-registered dependency rule, a third-judge trigger on a
C5/C6 or margin disagreement, and judge-sensitive outcomes held at `partial`.
Until that judging is done, the case stays `partial`. A model output is a test
artifact, never an authority.
