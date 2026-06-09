# Agent Claim Corpus v0.1

This is a deterministic synthetic benchmark for Anti-Slop's agent claim
verification checker. It measures whether `anti-slop-claims` catches fabricated
or unsupported references and receipts under the current resolver contract.

It is not a benchmark of agent quality, model quality, code correctness,
semantic support, benchmark validity, statistical meaning, safety, advice
quality, source truth, reasoning, or canon.

Run:

```sh
make agent-claim-benchmark
```

The runner creates a temporary local git fixture, evaluates the committed
`cases.json`, and writes:

- `results/summary.json`
- `results/summary.md`

Current corpus: 55 deterministic cases, including 5 cluster-derived regression
cases from the external dry-run learning loop. These cases are regression
coverage for resolver behavior, not market/usefulness evidence.
