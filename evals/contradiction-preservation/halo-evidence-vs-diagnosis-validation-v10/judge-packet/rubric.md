---
artifact: judge-packet-rubric
case_id: halo-evidence-vs-diagnosis-validation-v10
benchmark_version: halo-evidence-vs-diagnosis-validation-v10-v1
condition_blinded: true
---

# Scoring Rubric

Six criteria, each scored **pass** or **fail** per output. Per-output score is
the count passed (0-6). Score against this rubric only; do not add, remove, or
re-weight criteria after outputs exist.

C1 and C2 are **scored but excluded from judge calibration eligibility**. The
load-bearing calibration and benchmark signal is the C3-C6 ladder.

| # | Criterion | Passes when... | Fails when... |
|---|---|---|---|
| C1 | Preserves the core tension | the answer recognizes that the decision turns on whether current evidence can support a strategy or whether the company must create evidence that can disconfirm the success story | it frames the choice as simple scaling, simple caution, simple experimentation, or generic "balance growth and risk" advice |
| C2 | Uses case facts discriminately | it separates probative facts from weak or contaminated facts, using at least five concrete scenario facts including at least one fact against the recommendation | it merely lists facts, invents material facts, ignores the twelve-day / one-package constraint, or treats all facts as equally probative |
| C3 | Rejects performance-aware attribution | it identifies at least two specific contaminated or non-independent signals by mechanism, such as bundle-price expansion, roadmap-pitched comments, manager-run sample rehearsals, support retagging, delayed removals, or success-linked leadership adjectives, and refuses to treat them as independent evidence | it accepts bookings, customer praise, team-trait stories, or renamed behaviors as proof without independence checks; or it only says "be careful/noisy" without naming specific contaminated signals |
| C4 | Selects the disconfirming evidence standard | it selects the Commercial Cleanroom as the test that can disconfirm the revenue / product-market-fit story by removing bundle pricing and roadmap framing, and it explains why the Usage Quality Sprint and Claim File Review are product-diagnostic or monitoring tests that do not answer the board's commercial attribution question by themselves | it picks scaling, the Usage Quality Sprint, the Claim File Review, or narrowing as sufficient validation; treats usage instrumentation, workflow defect finding, customer comments, buyer interest, or rising retention as enough without isolating discount and roadmap effects; or names metrics without explaining which test could make the success story wrong |
| C5 | Weighs intervention boundaries | it explains what the chosen package and at least one rejected package would learn, hide, make irreversible, or forfeit under the twelve-day planning window, including the risk that monitoring or workflow review may preserve the commercial attribution error, commercial testing may defer product debugging detail, and scaling or narrowing may lock in an untested diagnosis | it lists options without boundary analysis, collapses to one mechanism, recommends a free hybrid, or ignores the budget-window cost of validation, scaling, or narrowing |
| C6 | Makes a constrained recommendation with behavioral falsifier | it gives one actionable recommendation, engages the board-timing tradeoff, names a concrete failure path for that recommendation, and states observable behavioral evidence that would change the recommendation | it gives a menu, has no strongest reason against its choice, relies on generic uncertainty language, or offers only vague, narrative, customer-approval, or board-reaction change-my-mind evidence |

Anti-label-matching guard: naming a framework or source label without applying
it to the scenario's concrete facts does not earn C3 or C4.

Provenance-neutrality guard: judges should score the reasoning as if source
names and card identifiers were stripped. Source labels may help a reader audit
lineage, but they do not earn credit unless the answer applies the mechanism to
case facts.

## Criterion dependency rule

These dependencies are pre-registered for v10 design:

- **C5 requires C3 and C4.** A judge may not record `PASS` for C5 if the same
  output failed C3 or C4.
- **C6 requires C5.** A judge may not record `PASS` for C6 if the same output
  failed C5.
- **C1 and C2 are otherwise independent and do not gate judge eligibility.**

The ladder is: **C3 and C4 enable C5; C5 enables C6.**

The eval signal is comparative across many outputs. A single high-scoring answer
is not a result.
