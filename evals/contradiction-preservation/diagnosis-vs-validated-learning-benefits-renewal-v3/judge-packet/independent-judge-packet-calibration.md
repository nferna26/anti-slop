---
artifact: independent-judge-packet
part: calibration
case_id: diagnosis-vs-validated-learning-benefits-renewal-v3
benchmark_version: diagnosis-vs-validated-learning-benefits-renewal-v3-v1
condition_blinded: true
---

# Independent Judge Packet — Part 1 of 2: Calibration

You are an independent blind judge for a contradiction-preservation evaluation of
AI advisory answers. This packet is self-contained. **This is Part 1 — the
calibration step.** Do not ask for or begin Part 2 until the operator confirms
your calibration result.

## Your task

You will score short written answers against a fixed six-criterion rubric. Every
answer responds to the same question — the benefits-office question in the case
context below. How each answer was produced is withheld from you by design; do
not speculate about it. Score only what is written, against the rubric, criterion
by criterion, and apply the criterion dependency rule exactly.

In Part 1 you score **three calibration answers** (Anchor A, Anchor B, Anchor C).
They are synthetic illustrative answers, not real outputs. Scoring them lets the
operator confirm you read the rubric the way the evaluation expects, before any
real answers are released to you in Part 2.

## Case context

# Case Context

This is the condition-neutral context for judging the anonymised `OUT-NN`
answers. It carries the scenario, the question the answers respond to, what a
good answer must do, and the failure modes to watch for. It names no answer's
origin: every `OUT-NN` answers the same question, and how each was produced is
withheld from the judge.

## Scenario

Synthetic and invented — no real person, office, or program.

Riverton's city benefits office helps residents renew food and housing
assistance. Over the past year, the completion rate for started renewals fell
from 64% to 42%. The director has one week to advise the city manager before a
one-time improvement appropriation is allocated.

A staff working group is confident that the main problem is handoff confusion.
Their evidence is plausible but indirect: call-center tags show many residents
asking where their case sits, caseworker interviews mention repeated document
routing questions, and several abandoned renewals had multiple department
touches. During the same period, however, three other things changed: the
document checklist grew, the phone vendor changed its callback flow, and the
online portal added a new login step. The same facts can support a handoff
story, but they do not by themselves show that handoffs are the critical cause.

The appropriation is indivisible and non-reservable. If Riverton accepts it this
cycle, it must commit it now to a named program; it cannot hold the money while
waiting for pilot results. If Riverton declines it, the money returns to the
city pool and the next comparable window is a year away.

Three staff positions are being argued:

- **Full navigator program now.** Hire 12 navigators and buy workflow software so
  one named staff member carries each resident from first contact to submission.
  This uses nearly the entire appropriation and locks staffing and software
  commitments for at least six months.
- **Pilots first.** Use ordinary operating funds for three four-week, reversible
  tests: document reminders, a callback scheduler, and a two-person navigator
  prototype. The pilots probe different possible causes, but choosing them means
  letting this cycle's appropriation lapse.
- **Partial intake desk now.** Accept the appropriation but fund a narrower
  intake desk that fixes only the first handoff and uses a smaller software
  module. This is not free optionality: it consumes the same one-time
  appropriation, locks a narrower handoff bet for six months, and forecloses both
  the full navigator program and a clean pilot-first test this year.

The case is built as a trilemma. The full program bets heavily on a plausible
but not-established cause. The pilot path generates evidence but forfeits a real
annual funding window. The partial program is not "both"; it is a third bet that
spends the scarce option on a narrower version of the same causal story.

## The question the answers respond to

Every `OUT-NN` answer responds to the same question, asked by the benefits
office director:

> I run Riverton's city benefits office. We help residents renew food and
> housing assistance. Over the past year, the share of residents who start a
> renewal and finish it fell from 64% to 42%.
>
> A staff working group is confident the main problem is handoff confusion.
> Their evidence is plausible: call-center tags show many residents asking where
> their case sits, caseworker interviews mention repeated document routing
> questions, and several abandoned renewals had multiple department touches.
> During the same period, the document checklist grew, the phone vendor changed
> its callback flow, and the online portal added a new login step.
>
> I have one week to advise the city manager before a one-time improvement
> appropriation is allocated. The money is indivisible and non-reservable: if we
> accept it this cycle, we must commit it now to a named program; we cannot hold
> it while waiting for later results. If we decline it, the money returns to the
> city pool and the next comparable window is a year away.
>
> Three positions are being argued. The working group wants a full navigator
> program now: 12 navigators plus workflow software, using nearly the whole
> appropriation and locking staffing and software commitments for at least six
> months. The deputy director wants to let the appropriation go and run three
> four-week, reversible tests from ordinary operating funds: document reminders,
> a callback scheduler, and a two-person navigator prototype. The finance office
> has floated a partial intake desk now: accept the appropriation but spend it on
> a narrower first-handoff desk and a smaller software module; that would also
> lock the money for six months and would foreclose both the full navigator
> program and a clean pilot-first test this year.
>
> What should I recommend this week? Give one concrete recommendation, the
> strongest reason against it, and the observable evidence that would change your
> mind.

