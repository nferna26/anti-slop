# Schema

Every page that compiles judgment across multiple sources carries a three-way split in its body: evidence (grouped by source, no opinion), judgment (what the operator concludes from the evidence), unknowns (what the evidence does not settle). Judgment is never smuggled into the evidence section. The discipline of keeping these three separate is the single most useful structural constraint in the whole pattern, and the directory layout, the frontmatter, and the cross-reference vocabulary all exist to make that discipline easy to enforce and hard to drift away from.

## The layers

A KB is five top-level directories.

`raw/` holds source material — book chapters, paper PDFs, doc excerpts, repo notes — verbatim, immutable, not tracked in git. This is the only layer the LLM does not write. If the substrate is sensitive (copyrighted books, internal documents), `raw/` stays local and is excluded from any push.

`cards/` holds one distilled card per source — one card per book, one per paper, one per repository. Each card translates the source into decision rules in the operator's voice, with every rule citing back to a specific chapter, section, or figure.

`canon/` holds compiled judgment that draws on multiple cards: patterns, guardrails, technology dossiers, concepts, capability maps, playbooks. A canon page takes a position; a card does not. The split exists because card-level prose stays close to its source, while canon-level prose synthesizes across sources and is where the operator's actual judgment lives. This is where the three-way evidence/judgment/unknowns split lands.

`execution/` holds the artifacts produced when canon is applied — ADRs, mini-PRDs, epics, risk registers, query-runs, writeback candidates. This layer does not exist in Karpathy's three-layer pattern (gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), and it is the layer that distinguishes a knowledge base from a journal. Without it, the substrate compiles knowledge but does not record what was done with it.

`registry/` holds generated metadata — a SQLite database built from the frontmatter of every page, plus exports for retrieval tools. Nothing here is hand-edited; it is rebuilt from the source-of-truth markdown.

A sixth directory, `lab/`, holds session notes. Lab is committed to private KBs and gitignored on the public side.

## The four operations

Ingest. Add a source to `raw/`, draft a card in `cards/`, propose 5–10 canon pages it touches, append to the log. The Skill for this step does not modify canon pages directly — it surfaces candidates for the operator to accept.

Query. Read the index, rank candidates, fetch the top cards, synthesize with citations. Every claim cites a card; every card cites a chapter, section, or figure. A query that cannot cite is a query that has not been answered.

Lint. Scan for contradictions (two pages making opposite claims without a `contradicts` link), orphan pages, schema violations, and staleness (`review_by` past due). Lint runs on a fixed weekly slot, not "when needed."

Index/log. Rebuild `cards/index.md` (content-oriented) and append to `log.md` (chronological) after any ingest or edit. They serve different queries and are not redundant.

## The frontmatter contract

Every page in `cards/`, `canon/`, and `execution/` carries the same nineteen-field block. Empty values are `[]`, not omitted keys.

```yaml
id:           <slug, prefix-typed>          # e.g. src-book-kleppmann-ddia
type:         <page-type>                   # one of 16 universal types
title:        <human title>
status:       active | draft | deprecated | superseded
summary:      <one-line distilled takeaway>
created:      YYYY-MM-DD
updated:      YYYY-MM-DD
owners:       [<role>]
source_refs:  [<page-ids>]                  # upstream cards this page cites
trust_level:  A | B | C | D                 # property of the source
freshness:    timeless | stable | volatile | live
review_by:    YYYY-MM-DD
domains:      [<list>]                      # e.g. [architecture, security]
tags:         [<list>]                      # KB-controlled vocabulary
related:      [<page-ids>]                  # adjacent pages, page IDs only
contradicts:  [<page-ids>]
supersedes:   [<page-ids>]
confidence:   high | medium | low
stage:        raw | card | canon | execution
```

Paper cards add six fields: `paper_type`, `venue`, `date_published`, `authors`, `extends`, `extended_by`.

Three fields earn specific attention.

`trust_level` calibrates the source, not the claim. A book carries a trust level; a paper carries one; a repository carries one. When a canon page is compiled from multiple sources, its trust is calibrated to the lowest of its *primary* anchors — not the lowest of every source it touches. This is the difference between an honestly-anchored claim and a hedged one.

`source_refs` is required on every canon and execution page. Empty `source_refs` on a canon page is a CRITICAL lint finding — the page is asserting judgment without showing what it rests on. Source cards by definition have empty `source_refs` (they are the sources); the lint distinguishes by `type`.

`confidence` is the operator's confidence in the page's claim, separate from the source's trust. A B-trust source can produce a low-confidence page if the page extrapolates beyond what the source establishes. The two fields are different dials.

## Cross-reference vocabulary

Four fields, plus two on paper cards.

`source_refs` cites upstream — what this page rests on. `related` lists adjacent pages — the catch-all for "you might also want to look at this." `contradicts` is reserved for explicit disagreement; setting it triggers a review page in `execution/reviews/` and lowers the contradicting page's confidence. `supersedes` flips the superseded page's status.

Paper cards add `extends` and `extended_by`, both required to be symmetric: every `extends: [X]` on this paper requires `extended_by` on X to include this paper. The lint enforces this. Asymmetry is a warning, not critical, but it means the lineage graph is out of date.

There is no `competes_with`, `depends_on`, or `see_also` vocabulary. `related` carries the weight the absent vocabulary might otherwise carry.

## The discipline underneath

Two more rules sit underneath the schema and do the rest of the work.

**Every claim cites at the page-and-section level.** A decision rule that says "follow X" without naming the chapter, section, figure, or page number it came from is a candidate for deletion. Vague citation is the surface failure mode that the rest of the schema exists to prevent.

**Trust is a source attribute, not a tone setting.** A confident-sounding canon page sourced from D-trust material is not honestly confident. The schema separates `trust_level` and `confidence` so the operator cannot accidentally calibrate one to the other. The propagation rule for canon pages — trust calibrated to the lowest of *primary* anchors, not the lowest of every cited source — is the operational consequence of this principle.
