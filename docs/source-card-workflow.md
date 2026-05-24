# Source Card Workflow

Source cards are reviewed evidence units. Each card captures one claim or tightly related evidence point from one source, with a locator, a short excerpt when appropriate, a paraphrase, scope conditions, and misuse risk.

Source cards are not canon. They sit one rung above book maps on the artifact ladder: book maps are noncanonical discovery aids; source cards are operator-reviewed evidence units. Source cards support, sit in tension with, or qualify later claim/tension cards and canon candidates — they do not themselves assert canon.

Use:

```sh
python3 scripts/new_source_card.py <source_id>
```

Keep excerpts short. Prefer locators and paraphrase over copied text.

For ordinary first-50 throughput, keep source cards compact: roughly 700-1,000 words unless the operator has selected the card as anchor evidence. Longer cards are allowed only when the added scope, lineage, or misuse detail reduces review risk rather than adding essay-like explanation.

## Frontmatter fields

- `card_id` — assigned by `new_source_card.py` (`<source_id>-card-NNN`).
- `source_id` — the book this card draws from.
- `title`, `author` — bibliographic metadata, from the verified `books-200.yaml` row.
- `locator` — chapter / section / page, consistent with the source's `locator_system`.
- `issue_or_question` — one line naming the question or issue the card's claim addresses. This is what the card is *for*; it keeps the card pointed at a real question rather than a free-floating fact.
- `claim_type` — exactly one value from the controlled set below.
- `operator_review_status` — `unreviewed` until an operator reviews the card.
- `publication_status` — per `publication-statuses.yaml`.

## claim_type — controlled set

Pick exactly one. The set is deliberately small; do not invent new values.

| Value | Use when the claim… |
|---|---|
| `factual` | states a fact or finding the source reports. |
| `diagnostic` | names what is wrong, or what the problem actually is. |
| `mechanism` | explains how or why something works. |
| `method` | describes a procedure, technique, or repeatable practice. |
| `norm` | states a should / ought rule. |
| `warning` | names a failure mode or risk to avoid. |
| `boundary_condition` | states where a claim does or does not apply. |
| `open_question` | something the source raises but does not resolve. |

## Relation sections: supports / tensions_with / qualifies

Three body sections record how this card relates to the rest of the substrate:

- `## Supports` — claims, cards, or maps this card provides evidence for.
- `## Tensions with` — claims, cards, or maps this card sits in tension with. A tension is a comparison to investigate, not a resolved contradiction. (This section replaces the older `## Contradicts` heading; the methodology preserves tensions rather than declaring contradictions.)
- `## Qualifies` — claims or cards this card narrows, bounds, or adds a scope condition to.

**Public-safe rule for all three sections.** Entries are public-safe references only: source IDs (`BK-XXXX`), card IDs (`BK-XXXX-card-NNN`), reviewed-map references (`corpus/book-maps/BK-XXXX.md`), and locators. No raw source text, no private paths, no source-prose quotes. One entry per line as `<ref> — <brief note>`. An empty section is acceptable — write `None.` rather than leaving it blank.

## Discipline

- One card, one claim. If the evidence carries two claims, write two cards.
- A source card never says "and the right rule is X." It says "this source claims X, at this locator, in this context." Synthesis belongs in claim/tension cards; advice belongs in canon.
- Excerpts stay within the per-card cap in the acquisition registry. When in doubt, paraphrase plus locator.
- No graph database, no embeddings, no automation: the relation sections are judgment rails the operator fills by hand, not machine-traversed edges.
