# Evals

The eval surface tests whether the substrate improves citation lineage, contradiction handling, canon promotion, long-tail transfer, and hostile source-lineage behavior.

Create a case with:

```sh
python3 scripts/new_eval_case.py <eval_type> <case_id>
```

Valid eval types:

- bibliographic-adversary
- contradiction-preservation
- canon-promotion-tournament
- long-tail-transfer
- source-lineage-hostile

## Result status

Each case's `score-sheet.md` carries a result status in its `## Result` section. See `docs/eval-result-status-policy.md` for the controlled vocabulary — `partial`, `inconclusive`, `falsified`, `dry_run_supported`, `benchmark_supported` — the difference between dry-run and benchmark evidence, and the bar an eval result must clear before it may support a canon candidate. Only a `benchmark_supported` result is strong enough for canon promotion.
