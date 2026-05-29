# Citation-Lineage Demo Receipt (example)

Example of the receipt `make demo` writes to a transient temp dir. The compiled
brief sha256 varies between runs because the brief carries a compile date; the
gate results are deterministic.

## Pipeline

1. compile_brief from 5 reviewed source cards (BK-0048-card-001,
   BK-0001-card-001, BK-0002-card-001, BK-0042-card-001, BK-0044-card-002);
   brief sha256 `<varies by compile date>`.
2. static sample corrected note (placeholder model output) under
   `proof/citation-lineage-demo/`.
3. gate_citation_lineage.py --require-reviewed.

## Results

- good sample (`sample-corrected-note.md`): gate exit 0 (PASS); cites only
  reviewed cards at reviewed locators.
- slop sample (`sample-slop-note.md`): gate exit 1 (FAIL — unresolved reference
  caught); cites a nonexistent card `BK-9999-card-001`.

A model output is a test artifact, never an authority. This receipt records a
deterministic citation check, not source truth or canon.
