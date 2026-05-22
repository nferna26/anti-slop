---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v2
artifact: run-packet
eval_type: contradiction-preservation
benchmark_version: diagnosis-vs-validated-learning-benefits-renewal-v2-v1
status: prepared_not_frozen_not_run
created: 2026-05-21
---

# Run Packet — diagnosis-vs-validated-learning-benefits-renewal-v2-v1

A **prepared** run packet for a future frozen benchmark run of the eval case in
this folder. It records the condition packet recipes, the equal-length filler
recipe, the run parameters, the output / anonymisation / answer-key rules, and
the judge-packet protocol — and a freeze checklist of the fields that must be
filled, before any output is generated, to turn this preparation into a frozen
pass.

**This run packet is operator-facing.** It names the model conditions because
it is the operator's run specification; it is **not** part of the blind judge
packet, and a judge never sees it. The blind, condition-anonymised materials a
judge does see are described in `## Judge-packet protocol` below.

## Status

**Prepared — not frozen, not run.** No model has been run for this case; no
model outputs exist under `model-outputs/`; nothing is scored. `score-sheet.md`
→ `## Result` is `partial`. This packet does not freeze the case by itself: the
freeze happens when the `## Freeze checklist` below is completed at run time,
immediately before the first output is generated. Preparing this packet
promotes nothing and changes no Result or status.

## Frozen inputs

The benchmark pass freezes, and does not edit during the run: `case.md` —
`## Scenario`, `## Advisor prompt`, `## Expected reasoning`, `## Failure modes`,
`## Scoring rubric`, `## Criterion dependency rule`, `## Positive result`,
`## Falsifier`, `## Judge protocol`, `## Anti-overfitting safeguards`, and the
`model_conditions` list — and the three reviewed lineage artifacts named in
`case.md` → `## Lineage` (`strategy-diagnosis-vs-validated-learning`,
`BK-0001-card-001`, `BK-0007-card-001`) at their committed head as of the
freeze. Any edit to a frozen input starts a new benchmark version
(`…-v2-v2`); it does not silently re-base `…-v2-v1`.

## Advisor prompt

The Advisor prompt is the one frozen input locked now. It is derived
deterministically from `case.md` → `## Advisor prompt`: take the block-quote
lines, remove a leading `> ` from each (a line that is exactly `>` becomes an
empty line), join with newlines, strip leading/trailing whitespace, append a
single trailing newline.

- **Words:** 271. **Characters:** 1537.
- **`advisor_prompt_sha256`:** `a1e406feb5014a857769f9c72edb5a0ac54afabbca59e72121fca0337b6e1d17`

At freeze time this hash is recomputed and must match; if `case.md`'s Advisor
prompt has changed, the freeze stops and a new benchmark version is opened.

## Condition packets

Five conditions. Each packet is the named added material followed by the
**verbatim Advisor prompt**. The Advisor prompt is byte-identical across all
five; the condition is the only deliberate variable.

| Condition | Added material before the Advisor prompt |
|---|---|
| `vanilla` | None. The Advisor prompt alone. |
| `famous_sources_supplied` | A two-paragraph preamble, name-level only. |
| `substrate_workflow` | A substrate preamble + the three reviewed artifacts, verbatim. |
| `vanilla_long_prompt` | The equal-length filler (see `## Equal-length filler recipe`). |
| `criteria_prompted_no_sources` | A paraphrased statement of the six rubric qualities, no sources. |

### Packet recipes (deterministic)

- **`vanilla`** — the Advisor prompt verbatim, nothing else.
- **`famous_sources_supplied`** — a two-paragraph preamble, then a blank line,
  then the Advisor prompt verbatim. Paragraph 1 states, as a widely-cited
  principle, that purposeful work should begin by judging what is genuinely
  critical about a confusing situation before committing to a course of
  action. Paragraph 2 states, as a widely-cited principle, that a team facing
  deep uncertainty about what will work should make progress by running cheap
  tests against real-world behaviour rather than committing to an untested
  plan. Name-level awareness only: no source card, no claim/tension card, no
  card text, no quotation, no book or author named.
