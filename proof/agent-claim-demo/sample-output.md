# Agent Claim Verification Demo Output

Command:

```sh
make agent-claim-demo
```

## Fake Report

`proof/agent-claim-demo/fake-agent-report.md`: FAIL

- line 3: changed_file docs/missing.md -> changed-file claim not found in supplied diff: docs/missing.md
- line 3: file docs/missing.md -> line 3: file does not resolve: docs/missing.md
- line 4: test tests/test_demo.py::test_missing -> line 4: test node not defined in tests/test_demo.py: test_missing
- line 5: command_receipt make package-smoke -> missing command receipt for claim: make package-smoke
- line 6: metric_receipt score=0.83 -> metric receipt mismatch for claim: score=0.83

## Receipt-Backed Report

`proof/agent-claim-demo/receipt-backed-report.md`: PASS
- hard claims passed: 5
- hard claims failed: 0

Boundary: this demo proves deterministic reference/receipt resolution only.
