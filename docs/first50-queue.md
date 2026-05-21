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
  - verified and map-ready sources with no map;
  - sourced books that still need metadata/locator packets;
  - rights/access blocked books;
  - not-yet-sourced books.
- A single suggested immediate move.

## Current Baseline

The first run reports:

- L4: 4 sources already participate in a reviewed claim/tension card or eval case.
- L3: 1 source has at least one reviewed source card but no reviewed tension/eval participation.
- L2: 1 source has a reviewed book map but no source card.
- L0: 44 sources are registered but blocked, unsourced, or not yet metadata/locator verified.

The immediate move is `BK-0003` (`Working Backwards`): its book map is reviewed, but it has no source card. The report recommends drafting the first approval-ready source card via `anti-slop-source-card` Workflow 5.

The next planning lane is metadata/locator packets for sourced-but-unverified first-50 books, especially map candidates and first-30 deep-card candidates.
