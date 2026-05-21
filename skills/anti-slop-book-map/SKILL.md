---
name: anti-slop-book-map
description: Six-workflow book-map pipeline for the books-kb, now with map-lite and deep-map classes. v1 is judgment rails — Claude follows the discipline by hand. No automation yet.
---

# anti-slop-book-map

This skill encodes the hand-rolled workflow used for BK-0001 (Rumelt, *Good Strategy Bad Strategy*) and BK-0003 (Bryar & Carr, *Working Backwards*) — operator-approval packets, applying verified metadata, drafting public-safe map-lite or deep book maps, and reviewing maps for drift. It is judgment rails, not a tooling framework. There are no `.py` scripts; Claude follows the discipline by reading the relevant workflow section and the matching template.

## When to invoke

The operator names one of the six workflows. Claude opens this file, reads the matching `## Workflow N` section, follows the steps using the named template, and runs the closing-gate suite if the workflow touches public files. The operator is the sign-off authority for every public write.

## Workflow selector

| Workflow | Section | Writes public? |
|---|---|---|
| `prepare-operator-approval` | `## Workflow 1` | No |
| `apply-verified-metadata` | `## Workflow 2` | Yes |
| `draft-book-map` | `## Workflow 3` | Yes |
| `review-book-map` | `## Workflow 4` | No (unless operator approves each fix) |
| `batch-metadata-verify` | `## Workflow 5` | No |
| `batch-map-draft` | `## Workflow 6` | Yes |

## Shared contract

Every workflow inherits these rules. A workflow that violates any of them must stop and surface to the operator.

- **Raw source text stays local-only.** Public files contain metadata, paraphrase, locators, questions, and receipts only. Chapter labels and bibliographic metadata are not "quotes" and may appear in public files.
- **Book maps are noncanonical discovery artifacts.** Public book-map frontmatter must carry `status: machine_generated_not_canon`, `operator_review_status: unreviewed`, `canonical_status: noncanonical`, `quote_word_count: 0`.
- **Comparison sources are questions to investigate, never claims.** In `## Possible contradictions`, every row's "Question to investigate" cell is phrased as `Compare BK-XXXX's … with BK-YYYY on …` or `Question whether/how …`. Never use assertion verbs (`treats`, `argues`, `rejects`, `claims`, `says`, `proves`, `shows`) attributed to comparison authors. Map inferences are labeled in-line with `(map inference)` or equivalent.
- **`quote_word_count: 0` by default.** Do not quote source prose. The single allowed YAML-style "quoted" strings are bibliographic metadata (`title:`, `author:`) and named concept labels (e.g. `"Diagnosis / guiding policy / coherent action"`), nothing more.
- **No `git add` or `git commit` unless the operator explicitly requests it.** The skill runs the closing-gate suite (read-only `make` targets and `git diff --check`), reports the result, and stops.
- **No model or API calls.**
- **No private paths or source filenames in any public file.** Paths under `local-only/`, `extracted-md/`, `/Users/`, `Desktop/`, and the `Archive.zip` shelf bundle never appear in public artifacts. Filename extensions for EPUB, PDF, MOBI, AZW, AZW3, DJVU, CBZ, and CBR formats are similarly blocked — `scripts/kb_lint.py` carries the exact regex. Public/local discipline is enforced by hand and by `make kb-lint`.
- **`books_200_yaml.owned_format` is a canonical public value.** Allowed values are bare lowercase tokens like `epub`, `pdf`, `mobi`, `print`, or `audiobook`. Never include conversion-tool detail in this field — phrases like `"ebook (PDF) extracted via pdftotext -layout"` belong in the local-only `approval-summary.md` and `quality-audit.md`, not in any public manifest value. The same rule applies to the book map's `owned format` line in `## Source metadata`: render the verified canonical token verbatim. Conversion tool, conversion status, and extraction signals are extraction *evidence* and stay under the local-only "Extraction / conversion quality" sections.

## Map classes

Book maps now have two depth classes. The class controls how much reviewer attention the map is allowed to consume; it does not change authority. Both classes remain public-safe discovery aids with `status: machine_generated_not_canon`.

