# skills/

The Skills pack. Each Skill is a folder containing a `SKILL.md` with YAML frontmatter, instructions for the LLM, and supporting scripts where determinism matters more than prose-instruction. Skills are the unit of installable capability in this pattern.

**`consult/`** — query a KB for a senior-practitioner answer with citations. Reads the schema, retrieves relevant pages, synthesizes, gates the output, retries on gate failure, falls back to an explicit `## Gap` section when the KB cannot back the question. Includes `gates.py` (deterministic output validators) and `load_config.py` (`.consult.yaml` reader for the canon-boost override).

**`ingest/`** — distill a raw source (book, paper, repository, postmortem) into a card matching the schema's frontmatter contract, propose 5–10 canon pages the source touches, append to the KB log. The operator reviews proposals before they reach canon.

See [`../methodology/schema.md`](../methodology/schema.md) for the rules layer these Skills operate against.
