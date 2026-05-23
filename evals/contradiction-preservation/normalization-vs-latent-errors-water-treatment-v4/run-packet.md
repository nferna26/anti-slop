---
case_id: normalization-vs-latent-errors-water-treatment-v4
artifact: run-packet
eval_type: contradiction-preservation
benchmark_version: normalization-vs-latent-errors-water-treatment-v4-v1
status: prepared_not_frozen_not_run
created: 2026-05-22
---

# Run Packet — normalization-vs-latent-errors-water-treatment-v4-v1

This is the prepared run packet for the v4 water-treatment contradiction
preservation case. It records the intended condition recipes, run parameters,
filler constraints, anonymisation rules, and external-judge plan.

**Status: prepared only — not frozen, not run.** The calibration anchors are
still `status: proposed_unreviewed`, so this packet cannot freeze a benchmark
version and no output generation may begin. A future freeze must update this
file with exact condition-packet hashes, equal-length filler word counts and
scan results, the generator model snapshot, accepted calibration-anchor hash,
and named eligible judge routes.

This file is operator-facing. It names model conditions and run mechanics. It
must not be shown to blind judges.

## Freeze blockers

The following must be true before `status` may change to a frozen state:

- `judge-packet/calibration-anchors.md` is operator-reviewed and set to
  `status: filled_pre_run`.
- At least two external eligible judge routes are named before generation. A
  judge route counts only if it is external to the orchestrating agent and did
  not author the v4 scenario, rubric, anchors, condition packets, or judge
  packet.
- The exact `vanilla_long_prompt` filler is generated, length-matched to the
  `substrate_workflow` added material within ±8%, and scanned clean against the
  forbidden vocabulary list below.
- All five condition packets are assembled byte-exactly and their `sha256`
  hashes are recorded in `## Freeze checklist`.
- The generator model and runtime snapshot are recorded.

## Prepared inputs

The future frozen pass will cover the case sections in `case.md` from
`## Scenario` through `## Anti-overfitting safeguards`, the declared
`model_conditions`, the reviewed lineage artifacts below, and the
operator-accepted calibration anchors.

Prepared lineage artifact `sha256`:

| Artifact | `sha256` |
| --- | --- |
| `corpus/claim-tension-cards/normalization-of-deviance-vs-latent-errors.md` | `f2741f834d5f7b3f21030339821040720b5d38a09a551603fcdc6004a1263dc1` |
| `corpus/source-cards/BK-0042-card-001.md` | `4b747866b13911b347d1a3acde4f98f7ba3577be978345818b7279464aad57c2` |
| `corpus/source-cards/BK-0044-card-001.md` | `e2a9014d3668ecf18ff3a82a685bf6d441a4ebb37f43e3500fe74900ba08c597` |
| `corpus/source-cards/BK-0044-card-002.md` | `20d496fec3e4aecf9ed38504bfedd82818da5f3a5d4704992f8d4c43fde9284f` |

## Advisor prompt

The Advisor prompt is derived deterministically from `case.md` -> `## Advisor
prompt`: take the block-quote lines, remove a leading `> ` from each line, turn
a line that is exactly `>` into an empty line, join with newlines, strip
leading/trailing whitespace, and append one trailing newline.

- Words: 311.
- Characters: 2024.
- `advisor_prompt_sha256`: `6844cf29154c9f73180d42ea5b7b83f475a0bada9ac7661eec61fbacfce5658f`.

At freeze and before every generation call, this hash must be recomputed. A
change opens a new benchmark version; it must not silently rebase v4-v1.

## Condition packets

Five conditions are declared in `case.md`. Each packet is the named added
material followed by one blank line and the verbatim Advisor prompt. The Advisor
prompt is byte-identical across conditions.

