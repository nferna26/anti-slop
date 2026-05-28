---
case_id: locator-accuracy-v2
benchmark_version: locator-accuracy-v2-v1
artifact: judge-discrimination-autopsy
status: design_only_followup
result_status: partial
eval_decision: do_not_promote
decision_class: non_discriminating_judge_and_famous_margin_failed
created: 2026-05-28
---

# Judge Discrimination Autopsy - locator-accuracy-v2-v1

## Scope

This is a design-only follow-up to `locator-accuracy-v2-v1`. It does not
rescore outputs, revise the frozen rule, add a judge, freeze a successor, lift a
Result, or promote canon. The purpose is to understand why the mechanical-lineage
signal did not clear the pre-registered two-route rule.

Evidence inspected: `case.md`, `score-sheet.md`, `eval-decision.md`,
`postmortem.md`, `run-packet.md`, `judge-packet/judge-instructions.md`,
`judge-packet/calibration-anchors.md`, both hosted judge-score receipts, the
condition-blind output manifest, committed model-output receipts, and the
local-only OUT-NN answer key. The answer key was used only to compute aggregate
condition and case summaries. No per-OUT to condition/case/run mapping is
committed here.

## Core Finding

The substrate signal did not vanish. Both judges scored `substrate_workflow` at
zero F1-F5 failures and assigned valid support coverage only to the substrate
condition. The scoring-surface failure is narrower: F1-F5 were calibrated as
safety and refusal flags, while the real discriminating behavior was positive
use of reviewed lineage. Anthropic treated many safe-refusal outputs as clean
passes; OpenAI often treated the same pattern as a failure to use or acknowledge
available reviewed lineage. That interpretation split is why one route saturated
at the failure floor and the other produced spread.

The v2 result should therefore be read as a mechanical-lineage near-miss, not as
a reason to rescue v2. Any future version needs a scoring surface where "safe
refusal with no support" is not confused with either "fabrication" or "correct
reviewed support."

## Aggregate Pattern

| Route | Total F1-F5 failures | Outputs with total failure count 0 | Valid support coverage | Route-local outcome |
| --- | ---: | ---: | ---: | --- |
| `hosted_anthropic_r2` | 35 | 208/240 (86.7%) | 43 | Blocked by non-discriminating guard and famous-source margin |
| `hosted_openai_r3` | 162 | 107/240 (44.6%) | 41 | Clears route-local rule |

Condition-level result from the committed score sheet:

| Condition | Anthropic failures / coverage | OpenAI failures / coverage | Read |
| --- | ---: | ---: | --- |
| `substrate_workflow` | 0 / 43 | 0 / 41 | Stable intended signal: support coverage without F1-F5 failures. |
| `criteria_prompted_no_sources` | 0 / 0 | 17 / 0 | Clean refusal under Anthropic; missed/denied lineage under OpenAI. |
| `famous_sources_supplied` | 9 / 0 | 34 / 0 | The Anthropic famous-source margin failed by one failure. |
| `generic_advice_prompted` | 10 / 0 | 27 / 0 | More failure-prone than criteria, but still no coverage. |
| `vanilla_long_prompt` | 11 / 0 | 45 / 0 | Controls fail more when not explicitly provenance-trained. |
| `vanilla` | 5 / 0 | 39 / 0 | Same pattern: no coverage, more OpenAI failures. |

The two routes disagreed on failure totals for 120/240 outputs. The differences
were concentrated in F5 and F1: F5 differed on 89 outputs and F1 differed on 58
outputs. Coverage was comparatively stable, disagreeing on only 4/240 outputs,
all inside `substrate_workflow` case 5.

Exact duplicate output bodies were common: the 240 public model outputs contain
111 unique output bodies, with 47 duplicate groups and a largest duplicate group
of 8. The low-temperature benchmark therefore gave judges many repeated refusal
patterns. That helped reveal the route difference, but it was not the whole
cause: OpenAI still generated spread on the same duplicate-heavy packet.

## Failure And Signal Taxonomy

### Safe Refusal With No Coverage

This was the dominant non-substrate pattern. Many outputs correctly refused a
requested card, locator, quote, false relation, book-map evidence move, or canon
claim, but did not add reviewed public-KB support. Anthropic usually scored this
as zero failures. OpenAI often agreed when the output merely refused, but fired
when the output also denied the availability of reviewed cards or left a
supportable claim unanchored.

This category is useful behavior, but it is not the substrate's intended edge.
It should receive low or zero support credit, not necessarily a safety failure.

### Correct Support Coverage

`substrate_workflow` produced the intended behavior: it refused unsupported
pressure and also used reviewed public-KB lineage where a supportable claim was
available. Both routes gave substrate zero failures. Coverage was high and
route-stable: 43 under Anthropic and 41 under OpenAI.

This is the real mechanical signal. It is narrower than "better advice": the
substrate adds inspectable public-KB lineage where controls often stay silent.

### Over-Refusal / Denial Of Available Reviewed Lineage

OpenAI repeatedly penalized outputs that said a reviewed card could not be
verified or was not available when the judge context listed that card as
reviewed lineage. Anthropic fired this much less often. This explains a large
share of the route gap.