- **Map-lite** is the default for first-50 breadth. It records verified metadata, locator scheme, a compact source-structure note, 3-5 candidate source-card claims, 3-5 candidate tensions, eval relevance, misuse risks, and operator notes. Use it when the immediate goal is coverage and triage.
- **Deep map** is the current full map shape. Use it for anchors, source-id registry `map_candidate` / `deep_card_candidate` sources, or operator-selected books expected to yield multiple source cards, tensions, or evals.

Do not upgrade a map-lite to a deep map just because it is available to draft. Upgrade only when the operator or `make first50-queue` identifies a reason.

## Workflow 1 — prepare-operator-approval

**When to use it.** Producing an operator-approval packet for a single source whose local extraction is ready (i.e., `local-only/extracted-md/<source_id>/source.md` exists and the conversion status is `ok`).

**Inputs.**
- `corpus/manifests/books-200.yaml` (the row for `source_id`)
- `corpus/manifests/acquisition-registry.yaml` (the row for `source_id`)
- `local-only/extracted-md/<source_id>/source.md` (read only the first ~50 lines for front-matter signals; never read body prose)
- `local-only/extracted-md/<source_id>/conversion-metadata.json` (for tool, status, format)
- `corpus/book-maps/BK-0001.md` and `BK-0003.md` as accepted-quality references
- `templates/approval-summary.md.tmpl`, `templates/proposed-public-update.yaml.tmpl`, `templates/operator-checklist.md.tmpl`, `templates/quality-audit.md.tmpl`

**Outputs (local-only).**
- `local-only/phase-2-verification/<source_id>/operator-approval/approval-summary.md`
- `local-only/phase-2-verification/<source_id>/operator-approval/proposed-public-update.yaml`
- `local-only/phase-2-verification/<source_id>/operator-approval/operator-checklist.md`
- `local-only/phase-2-verification/<source_id>/operator-approval/quality-audit.md`

**Pre-checks.**
- `source_id` resolves to exactly one row in both manifests. If 0 or >1 matches, stop and surface.
- `local-only/extracted-md/<source_id>/source.md` exists and is non-empty.
- The output directory does not already contain a packet. If it does, stop and surface — overwriting a prior packet erases prior operator decisions.

**Steps.**

1. **Snapshot the public registry state.** Read the BK-XXXX row from `books-200.yaml` and from `acquisition-registry.yaml`. Record the current values verbatim into the approval-summary's "Current public registry state" section. Do not edit the public files.
2. **Inspect the front-matter region only.** Open `source.md` and read the first ~50 lines (or until you hit body prose — whichever comes first). Look for: ISBN-13 strings (pattern: `978-` followed by 10 digits, optionally hyphenated); copyright-style year lines (`© YYYY`, `Copyright YYYY`, `First published YYYY`); publisher names (compare against the `publisher:` set already used in `books-200.yaml`); edition statements. Do not read body prose. Do not copy any extracted text into the public artifact later.
3. **Audit conversion quality.** Count H1/H2/H3/H4 headings across the whole file. Check for: form-feed page-break chars (`\x0c`); standalone numeric lines that resemble print page numbers (`^\s*\d{1,4}\s*$`); Unicode replacement characters (`�`); control chars in the first 200 KB (`ord(c) < 0x20 and c not in '\n\r\t\x0c'`); camelCase-style word joins (OCR signal). Record the counts in `quality-audit.md`.
4. **Decide the candidate locator scheme.** If H2/H3/H4 form a clean nested hierarchy and form-feed = 0, propose `chapter_section`. If form-feeds or standalone numeric lines appear, note that print-page locators are an option (record as fallback, not default). Note whether `parts_present` is supported by extraction (if `Part [IVX]+` strings appear only in body prose and not in headings, parts did NOT survive — the locator scheme stays chapter-only).
5. **Render the four template files.** Fill each `*.tmpl` against the extracted candidate metadata and audit signals. In `proposed-public-update.yaml`:
   - Top-level guards: `operator_approval_required: true`, `do_not_apply_without_operator_approval: true`.
   - Both YAML blocks present (`books_200_yaml:`, `acquisition_registry_yaml:`).
   - `edition_verified: false` with inline comment "set true only after operator approval".
   - `raw_text_public_allowed: false` (validator enforces).
   - `raw_file_path_public: null`.
   - `local_locator_key: "<source_id>-local-source"` (public-safe alias; never a path).
   - `kb_log_note:` a single-line public-safe string.
