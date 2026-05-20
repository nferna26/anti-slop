# Claim / Tension Card Workflow

Claim/tension cards are the synthesis layer of the books-kb. A claim/tension card sits one rung above source cards on the artifact ladder: source cards are operator-reviewed evidence units, each drawn from a single source; a claim/tension card compares claims *across* sources and records how they relate.

A claim/tension card is **synthesis, not canon**. It states no advice and decides no rule. Its job is to hold two source-card-grounded claims next to each other, name the tension between them honestly, and record what would resolve it — without flattening a real disagreement into a false consensus.

Use:

```sh
python3 scripts/new_claim_tension_card.py <slug>
```

The slug becomes the filename and the `card_id`. The script copies the template; every frontmatter field is filled by hand.

## What a claim/tension card may and may not do

- It **may** cite operator-reviewed source cards as evidence.
- It **may not** cite a book map as evidence. A book map is a discovery hint only — it can point you toward which source cards to compare, but it is never the ground of a claim. If a map informed the card, name it under Operator notes as a discovery hint, never under a "Source cards for…" section.
- It **may not** cite an unreviewed source card. Evidence must be operator-reviewed.
- It **may not** assert canon or state advice. It records synthesis; canon is a later, separately operator-approved artifact.
- It **must not** force consensus. If the tension is real, the card preserves it.

## Frontmatter fields

- `card_id` — the file slug (matches the filename, without extension).
- `card_type` — exactly one value from the controlled set below.
- `title` — a short title for the synthesis.
- `question` — one line naming the issue the card synthesises.
- `operator_review_status` — `unreviewed` until an operator reviews the card; `reviewed` only on explicit operator approval.
- `tension_status` — exactly one value from the controlled set below.
- `publication_status` — per `publication-statuses.yaml`.

## card_type — controlled set

Pick exactly one.

| Value | Use when… |
|---|---|
| `tension` | two source-card-grounded claims stand in genuine tension — Claim A and Claim B oppose, qualify, or pull against each other. |
| `claim` | several source cards jointly support one synthesised claim; Claim B holds a bounding or qualifying claim rather than an opposing one. |

v1 expects mostly `tension` cards — preserving disagreement is the methodology's distinctive job.

## tension_status — controlled set

Pick exactly one.

| Value | Use when… |
|---|---|
| `open` | the tension is genuinely unresolved; the card preserves it as such. |
| `conditionally_resolved` | the deciding conditions identify which claim holds under which conditions; the card is still not canon, and any tension beyond those conditions stays open. |

## Body sections

- `## Tension` — one paragraph stating the issue and why the two claims pull against each other. State the question; do not answer it here.
- `## Claim A` / `## Claim B` — one claim each, in the drafter's own words. For a `claim`-type card, Claim B is a bounding or qualifying claim.
- `## Source cards for Claim A` / `## Source cards for Claim B` — the reviewed source cards that ground each claim. One entry per line as `<card-id> — <brief note>`. Card IDs and locators only; operator-reviewed source cards only.
- `## Nature of the tension` — classify the tension honestly: genuine contradiction; difference of scope or domain; sequencing disagreement; complementary claims misread as opposed; or unresolved empirical question. Synthesis, not a verdict.
- `## Deciding conditions` — what evidence or conditions would tip the issue toward Claim A, toward Claim B, or dissolve the tension. Name the conditions; do not declare a winner.
- `## Tension preserved` — state plainly what remains unresolved and why the card does not flatten it.
- `## Scope conditions` — where the synthesis applies and where it does not.
- `## Canon implication` — what canon candidate the card could later feed, and what would have to be true first. Drafting the card is not canon and creates no canon candidate.
- `## Operator notes` — drafting provenance, `card_type` rationale, confirmation that every cited source card is operator-reviewed, any book maps used only as discovery hints, and status.

## Drafting steps

1. Choose a target: an issue on which two (or more) reviewed source cards carry claims that pull against each other. Reviewed source cards only.
2. Re-read the cited source cards. Confirm each is `operator_review_status: reviewed`.
3. Write Claim A and Claim B in your own words. Synthesise; do not copy source-card prose verbatim.
4. Under each "Source cards for…" section, list only the reviewed source cards that ground that claim.
5. Classify the tension under "Nature of the tension." Be honest — many apparent contradictions are scope or sequencing differences.
6. Name the deciding conditions. Preserve the tension; do not pick a winner.
7. Fill scope conditions and canon implication. Leave `operator_review_status: unreviewed`.
8. Append a public-safe bullet to `kb/log.md`.
9. Run the closing-gate suite.

## Review checklist

Run every check before a claim/tension card goes to an operator. A blocker on any check sends the card back.

1. **Source-card lineage.** Every card listed under a "Source cards for…" section is an operator-reviewed source card, cited by `card_id` and locator. No unreviewed source cards.
2. **No unsupported comparison claims.** Claim A and Claim B each rest on the cited source cards; the card asserts nothing about a source that its source card does not support.
3. **No hidden canon.** The card records synthesis only — no advice, no "the right rule is X," no operator-approved authority.
4. **Tension preserved.** A real disagreement is held open, not flattened. `tension_status` matches the body; if `conditionally_resolved`, the conditions are explicit and the residual open question is named.
5. **Scope conditions.** The synthesis names where it applies and where it does not; it does not universalise.
6. **Deciding conditions.** The card names what evidence or conditions would move the issue, rather than declaring a winner.
7. **Public-safe scan.** No raw source text, no private paths, no raw-source filenames or extensions, and no book map cited as evidence.
8. **Status discipline.** `operator_review_status` is `unreviewed` on a draft and becomes `reviewed` only on explicit operator approval.

## Discipline

- One card, one tension. If two distinct tensions surface, write two cards.
- A claim/tension card never says "and the right rule is X." Advice belongs in canon; synthesis belongs here.
- Book maps are discovery hints, never evidence. Operator-reviewed source cards are the only evidence a claim/tension card cites.
- No graph database, no embeddings, no automation: the relations are judgment rails the operator fills and reviews by hand.