| Condition | Added material before the Advisor prompt |
| --- | --- |
| `vanilla` | None. Advisor prompt only. |
| `famous_sources_supplied` | Name-level list of relevant famous sources and decoys only; no claims or summaries. |
| `substrate_workflow` | Substrate preamble plus the reviewed tension card and three reviewed source cards. |
| `vanilla_long_prompt` | One-line note plus neutral equal-length filler plus transition. |
| `generic_advice_prompted` | Short generic advice-quality request; no rubric or source content. |

### Packet recipes

- **`vanilla`** — the Advisor prompt verbatim, nothing else.

- **`famous_sources_supplied`** — the frozen preamble below, then a blank line,
  then the Advisor prompt verbatim. The list supplies titles and authors only.
  It states no claim about what any source argues, supplies no source-card or
  tension-card content, marks no source as authoritative, and includes decoys.

  ```text
  The list below names some widely known works on safety, accidents, and
  organisational risk that are sometimes mentioned near questions like the one
  that follows. They are given by title and author only. Nothing here states or
  summarises what any work argues, and nothing here marks any title as relevant
  to, or authoritative for, the question below.

  - The Challenger Launch Decision — Diane Vaughan
  - Normal Accidents — Charles Perrow
  - Human Error — James Reason
  - Managing the Unexpected — Karl Weick and Kathleen Sutcliffe
  - The Field Guide to Understanding Human Error — Sidney Dekker

  The question follows.
  ```

- **`substrate_workflow`** — the frozen preamble below, then a blank line, then
  the four reviewed artifacts supplied as their full committed file content
  behind `--- ARTIFACT n of 4 ---` separators in this order: (1)
  `corpus/claim-tension-cards/normalization-of-deviance-vs-latent-errors.md`,
  (2) `corpus/source-cards/BK-0042-card-001.md`, (3)
  `corpus/source-cards/BK-0044-card-001.md`, (4)
  `corpus/source-cards/BK-0044-card-002.md`; then the transition line below;
  then the Advisor prompt verbatim.

  Preamble:
  ```text
  The reviewed artifacts below come from a public-safe knowledge base and may be
  useful background for the question that follows. Three are source cards:
  each is an evidence-level note that records one reviewed claim with a locator,
  paraphrase, scope conditions, and misuse risks. One is a claim/tension card:
  a synthesis-level note that relates reviewed source-card claims while keeping
  the tension open. None of these artifacts is canon, none is authoritative, and
  none settles the operational decision. Use them as evidence aids only. The
  question follows after the artifacts.
  ```

  Transition line: `That is the end of the reviewed artifacts. The question follows.`

- **`vanilla_long_prompt`** — the note below, then a blank line, then neutral
  equal-length filler, then the transition below, then the Advisor prompt
  verbatim. The filler must contain no substrate artifacts, no source names, no
  safety/water/utility/accident/risk content, and no advice-like content.

  Note line: `The text below is unrelated background reading on everyday subjects. It has no connection to the question that follows; it is included only as reading material. The question comes after it.`

  Transition line: `That is the end of the unrelated background reading. The question follows.`

- **`generic_advice_prompted`** — the frozen preamble below, then a blank line,
  then the Advisor prompt verbatim. It must not enumerate the rubric, name the
  two mechanisms, mention contradiction preservation, ask for source lineage, or
  leak the answer key.

  ```text
  Please give careful, practical advice on the question below. Take the
  tradeoffs seriously, explain your reasoning, and be honest about uncertainty.
  The question follows.
  ```

## Equal-length filler requirements

The `vanilla_long_prompt` filler is not generated in this prepared packet. At
freeze, generate a neutral filler body with these requirements:

- Distinct, non-repetitive everyday-topic paragraphs.
- Word count matches the `substrate_workflow` added-material word count within
  ±8%.
- Zero occurrences of these stems or close variants in the filler body:
  `safe`, `risk`, `accident`, `hazard`, `water`, `plant`, `utility`, `alarm`,
  `signal`, `filter`, `operator`, `manage`, `organis`, `normal`, `deviance`,
  `latent`, `defence`, `defense`, `error`, `diagnos`, `decid`, `decision`,
  `advice`, `advise`, `recommend`.
