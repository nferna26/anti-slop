# Real Command Receipt Dogfood

- Schema: `anti-slop-real-command-receipt-dogfood.v1`
- Status: `pass`
- Reports: 2
- Command receipt claims: 2
- Command receipt dogfood rate: 100%
- Receipt source: generated at smoke time with anti-slop-run; raw receipts are not committed

Raw anti-slop-run receipts are regenerated in temporary storage and are not committed because command receipts record local cwd.

Boundary: command receipts prove local command facts only, not correctness, relevance, support, safety, source truth, advice quality, reasoning, benchmark validity, statistical meaning, or canon.

## Reports

- `proof/real-command-receipt-dogfood/reports/real-checkout-final-report.md`: 1/1 command receipt claims passed
- `proof/real-command-receipt-dogfood/reports/real-checkout-actionability-final-report.md`: 1/1 command receipt claims passed
