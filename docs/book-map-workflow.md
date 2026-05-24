# Book Map Workflow

Book maps are triage artifacts. They help index a source, identify arguments, surface possible Anti-Slop relevance, and point toward future source cards.

There are two map classes:

- **Map-lite** for first-50 breadth: verified metadata, locator scheme, compact structure, 3-5 candidate claims, 3-5 candidate tensions, eval relevance, and misuse risks.
- **Deep map** for anchors or operator-selected sources likely to produce multiple cards, tensions, or evals.

Book maps are not canon. Machine-generated maps must be reviewed before they are used in evals, canon candidates, or public reasoning.

Use:

```sh
python3 scripts/new_book_map.py <source_id>
```

Then fill the map from a lawfully accessible local source without pasting long copyrighted excerpts.