- **`substrate_workflow`** — a short preamble naming the artifacts and their
  authority levels (source cards are evidence-level, the claim/tension card is
  synthesis-level, none of it is canon, the tension is explicitly open), then
  the three reviewed artifacts supplied verbatim in order behind
  `--- ARTIFACT n of 3 ---` separators — (1)
  `corpus/claim-tension-cards/strategy-diagnosis-vs-validated-learning.md`,
  (2) `corpus/source-cards/BK-0001-card-001.md`, (3)
  `corpus/source-cards/BK-0007-card-001.md` — each at its committed head as of
  the freeze, then a one-line transition, then the Advisor prompt verbatim.
- **`vanilla_long_prompt`** — a one-line note that unrelated background
  follows, then the equal-length filler (see next section), then a one-line
  transition, then the Advisor prompt verbatim. No reviewed substrate artifact,
  no claim/tension card, no source card.
- **`criteria_prompted_no_sources`** — a preamble that paraphrases, in neutral
  language, the six qualities a good answer should have — keep both competing
  readings of the situation live; anchor in the scenario's specific facts;
  preserve the objection from each reading; do not flatten to one move or a
  vague "both"; reach a recommendation that confronts the binding constraint,
  names the strongest reason against itself, and states disconfirming evidence
  — then a blank line, then the Advisor prompt verbatim. The preamble names no
  book, author, framework, source ID, or card ID, and supplies **no** source
  card and **no** claim/tension card. This control isolates a substrate effect
  from a mere being-told-the-criteria effect.

## Equal-length filler recipe

The `vanilla_long_prompt` filler is a neutral, topic-free body that matches the
length of the `substrate_workflow` added material so a substrate advantage
cannot be a more-tokens effect.

- **Structure.** N **distinct, non-repetitive** neutral paragraphs — one per
  everyday topic, no two paragraphs alike (repetition triggered a generation
  loop in an earlier case).
- **Topic set** (everyday, sensory, non-topical): clouds, rivers, tides, bread
  baking, brewing tea, hand-brewed coffee, coastal-path walking, moon phases, a
  vegetable patch, autumn leaves, snow, morning birdsong, stargazing, pottery,
  a rainy afternoon, mountain weather, a quiet beach, cycling a country lane,
  reading paper maps, woodworking, knitting, a lake at dawn, deserts, a forest
  floor, kite flying, sandcastles, paper folding, jigsaw puzzles, beekeeping,
  shells and pebbles. Add further everyday topics if more length is needed.
- **Forbidden vocabulary.** The assembled filler is scanned and must contain
  **zero** occurrences of, and of close variants of: strategy / strategic,
  learn / learning, startup, organisation / organization / organisational,
  management / manage / manager, diagnosis / diagnose / diagnostic,
  experiment / experimentation / experimental, benefit / benefits, budget /
  budgets, pilot / pilots, and decision / decide / advice / advise / recommend.
  A nonzero scan stops the freeze.
- **Length rule.** The filler's word count matches the `substrate_workflow`
  **added-material** word count (the substrate preamble plus the three
  artifacts — everything in that packet beyond the Advisor prompt) within
  **±8%**. The match is computed and recorded at freeze.

## Run parameters

- **Run count.** Three real runs per condition for the `…-v2-v1` benchmark
  pass — five conditions × 3 = **15 outputs** minimum; five runs per condition
  preferred if feasible. Single-run results are not a benchmark pass.
- **Seeds (deterministic).** Condition index 1–5 in the order `vanilla`,
  `famous_sources_supplied`, `substrate_workflow`, `vanilla_long_prompt`,
  `criteria_prompted_no_sources`. Run *r*, condition *i* → seed `r*100 + i`:
  run 1 = 101–105, run 2 = 201–205, run 3 = 301–305 (run 4 = 401–405, run 5 =
  501–505 if used). A call that times out is re-attempted on a fresh
  deterministic seed (`seed + 10`), recorded as such, never fabricated.
- **Decoding.** Generation `temperature 0.7`, `top_p 0.9`, held constant across
  all conditions and runs. Per-call timeout 600 s.
- **Generator model.** One fixed real model, held constant across every
  condition and run, so the model condition is the only deliberate variable. A
  local model via a local runtime is the default. The exact generator model ID
  and snapshot/digest are recorded in the `## Freeze checklist` at freeze time.
  The generator must be a different model family from every planned judge (see
  `## Judge-packet protocol`).