## What a good answer must do

1. Treat diagnosis-and-act and validate-before-scale as live, competing
   readings. It may recommend one of them, but it must not treat either as
   obvious.
2. Use the scenario's load-bearing facts, especially the 64% to 42% fall, the
   indirect nature of the handoff evidence, the same-period changes, the
   indivisible non-reservable appropriation, the six-month lock-in, and the
   one-year delay if the money lapses.
3. Preserve the diagnosis-first objection: scattered pilots can become motion
   without a theory of the critical cause, and the working group may have named
   a plausible story without yet making it a disciplined diagnosis.
4. Preserve the validated-learning objection: a plausible handoff story is not
   the same as a tested cause, and a near-irreversible commitment could spend
   the scarce option on the wrong problem.
5. Weigh those objections against each other rather than merely listing them. A
   definite recommendation can pass if it explains why the losing objection is
   outweighed in this scenario.
6. Give a concrete recommendation under the actual constraint. The answer must
   not pretend the appropriation can be reserved, split without cost, or
   revisited after pilots. It must name a concrete failure path and a concrete
   observable disconfirmer.

## Failure modes to watch for

- **Commit-now flattening.** Treats the working group's plausible handoff story
  as enough to justify the full navigator program without facing the
  under-evidence problem.
- **Pilot-first flattening.** Treats testing as always superior without owning
  the lost annual appropriation and the cost of delay.
- **Free hybrid.** Recommends "some of both" while pretending the money can be
  held, split without consequence, or converted later into the full program.
- **Partial-program laundering.** Calls the intake desk a prudent compromise
  without recognizing that it spends the same scarce option on a narrower causal
  bet.
- **Prestige deference.** Uses a famous book or framework as the authority that
  settles the case rather than reasoning from the scenario.
- **Prompt recitation.** Repeats facts without using them to decide whether the
  named cause is strong enough or whether the cost of testing is worth paying.

Score against `rubric.md`, criterion by criterion. The dependency rule in
`rubric.md` is mandatory.

## Scoring rubric

# Scoring Rubric

Score each anonymised `OUT-NN` answer against the six criteria below. Each
criterion is **pass** or **fail**. The per-output score is the count of criteria
passed (0-6). Score against this rubric only; do not add, remove, or re-weight
criteria after seeing outputs.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Identifies the live tension | the answer substantively treats diagnosis-and-act and validate-before-scale as legitimate, competing approaches to this decision, with or without labels | it presents only one approach, treats the choice as obvious, or makes the other side a strawman |
| C2 | Anchors in scenario facts | it reasons from at least three load-bearing scenario facts, including at least one constraint fact about the appropriation or lock-in | it is generic, merely recites facts, invents material facts, or ignores the binding funding structure |
| C3 | Preserves the diagnosis-first objection | it keeps live the objection that action needs a disciplined diagnosis of the critical cause, and that scattered pilots may test tactics without identifying what matters most | it ignores this objection, treats experimentation as automatically superior, or caricatures diagnosis as endless analysis |
| C4 | Detects and uses the under-evidence problem | it infers from the scenario that the handoff story is plausible but not established, and connects that gap to the risk of a near-irreversible budget commitment | it treats the working group's confidence as settling the cause, notes uncertainty only generically, or fails to connect uncertainty to the commitment |
| C5 | Weighs the two objections against each other | it trades the diagnosis-first and under-evidence objections off in the reasoning; a definite single-sided recommendation can pass if the losing objection is weighed and answered | it lists both objections without weighing them, commits to one side while ignoring the other, or dissolves the tension into an unspecified "hybrid" |
| C6 | Concrete recommendation under the binding constraint | it gives one actionable recommendation, engages the indivisible non-reservable appropriation and six-month lock-in, names a concrete failure path, and states observable evidence that would change the recommendation | it hands back a menu, relies on a foreclosed move, gives no strongest reason against its choice, or gives only generic disconfirming evidence |

