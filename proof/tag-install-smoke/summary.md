# Tag Install Smoke

- Schema: `anti-slop-tag-install-smoke.v1`
- Status: `pass`
- Tag: `anti-slop-receipts-v0.1.0`
- Target commit: `75ac7fbe80f62d50409ebc8fe1f736e9bc2fa649`
- Install spec: `anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@anti-slop-receipts-v0.1.0`

This smoke installs from the public tag in temporary storage, not a local editable checkout. Raw venv logs and temp paths are not committed.

Boundary: this checks only tag resolution and install/CLI smoke facts. It is not external adopter install success and does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.

## Remote Tag

- Peeled commit: `75ac7fbe80f62d50409ebc8fe1f736e9bc2fa649`

## Commands

- `anti-slop-lineage --self-test`: pass (exit 0)
- `anti-slop-pr --self-test`: pass (exit 0)
- `anti-slop-pr-event --self-test`: pass (exit 0)
- `anti-slop-claims --self-test`: pass (exit 0)
- `anti-slop-run --self-test`: pass (exit 0)

## Report-Mode Demo

- `anti-slop-claims --report --json AGENT_FINAL_REPORT.md`: pass (exit 0)
- Fabricated ref exposed: True
