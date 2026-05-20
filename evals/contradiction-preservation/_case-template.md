---
case_id:
eval_type: contradiction-preservation
status: draft
created:
source_packet:
expected_output:
model_conditions:
  - vanilla
  - famous_sources_supplied
  - substrate_workflow
  - optional_local_model
scoring_status: unscored
---

# Eval Case

## What this eval tests

This eval tests whether an advisor preserves a real tension between sources instead of flattening it into a false consensus — and, where a scenario's specifics favour one side, whether it reasons from those specifics rather than defaulting to a familiar framework.

## Lineage

<!-- The substrate artifacts this case derives from. Public-safe references only:
     the reviewed claim/tension card this case operationalises, and the reviewed
     source cards under it. One per line as <ref> — <brief note>, with the authority
     level named. No book maps as evidence, no raw source text, no private paths. -->

## Scenario

<!-- A synthetic, public-safe operator situation. Invented — not drawn from a real
     person or company — with no raw book text and no private detail. Build it so
     the tension under test actually bites: the right move depends on specifics the
     answer has to read. -->

## Advisor prompt

<!-- The exact prompt given to the advisor/model. Self-contained, and phrased as a
     real operator would ask it — it does not name the sources or frameworks. -->

## Expected reasoning

<!-- What a good answer must do: the reasoning steps and distinctions it must show.
     For a tension case, this includes naming both readings and locating the
     scenario against the claim/tension card's deciding conditions. -->

## Expected source behavior

<!-- How the substrate and sources should be used across model_conditions, and what
     correct lineage and attribution look like. -->

## Failure modes

<!-- The traps: the specific wrong answers this case is built to catch — flattening
     to one side, framework-default, misattribution, false consensus. -->

## Scoring rubric

<!-- The criteria an answer is scored on, and what passes or fails each. -->

## Positive result

<!-- What an answer that confirms the substrate's value looks like. -->

## Falsifier

<!-- What an answer would look like if the substrate did not help — the result that
     would refute this eval's hypothesis. -->

## Model outputs

<!-- One file per run under model-outputs/. A model output is never an authority. -->

## Score sheet

<!-- Pointer to score-sheet.md in this case folder; filled by the judge. -->

## Judge notes
