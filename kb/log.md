# Anti-Slop KB Log

This is the chronological memory layer for public-safe KB changes.

## 2026-05-20

- Repaired the first source card `corpus/source-cards/BK-0048-card-001.md`: grounded it in the local Chapter 4 source by reading and verifying the chapter (the halo-effect chapter of Rosenzweig, *The Halo Effect*), rather than promoting the claim from the book map. Confirmed the Chapter 4 boundary against the source. Corrected the Operator notes and the Supports section so the BK-0048 book map is named only as a discovery aid that located the chapter, not as the card's authority; removed the "operator-reviewed evidence unit" and "upgrades map note to evidence" framing. `operator_review_status` remains `unreviewed`; `Short excerpt` remains `None.`; no source prose, quotes, or private paths added.
- Operator approved `corpus/source-cards/BK-0048-card-001.md` as a reviewed source card (`anti-slop-source-card` Workflow 4). Lifted `operator_review_status` from `unreviewed` to `reviewed` in frontmatter and Operator notes; applied the non-blocking wording polish from the Workflow 3 review (clarified that the Chapter 4 / Chapter 9 parenthetical in the BK-0001 tension entry refers to BK-0048 locators). First reviewed source card in the substrate. `Short excerpt` remains `None.`; no source prose, quotes, or private paths added; no claim/tension card or canon candidate created.
- Drafted the second source card: `corpus/source-cards/BK-0001-card-001.md` (BK-0001, *Good Strategy Bad Strategy*, Chapter 5 — the strategy kernel: diagnosis, guiding policy, coherent action). `claim_type: method`, `operator_review_status: unreviewed`, `publication_status: metadata_public`. Drafted via `anti-slop-source-card` Workflow 2; grounded in the local Chapter 5 source (read in full, chapter boundary confirmed), with the BK-0001 book map used only to locate the chapter. Paraphrase + chapter locator only; `Short excerpt: None.`; no raw book text, quotes, or private paths. No claim/tension card or canon candidate created.
- Reworded the Claim and Paraphrase of `corpus/source-cards/BK-0001-card-001.md` after the Workflow 3 review flagged close paraphrase: replaced near-verbatim Chapter 5 wording runs with independent paraphrase so the card's `Short excerpt: None.` / no-source-prose statement is accurate. Meaning, claim boundary, locator, `claim_type`, relation sections, scope, misuse risk, and `operator_review_status: unreviewed` all unchanged. No source prose, quotes, or private paths added; no claim/tension card or canon candidate created.
- Operator approved `corpus/source-cards/BK-0001-card-001.md` as a reviewed source card (`anti-slop-source-card` Workflow 4), after a Workflow 3 re-review confirmed all twelve checks pass. Lifted `operator_review_status` from `unreviewed` to `reviewed` in frontmatter and Operator notes. Claim, paraphrase, locator, relation sections, scope, and misuse risk unchanged. Second reviewed source card in the substrate. No source prose, quotes, or private paths added; no claim/tension card or canon candidate created.
- Drafted the third source card: `corpus/source-cards/BK-0042-card-001.md` (BK-0042, *The Challenger Launch Decision*, Chapter 10, pp. 404–439 — normalization of deviance). `claim_type: mechanism`, `operator_review_status: unreviewed`, `publication_status: metadata_public`. Drafted via `anti-slop-source-card` Workflow 5; grounded in the local Chapter 10 source (read in full, page range pp. 404–439 confirmed), with the BK-0042 book map used only to locate the chapter. Paraphrase + page-range locator only; `Short excerpt: None.`; no raw book text, quotes, or private paths. No claim/tension card or canon candidate created.

## 2026-05-19

