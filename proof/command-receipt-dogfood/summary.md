# Command Receipt Dogfood

- Schema: `anti-slop-command-receipt-dogfood.v1`
- Status: `pass`
- Report fixture: `proof/command-receipt-dogfood/AGENT_FINAL_REPORT.md`
- Receipt source: generated at smoke time with anti-slop-run; raw receipts are not committed
- Claim check: `anti-slop-claims --receipts`
- Command receipt claims: 2
- Command receipt dogfood rate: 100%

Raw anti-slop-run receipts are not committed because the schema records local cwd. The smoke regenerates them in a temporary repo.

Boundary: command receipts prove local command facts only, not correctness, relevance, support, safety, benchmark validity, source truth, advice quality, reasoning, statistical meaning, or canon.
