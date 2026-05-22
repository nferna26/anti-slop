---
case_id: diagnosis-vs-validated-learning-benefits-renewal-v2
benchmark_version: diagnosis-vs-validated-learning-benefits-renewal-v2-v1
artifact: postmortem
result_status: partial
postmortem_date: 2026-05-22
v3_status: design-direction-only — no v3 case drafted
---

# Postmortem — diagnosis-vs-validated-learning-benefits-renewal-v2

This is a public-safe postmortem of the frozen `diagnosis-vs-validated-learning-benefits-renewal-v2-v1`
benchmark pass. It reads on top of `eval-decision.md` and `judge-packet/judge-variance-summary.md`;
it explains **why** the case was decided `do_not_promote` and proposes a v3 eval-design
direction. It changes no model output, no judge receipt, no score total, no Result
status, no eval decision, and no source/tension/canon/registry artifact. The `## Result`
in `score-sheet.md` stays `partial`. No v3 case is drafted here — only design direction.

## What this postmortem is built from

The committed, public-safe case artifacts only: `case.md`, `score-sheet.md`,
`run-packet.md`, `eval-decision.md`, `judge-packet/judge-variance-summary.md`, and
the two condition-blind judge receipts (`judge-packet/independent-judge-score-gpt-oss-20b.md`,
`judge-packet/independent-judge-score-claude-opus.md`). It does **not** use the
local-only `OUT-NN` → condition answer key, raw model prompts, raw responses, or raw
source texts. Condition-level figures below are quoted from the already-committed
`judge-variance-summary.md`, which reconciled the receipts aggregate-only.

## Why the case was `do_not_promote`

The eval ran cleanly — forty real `gemma4:31b` outputs, eight per condition, frozen
before judging, blind-scored by two judges from different model families. The
non-promotion is not a process failure; it is the **correct** output of a
well-instrumented eval that returned a non-result. Five things drove it.

1. **The substrate did not clear the pre-registered positive rule.** `## Positive
   result` requires the `substrate_workflow` mean to beat *both* `vanilla_long_prompt`
   and `criteria_prompted_no_sources` by ≥1.5 points, to beat both controls by ≥0.33
   on each of C4/C5/C6 pass rate, and to do so under ≥2 agreeing judges. Neither judge
   met the rule. `gpt-oss:20b` ranked the substrate highest (mean 4.25) but beat the
   criteria-prompted control by only +1.25 (below the +1.5 bar) and missed the C4
   margin against both controls (+0.25 and +0.125, below +0.33). Claude Opus scored
   the substrate at ceiling (6.00) but with no separation at all from the controls.

2. **`criteria_prompted_no_sources` matched the substrate under Claude Opus.** Under
   that judge `criteria_prompted_no_sources`, `vanilla`, and `famous_sources_supplied`
   all scored 6.00 — identical to `substrate_workflow`. The criteria-prompted control
   exists precisely to catch this: if merely *being told the rubric qualities* equals
   supplying the reviewed substrate, the substrate's lineage **content** is not what
   moves the score. Under Opus, that is exactly what happened.

3. **The two judges diverged heavily on C5 and C6.** C5 (`No flattening`) verdicts
   differ on 20 of 40 outputs; C6 (`Honest recommendation under constraint`) differ on
   22 of 40. `gpt-oss:20b` produced a wide spread (0/6–6/6); Claude Opus concentrated
   35 of 40 at 6/6. That disagreement triggers the case's third-judge rule, and per
   `## Judge protocol` a judge-sensitive outcome stays `partial`: a win that depends on
   which judge is picked is not a win.

4. **The Claude Opus pass was not independent of the orchestrator.** The Opus judge is
   the same agent that designed the substrate, wrote the rubric, froze the packets, ran
   the generator, and built the judge packet. `case.md` → `## Judge protocol` and
   `judge-instructions.md` require a judge that is *not* the orchestrating agent. The
   Opus pass is recorded honestly as a judge-variance data point, not as one of the two
   independent judges the rule needs.

