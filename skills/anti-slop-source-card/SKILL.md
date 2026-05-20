---
name: anti-slop-source-card
description: "Five-workflow source-card pipeline for the books-kb: select-source-card-target, draft-source-card, review-source-card, mark-source-card-reviewed, and draft-approval-ready-source-card. Judgment rails for keeping source cards grounded in the local source rather than promoted from book maps."
---

# anti-slop-source-card

This skill encodes the source-card workflow for the books-kb. It is judgment rails, not a tooling framework. There are no helper scripts and no new templates; use the repo's existing source-card template and workflow docs.

## When to invoke

Invoke this skill when the operator asks Claude to select a source-card target, draft a source card, review a source card, mark a source card reviewed, or produce an approval-ready source-card draft with review and one repair cycle included.

## Workflow selector

| Workflow | Section | Writes public? |
|---|---|---|
| `select-source-card-target` | `## Workflow 1` | No |
| `draft-source-card` | `## Workflow 2` | Yes |
| `review-source-card` | `## Workflow 3` | No |
| `mark-source-card-reviewed` | `## Workflow 4` | Yes |
| `draft-approval-ready-source-card` | `## Workflow 5` | Yes |

## Shared contract

Every workflow inherits these rules. If a workflow violates any rule, stop and surface to the operator.

- **Bright-line source-grounding rule.** If Claude has not checked the local source at the target locator, Claude may write a local-only selection note, but may not draft a public source card.
- **Book maps are discovery aids only.** Reviewed book maps may help choose a target chapter or claim. They are not authority for a source card. The source card's authority is the local source at the verified locator.
- **Source cards are evidence units, not canon.** A source card records what one source supports at one locator. Synthesis belongs in claim/tension cards; advice belongs in canon.
- **Raw source text stays local-only.** Public cards use locator + paraphrase by default. `Short excerpt` should be `None.` unless the operator explicitly approves a short excerpt and the quote budget is counted.
- **One card, one claim.** Split multi-claim evidence into separate cards.
- **Use the controlled `claim_type` set.** Exactly one of `factual`, `diagnostic`, `mechanism`, `method`, `norm`, `warning`, `boundary_condition`, `open_question`.
- **Relation sections are public-safe references.** `Supports`, `Tensions with`, and `Qualifies` use source IDs, card IDs, reviewed-map refs, and locators only. Comparison-source entries are questions to investigate, not assertions about what another source says.
- **Status stays unreviewed until operator approval.** Drafted cards keep `operator_review_status: unreviewed` in frontmatter and body notes.
- **No private paths or raw-source filenames in public files.** Public files must not include `local-only/`, `extracted-md/`, `/Users/`, `Desktop`, the Archive bundle name, or raw-source format extensions named by `scripts/kb_lint.py`.
- **No `git add` or `git commit` unless the operator explicitly requests it.** Run the closing-gate suite and report results.

## Workflow 1 — select-source-card-target

**When to use it.** Choosing the next card target from reviewed book maps, without drafting a source card yet.

**Inputs.**
- Reviewed book maps under `corpus/book-maps/`.
- `corpus/manifests/phase-2-verification-queue.yaml`.
- Existing local-only selection packets, if present.
- `docs/wip-limits.md`.

**Outputs (local-only).**
- A short selection packet under `local-only/phase-2-verification/`, such as `first-source-card-selection.md` or a batch-specific successor.

**Steps.**

1. Confirm the candidate map has `operator_review_status: reviewed`. If not, stop.
2. Pick one target claim, not a batch of claims. Prefer narrow, high-leverage, locator-stable claims.
3. Record a top-candidate table: source ID, candidate claim, locator, why it matters, risk/caveat, and whether local-source verification is still required.
4. Name a single recommended first target.
5. Do not create or edit any public source card.

## Workflow 2 — draft-source-card

**When to use it.** Drafting exactly one public source card from a selected target after verifying the target locator against the local source.

**Inputs.**
- `corpus/source-cards/_template.md`.
- `docs/source-card-workflow.md`.
- The reviewed book map that suggested the target.
- `corpus/manifests/books-200.yaml` and `corpus/manifests/acquisition-registry.yaml`.
- The local source corresponding to the source ID.

**Outputs (public).**
- One new card in `corpus/source-cards/`, created with `python3 scripts/new_source_card.py <source_id>`.
- One public-safe bullet in `kb/log.md`.

**Pre-checks.**
- The source's book map is reviewed.
- The source row has a populated locator system.
- The target locator can be found in the local source.
- The local source section needed for this card has been read and checked. If not, stop and run Workflow 1 instead.

**Steps.**

1. Use the reviewed map only to locate a promising target. Do not treat the map as authority.
2. Open the local source and verify the target locator. Read enough of the local section to ground the claim and confirm the boundary. Do not copy source prose into the public card.
3. Run `python3 scripts/new_source_card.py <source_id>`.
4. Fill frontmatter from verified metadata and the target claim:
   - `card_id`
   - `source_id`
   - `title`
   - `author`
   - `locator`
   - `issue_or_question`
   - `claim_type`
   - `operator_review_status: unreviewed`
   - `publication_status`
5. Fill the body with one claim, one locator, `Short excerpt: None.` by default, a conservative paraphrase, why it matters, relation sections, scope conditions, misuse risk, related canon, and operator notes.
6. In `Supports`, the reviewed map may appear only as the discovery aid that identified the chapter or claim. State explicitly that the evidence is the local source at the locator, not the map note.
7. In `Tensions with`, write questions to investigate. Do not claim that comparison books argue, prove, reject, or show anything unless a source card already verifies it.
8. In `Operator notes`, state that the card is grounded in the local source, the local locator was checked, no source prose is reproduced, and operator review is still pending.
9. Append a single public-safe `kb/log.md` bullet.
10. Run the closing-gate suite.

