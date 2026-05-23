---
artifact: judge-packet-readme
case_id: normalization-vs-latent-errors-water-treatment-v4
benchmark_version: normalization-vs-latent-errors-water-treatment-v4-v1
condition_blinded: true
---

# Judge Packet — normalization-vs-latent-errors-water-treatment-v4-v1

This is the condition-blind judge packet for the contradiction-preservation eval
`normalization-vs-latent-errors-water-treatment-v4`. It is public-safe. It holds
everything a blind judge needs to score the run's anonymised answers, and
nothing that would reveal how any answer was produced.

## Judge-facing files

- `judge-instructions.md` — how to judge: the calibration step, the scoring
  steps, and the rules.
- `case-context.md` — the scenario, the question every answer responds to, what
  a good answer must do, and the failure modes.
- `rubric.md` — the six binary criteria C1-C6 and the mandatory criterion
  dependency rule.
- `calibration-exercise.md` — the calibration exercise (Surface 1): three
  illustrative answers to score before scoring the real outputs. It contains no
  reference verdicts.
- `outputs/OUT-01.md` through `outputs/OUT-40.md` — the anonymised answers to be
  scored.
- `output-manifest.yaml` — the map from each `OUT-NN` label to the sha256 of its
  answer body, for integrity checking. It carries no origin information.
- `blank-score-sheet.md` — the template a judge fills, one row per `OUT-NN`.
- `independent-judge-packet-calibration.md` — copy-paste-ready Part 1 for an
  external judge: calibration only, with a hard stop before scoring.
- `independent-judge-packet-scoring.md` — copy-paste-ready Part 2 for an
  external judge that has cleared calibration: all 40 anonymised outputs plus
  the return format.

## Operator-only files (not judge-facing)

- `calibration-anchors.md` — the full calibration artifact. It contains the
  Surface 2 reference verdicts for the three calibration anchors. **It is
  operator-only.** A judge sees `calibration-exercise.md` (Surface 1) and must
  not be shown the reference verdicts until after submitting the calibration
  grid. Do not read `calibration-anchors.md` while judging.
- `operator-calibration-check.md` — operator-only instructions for comparing an
  external judge's Part 1 answer against the withheld reference verdicts before
  releasing Part 2.

## Blind protocol

- Every answer in `outputs/` responds to the same question. The answers are
  labelled `OUT-NN` in the ascending order of their body sha256, so the order
  carries no information about origin.
- No judge-facing file names, hints at, or lets a judge reconstruct how any
  answer was produced.
- A judge scores each `OUT-NN` against `rubric.md` only, criterion by criterion,
  applying the dependency rule, after passing the calibration exercise.
- The map from `OUT-NN` to its producing origin is kept out of this packet
  entirely; it is local-only and never committed.

## Discipline note

A model output is a test artifact — never an authority, never citable as a
source. This packet supports scoring; it sets no eval `## Result` and promotes
nothing.
