---
case_id: managerial-output-vs-industry-structure
benchmark_version: managerial-output-vs-industry-structure-v1
artifact: judge-packet-readme
judge_status: prepared_not_judged
frozen_judge_prompt_sha256: 691eec0e5b28111e75fef6e7ffc05355dc41dc5f8b800ad64bc3de963ef26a44
---

# Independent-Judge Packet — managerial-output-vs-industry-structure

This is the condition-blinded packet for an **independent blind judge pass** of
the contradiction-preservation eval in the parent folder. It is prepared but
**not yet judged**: no independent judge has scored it, and nothing here changes
the case's `## Result`, which stays `partial`.

The case has fifteen real `qwen3.5:latest` model outputs (three runs each of
five conditions). The current scores in `../score-sheet.md` were produced by a
model-family-separated judge that was also the agent orchestrating the eval —
not an independent third-party judge. This packet exists so a genuinely
independent judge can re-score the same answers without knowing which condition
produced which answer.

## What is in the packet

- `judge-instructions.md` — the frozen judge prompt: the judge's role, the
  scoring procedure, and the prohibitions. Frozen; sha256
  `691eec0e5b28111e75fef6e7ffc05355dc41dc5f8b800ad64bc3de963ef26a44` (recorded
  in this file's frontmatter as `frozen_judge_prompt_sha256`). A receipt for
  the independent pass should carry this hash as `judge_prompt_sha256`.
- `case-context.md` — verbatim, condition-neutral excerpts of the frozen
  `case.md`: what the eval tests, the scenario, the advisor prompt, the
  expected reasoning, and the failure modes. The `Lineage` and
  `Expected source behavior` sections are withheld — they name the conditions.
- `rubric.md` — the five scoring criteria, verbatim from the frozen `case.md`.
- `outputs/OUT-01.md` … `OUT-15.md` — the fifteen model answers, each behind a
  stable anonymous label. The output bodies are verbatim and unaltered; the
  generating condition, run number, and seed are withheld. The labels are
  assigned in ascending order of each answer's body sha256, so the order
  carries no condition information.
- `output-manifest.yaml` — `OUT-NN` → output body sha256. Public-safe: it
  carries no condition identity.
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
in `output-manifest.yaml` is the bridge: re-hash any `../model-outputs/`
answer body and match it to a label.

## Status

Prepared, not judged. Running the pass requires an independent judge — a
different model family, a human, or a two-judge panel, none of them the agent
that orchestrated this eval. Until that judge scores the packet and its
independence is affirmatively recorded, the case stays `partial` and is not
eligible for `benchmark_supported`. A model output is a test artifact, never
an authority.
