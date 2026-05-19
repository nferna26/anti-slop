# Artifact Definitions

This is the glossary of every public-safe artifact in books-kb. Each definition names what the artifact is, what it is not, what authority level it carries, and which workflow doc governs it.

The artifact ladder, from lowest authority to highest:

| # | Artifact | Authority | Lives in |
|---|---|---|---|
| 1 | Manifest entry | metadata | `corpus/manifests/books-200.yaml` |
| 2 | Acquisition registry entry | rights/access tracking | `corpus/manifests/acquisition-registry.yaml` |
| 3 | Book map | discovery aid | `corpus/book-maps/<slug>.md` |
| 4 | Source card | evidence | `corpus/source-cards/<slug>.md` |
| 5 | Claim / tension card | synthesis | `corpus/claim-tension-cards/<slug>.md` |
| 6 | Canon candidate | proposal | `corpus/canon-candidates/<slug>.md` |
| 7 | Canon entry | advisory | `canon/...` |
| — | Eval case | test, not advice | `evals/<family>/<case_id>.md` |
| — | Gate log | test, not advice | `runs/gate-logs/<run_id>.yaml` |
| — | Model output | test, not advice | `runs/model-outputs/<run_id>.md` |
| — | Accepted/rejected diff | receipt | `registry/<decision>.md` |

## 1. Manifest entry

One row per source in `books-200.yaml`. Carries identity (source_id, author, title), category, status_tag, availability_tier, acquisition_status, publication_status, raw_source_status, optional bibliographic fields (edition, year, publisher, ISBN), eval relevance flags, rationale, notes.

Not canon. Not a claim about the source's argument. Just enough to plan ingest.

Schema: `corpus/manifests/schema.yaml`. Validator: `scripts/validate_manifest.py`.

## 2. Acquisition registry entry

One row per source in `acquisition-registry.yaml`. Carries the rights/access view alongside the manifest's metadata view. Fields cover `edition_verified`, `locator_scheme`, `locator_confidence`, `rights.*` (excerpt policy + caps), `local_source_status.*` (boolean presence flags only — no paths, no filenames), and `processing_status.*`.

Not canon. Not a substitute for the manifest. The two are joined by `source_id` and must be in 1:1 correspondence.

Validator: `scripts/validate_acquisition_registry.py`. The strict ban: `raw_file_path_public` and `local_locator_key` never carry raw paths or filenames.

## 3. Book map

A public-safe overview of one source: parts, chapters, sections, key terms, recurring patterns. Designed to make the source's structure legible without leaking its content. Helps the operator (and later the methodology) find pages worth carding.

Discovery aid only. A book map's claim about what a chapter argues is a discovery hint, not an evidence assertion. Workflow: `docs/book-map-workflow.md`.

## 4. Source card

One claim from one source, with the locator (chapter/section/page) and a conservative paraphrase or short excerpt. Each card cites the source and stays within the per-source excerpt budget defined in `legal-publication-policy.md` and the per-card cap in the acquisition registry.

Evidence unit. Not synthesis. A source card never says "and the right rule is X" — it says "this source claims X, on these pages, in this context."

Workflow: `docs/source-card-workflow.md`.

## 5. Claim / tension card

A synthesis layered above source cards. Names a claim and cites the source cards that ground it. A tension card preserves disagreement: card A says X, card B says Y, the disagreement is not yet resolved and that fact is itself recorded.

Synthesis unit. Not canon. Tension cards explicitly stay in the substrate when the evidence is split — the methodology refuses to flatten the disagreement.

Workflow: `docs/claim-tension-card-workflow.md`.

## 6. Canon candidate

A proposed elevation of a claim from synthesis to canon. Includes the candidate rule, the source cards and claim/tension cards that ground it, the cases it covers, the cases it does not cover, the open questions, and the alternative formulations considered.

Proposal only. Drafting a candidate does not make it canon. The candidate sits in `corpus/canon-candidates/` until accepted, rejected, or deferred.

Workflow: `docs/canon-promotion-workflow.md`.

## 7. Canon entry

An operator-approved advisory claim. Lives in `canon/concepts/`, `canon/patterns/`, `canon/guardrails/`, or `canon/playbooks/`. Cites source cards. Names contradictions it does not resolve. Names scope.

Advisory. Canon entries are the only public-safe artifacts in the repo that carry an operator-approved advisory authority. Every other artifact is substrate, evidence, synthesis, test, or receipt.

Canon promotion is recorded in `registry/` with the decision rationale.

## Eval case, gate log, model output, accepted/rejected diff

These are the proof-surface artifacts. They test whether the substrate actually produces inspectable advice — they do not themselves carry advice.

- **Eval case**: a frozen test artifact. Source packet, expected facts, rubric, traps.
- **Gate log**: deterministic pass/fail per gate per run.
- **Model output**: the raw response from a model on a given case. Never an authority. Always citable but not citable as a source.
- **Accepted/rejected diff**: the receipt for what changed (or did not change) in the KB after a case was scored. Lives in `registry/`.

## What is not an artifact

- A prompt that produced a useful answer is not an artifact unless it lives inside an eval case.
- A model output that "looked right" is not an artifact unless it has a gate log and a judge score.
- An idea jotted in `kb/log.md` is a log entry, not a card, not a candidate, not canon.
