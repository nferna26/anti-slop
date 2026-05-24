# Anti-Slop books-kb

Anti-Slop books-kb is a governed Markdown knowledgebase for making AI-assisted advice inspectable before it becomes operational.

## Objective

Build a citation-traceable, contradiction-aware advisory substrate from a sourced 200-book corpus.

The claim is deliberately narrow:

> A maintained knowledgebase with source lineage, contradiction handling, deterministic gates, and operator approval can reduce slop compared with vanilla model use and vanilla model use with famous manually supplied sources.

This repo proves the method, not possession of books.

## Why

AI can sound strategic while quietly failing at the parts that matter: fabricated lineage, famous-source defaults, flattened contradictions, universal advice from narrow cases, and no audit trail for what changed the recommendation.

Anti-Slop turns that into a workflow:

```text
source -> map -> card -> preserve tension -> propose canon -> test -> publish receipts
```

The point is not to make AI sound more informed. The point is to make advice accountable: what sources were allowed, what claims were rejected, what contradictions remained unresolved, what gates failed, and what changed in the KB.

## What This Is

This is a Karpathy-style persistent Markdown knowledgebase, not a prompt pack and not query-time RAG.

- Raw sources stay local-only.
- Public-safe Markdown pages compound over time.
- Maps and cards organize source lineage.
- Tension cards preserve disagreement instead of smoothing it away.
- Canon requires explicit operator approval.
- Evals and gates test whether the method beats simpler baselines.

## What This Is Not

- Not a public archive of copyrighted book text.
- Not a raw document dump.
- Not a vector store of book contents.
- Not a replacement for the books.
- Not a claim that 200 books automatically make AI advice better.

Canon Patch Trial is prior context only. It is not the active workstream and not a gate.

## Publication Rule

Raw copyrighted book text must never be committed.

No PDFs, EPUBs, MOBIs, AZW files, OCR dumps, extracted text, copied chapters, long excerpts, public raw-text prompts, or public embeddings of copyrighted source text.

Public artifacts are receipts: metadata, locators, short conservative excerpts when necessary, paraphrases, cards, evals, gate logs, model-output metadata, decisions, and methodology notes.

## Authority Order

- Book maps are discovery aids, not canon.
- Source cards are evidence units, not canon.
- Claim/tension cards are synthesis units, not canon.
- Canon candidates are proposals.
- Canon requires operator approval.

Machine-generated maps or summaries must never become hidden canon.

## Proof Surface

The first eval families:

- bibliographic adversary
- contradiction preservation
- canon promotion tournament
- long-tail transfer
- source-lineage hostile

The first gates:

- citation-lineage
- source-diversity
- canon-duplication
- contradiction
- quote-limit
- authority-order
- no-universalization

Positive evidence requires more than a better-sounding answer. It requires fewer critical failures, better source fit, better contradiction preservation, and better gate compliance than baselines.

See [proof/README.md](proof/README.md).

## Start

Current status: Phase 0 (scaffold + rules) and Phase 1 (manifest + acquisition registry) closed. `corpus/manifests/books-200.yaml` carries the operator-provided 200-book corpus. `corpus/manifests/source-id-registry.yaml` locks wave-1 at BK-0001 through BK-0050. `corpus/manifests/acquisition-registry.yaml` carries the public-safe rights/access view.

Run:

```sh
make validate
make check-raw
make kb-lint
make report
```

Create artifacts:

```sh
python3 scripts/new_book_map.py <source_id>
python3 scripts/new_source_card.py <source_id>
python3 scripts/new_claim_tension_card.py <slug>
python3 scripts/new_canon_candidate.py <slug>
python3 scripts/new_eval_case.py <eval_type> <case_id>
python3 scripts/new_gate_log.py <run_id>
```

Next useful path:

1. Verify rights/access for BK-0020 and BK-0046 (currently `raw_source_status: metadata_only`).
2. Verify edition / publisher / ISBN / year for the wave-1 books with local filename evidence; lift `edition_verified` in the acquisition registry.
3. Pick a locator scheme per source; lift `locator_confidence` from `none` only on verification.
4. Create the first public-safe book map (start with a wave-1 map candidate).
5. Run gates.
6. Log the result in `kb/log.md`.

## Repo Map

- `kb/`: maintained Markdown KB, index, log, question and synthesis templates.
- `corpus/`: manifests, maps, source cards, tension cards, canon candidates.
- `canon/`: operator-approved concepts, patterns, guardrails, and playbooks.
- `evals/`: proof-surface cases.
- `gates/`: gate definitions.
- `proof/`: claims, baselines, proof thresholds, and falsifiers.
- `runs/`: model-output metadata, gate logs, and score sheets.
- `registry/`: accepted, rejected, deferred, and retired decisions.
- `scripts/`: local validation and artifact helpers.

## Claim Boundary

This project does not yet prove that Anti-Slop improves advice. It provides the scaffold for testing that claim.

If evals show no meaningful delta over simpler baselines, the method should narrow or reset.