6. **Hand-check the packet.** Search each output file for path markers (`/Users/`, `Desktop`, the `Archive.zip` shelf bundle) and the blocked raw-source format extensions named in the Shared contract. None should appear. Verify `raw_file_path_public: null` and the two top-level guards in the YAML.

**Output template.** Templates 1–4 in this skill's `templates/` directory.

**Reference fixtures.** `local-only/phase-2-verification/BK-0001/operator-approval/*` and `local-only/phase-2-verification/BK-0003/operator-approval/*` are the accepted shape.

**On failure.** Pre-check failures stop the workflow and surface to the operator (do not produce a partial packet). Hand-check failures at step 6 surface the offending line and the operator decides whether to fix or abandon.

## Workflow 2 — apply-verified-metadata

**When to use it.** The operator has reviewed an approval packet and signed off. The skill applies the proposal to public files.

**Inputs.**
- `local-only/phase-2-verification/<source_id>/operator-approval/proposed-public-update.yaml`
- An explicit operator approval signal in the prompt (e.g., "operator approves BK-XXXX with ISBN <xxx>, publisher <yyy>").
- `corpus/manifests/books-200.yaml`
- `corpus/manifests/acquisition-registry.yaml`
- `corpus/manifests/phase-2-verification-queue.yaml` (if the source is listed there)
- `kb/log.md`

**Outputs (public).**
- One row updated in `corpus/manifests/books-200.yaml`.
- One row updated in `corpus/manifests/acquisition-registry.yaml`.
- If the source appears in `corpus/manifests/phase-2-verification-queue.yaml`, one queue row updated from verification-needed to map-ready.
- One bullet appended in `kb/log.md` under the most recent dated entry.

**Pre-checks.**
- Operator approval signal present in the prompt. Refuse without it.
- `proposed-public-update.yaml` contains both top-level guards.
- `source_id` matches exactly one row in each YAML file. If 0 or >1, stop and surface.

**Steps.**

1. **Read the proposal.** Extract the `books_200_yaml:` and `acquisition_registry_yaml:` blocks and the `kb_log_note:` string from the proposal file. Note which fields are present — only those fields will be edited.
2. **Locate the books-200.yaml row.** Find the line `  - source_id: <source_id>` (exact match, two-space indent). Verify exactly one occurrence. The row ends at the next `  - source_id:` line or EOF.
3. **Apply books-200.yaml edits.** Within the bounded row range, update only the keys named in `books_200_yaml:` block. Preserve the existing indentation and quoting style (e.g. if the row uses `"value"` double-quoted strings, the replacement uses double-quoted strings). Do not touch keys not named in the proposal.
4. **Locate the acquisition-registry.yaml row.** Same procedure: `  - source_id: <source_id>` exact match, one occurrence required.
5. **Apply acquisition-registry.yaml edits.** Within the bounded row range, update only keys named in `acquisition_registry_yaml:` at their correct parent-key path (e.g. `rights.rights_notes_public` is inside the `rights:` block, not at row top-level). If the proposal's `acquisition_registry_yaml.edition_verified` is `false` (the default), leave the registry's value as `false` unless the operator has explicitly approved lifting it to `true` in their approval signal. The `local_locator_key` value lifts from `null` to the proposed alias only if the operator approved that lift.
6. **Update the Phase 2 queue if present.** If `source_id` appears in `corpus/manifests/phase-2-verification-queue.yaml`, update only that row: `edition_verified: true`, `locator_status: chosen`, and `next_operator_action:` to the next map-drafting action using the verified locator scheme. If the source is absent from the queue, skip this step.
7. **Append to kb/log.md.** Find the most recent `## YYYY-MM-DD` heading. Append `- <kb_log_note>` as a new bullet under it. If today's date heading does not exist yet, create it at the top of the file (newest-first convention) and add the bullet under it. Do not edit existing bullets.
8. **Run the closing-gate suite.** See `## Commands to run` below. All gate steps must pass. If any fails, print the failure and stop — do not roll back, because the operator decides whether to revert manually.

