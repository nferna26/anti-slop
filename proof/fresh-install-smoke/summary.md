# Fresh Install Smoke

- Schema: `anti-slop-fresh-install-smoke.v1`
- Status: `pass`
- Candidate commit: `4bda4fd727018a2a027ba8c660c48c30b8aa2144`
- Install spec: `anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@4bda4fd727018a2a027ba8c660c48c30b8aa2144`

This smoke uses temporary storage and installs from the public git/SHA spec, not a local editable checkout. Raw venv logs and temp paths are not committed.

Boundary: this checks only install/CLI smoke facts for the candidate commit. It is not external adopter install success and does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.

## Commands

- `anti-slop-lineage --self-test`: pass (exit 0)
- `anti-slop-pr --self-test`: pass (exit 0)
- `anti-slop-pr-event --self-test`: pass (exit 0)
- `anti-slop-claims --self-test`: pass (exit 0)
- `anti-slop-run --self-test`: pass (exit 0)

## Report-Mode Demo

- `anti-slop-claims --report --json AGENT_FINAL_REPORT.md`: pass (exit 0)
- Fabricated ref exposed: True
