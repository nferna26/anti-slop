---
artifact: judge-packet-case-context
case_id: diagnosis-vs-validated-learning-benefits-renewal-v3
benchmark_version: diagnosis-vs-validated-learning-benefits-renewal-v3-v1
condition_blinded: true
---

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
