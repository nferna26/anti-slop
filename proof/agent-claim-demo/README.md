# Agent Claim Verification Demo

Run:

```sh
make agent-claim-demo
```

The demo builds a temporary local git fixture. The fake report fails with
line-level reasons. The receipt-backed report passes because its file, changed
file, test, command receipt, and metric receipt claims resolve.

This proves only deterministic reference/receipt resolution. It does not prove
correctness, relevance, source truth, support, safety, advice quality, reasoning,
benchmark validity, statistical meaning, or canon.
