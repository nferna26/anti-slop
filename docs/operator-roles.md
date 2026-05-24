# Operator Roles

books-kb is small enough that a single operator usually wears every hat. This doc names the hats so accountability stays legible as the project grows or as additional people start contributing.

A role is not a person. One person can hold several roles at once. A role can also be vacant for a while — the work the role would do simply does not get done until someone picks it up.

## The six roles

### GM (General Maintainer)

Owns the repo. Decides what lands in `kb/`, `corpus/`, `canon/`, `evals/`, `gates/`, `proof/`, `runs/`, `registry/`. Final say on the README, AGENTS.md, methodology, and the seven-layer substrate.

Day-to-day: reviews PRs (or self-review for solo runs), keeps `kb/index.md` and `kb/log.md` honest, runs the gates before commit, prunes archive content from the front door.

### Source owner

Owns a specific source from manifest entry through source card. Marks `acquisition_status`. Sources lawful copies. Records edition / year / publisher / ISBN / locator system. Stores raw text local-only. Authors the book map and the source card(s) for that source.

Multiple source owners can exist in parallel. One source owner per source at a time.

### Judge

Reads model outputs and scores them against the case rubric. Does not propose canon. Does not edit cards. Records dimension-by-dimension scores in the eval's `scores.md` and observations in `judge-notes.md`.

The judge role is structural: it keeps "did this run pass" separate from "what should canon say." Conflating the two is one of the failure modes the methodology exists to prevent.

### Editor

Owns the prose layer of public-safe artifacts: README, docs, methodology pages, workflow files. Light copyedits to cards and canon candidates are fine; structural changes go through the artifact owner.

The editor does NOT change advisory claims. Authority changes go through canon promotion.

### Canon owner

Approves or rejects canon candidates. Owns the canon promotion workflow at `canon-promotion-workflow.md`. Records decisions in `registry/`.

The canon owner is the only role allowed to elevate a claim from synthesis to canon. The GM and canon owner are often the same person; they don't have to be.

### Eval owner

Owns an eval family (e.g., bibliographic-adversary, contradiction-preservation, canon-promotion-tournament, long-tail-transfer, source-lineage-hostile). Defines cases. Maintains the case rubric. Updates the eval methodology doc.

One eval owner per family.

## Solo operator default

When one person holds all six roles, the helpful discipline is to ask whose-hat-am-I-wearing-right-now before acting:

- Adding a source card? → source owner.
- Scoring a model run? → judge.
- Approving a canon candidate? → canon owner.
- Tightening README prose? → editor (or GM).
- Building an eval case? → eval owner.
- Fixing a broken link in `kb/index.md`? → GM.

The hats keep the substrate honest even at n=1.
