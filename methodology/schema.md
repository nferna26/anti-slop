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

Query. Read the index, rank candidates, fetch the top pages, synthesize with citations. Every claim cites a page. Source cards cite at the chapter, section, or figure level; canon pages cite at the page-id level via `source_refs`. A query that cannot cite is a query that has not been answered.

Lint. Scan for contradictions (two pages making opposite claims without a `contradicts` link), orphan pages, schema violations, and staleness (`review_by` past due). Lint runs on a fixed weekly slot, not "when needed."

Index/log. After any ingest or edit, rebuild the content-oriented index of queryable pages (cards and canon) and append to `log.md` (chronological). By convention the index lives at `<kb-root>/index.md`, though operators with an existing root index can place it at `<kb-root>/cards/index.md` instead — the consult Skill reads whichever path is present. The two surfaces serve different queries and are not redundant.

## Retrieval

Query is the operation; ranking is how the operation picks what to retrieve. The consult Skill enumerates every page under `cards/` and `canon/`, reads each page's frontmatter (not its body), and scores candidates by overlap between the question and the page's `tags` plus `domains`. Ties break by `trust_level` (A > B > C > D), then by `confidence` (high > medium > low). The top three pages are fetched in full for synthesis.

Canon pages get a boost. By default the boost is +2 added to canon's tag-overlap score before ranking. The rationale: source cards (broad anchors) tend to carry rich tag sets, while canon pages (focused judgment) carry narrower tags, so surface-overlap ranking systematically under-weights canon relative to where operator expectation places it. Without the boost, compiled judgment loses to source cards on questions where the operator would have chosen canon.

The +2 default is calibrated against the reference KB and may not transfer cleanly to KBs with different tag-density profiles. Operators override per-KB by placing a `.consult.yaml` at `<kb-root>/` with `canon_boost: <integer>`. The Skill reads this file at retrieval time and falls back to +2 if absent. Calibrate by running the Skill on five to ten representative queries: if compiled-judgment pages systematically fall outside the top three despite operator expectation, raise the boost; if they crowd out clearly-relevant source cards, lower it.

Surface-tag overlap has known lossy recall when the question's vocabulary names the problem while the relevant card's tags name the solution. Three documented cases in the reference KB: a question about "shipping multiple times a day" did not surface a card tagged `feature-flag, progressive-rollout, canary` because the question used no feature-flag vocabulary; a question about replacing change advisory boards missed the same card for the same reason; a question about LLM agent failure modes did not surface a paper tagged `prompt-injection, instruction-following`. Semantic or embedding-augmented ranking, or a maintained tag-synonym table, closes the gap. Surface-overlap is the current ranker; the limitation is documented and the eval set deliberately exercises it.

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
source_refs:  [<page-ids>]                  # upstream pages this page cites
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

**Quoted text appears verbatim, or it is not quoted.** When the synthesis frames a passage as quoted (with quotation marks), the quoted text must appear verbatim in the cited card. If a gate or constraint forces a banned word out of a quoted span, the synthesis drops the quote framing and paraphrases — it does not partially-rewrite quoted text. Partially-rewritten quotes misrepresent the source; honest paraphrase signals that the operator is summarizing rather than reporting verbatim.
