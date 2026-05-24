---
case_id: normalization-vs-latent-errors-runway-lighting-v5
benchmark_version: normalization-vs-latent-errors-runway-lighting-v5-v1
artifact: postmortem
result_status: partial
postmortem_date: 2026-05-23
v6_status: design-from-failure
---

# Postmortem - normalization-vs-latent-errors-runway-lighting-v5

This is a public-safe postmortem of the frozen
`normalization-vs-latent-errors-runway-lighting-v5-v1` benchmark pass. It reads
on top of `eval-decision.md`, `score-sheet.md`, and the two hosted API judge
receipts. It changes no model output, no judge receipt, no score total, no
Result status, no eval decision, and no source/tension/canon/registry artifact.
The `## Result` in `score-sheet.md` stays `partial`.

## What this postmortem is built from

The committed, public-safe case artifacts only: `case.md`, `run-packet.md`,
`score-sheet.md`, `eval-decision.md`, `judge-packet/judge-calibration-openai-gpt-5.4-mini-api.md`,
`judge-packet/judge-score-anthropic-claude-opus-4-7-api.md`, and the
condition-blind judge packet. It does not use the local-only `OUT-NN` to
condition answer key, raw model prompts, raw API transcripts, or raw source
texts. Condition-level figures below are quoted from the committed
aggregate-only reconciliation in `score-sheet.md` and `eval-decision.md`.

## What worked

The v5 machinery worked. The case froze only after operator approval of the
calibration anchors, generated forty real `gemma4:31b` outputs, built a
condition-blind `OUT-NN` packet, enforced calibration before scoring, recorded
hosted OpenAI and Anthropic API receipts, and reconciled scored outputs
aggregate-only from committed hashes. The local-only answer key was not
committed, and no per-`OUT-NN` to condition mapping appears in the public tree.

That matters. v5 is useful as evidence that the benchmark pipeline can execute
cleanly from freeze through public-safe reconciliation.

## Why the case was `do_not_promote`

The case did not fail because the run was informal or incomplete. It failed
because the pre-registered rule correctly rejected the evidence.

OpenAI `gpt-5.4-mini` failed the calibration gate. It returned all PASS verdicts
for all three anchors, producing 7 criteria differences and an Anchor C C5/C6
disagreement against the withheld reference. Per the frozen protocol, OpenAI
scored zero real outputs. This is a judge-calibration failure, not a model-run
failure.

Anthropic `claude-opus-4-7` passed calibration and scored all forty blinded
outputs. Its receipt is eligible for aggregate reconciliation, but one scored
judge is not enough for a positive benchmark result. The positive rule requires
at least two eligible external scored judges with stable margins.

More importantly, the Anthropic aggregate showed the v5 task was still too easy
for generic practical advice. `substrate_workflow` scored 6.000, but
`generic_advice_prompted` also scored 6.000. The substrate-minus-generic margin
was +0.000. The generic condition also saturated the two critical mechanism
criteria: C3 pass rate 1.00 and C4 pass rate 1.00. That means the task did not
force a separation between substrate-shaped reasoning and competent generic
advice.

The equal-length control did separate: `vanilla_long_prompt` averaged 1.125,
with C3 at 0.12 and C4 at 0.00. So v5 did not collapse into a prompt-length
effect. The failure is narrower and more instructive: a short prompt asking for
careful practical tradeoff-aware advice was enough to elicit the same mechanism
and boundary language that the substrate condition needed to show.

## The failure signal

v5 made the right answer too visible. The scenario contained strong traces of
both mechanisms and an explicit option structure whose tradeoff was easy to
name: repair/audit learns more about the pattern, while a monitor adds warning
coverage without resolving the underlying circuit or closure practice. A good
general-purpose advisor could infer that boundary from ordinary operational
reasoning without needing the reviewed substrate artifacts.

That is not a reason to tweak v5 after the fact. v5 should remain frozen as a
clean negative result and as proof that the machinery works. The next case has
to be a fresh design from the failure mode.

## v6 implication

v6 should make generic practical advice insufficient unless the answer infers:

1. the repeated-acceptance mechanism from subtler administrative evidence;
2. the latent-defect / defence-stack mechanism from subtler technical evidence;
3. the intervention boundary: what the recommended action reveals, prevents, or
   leaves dangerously unlearned under the actual constraint.

The v6 scenario should not hand the model an obvious "audit versus monitor"
frame. It should make the tempting generic advice locally plausible but
insufficient: for example, a sensible-sounding action should reduce visible
risk while worsening acceptance drift, or produce reassuring measurements that
do not touch the dormant failure path. Passing should require identifying the
specific boundary, not merely recommending caution, more checks, better
documentation, escalation, or "do both."

## Discipline note

This postmortem records design learning. It promotes nothing. The v5 case stays
`partial` and `do_not_promote`; no benchmark-supported result, canon candidate,
or public advice claim follows from it.