- If the scan is nonzero, discard the filler and regenerate before freeze.

## Run parameters

- Run count: eight real runs per condition minimum, five conditions x 8 = 40
  outputs. Ten runs per condition may be used only if recorded before freeze.
- Seeds: condition index follows the declared `model_conditions` order:
  `vanilla` (1), `famous_sources_supplied` (2), `substrate_workflow` (3),
  `vanilla_long_prompt` (4), `generic_advice_prompted` (5). Run `r`, condition
  `i` -> seed `r*100 + i`: 101-105 through 801-805 for the required eight runs.
  A timeout retry uses `seed + 10` and is recorded; no output is fabricated.
- Decoding: generation `temperature 0.7`, `top_p 0.9`, `num_ctx 32768`,
  timeout 600 s, held constant across all conditions and runs.
- Planned generator: `gemma4:31b`, pending freeze-time availability and runtime
  snapshot. If a different generator is used, it must be selected before freeze
  and held constant across all conditions.

## External judge routes

The v4 pass requires at least two eligible external blind judges from different
families/providers. Prepared routes:

- Judge A: hosted OpenAI model, operated by the human operator outside the
  orchestration session. Candidate: `gpt-5.4-mini` or successor explicitly
  recorded at judge time.
- Judge B: hosted Anthropic model or human third-party judge, operated outside
  the orchestration session and not involved in authoring the rubric, anchors,
  run packet, or judge packet.

A judge route is not eligible if it is in-session self-judging, authored the
anchors/reference verdicts, saw condition labels or the answer key before
scoring, failed calibration, or belongs to the generator family in a way that
violates the frozen judge protocol.

## Output, anonymisation, and answer key

- One public-safe model-output receipt per run under `model-outputs/`, with full
  benchmark provenance per `runs/model-outputs/_metadata-template.yaml`.
- Real outputs only; no simulations in the comparison set.
- After all outputs exist and before any judge sees them, hash each output body
  with `sha256`, sort ascending, and assign `OUT-01` through `OUT-NN`.
- The `OUT-NN` to condition answer key stays local-only and git-ignored. It is
  read only after all blind scoring is complete.
- Committed reconciliation is aggregate-only; no per-`OUT-NN` to condition
  mapping is committed.

## Judge-packet structure

After outputs are generated and anonymised, build a condition-blind
`judge-packet/` containing:

- `README.md`;
- `judge-instructions.md`;
- `case-context.md`;
- `rubric.md`;
- `calibration-exercise.md` containing only Surface 1 anchors;
- `output-manifest.yaml` with `OUT-NN` hashes but no conditions;
- `blank-score-sheet.md`;
- `outputs/OUT-01.md` through `outputs/OUT-NN.md`.

Do not copy Surface 2 reference verdicts, condition labels, seeds, run numbers,
model-output receipt paths, source-card IDs as metadata, or the answer key into
judge-facing files. If a model output body itself mentions a source ID, leave
the body unchanged and record that it is output text, not packet metadata.

## Freeze checklist

Fill these fields before changing `status` to frozen:

| Item | Value |
| --- | --- |
| Calibration-anchor status | pending — currently `proposed_unreviewed` |
| Calibration-anchor `sha256` | pending operator acceptance |
| Generator model and snapshot | pending |
| Judge route A | pending final model/operator record |
| Judge route B | pending final model/operator record |
| `vanilla` packet words / `sha256` | pending |
| `famous_sources_supplied` packet words / `sha256` | pending |
| `substrate_workflow` packet words / `sha256` | pending |
| `vanilla_long_prompt` packet words / `sha256` | pending |
| `generic_advice_prompted` packet words / `sha256` | pending |
| Filler word count and ratio | pending |
| Filler forbidden-vocabulary scan | pending |

## Current stop condition

Stop here until the calibration anchors are operator-reviewed. This prepared
packet exists to reduce freeze-time ambiguity; it is not a frozen benchmark
version and authorizes no output generation.
