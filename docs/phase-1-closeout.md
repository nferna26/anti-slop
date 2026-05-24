# Phase 1 Closeout

Phase 1 was the manifest-and-registry phase: stand up the substrate's source list, lock the priority wave, and add a public-safe rights/access view alongside the metadata. This doc records what closed and what remains manual.

## What is closed

### Manifest

- `corpus/manifests/books-200.yaml` is populated from the operator-provided 200-book list.
- All 200 source IDs (BK-0001 through BK-0200) are stable and independent of acquisition order.
- 200 entries × 18 fields each, all required fields present, `make validate` passes.
- `legal_rule: no_raw_copyrighted_text_in_public_repo` preserved.

### Wave-1 lock

- BK-0001 through BK-0050 are the locked first-50 priority wave.
- `corpus/manifests/source-id-registry.yaml` carries `priority_rank`, `title`, `author`, `slug`, `wave`, `map_candidate`, `deep_card_candidate`, and `first_30_deep_card_candidate` for each wave-1 ID.
- The 10 map candidates and 5 deep-card candidates match the playbook exactly.
- The 30 first-30 deep-card candidates from the playbook are flagged.

### Acquisition registry

- `corpus/manifests/acquisition-registry.yaml` holds one entry per manifest source_id (1:1).
- Each entry records: `edition_verified` (boolean), `locator_scheme` (empty until verified), `locator_confidence` (none), `rights` block (excerpt policy + caps + public-safe rights note), `local_source_status` block (boolean presence flag plus three null fields by design), `processing_status` block (mapped, source_cards_started, deep_card_candidate, canon_candidate_exists).
- No raw file paths or filenames appear in the registry.
- `raw_text_public_allowed` is `false` for all 200 entries.

### Rights/access conservatism

- BK-0020 (Shape Up) and BK-0046 (To Err Is Human) carry `raw_source_status: metadata_only` with notes that rights/access status needs operator verification. The earlier `public_domain` claim was an unverified overclaim and has been withdrawn.
- BK-0047 (On War) is nuanced: the original 1832 work is public domain, but the locally evidenced artifact is a copyrighted modern translation. Notes call this out.
- Every entry's rights note states "requires operator verification" unless the rights are unambiguously commercial (local-only) or already noted conservatively.

### Tooling

- `scripts/validate_acquisition_registry.py` — checks 1:1 IDs, no raw paths, boolean field discipline, deep-card alignment.
- `scripts/manifest_report.py` — public-safe status report.
- `make validate` runs both manifest validations.
- `make report` prints the status report.
- `scripts/check_no_raw_text.py` recognizes the two structured manifests and emits a clearer informational warning for their legitimate size; the raw-text detection logic is unchanged.

### Docs

- `docs/phase-0-closeout.md`, `docs/phase-1-closeout.md`.
- `docs/operator-roles.md`, `docs/local-source-shelf.md`, `docs/artifact-definitions.md`, `docs/public-writing-rules.md`, `docs/wip-limits.md`.
- `docs/acquisition-workflow.md` updated to point at the source-id-registry as the wave-1 priority order.

## What remains manual

These are decisions or one-off verifications that only the operator can make.

- **Edition verification.** No entry has `edition_verified: true` yet. The 43 books with `local filename evidence present; edition unverified` are the most efficient pool to verify first.
- **Locator scheme.** All entries have an empty `locator_scheme`. Operator decides per source: "chapter/section/page", "page only", "section number", or another. `locator_confidence` lifts from `none` only with explicit verification.
- **Rights/access verification.** BK-0020 and BK-0046 are the most urgent. After those, the wave-1 books in `tier: MM` whose acquisition status is `not_started` are the next acquisition batch.
- **First map.** No book maps exist yet (Phase 2). The wave-1 map candidates are the natural first targets.
- **First source cards.** No source cards exist yet (Phase 2). The wave-1 deep-card candidates and first-30 deep-card candidates are flagged.

## What is explicitly NOT in scope for Phase 1

- Building book maps. (Phase 2.)
- Drafting source cards from book content. (Phase 2.)
- Authoring claim or tension cards. (Phase 2.)
- Promoting anything to canon. (Phase 3+.)
- Running model evals. (Phase 3+.)

## How Phase 2 should start

1. Verify rights/access for BK-0020 and BK-0046, then update their acquisition registry entries.
2. Verify edition / publisher / ISBN / year on the wave-1 books with local filename evidence; lift `edition_verified: false` to `true` for those.
3. Pick the next acquisition batch from wave-1 `acquisition_status: not_started` entries.
4. Once at least one wave-1 book has `edition_verified: true` and an operator-decided `locator_scheme`, the first book map can begin (per `docs/book-map-workflow.md`).
5. Run `make validate && make check-raw && make kb-lint && make report` after each batch.

## Verifying Phase 1 closeout locally

```sh
make validate
make check-raw
make kb-lint
make report
python3 -m py_compile scripts/*.py
```

All five should pass. `make check-raw` will emit an informational warning on the two structured manifests (curated metadata, not raw text); that warning is expected and documented in `docs/front-door-quality-gate.md`.