**Reference fixture.** `corpus/source-cards/BK-0048-card-001.md` after the repair commit that grounded it in the local Chapter 4 source.

**Failure signs.** Phrases like "built from the book map", "upgrades the map note to evidence", or "operator-reviewed evidence unit" on an unreviewed card are failures. Fix before reporting success.

## Workflow 3 — review-source-card

**When to use it.** Reviewing a drafted source card before operator approval or before any higher artifact cites it.

**Inputs.**
- The source card under `corpus/source-cards/`.
- `docs/source-card-workflow.md`.
- The verified manifest and acquisition rows.
- The local source at the card locator.

**Outputs (local-only).**
- A review report under `local-only/phase-2-verification/<source_id>/source-card-review/`.

**Review checklist.**

1. **Source grounding.** The card states that the claim was checked against the local source at the locator. If it was built only from a map, send it back.
2. **Artifact ladder.** The card never treats a book map as authority and never promotes itself to canon.
3. **One claim.** Claim, paraphrase, scope, and misuse risk all describe the same single claim.
4. **Locator fit.** Locator format matches `locator_system`; chapter/page/section boundary is confirmed or explicitly marked pending.
5. **Controlled fields.** `claim_type` is one allowed value; `issue_or_question` is a real question or issue, not a title.
6. **Quote discipline.** `Short excerpt` is `None.` or the excerpt is explicitly counted and within policy. No source-prose quote is smuggled into prose.
7. **Public-safe scan.** No private paths, local-only path names, raw-source filenames, or raw-source extensions.
8. **Relation sections.** `Supports`, `Tensions with`, and `Qualifies` use public-safe refs only. Tensions are questions, not unsupported comparison claims.
9. **Scope and misuse.** Scope conditions and misuse risk are concrete enough to prevent universalization.
10. **Status.** Draft card remains `operator_review_status: unreviewed`; reviewed status appears only after explicit operator approval.
11. **Navigation/log.** `kb/log.md` records the draft if the card is public.
12. **No higher artifact created.** Review does not create claim/tension cards or canon candidates.

## Workflow 4 — mark-source-card-reviewed

**When to use it.** The operator explicitly approves a drafted source card after reviewing it.

**Inputs.**
- Explicit operator approval in the prompt.
- The source card.
- The local-only review report, if one exists.
- `kb/log.md`.

**Outputs (public).**
- The source card's `operator_review_status` lifted to `reviewed` in frontmatter and operator notes.
- One `kb/log.md` bullet.

**Steps.**

1. Refuse without explicit operator approval.
2. Re-open the card and check the `review-source-card` checklist. If a blocker remains, do not mark reviewed.
3. Change only the review-status fields and any operator-approved review-note cleanup.
4. Append a public-safe log bullet.
5. Run the closing-gate suite.
6. Do not create a claim/tension card or canon candidate in the same workflow.

## Workflow 5 — draft-approval-ready-source-card

**When to use it.** Drafting exactly one source card and absorbing the normal draft-review-repair loop before asking the operator for approval.

**Inputs.**
- Everything required by Workflow 2.
- Everything required by Workflow 3.
- The selected source-card target: source ID, locator, candidate claim, and reviewed-map discovery hint.

**Outputs.**
- One public source card in `corpus/source-cards/` with `operator_review_status: unreviewed`.
- One local-only review report under `local-only/phase-2-verification/<source_id>/source-card-review/`.
- One public-safe `kb/log.md` bullet for the draft, plus a repair note if the loop had to fix a blocker.

**Hard limits.**
- Draft exactly one card.
- Run at most one repair cycle after the first review.
- Do not mark the card reviewed. Workflow 4 still requires explicit operator approval.
- Do not create a claim/tension card, canon candidate, graph edge, or additional source card.
- Do not `git add` or `git commit` unless the operator explicitly requested a commit in this prompt.

**Steps.**

1. Run the drafting steps from Workflow 2, including local-source verification at the target locator. The card must be source-grounded before it is public.
2. Immediately run the Workflow 3 review checklist on the drafted card. Write the local-only review report.
3. If all checks pass, run the closing-gate suite and report `READY FOR OPERATOR APPROVAL`. Leave the card unreviewed.
4. If the review finds blockers, repair only the blocked sections. Keep the original claim boundary, locator, source ID, and one-card-one-claim discipline unless the blocker proves the target itself is invalid.
5. Rerun the Workflow 3 review checklist after the repair and update the local-only review report so it supersedes the first pass.
6. If the rerun passes, run the closing-gate suite and report `READY FOR OPERATOR APPROVAL`, including the repair summary. Leave the card unreviewed.
7. If the rerun still has a blocker, stop and report `SEND BACK` with the blocker, file path, line reference when available, and the smallest safe next instruction. Do not keep repairing.

**Final report format.**
- Verdict: `READY FOR OPERATOR APPROVAL` or `SEND BACK`.
- Card path and card ID.
- Source-grounding summary: what local locator was read and how the boundary was confirmed.
- Claim boundary and `claim_type` rationale.
- Review result: all-pass or named blockers.
- Repair summary, if a repair cycle happened.
- Closing-gate results.
- Explicit statement that `operator_review_status` remains `unreviewed` and no higher artifact was created.

## Commands to run

After any workflow that touches public files, run:

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

The final `rg` sweep must return zero matches. `make kb-lint` carries the raw-source-extension checks for public Markdown.

## Batch rules

Do not batch source-card drafts in v1. Draft one card, review one card, then decide whether the next card should be drafted. Workflow 5 is the preferred single-card loop when the operator wants fewer handoffs: Claude drafts, self-reviews, repairs blockers once, and stops for operator approval. A backlog of unreviewed source cards is not evidence; it is WIP debt.
