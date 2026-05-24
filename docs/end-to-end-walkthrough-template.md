# End-to-End Walkthrough — Template

This is a fill-in-the-blanks walkthrough an operator (or an agent reading the repo for the first time) can use to trace one source from acquisition to public receipt. Copy this file when running a real walkthrough; do not edit it in place.

The walkthrough has nine stations. Each station names its artifact, its authority level, its workflow doc, and the lint or gate that catches errors at that stage.

## 0. Choose a source

- **Source candidate:** [book title, author, year]
- **Why this source for this walkthrough:** [one sentence — diversity, contradiction value, eval relevance]
- **Manifest entry status:** [not-yet-added / drafted / in manifest]
- **Acquisition status:** [unknown / sourced / verified-lawful]
- **Workflow:** [acquisition-workflow.md](acquisition-workflow.md)

## 1. Manifest entry

- **File:** `corpus/manifests/books-200.yaml`
- **Authority:** metadata only
- **Schema:** `corpus/manifests/schema.yaml`
- **Lint:** `make validate`
- **Outcome:** [pass / fail + fix notes]

## 2. Book map

- **File:** `corpus/book-maps/<slug>.md`
- **Authority:** discovery aid (not canon)
- **Helper:** `python3 scripts/new_book_map.py <source_id>`
- **Workflow:** [book-map-workflow.md](book-map-workflow.md)
- **Outcome:** [pass / fail + fix notes]

## 3. Source card

- **File:** `corpus/source-cards/<slug>.md`
- **Authority:** evidence (not canon)
- **Helper:** `python3 scripts/new_source_card.py <source_id>`
- **Workflow:** [source-card-workflow.md](source-card-workflow.md)
- **Operator verification recorded in:** [registry/ entry]
- **Outcome:** [pass / fail + fix notes]

## 4. Claim or tension card

- **File:** `corpus/claim-tension-cards/<slug>.md`
- **Authority:** synthesis (not canon)
- **Helper:** `python3 scripts/new_claim_tension_card.py <slug>`
- **Workflow:** [claim-tension-card-workflow.md](claim-tension-card-workflow.md)
- **Contradiction preserved with:** [other card id, if applicable]
- **Outcome:** [pass / fail + fix notes]

## 5. Canon candidate (optional)

- **File:** `corpus/canon-candidates/<slug>.md`
- **Authority:** proposal
- **Helper:** `python3 scripts/new_canon_candidate.py <slug>`
- **Workflow:** [canon-promotion-workflow.md](canon-promotion-workflow.md)
- **Decision (if any) recorded in:** [registry/ entry]
- **Outcome:** [pass / fail / deferred + notes]

## 6. Eval case

- **File:** `evals/<family>/<case_id>.md`
- **Authority:** test, not advice
- **Helper:** `python3 scripts/new_eval_case.py <eval_type> <case_id>`
- **Workflow:** [eval-methodology.md](eval-methodology.md)
- **Eval family:** [bibliographic-adversary / contradiction-preservation / canon-promotion-tournament / long-tail-transfer / source-lineage-hostile]
- **Outcome:** [pass / fail + notes]

## 7. Gate run

- **File:** `runs/gate-logs/<run_id>.yaml`
- **Authority:** test, not advice
- **Helper:** `python3 scripts/new_gate_log.py <run_id>`
- **Workflow:** [gate-methodology.md](gate-methodology.md)
- **Gates exercised:** [citation-lineage / source-diversity / canon-duplication / contradiction / quote-limit / authority-order / no-universalization]
- **Outcome:** [pass / fail + notes]

## 8. Log entry

- **File:** `kb/log.md`
- **Authority:** chronological record
- **Required:** dated entry naming what changed in this walkthrough.
- **Template:** see the bottom of `kb/log.md`.

## After the walkthrough

- Cross-link the source card from `kb/index.md` if the source surfaces a content category not previously listed.
- Open a new tension card if the source surfaced a disagreement not previously recorded.
- Record any deferred decisions in `registry/`.
- Run `make validate && make check-raw && make kb-lint` and fix any failures before commit.

## What a complete walkthrough proves

- The substrate handled one real source end-to-end without raw text leaking into the public tree.
- The artifact chain (manifest → map → card → tension → candidate → eval → gate → log) held together under operator review.
- The methodology produced a public receipt the operator would defend.

A walkthrough that stops short of an eval or gate run is incomplete — it shows the ingest loop without showing the proof loop. Note such truncations explicitly in section 8.
