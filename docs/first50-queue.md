# First-50 Queue

`scripts/first50_queue.py` is a read-only queue report for the first-50 source wave. Run it with:

```sh
make first50-queue
```

It ranks the next useful work from public manifests and public artifacts only. It does not read `local-only/`, call models/APIs, edit statuses, or create artifacts.

## What It Reports

- L0-L4 level counts for wave-1 sources.
- A ranked table of recommended next actions.
- Ready lanes:
  - reviewed maps with no source card;
  - verified and deep-map-ready sources with no map;
  - verified and map-lite-ready sources with no map;
  - sourced books that still need metadata/locator packets;
  - rights/access blocked books;
  - not-yet-sourced books.
- A single suggested immediate move.

## Map Class Routing

The queue distinguishes map depth because first-50 coverage should not require a full deep map for every verified source.

- **Deep map** is recommended for source-id registry `map_candidate` or `deep_card_candidate` sources. These are anchors likely to produce several source cards, tensions, or evals.
- **Map-lite** is recommended for other verified first-50 breadth sources. It is still public-safe and reviewable, but it limits the map to verified metadata, locator scheme, source structure, 3-5 candidate claims, 3-5 candidate tensions, eval relevance, and misuse risks.

Both classes remain `machine_generated_not_canon`; the distinction is workflow depth, not authority.

## Current Operating Use

After the first metadata/locator packet drain, `first50-queue` became the main breadth/depth router: metadata packets are no longer the bottleneck for sourced first-50 books, and the next decision is whether each verified unmapped source should get map-lite or a deep map.

Use the suggested immediate move for the next single artifact pass. Use the ready lanes to batch only compatible map classes under `anti-slop-book-map` Workflow 6.