## Output, anonymisation, and answer key

- **Output naming.** One file per run under `model-outputs/`, named
  `<condition>` for run 1 and `<condition>-NN` for later runs (`-02`, `-03`).
  Each file records full provenance per `runs/model-outputs/_metadata-template.yaml`
  — provider/runtime, model ID and snapshot, decoding params, per-run seed,
  prompt and condition-packet `sha256`, output path, and the run vs simulation
  status. Real runs only; no simulated outputs.
- **Anonymisation rule.** After all outputs exist and **before any judge sees
  them**, each output body is hashed with `sha256` and the outputs are sorted
  in ascending hash order; labels `OUT-01 … OUT-NN` are assigned in that order.
  The hash-sorted order carries no condition information.
- **Answer-key locality.** The `OUT-NN` → condition map is written **only** to
  the case's local-only run folder (git-ignored). It is **never** committed and
  is not read until after blind scoring is complete (see `score-sheet.md` →
  `## Post-reconciliation condition aggregate`).

## Judge-packet protocol

At run time a **condition-blind** judge packet is built (committed, public-safe)
containing: frozen judge instructions naming no condition; condition-neutral
case-context excerpts; a condition-neutral copy of the `## Scoring rubric`; the
anonymised `OUT-NN` outputs; an output-hash manifest (`OUT-NN` → body `sha256`);
and a blank score sheet (`OUT-NN` rows × C1–C6). No judge-facing file in that
packet carries a condition label.

Per `case.md` → `## Judge protocol`: at least two blind judges from different
model families (a human judge or a two-model panel of different families is
required), criterion-level pass/fail scoring on every `OUT-NN` with the
pre-registered `## Criterion dependency rule` applied, a third independent judge
triggered on a C5/C6 disagreement or a margin disagreement, and a judge-sensitive
outcome held at `partial`.

## Freeze checklist

To be completed at run time, **before any output is generated**. The freeze is
not complete — and no model may be run — until every box is checked.

- [ ] Generator model ID and snapshot/digest recorded below.
- [ ] All five condition packets assembled per `## Condition packets`; each
      packet's word count and `sha256` recorded in the table below.
- [ ] `vanilla_long_prompt` filler assembled; forbidden-vocabulary scan returns
      zero hits; filler word count within ±8% of the `substrate_workflow`
      added-material word count — both recorded.
- [ ] `advisor_prompt_sha256` recomputed and matches
      `a1e406feb5014a857769f9c72edb5a0ac54afabbca59e72121fca0337b6e1d17`.
- [ ] `case.md` frozen inputs (see `## Frozen inputs`) confirmed unchanged
      since this packet; if changed, a new benchmark version is opened.
- [ ] Freeze timestamp recorded.

| Condition | Packet word count | Packet `sha256` | Seeds (runs 1–3) |
|---|---|---|---|
| `vanilla` | _freeze_ | _freeze_ | 101 / 201 / 301 |
| `famous_sources_supplied` | _freeze_ | _freeze_ | 102 / 202 / 302 |
| `substrate_workflow` | _freeze_ | _freeze_ | 103 / 203 / 303 |
| `vanilla_long_prompt` | _freeze_ | _freeze_ | 104 / 204 / 304 |
| `criteria_prompted_no_sources` | _freeze_ | _freeze_ | 105 / 205 / 305 |

Generator model ID: _freeze_ — snapshot/digest: _freeze_ — freeze timestamp: _freeze_.

## Formatting rehearsal

Before this packet was prepared, a **formatting-only** rehearsal was run
local-only — packet assembly, output-capture file shape, `OUT-NN`
anonymisation, and blind judge-packet shape were exercised end to end on a
**different, throwaway synthetic scenario** (not the benefits-renewal Advisor
prompt) with placeholder, non-model outputs. It confirmed the mechanics; it
generated no real model output, scored nothing, and its artifacts are
git-ignored under the case's local-only run folder. The final benefits-renewal
Advisor prompt was **not** run.

## Discipline note

This packet prepares a run; it does not perform one. No model output exists, no
score exists, `## Result` stays `partial`, and no canon or authority follows
from this file. A model output, when it exists, will be a test artifact — never
an authority, never citable as a source.
