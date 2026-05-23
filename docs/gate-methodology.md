# Gate Methodology

Gates are review checks applied to substrate artifacts and later model outputs. They are scaffold-only in this pass.

The seven gates are citation-lineage, source-diversity, canon-duplication, contradiction, quote-limit, authority-order, and no-universalization.

Gate logs belong in `runs/gate-logs/`. Gate specs live in `gates/gate-specs.yaml`.

Use:

```sh
python3 scripts/new_gate_log.py <run_id>
```
