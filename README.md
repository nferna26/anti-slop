# anti-slop

> Personal project. Not affiliated with my employer.

A Claude Code Skills pack that turns a folder of decision-rule cards into a queryable consultation surface, with deterministic gates that fail any output without citations or honest caveats.

Methodology at [anti-slop.dev](https://anti-slop.dev). Schema, frontmatter contract, retrieval ranking, and quotation discipline in [`methodology/schema.md`](methodology/schema.md). Session-rules template at [`methodology/CLAUDE.md`](methodology/CLAUDE.md).

Currently shipped: a consultation Skill ([`skills/consult/SKILL.md`](skills/consult/SKILL.md)) with deterministic output gates ([`skills/consult/gates.py`](skills/consult/gates.py)) and a `.consult.yaml` config loader ([`skills/consult/load_config.py`](skills/consult/load_config.py)). An ingest Skill ([`skills/ingest/SKILL.md`](skills/ingest/SKILL.md)) for distilling raw sources into cards.

The install command lands when the productization sprint ships in Month 5. Until then, the methodology page and the Skills are the canonical artifacts. Clone the repo, read the schema, decide if the pattern fits your work.

MIT.
