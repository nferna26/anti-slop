# Tag Install Smoke

- Schema: `anti-slop-tag-install-smoke.v1`
- Status: `pass`
- Tag: `anti-slop-receipts-v0.1.1`
- Target commit: `4bb51ced8035d0984515002197306dfc737e1f09`
- Install spec: `anti-slop-lineage @ git+https://github.com/nferna26/anti-slop@anti-slop-receipts-v0.1.1`

This smoke installs from the public tag in temporary storage, not a local editable checkout. Raw venv logs and temp paths are not committed.

Boundary: this checks only tag resolution and install/CLI smoke facts. It is not external adopter install success and does not prove correctness, relevance, source truth, support, safety, advice quality, reasoning, benchmark validity, statistical meaning, or canon.

## Remote Tag

- Peeled commit: `4bb51ced8035d0984515002197306dfc737e1f09`

## Tag Source Disclosure

- Do not force-move `anti-slop-receipts-v0.1.0` or `anti-slop-receipts-v0.1.1`.
- v0.1.1 Source-Doc Invariant is present in the tag source.
- The tag source explains that post-tag install proof may live outside the tag commit because proof can only be generated after the tag exists.
- The historical v0.1.0 stale-tag disclosure remains separate from v0.1.1.

## Commands

- `anti-slop-lineage --self-test`: pass (exit 0)
- `anti-slop-pr --self-test`: pass (exit 0)
- `anti-slop-pr-event --self-test`: pass (exit 0)
- `anti-slop-claims --self-test`: pass (exit 0)
- `anti-slop-run --self-test`: pass (exit 0)

## Report-Mode Demo

- `anti-slop-claims --report --json AGENT_FINAL_REPORT.md`: pass (exit 0)
- Fabricated ref exposed: True