**Output template.** Not applicable — this workflow edits existing files surgically.

**Reference fixtures.** The BK-0001 and BK-0003 commits that landed verified metadata into `books-200.yaml`, `acquisition-registry.yaml`, and `kb/log.md`.

**On failure.** Ambiguous row match → abort. Missing operator approval signal → abort. Closing-gate failure post-edit → surface, do not auto-revert. Wrong YAML block edited (e.g. applied to `books_200_yaml`'s top-level when the value belonged under `acquisition_registry_yaml.rights:`) → abort and surface; this is the "wrong YAML block" review-checklist item.

## Workflow 3 — draft-book-map

**When to use it.** A source has verified metadata (Workflow 2 has been applied; `acquisition-registry.yaml` row has `edition_verified: true` and `locator_scheme` populated). The skill drafts a public map-lite or deep book map.

**Inputs.**
- The verified row in `corpus/manifests/books-200.yaml`.
- The verified row in `corpus/manifests/acquisition-registry.yaml`.
- `local-only/extracted-md/<source_id>/source.md` — read only the heading structure (collect H1/H2/H3/H4 headings as a structural outline). Do not read body prose.
- `corpus/book-maps/BK-0001.md` and `BK-0003.md` as accepted-quality references.
- `templates/map-lite.md.tmpl` for map-lite or `templates/book-map.md.tmpl` for a deep map.

**Outputs (public).**
- `corpus/book-maps/<source_id>.md`.

**Pre-checks.**
- `acquisition-registry.yaml` row for `source_id` has `edition_verified: true` and a non-empty `locator_scheme`. If not, point the operator to Workflow 2.
- The book map already exists as a shell at `corpus/book-maps/<source_id>.md` (created by `scripts/new_book_map.py`) or does not exist. If a fully-drafted map already exists, refuse to overwrite — review the existing map via Workflow 4 instead.

**Steps.**

0. **Choose the map class before reading local structure.** Use the operator's explicit `map_class` if provided. Otherwise use `make first50-queue`: `deep` for deep-map-ready sources and `lite` for map-lite-ready sources. If neither applies, default to `lite` unless the source is a known anchor.
1. **Render the frontmatter.** Eleven fields in this order: `source_id`, `title`, `author`, `status: machine_generated_not_canon`, `operator_review_status: unreviewed`, `public_safe: true`, `raw_text_used_local_only: false`, `edition_verified: true`, `locator_system: <verified>`, `canonical_status: noncanonical`, `quote_word_count: 0`. Values for `title`, `author`, `locator_system` come from the verified manifest row.
2. **Outline the source structure.** Walk the H1/H2/H3/H4 of `source.md`. Identify which headings are chapter markers (numbered chapters), which are part dividers, which are front/back matter (Contents, Notes, Index, Appendix). Do not copy heading text into the public map verbatim — paraphrase the structural role. If part dividers did not survive as headings, do not use `Part I / Chapter N` locators anywhere in the map (the BK-0001 lesson — use chapter-only locators).
3. **Fill the body for the selected class.**
   - **Map-lite:** one `# Book Map` H1 with the short "not canon" intro plus these nine `##` sections in this exact order: `## What this is`; `## What this is not`; `## Source metadata`; `## Source structure`; `## Candidate source-card claims` (3-5 rows); `## Candidate tensions` (3-5 rows, framed as questions); `## Eval relevance`; `## Misuse risks`; `## Operator review notes`. Match `templates/map-lite.md.tmpl`.
   - **Deep map:** one `# Book Map` H1 (with its short intro paragraph and the "what this is / what this is not" framing) plus the following thirteen `##` sections in this exact order: `## What this is`; `## What this is not`; `## Source metadata`; `## Source structure` (table); `## Central thesis` (≤150 words, ends with `(Locators: …)`); `## Argument structure` (5–8 bullets each with locator); `## Key concepts` (table ≤8 rows); `## Claims relevant to Anti-Slop` (table ≤10 rows, priorities A/B/C); `## Possible contradictions` (table ≤8 rows, framed as questions); `## Possible canon touchpoints` (≤6 bullets); `## Eval relevance` (5 booleans with one sentence each); `## Misuse risks` (5–7 bullets); `## Operator review notes` (checklist + `quote_word_count: 0` + `operator_review_status: unreviewed` + `locator_quality_note:` if locator confidence is medium or lower). The accepted reference shape is `corpus/book-maps/BK-0001.md` and `BK-0003.md` — match them.
4. **Source metadata section uses verified values.** Pull publisher / year / ISBN / owned format / locator system / edition_verified directly from the verified manifest row — never re-derive from the local source.
5. **Possible contradictions uses questions, never claims.** Every row in the contradictions table follows the shape `Compare BK-XXXX's <X> with BK-YYYY on <Y>` or `Question whether/how <Z>`. No assertion verbs about comparison authors.
6. **Label all map inferences.** Any claim that is the map's own synthesis (not supported by a specific chapter locator) gets `(map inference)` or equivalent in-line marker, both in the bullet and in the candidate-card table.
7. **Hand-check against the review checklist.** Run the 10-point review checklist (below) against the draft before saving.
8. **Run the closing-gate suite.** See `## Commands to run` below.

**Output template.** `templates/map-lite.md.tmpl` or `templates/book-map.md.tmpl`.

**Reference fixtures.** `corpus/book-maps/BK-0001.md` and `corpus/book-maps/BK-0003.md`.

**On failure.** Pre-check failure: surface to operator, do not draft. Review-checklist failure at step 7: do not save the public file; report the failed check and surface. Closing-gate failure post-write: surface; do not auto-revert.

## Workflow 4 — review-book-map

**When to use it.** A book map exists at `corpus/book-maps/<source_id>.md` and the operator wants a structured review pass before promoting it or before drafting a source card from it.

**Inputs.**
- `corpus/book-maps/<source_id>.md` (read-only).
- The current row in `corpus/manifests/books-200.yaml` and `corpus/manifests/acquisition-registry.yaml` (to check stale metadata).
- `templates/review-report.md.tmpl`.

**Outputs (local-only).**
- `local-only/phase-2-verification/<source_id>/review/review-report.md`.
- Public file is NOT edited unless the operator explicitly approves each suggested fix and asks Claude to apply it.

**Pre-checks.**
- Book map exists at the expected path.
- Operator did not pass `--apply-fixes` or equivalent (default is report-only).

**Steps.**

1. **Open the map read-only.** Do not modify it.
2. **Run the 10-check review checklist** below. For each check, scan the relevant section(s) of the map and record either "no findings" or specific quotes with line numbers (line numbers in the public map, not in the local source).
3. **Cross-reference frontmatter against the manifest.** The map's `title`, `author`, and `locator_system` must match the current books-200.yaml row; `edition_verified: true` should be present only if the acquisition-registry row also shows `edition_verified: true`. Mismatches are flagged under the "stale metadata" check.
4. **Render the review report.** Fill `templates/review-report.md.tmpl` with one section per check; each section has "Findings" and "Suggested fix" subsections. If no findings, mark the check as "PASS — no fixes needed."
5. **Save to `local-only/phase-2-verification/<source_id>/review/review-report.md`.** Do not save anywhere public.
6. **Surface the report path to the operator.** Do not auto-apply fixes.

**Output template.** `templates/review-report.md.tmpl`.

**Reference fixture.** The BK-0001 review pass that produced fixes for stale source-metadata language, locator-prefix residue, and assertion-style prose in Possible contradictions.

**On failure.** Cannot fail in the closing-gate sense because nothing public is written. If the operator passes `--apply-fixes` for a specific finding, the apply step uses Workflow 2's surgical edit pattern and the closing-gate suite runs.

## Workflow 5 — batch-metadata-verify

**When to use it.** Producing operator-approval packets for 3–5 sources in one pass (the per-batch cap from `## Batch rules` below).

**Inputs.**
- A list of `source_ids` from the operator (3–5 IDs), or the default: every entry in `corpus/manifests/phase-2-verification-queue.yaml`.
- Per-source inputs as in Workflow 1.

**Outputs (local-only).**
- One packet per source under `local-only/phase-2-verification/<source_id>/operator-approval/`.
- `local-only/phase-2-verification/batch-summary.md` listing per-source status (success / gap / blocked) and a recommended order for operator review.

**Pre-checks.**
- The source-id list is between 3 and 5 entries inclusive. If outside the range, surface the per-batch cap and ask the operator to adjust.
- Each source has a non-empty local extraction.

**Steps.**

1. **For each source in the list, in order:** run Workflow 1's steps. If a per-source pre-check fails, record the failure in `batch-summary.md` and continue with the next source — failures isolate at the source level.
2. **Compile `batch-summary.md`.** One section per source: status (success / gap / blocked), per-section quality signals, recommended operator-review priority (e.g. "BK-0007 has the cleanest extraction; review first").
3. **Run the closing-gate `make check-raw` only** at the end. No public files were touched, so the heavier gates are not needed.

**Output template.** Per-source: Workflow 1's four templates. Batch-level: not templated — short Markdown.

**Reference fixture.** None yet — BK-0007 / BK-0042 / BK-0048 will be the first batch.

**On failure.** Per-source failures isolate; batch continues. If all sources fail pre-checks, the batch ends with a single batch-summary listing all reasons.

## Workflow 6 — batch-map-draft

**When to use it.** Drafting public book maps for a small batch whose metadata has already been verified (the per-batch caps from `## Batch rules` below).

**Inputs.**
- A list of `source_ids`, all with `edition_verified: true` in the acquisition registry.
- One map class for the batch: `lite` or `deep`. Mixed batches are allowed only if the operator explicitly asks, and the smaller deep-map cap applies.
- Per-source inputs as in Workflow 3.

**Outputs (public).**
- One book map per source at `corpus/book-maps/<source_id>.md`.
- `local-only/phase-2-verification/batch-summary.md` updated with per-source draft status.

**Pre-checks.**
- The source-id list is 3-5 entries for an all-map-lite batch, or 2-3 entries for any batch containing a deep map.
- Each source has `edition_verified: true` in the acquisition registry. Any source that does not is dropped from the batch with a note pointing to Workflow 2.

**Steps.**

1. **For each verified source:** run Workflow 3's steps end-to-end, including the per-source closing-gate suite. If a draft fails the review checklist, do not save that source's public file; record the failure and continue with the next source.
2. **Final batch-summary update.** Record per-source draft status (saved / blocked / review-checklist-failed).
3. **Run the full closing-gate suite once at the end** to confirm the cumulative effect on the public repo.

**Output template.** Per-source: `templates/map-lite.md.tmpl` or `templates/book-map.md.tmpl`. Batch-level: short Markdown appended to `batch-summary.md`.

**Reference fixture.** None yet.

**On failure.** Per-source failures isolate; batch continues. Closing-gate failure at end → surface; do not auto-revert.

## Review checklist

The ten checks every map review (Workflow 4) runs through. Workflows 1, 3, 5, and 6 also hand-check against this list before saving.

1. **Stale metadata.** Source metadata section still says "pending operator update" / "candidate only" / contains empty fields after Workflow 2 has applied verified values. Fix: replace with verified values from the current manifest row.
2. **Wrong YAML block edited.** Edits landed in `books_200_yaml:` when they should have landed in `acquisition_registry_yaml:`, or vice versa; or a value landed at the wrong parent-key path inside `acquisition_registry_yaml` (e.g. `rights_notes_public` placed at row top-level instead of inside the `rights:` block). Fix: re-apply edits at the correct parent-key path.
3. **Private paths / extensions.** Any `local-only/`, `extracted-md/`, `/Users/`, `Desktop`, or `Archive.zip` substring in public files. Plus the blocked raw-source format extensions (EPUB, PDF, MOBI, AZW, AZW3, DJVU, CBZ, CBR — see `scripts/kb_lint.py` for the exact regex). Fix: rewrite using author + title + edition + locator only.
4. **Raw-text leakage.** Verbatim sentences or near-verbatim paraphrase from the source's prose body in the public artifact. Fix: rewrite as a high-level paraphrase with locator only.
5. **Hidden canon drift.** Assertion-style prose attributing claims to comparison sources (e.g. `BK-0024 says …`, `Mintzberg treats …`, `Ries argues …`). Fix: rephrase as a question or comparison invitation.
6. **Unsupported comparison claims.** Possible-contradictions rows that assert what another book contains rather than naming a question to investigate. Fix: re-frame the row's "Question to investigate" cell as `Compare … with … on …` or `Question whether/how …`.
7. **Locator mismatch.** Locators reference structural divisions (`Part I`, parts, sub-parts) that did not survive in the extraction; or the locator format does not match `locator_system` in frontmatter. For `pdf_page`, every locator must use a stable page or page range; open-ended ranges such as `pp. 404–~` fail review. Fix: drop the unsupported prefix, replace open-ended page ranges with stable ranges from the preserved page boundaries, or update `locator_system` (rarely; prefer the first two).
8. **Over-summary.** Section length exceeds caps. Deep map caps: Argument structure 5–8 bullets; Key concepts ≤8 rows; Claims relevant ≤10 rows; Possible contradictions ≤8 rows; Possible canon touchpoints ≤6 bullets; Misuse risks 5–7 bullets; Central thesis ≤150 words. Map-lite caps: Candidate source-card claims 3–5 rows; Candidate tensions 3–5 rows; Misuse risks 3–5 bullets. Fix: trim to the cap; move detail into source cards later.
9. **Universalization.** Map text treats the source's domain as universally applicable without flagging boundary conditions (BK-0001 lesson: anchored in large-org examples; transferring kernel to 2-person teams without adaptation is misuse). Fix: add a misuse-risks bullet that names the universalization risk.
10. **Map inference not labeled.** A claim that is the map's own synthesis (rather than supported by a specific chapter locator) is presented without the `(map inference)` label or equivalent in-line marker. Fix: add the label, or replace the claim with a chapter-cited claim.

## Batch rules

- **Metadata verification batch:** 3–5 books per batch. Larger batches dilute operator focus; smaller batches forfeit batch economics.
- **Map-lite drafting batch:** 3–5 books per batch. The artifact is deliberately compact, so breadth batches are acceptable while review remains manageable.
- **Deep-map drafting batch:** 2–3 books per batch. Deep maps are heavier than metadata work; small batches keep review attention high.
- **Reviews:** individually, or in small batches of 2–3 maps. Reviewing more than 3 maps in one pass tends to surface the same fix repeatedly with diminishing returns.
- **Source cards and canon candidates:** not batched in v1. Drafted one at a time with operator review per artifact. The skill does not produce source cards or canon candidates.

## Commands to run

The closing-gate suite, run after every workflow that touches public files (Workflows 2, 3, 6):

```sh
make validate
make check-raw
make kb-lint
make report
make phase2-queue
python3 -m py_compile scripts/*.py
git diff --check
rg -n "(/Users/|Desktop|Archive[.]zip)" corpus/ kb/ docs/
```

Discipline:
- None of the eight commands mutates tracked public files; none stages or commits. `python3 -m py_compile scripts/*.py` may refresh `scripts/__pycache__/` bytecode, which is gitignored and out of scope for the closing gate.
- `make kb-lint` already enforces the raw-source-extension content check on every public Markdown file (the regex lives in `scripts/kb_lint.py`). The final `rg` sweep is the additional hand-check for private-path substrings that the lint does not catch (e.g., a stray `/Users/` reference inside a YAML file). It must return zero matches.
- If any command fails, print the failure verbatim and stop. Do not retry without surfacing.
- Closing-gate failure is never auto-recovered by the skill — the operator decides whether to revert manually.

## Reference outputs

Match these in shape:

- `corpus/book-maps/BK-0001.md` — Rumelt, *Good Strategy Bad Strategy*. The locked book-map shape: 11-field frontmatter, one `# Book Map` H1 plus thirteen `##` sections, chapter-only locators, Possible contradictions framed as questions.
- `corpus/book-maps/BK-0003.md` — Bryar & Carr, *Working Backwards*. Same shape, plus the `locator_quality_note:` line in Operator review notes for sources with heterogeneous heading levels.
- `local-only/phase-2-verification/BK-0001/operator-approval/*` — the four-file packet template that Workflow 1 produces.
- `local-only/phase-2-verification/BK-0003/operator-approval/*` — same shape for a slightly more complex extraction.

If a workflow's output meaningfully diverges from these references in shape, surface the divergence to the operator before saving.
