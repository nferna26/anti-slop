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

## Tag Source Disclosure

- Do not force-move `anti-slop-receipts-v0.1.0`.
- The tag's embedded docs predate PR #46 finalization: `docs/tag-approval-packet.md` inside the tag says Decision: `ready_to_request_operator_tag`, candidate `4bda4fd727018a2a027ba8c660c48c30b8aa2144`, and `No tag has been created`.
- The installable package smoke passes, but the tag's embedded docs predate PR #46 finalization.
- Any GitHub release from v0.1.0 requires explicit disclosure, or the safer path is creating `anti-slop-receipts-v0.1.1` after PR #46 merges and fresh tag-install proof passes.

## Commands

- `anti-slop-lineage --self-test`: pass (exit 0)
- `anti-slop-pr --self-test`: pass (exit 0)
- `anti-slop-pr-event --self-test`: pass (exit 0)
- `anti-slop-claims --self-test`: pass (exit 0)
- `anti-slop-run --self-test`: pass (exit 0)

## Report-Mode Demo

- `anti-slop-claims --report --json AGENT_FINAL_REPORT.md`: pass (exit 0)
- Fabricated ref exposed: True
