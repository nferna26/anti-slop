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
