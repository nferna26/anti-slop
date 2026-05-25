# Gates

Gate specs define review checks for substrate artifacts and later model-output
receipts. Most gates are still scaffold-only. The citation-lineage and
no-universalization gates now have deterministic first-pass scripts:

```sh
make gate-citation-lineage FILE=<path>
make gate-no-universalization FILE=<path>
```

See `gate-specs.yaml`.