The ambiguity comes from the v2 task wording. The advisor tells the model to use
only lineage available in its packet, while the judge packet gives judges the
global reviewed lineage for scoring. A non-substrate condition can truthfully say
it did not receive card content, but a judge can also truthfully say the
corrected public note failed to use available reviewed lineage. V2 did not
separate those two interpretations cleanly enough.

### Unsupported Acceptance

OpenAI used F5 broadly for outputs that accepted, left standing, or failed to
repair an unsupported requested relation. Anthropic used F5 narrowly, mostly
when an answer accepted the adversarial pressure outright. This is the largest
single route-disagreement source.

For v3, F5 should stay a safety flag for accepting unsupported pressure. A
separate support-opportunity score should carry the "missed available lineage"
distinction.

### Source, Locator, Or Canon Drift

F2 and F3 did not carry much of the result. Anthropic saw no F2 outside
case 5, while OpenAI saw no F2 at all. Anthropic found 7 F3 failures and OpenAI
found none. F4 also did not behave symmetrically: Anthropic scored zero F4 in
the full run, while OpenAI found 12 F4 failures concentrated in authority-drift
patterns.

The hidden-canon and book-map traps remain useful, but their v2 anchors did not
produce a stable enough full-run F4 surface.

### Judge Floor Saturation / Over-Forgiveness

Anthropic's 208/240 zero-failure count is not random noise. It reflects a
coherent scoring interpretation: if an output refuses unsupported pressure and
does not fabricate, it usually passes F1-F5, even if it provides no positive
reviewed support. That is a reasonable safety interpretation, but it makes F1-F5
too low-spread to promote a coverage-led result.

## Why Anthropic Saturated

Anthropic passed the calibration anchors, but the anchors did not include enough
realistic cases where an output safely refuses while also failing to use an
available reviewed card for a supportable claim. Anchor F taught clean refusal;
Anchor H taught correct refusal has coverage 0. Neither anchor forced a clear
choice between "safe refusal is a zero-failure pass" and "missed available
lineage is a failure."

In the full run, Anthropic mostly chose the first interpretation. That made
`criteria_prompted_no_sources` a perfect 0-failure control, gave
`famous_sources_supplied` only 9 total failures, and tripped the
non-discriminating-judge guard.

## Why OpenAI Produced Spread

OpenAI interpreted the judge-side reviewed-lineage list more aggressively. It
penalized outputs that denied reviewed card availability, removed supportable
lineage, left bare book-level claims standing, or refused without making the
available correction. This created the intended separation on failure rates:
`criteria_prompted_no_sources` had 17 failures, `famous_sources_supplied` had
34, and `substrate_workflow` had 0.

That interpretation is closer to the product claim if the task is "produce a
source-backed public note," but v2 did not pre-register the distinction with
enough precision. The lab correctly refused to let one favorable route carry
the result.

## Design Implications

1. Keep F1-F5 as provenance-safety guardrails, not the only promotion surface.
   They are good at catching fabrication, locator drift, false attribution, and
   authority laundering, but they floor-saturate when controls safely refuse.

2. Add a first-class support-opportunity surface. Each case should state which
   supportable claim exists and which reviewed card/locator can anchor it. A
   score can then distinguish:
   - unsupported acceptance or fabrication;
   - safe refusal with no reviewed support;
   - false denial of available reviewed lineage;
   - correct reviewed support.

3. Calibrate judges on safe refusal versus missed support directly. V3 anchors
   need naturalistic examples where an answer refuses the bad page/card/canon
   request but also omits, denies, or preserves the correct reviewed card.

4. Apply the non-discriminating guard to the load-bearing registered surface.
   A coverage-led benchmark should not be blocked merely because safety failures
   floor-saturate, if the pre-registered support surface shows stable spread.
   Conversely, if both failures and support scores saturate, the guard should
   still block promotion.

5. Preserve the strict famous-sources rule. Author/title/topic memory should
   remain 0 coverage unless it supplies reviewed public-KB lineage with the
   reviewed locator and claim. V3 should keep famous-source controls because
   they are the right pressure test for training-data memory.

6. Reduce duplicate-output pressure before a full run. Either raise the run
   temperature modestly within a pre-registered band or run a small manual
   variation probe before freezing. The point is not to make outputs worse; it
   is to ensure the scoring surface sees enough real variation to test judge
   discrimination.

## Recommended Next Path

Proceed to a design-only `locator-accuracy-v3` draft, not a full benchmark and
not a product prototype yet. The v2 signal is strong enough to keep the
mechanical-lineage family alive, but the scoring surface needs a pre-freeze
repair before any generation spend.

The v3 design target should be:

- mechanical-lineage claim unchanged;
- F1-F5 retained as safety guardrails;
- new support-opportunity score as the primary discriminator;
- calibration anchors that include safe refusal, missed support, false denial
  of available lineage, and correct support;
- non-discriminating-judge guard defined over the registered load-bearing
  surface, not F1-F5 totals alone;
- a tiny high-agency probe that manually inspects every output before freeze.

Do not rescue v2. Do not cite v2 as `benchmark_supported`. Do not promote canon.
If v3 cannot make safe refusal versus correct support judge-stable at probe
stage, pause the benchmark family and redirect to the product prototype: a
brief compiler plus lineage gates that makes the same distinction operational
for an operator without needing a promotion-grade eval first.
