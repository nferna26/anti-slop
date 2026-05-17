# Anti-Slop

> Personal project. Not affiliated with my employer.

AI-assisted output without senior judgment in the loop is dismantleable by any senior reader who looks closely. The fix is not a better model. It is putting that judgment in the loop — compiled once into a queryable substrate, queried with citation discipline, and gated against the specific failure modes that make AI output sloppy.

This is a six-month build of that pattern in the open. Code and substrate at [github.com/nferna26/anti-slop](https://github.com/nferna26/anti-slop). MIT.

## What the pattern enforces

Evidence, judgment, and unknowns are tracked separately, and judgment is never smuggled into evidence. Every claim cites the specific page, chapter, or figure it came from. Trust is a property of the source, not the rhetorical confidence of the page that uses it. Cited numbers must appear verbatim in the cited source. Quoted text appears verbatim in the cited card; if a gate forces a banned word out of a quote, the synthesis paraphrases rather than partially-rewriting quoted text.

## How it is enforced

A knowledge base — a folder of markdown organized in five layers — that compiles books, papers, and operational documents into operator-voiced decision rules with chapter-and-section citations.

A consultation Skill that retrieves relevant decision rules for a question, synthesizes an answer, and cites every claim back to its source.

A small set of deterministic gates that fail any output without citations, without honest caveats, with marketing words, or with numbers that aren't in the cited sources. A retry loop that asks the model to fix specific gate failures before the output reaches the user. A gap fallback that returns an explicit "the KB cannot back this" section instead of papering over with general knowledge.

## What this is not

This is not retrieval-augmented generation. RAG fetches chunks of source material into an LLM's context at query time; this pattern compiles the source material into operator-voiced cards once, then queries the compilation. The operator owns the synthesis.

This is not a turnkey product. The schema accreted over months of operational use; the gates accreted over the first end-to-end runs. A reader pasting the structure into a new folder will get the field layout right and the discipline wrong. The discipline is the load-bearing piece, and it takes time and friction to develop.

This is not a critique of people doing AI work without these guardrails. It is a description of what the guardrails are, why each one earns its place, and where each one came from in the work.

## Reading further

The full schema, the four operations, the frontmatter contract, the retrieval ranking rules, and the quotation discipline are all in [methodology/schema.md](https://github.com/nferna26/anti-slop/blob/main/methodology/schema.md). The session-rules template that operates against the schema is at [methodology/CLAUDE.md](https://github.com/nferna26/anti-slop/blob/main/methodology/CLAUDE.md). The consultation Skill itself, with the gates and the retry loop, is at [skills/consult/SKILL.md](https://github.com/nferna26/anti-slop/blob/main/skills/consult/SKILL.md).

The install command lands when the productization sprint ships in Month 5. Until then, the repo is the canonical thing — clone it, read the schema, decide if the pattern fits your work.