- Created books-kb scaffold.
- Archived legacy-v0 state under `_archive/legacy-v0-2026-05-19/`.
- Added publication policy: no raw copyrighted text in the public repo.
- Added manifest, card, eval, gate, run, registry, and public-post scaffolds.
- Reframed the project as a Karpathy-style maintained Markdown knowledgebase.
- Added `kb/index.md` and `kb/log.md` conventions.
- Added `AGENTS.md` (root) as the maintenance contract for any agent touching the repo.
- Added `docs/kb-maintenance-contract.md` as the operational expansion of `AGENTS.md`.
- Added `docs/front-door-quality-gate.md` explaining what `make kb-lint` enforces.
- Added `docs/end-to-end-walkthrough-template.md` as a fill-in walkthrough skeleton.
- Hardened `scripts/kb_lint.py` to check for `AGENTS.md`, required README sections, no "Archived Legacy Work" section, and raw-source extensions in public Markdown.
- CORE-909: Populated `corpus/manifests/books-200.yaml` with all 200 books. The full 200-book list was operator-provided in the CORE-909 prompt. Stable IDs BK-0001 through BK-0200. Validator passes.
- CORE-910: Locked the first-50 priority wave at IDs BK-0001 through BK-0050; added `corpus/manifests/source-id-registry.yaml` listing wave-1 with title, author, slug, priority rank, map-candidate flag, and deep-card-candidate flag.
- Recorded 43 books with public-safe `local filename evidence present; edition unverified` notes (27 within wave-1, 16 in the broader corpus). No raw file paths or filenames were copied into the public manifest.
- Review pass: tightened rights status on BK-0020 (Shape Up) and BK-0046 (To Err Is Human). Both moved from `raw_source_status: public_domain` (unverified rights overclaim) to `metadata_only`, with notes that rights/access status needs operator verification. BK-0047 (On War) kept as nuanced — original 1832 work is PD, local artifact is a copyrighted modern translation.
- Phase 0 closeout: added `docs/operator-roles.md`, `docs/local-source-shelf.md`, `docs/artifact-definitions.md`, `docs/public-writing-rules.md`, `docs/wip-limits.md`, `docs/phase-0-closeout.md`.
- Phase 1 closeout: generated `corpus/manifests/acquisition-registry.yaml` (200 entries, 1:1 with the manifest, public-safe rights/access view). Added `docs/phase-1-closeout.md`.
- Tooling: added `scripts/validate_acquisition_registry.py` (checks 1:1 IDs, no raw paths, boolean fields, deep-card alignment) and `scripts/manifest_report.py` (public-safe counts and wave-1 progress). Updated `Makefile` so `make validate` covers both manifests and added `make report`.
- Lint: hardened `scripts/check_no_raw_text.py` to emit clearer informational text for the two structured-manifest paths that legitimately exceed the size heuristic; did not weaken raw-text detection or broaden the allowlist.
- Source ID registry: added `first_30_deep_card_candidate` flag for the 30 wave-1 IDs identified in the playbook. Existing `map_candidate` and `deep_card_candidate` sets unchanged.
- Baseline commit created: `e417681` (`chore: initialize books-kb scaffold`).
- Phase 2 starter lane: added `docs/phase-2-readiness.md`, `corpus/manifests/phase-2-verification-queue.yaml`, and `make phase2-queue`. First verification batch is BK-0001, BK-0003, BK-0007, BK-0042, and BK-0048.
- BK-0001 verification: operator verified public-safe front-matter metadata for Rumelt, `Good Strategy Bad Strategy`; updated manifest/acquisition registry with Profile Books Ltd, 2011, eISBN metadata, `epub` owned format, and `chapter_section` locator. Created public-safe noncanonical book-map shell at `corpus/book-maps/BK-0001.md`.
- Drafted the first public-safe book map body for `corpus/book-maps/BK-0001.md` (Rumelt, *Good Strategy Bad Strategy*). Status remains `machine_generated_not_canon`, `operator_review_status: unreviewed`, `quote_word_count: 0`. Paraphrase + chapter-locator references only; no raw book text, no quotes, no private paths included.
- BK-0001 book-map review fixes: filled in verified Source metadata (Profile Books Ltd, 2011, ISBN 978-1-84765-746-6, epub, chapter_section); switched all locator references from `Part X / Chapter N` to chapter-only form since part dividers are not preserved in the extracted markdown; rewrote Possible contradictions as tensions/questions to investigate (no assertions about comparison sources). Frontmatter unchanged.
- BK-0003 verification: operator verified public-safe front-matter metadata for Bryar and Carr, `Working Backwards`; updated manifest/acquisition registry with St. Martin's Press, 2021, eISBN metadata, `epub` owned format, and `chapter_section` locator. Created public-safe noncanonical book-map shell at `corpus/book-maps/BK-0003.md`.
- Drafted the public-safe book map body for `corpus/book-maps/BK-0003.md` (Bryar & Carr, *Working Backwards*). Status remains `machine_generated_not_canon`, `operator_review_status: unreviewed`, `quote_word_count: 0`, `locator_confidence: medium`. Paraphrase + chapter-locator references only; Possible contradictions phrased as tensions/questions to investigate; locator_quality_note flags heterogeneous heading levels for operator verification before source-card creation. No raw book text, no quotes, no private paths included.
- Phase 2 verification: operator approved BK-0007 bibliographic metadata (`The Lean Startup`, Ries, Eric). Set edition, year, publisher, ISBN, `epub` owned format, and `chapter_section` locator in `books-200.yaml`; lifted `edition_verified` to true and `locator_confidence` to verified in `acquisition-registry.yaml`. No raw text, raw paths, or raw filenames added to the public repo.
- Phase 2 verification: operator approved BK-0042 paperback bibliographic metadata (`The Challenger Launch Decision`, Vaughan, Diane). Set edition, year, publisher, ISBN `0-226-85176-1`, `pdf` owned format, and `pdf_page` locator in `books-200.yaml`; lifted `edition_verified` to true and `locator_confidence` to verified in `acquisition-registry.yaml`. No raw text, raw paths, or raw filenames added to the public repo.
- Phase 2 verification: operator approved BK-0048 bibliographic metadata (`The Halo Effect`, Rosenzweig, Phil). Set edition `first edition (2007)`, year `2007`, publisher `Free Press`, ISBN `978-1-4165-3858-5`, `epub` owned format, and `chapter_section` locator in `books-200.yaml`; lifted `edition_verified` to true and `locator_confidence` to `medium` in `acquisition-registry.yaml`. Phase-2 queue updated to map-ready. No raw text, raw paths, or raw filenames added to the public repo.
- First-five book maps BK-0001, BK-0003, BK-0007, BK-0042, and BK-0048 operator-reviewed after cleanup; `operator_review_status` lifted to `reviewed` in each map and the phase-2 queue; source-card selection may begin (one card at a time with operator review per card); `quote_word_count` remains 0; no raw text or private paths added.
- Drafted the first source card: `corpus/source-cards/BK-0048-card-001.md` (BK-0048, *The Halo Effect*, Chapter 4 — the halo effect proper). `claim_type: mechanism`, `operator_review_status: unreviewed`, `publication_status: metadata_public`. Filled the new schema rails (issue_or_question, claim_type, Supports, Tensions with, Qualifies). Paraphrase + chapter locator only; `Short excerpt: None.`; no raw book text, quotes, or private paths. Built from the operator-reviewed BK-0048 book map.

## Log Entry Template

```md
## YYYY-MM-DD

- Ingested:
- Mapped:
- Carded:
- Tension preserved:
- Gate run:
- Eval run:
- Decision:
- Rejected/deferred:
- Follow-up:
```