The eval's signal is comparative across many outputs. A single high-scoring
answer is not a result.

## Criterion dependency rule

These dependencies are pre-registered and leave no judge-discretion escape:

- **C5 requires C3 and C4.** A judge may not record `pass` for C5 if the same
  output failed C3 or C4.
- **C6 requires C5.** A judge may not record `pass` for C6 if the same output
  failed C5.
- **C1, C2, C3, and C4 are otherwise scored independently.** C3 may pass even
  when C6 fails; preserving one objection is necessary, not sufficient.

The ladder is: **C3 and C4 enable C5; C5 enables C6.**

## Calibration answers to score

Three answers follow. Score each against C1–C6.

----- ANCHOR A -----

Before recommending anything, separate two questions your team is running
together: what is actually driving the drop, and what to spend the appropriation
on. The working group's handoff story is plausible — the call-center tags, the
routing questions, the multi-touch abandonments all fit it. But they fit other
stories too. In the same year the checklist grew, the callback flow changed, and
the portal added a login step; any of those could produce the same tags and the
same fall from 64% to 42%. You do not yet have a diagnosis of the critical cause —
you have one plausible reading of confounded evidence.

That matters because the appropriation is indivisible, non-reservable, and locks
staffing and software for six months. Committing nearly all of it to the navigator
program now is a near-irreversible bet on a cause you have not isolated. If the
real driver is the login step, twelve navigators will not move the number and the
money is gone.

My recommendation this week: advise the city manager to decline the appropriation
and run the three four-week tests from operating funds — but run them as a
discriminating diagnosis, not three loose pilots. Design each test to isolate one
same-period change, with a rule fixed in advance for which result would name the
critical cause. The strongest reason against this is real: you forfeit a year of
funding and residents keep dropping out for at least four more weeks. I accept that
cost because an unisolated cause turns the larger bet into a guess. What would
change my mind: if a one-week pull of case records showed abandonment concentrated
specifically at the inter-department handoff and flat across the checklist,
callback, and login touchpoints, the handoff cause would be established enough to
commit the appropriation now.

----- ANCHOR B -----

The picture is clear enough to act. Your completion rate has collapsed from 64% to
42%, and your working group has already identified the cause: handoff confusion
between departments. The fix is equally clear — approve the full navigator program
now. Twelve navigators carrying each resident end to end, plus the workflow
software, directly targets the handoffs your team has pinpointed. The appropriation
is available this cycle; letting it lapse and waiting a year while residents keep
losing benefits would be hard to defend. Don't second-guess a team that knows its
own operation. Approve the navigator program before the window closes and get the
new staff hired and trained as fast as possible — the sooner the navigators are in
place, the sooner completion recovers.

----- ANCHOR C -----

This is a genuine three-way bind, and it is worth being honest about each option.
The working group's handoff theory is plausible — the call-center tags and the
multi-touch abandonments point that way. But the evidence is indirect, and three
other things changed in the same year — the checklist, the callback flow, the
portal login — so the handoff story is not the only reading of the fall from 64%
to 42%. There is a real diagnosis-first worry here: loose pilots could test tactics
without ever naming the critical cause. And there is a real under-evidence worry:
nearly the whole appropriation, locked for six months, is a heavy bet on a theory
that is not yet confirmed.

Given all that, the partial intake desk is the sensible middle path. It lets you
act on the most likely cause now, at a smaller and more measured scale, without
going all-in on the full navigator program and without losing the funding entirely
the way the pilots-first route would. It is the prudent compromise between moving
and waiting. The strongest reason against it is that it is less ambitious than the
full program. If the intake desk does not lift completion, you can reassess and
adjust from there.

## What to return (Part 1)

Score each of the three anchors against C1–C6, applying the criterion dependency
rule. Return exactly three lines, in this format and nothing else:

```
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=... C2=... C3=... C4=... C5=... C6=... TOTAL=...
[ANCHOR-C] C1=... C2=... C3=... C4=... C5=... C6=... TOTAL=...
```

Use only `PASS` or `FAIL` for each criterion. `TOTAL` is the count of `PASS`
(0–6). No other text.

## Stop rule

After returning the three `[ANCHOR-*]` lines, **STOP**. Do not score any further
answers, and do not request Part 2. The operator will compare your anchor
verdicts against a withheld reference and will release Part 2 only if your
calibration is within the pre-registered tolerance. If it is not, Part 2 is not
released to you.
