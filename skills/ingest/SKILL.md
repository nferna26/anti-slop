---
name: ingest
description: Distill a raw source into a card in the schema, propose canon pages it touches, append to the KB log.
---

# ingest

Run this Skill when an operator has a new source — book, paper, repo, postmortem, or operational document — to compile into the KB. The Skill distills the source into a card matching the schema's frontmatter contract, proposes the canon pages the source touches, and appends to the KB log. The operator reviews before anything reaches canon.

## Parameters

- `source` — path or URL of the raw source. For URLs, the operator's environment must supply web-fetching capability.
- `kb_root` — required. Path to a KB laid out per `anti-slop/methodology/schema.md`.
- `card_type` — `source-card`, `paper-card`, or `repo-candidate`. Default `source-card`. Override based on source shape: arXiv URL → `paper-card`; GitHub URL → `repo-candidate`.

## Step 1 — Read

Read end-to-end if short; for books, skim the structure and select 3–5 high-signal chapters. Store a working copy at `<kb_root>/lab/<batch>/source/<slug>.md` (committable for public sources; the `source/` naming avoids collision with the substrate-protection `raw/` gitignore convention) or `<kb_root>/raw/` (gitignored, for copyrighted or private material). Citations in the card will resolve to this path.

## Step 2 — Summarize

Write a one-paragraph summary in the operator's voice — the source's central claim and where it applies. This becomes `summary:` in frontmatter, truncated to about 200 characters. Takeaway, not abstract.

## Step 3 — Extract decision rules

For every substantive claim, produce a rule that is imperative ("Never X because Y"; "When X, do Y"), testable (verifiable in finite time), self-contained (carries its own justification in one sentence), and cited (chapter, section, figure, page number for documents — incident phase or section heading for postmortems). Target 10–20 rules. Rules that read as summaries ("the author argues...") are rejected.

## Step 4 — Calibrate trust

`trust_level`: A for primary postmortems from the responsible party, RFCs, and standards-body publications; B for quality books by recognized practitioners and well-maintained OSS; C for secondary commentary and practitioner blogs; D for speculation and marketing material, cite only to debunk.

`confidence`: the operator's confidence in the synthesis itself, separate from `trust_level`. A B-trust source can produce a low-confidence card if the rules extrapolate beyond what the source establishes.

## Step 5 — Propose canon links

Identify 5–10 canon pages the source touches — patterns, guardrails, tech-dossiers, concepts, capability maps, or playbooks. For each, write a one-line rationale naming which rule(s) it touches and whether the relationship is reinforcement, extension, or contradiction. **Do not auto-edit canon pages.** The operator reviews and applies the cross-references separately. Auto-edits invert the operator's review authority.

## Step 6 — Append to log

Add a one-line entry to `<kb_root>/log.md` (create if absent) under the appropriate date heading: `Ingested <source>: <card-id> (N canon candidates).` The log is chronological by convention — newest entries at the top.

## Card body shape (by card_type)

- **source-card (book or doc):** Bibliographic, Decision rules, Anti-patterns, Checklists, When this matters, Open questions, Citations.
- **paper-card:** Bibliographic, Summary, Decision rules, Anti-patterns, Limitations & non-claims, When this matters, Lineage, Key evidence, Citations.
- **repo-candidate:** URL & license, Use case, Verdict, Scores, Files inspected, Strengths, Risks, Recommended use.
- **postmortem source-card:** Bibliographic, Summary, Timeline, Decision rules, Anti-patterns, When this matters, Open questions, Citations.

## Discipline

No marketing words in the card body. Every rule cites a specific location in the source. Quoted text appears verbatim in the source, or it is not quoted — paraphrase rather than partially-rewrite quoted spans.

## Schema contract

The frontmatter contract, the body discipline, and the canon/cards distinction are in `anti-slop/methodology/schema.md`. Do not restate the schema here. If this Skill and the schema disagree, the schema wins; file the divergence as a Skill bug.