5. **Result remains `partial`.** With the positive rule unmet under both judges, an
   unresolved third-judge trigger, and only one of the two required *independent*
   judges, no clause supports a lift. `eval-decision.md` records `do_not_promote`;
   `score-sheet.md` → `## Result` stays `partial`.

## Design lessons

The instrumentation worked. The equal-length control did its job — `vanilla_long_prompt`
scored *lowest* under both judges (1.00 and 3.50), cleanly ruling out a more-tokens
effect. The freeze, blinding, and dependency rule held. The failures are in three
design surfaces: the rubric wording, the strength of the criteria-prompted control, and
the scenario's shape.

### The rubric had a built-in C5/C6 contradiction that judges resolved differently

This is the central finding. C5 passes when the answer "keeps the decision genuinely
open between the readings"; C6 requires the answer to "reach a recommendation." But
`## Expected reasoning` clause 5 explicitly blesses "an explicit, reasoned pilot-first
or rollout-now choice that *owns* its cost." So a single-sided-but-reasoned answer is
simultaneously **expected behaviour** and a literal C5 fail ("keeps the decision
genuinely open" reads as "do not decide"). Judges resolved the contradiction in
opposite directions: `gpt-oss:20b` read C5 strictly and failed reasoned single-sided
answers; Claude Opus read C5 as being about the *reasoning* and passed them. That is
the precise mechanism behind the 20/40 C5 split and, through the dependency rule, much
of the 22/40 C6 split. C5 conflated "hold the tension live while reasoning" with "leave
the decision unmade" — two different things — and never said which it meant.

### C1 was judge-sensitive on a labelling technicality

`gpt-oss:20b` failed C1 whenever an answer engaged both readings substantively but did
not *explicitly name* them as two readings; Claude Opus passed those answers. C1 split
roughly 20/20 between the judges. "Identifies live tension" needs to say whether it
scores substantive engagement or explicit labelling.

### C4 was too permissive to discriminate — the prompt pre-answers it

C4 (`Preserves validated-learning objection`) is satisfied by noting the diagnosis is
untested — but the Advisor prompt *itself* says "no one has actually tested it." An
answer that simply echoes the prompt passes C4. Both controls cleared it (`gpt-oss`:
0.625–0.750; Opus: 1.000 across the board), so the substrate could show no C4 margin
under either judge. A criterion the scenario prompt pre-answers cannot separate
conditions. By contrast C3 (`Preserves diagnosis-first objection`) requires an insight
the prompt does *not* supply — that three scattered pilots may test tactics without
naming the critical cause — and C3 was the one criterion that genuinely discriminated.

### The criteria-prompted control leaked the rubric, not just the criteria

`criteria_prompted_no_sources` was meant to be a mild confound — "did being told the
qualities matter?" But its recipe (`run-packet.md` → `## Condition packets`) paraphrases
all six rubric criteria in operational detail: keep both readings live, anchor in the
facts, preserve each objection, do not flatten, reach a recommendation that confronts
the constraint and names the reason against itself and disconfirming evidence. That is
a near-verbatim restatement of C1–C6 — effectively the grading key. Any competent model
handed the grading key will sit at ceiling on a rubric-graded answer. The control did
correctly reveal that the substrate adds nothing *beyond* criteria-awareness — but it
is so strong that it cannot distinguish "the substrate adds nothing" from "nothing
could have beaten this control."

### The scenario let a generic constrained hybrid score too well

The Advisor prompt lists "do some constrained version of both" as an option, and
`## Expected reasoning` blesses a constrained hybrid. The scenario also leaves an
obvious, *cheap* hybrid escape hatch — secure the funding line now, gate the actual
spend on the pilot results. Once that hybrid is available and low-cost, the
window constraint does not truly bind, and any answer that lands on the hybrid passes
C1, C5, and C6 almost by construction. Under Claude Opus, 35 of 40 outputs scored 6/6 —
the generator largely converged on the hybrid, and the hybrid *is* the rubric-shaped
answer. The case was supposed to make holding the tension hard; instead it made the
passing answer the salient one.

### What a future case must make harder

There must be **no answer template that satisfies the rubric without genuinely holding
the tension**. The hybrid must be a real, costed third horn — not a free synthesis the
prompt already names. Each criterion must require reasoning the scenario does not
spoon-feed. And the rubric must not contain a criterion whose pass condition contradicts
another criterion's.

## v3 design direction

Direction only — no v3 case is drafted here. v3 would open a new benchmark version
(`…-v2-v3` or a fresh `-v3` case id) and re-freeze; the v2 case and its receipts stay
untouched as the design/dry-run record.

1. **Sharper C5/C6 wording.**
   - Rewrite C5 so it is unambiguously about the *reasoning*, not the *decision*. C5
     passes when both readings' objections are materially weighed in the answer's
     reasoning *even if it reaches a definite single-sided recommendation*; C5 fails
     only when (a) one reading is absent, dismissed, or strawmanned, or (b) the answer
     substitutes a hybrid label for engaging the tradeoff without saying which
     commitments are reversible and how the window is met. Delete the phrase "keeps the
     decision genuinely open" — it reads as "do not decide" and collides with C6.
   - Tighten C6 to require the answer to engage the *specific* binding mechanism by
     name (four-week pilots cannot report before this cycle's funding window closes;
     the next window is a year out) and to state a *concrete, observable* disconfirming
     trigger, not a generic "if the evidence changes."
   - Pre-register, in the `## Criterion dependency rule`, how C5 and C6 relate so the
     v2 contradiction cannot recur.

2. **Calibration examples for judges.** Add 2–3 pre-scored anchor outputs to the judge
   packet — one clear pass, one clear fail, one deliberate borderline — each with the
   operator's reference C1–C6 verdicts and a one-line rationale, frozen before the run.
   Each judge scores the anchors first and checks against the reference before scoring
   the real outputs. This directly attacks the 20/40 and 22/40 divergence by aligning
   the bar up front.

3. **A weaker criteria-prompted control.** Replace the operational rubric paraphrase
   with a control that conveys only the *spirit* — e.g. "give balanced, well-reasoned
   advice that takes the tradeoffs seriously" — naming no enumerated criteria.
   Optionally keep a graded ladder: a weak generic-advice control *and* the current
   strong criteria control, so the substrate is measured against a range rather than a
   single near-ceiling control.

4. **A scenario where "constrained hybrid" is not automatically enough.** Redesign so
   the hybrid is a genuine third cost, not an escape hatch: make the budget indivisible
   (no "reserve the funding line" move), or make any funding commitment this cycle
   itself trigger the irreversibility, or shape the options as a true trilemma no
   synthesis dissolves. Reconsider whether the Advisor prompt should pre-name "a
   constrained version of both" at all — naming it scripts the passing shape. Ensure
   each criterion needs reasoning the prompt does not hand the model (the C3-vs-C4
   asymmetry above is the template: keep C3's property, fix C4's).

5. **A true independent / human judge requirement before any promotion.** v3 must
   pre-register, as a frozen gate, that no Result lift above `partial` is possible until
   at least one judge that is **not** the orchestrating agent — ideally a human, or a
   genuinely external model evaluation — has scored the packet. A judge run inside the
   orchestrating session does not count toward the two-judge minimum. In v2 this was a
   retrospective caveat on the Opus pass; in v3 it should be a gate set before the run.

## Discipline note

This postmortem records analysis and design direction. It confers no authority on any
model output, judge score, source card, or tension card, and it promotes nothing. A
model output, and a judge's score of one, is a test artifact — never an authority,
never citable as a source. The case stays `partial` and `do_not_promote`; this file
does not change that and does not itself constitute a Result status.
