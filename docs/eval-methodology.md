# Eval Methodology

The first proof surface is five eval families:

- bibliographic adversary
- contradiction preservation
- canon promotion tournament
- long-tail transfer
- source-lineage hostile

Each eval case records its input packet, expected source behavior, expected output shape, scoring rubric, failure modes, positive result, falsifier, model outputs, score sheet, and judge notes.

Use:

```sh
python3 scripts/new_eval_case.py <eval_type> <case_id>
```

This scaffold does not run model calls. Model outputs are receipts added later.
