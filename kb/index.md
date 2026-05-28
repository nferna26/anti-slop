# Anti-Slop KB Index

This is the public-safe navigation layer for the maintained Markdown knowledgebase.

## Start Here

- [Project README](../README.md): objective, proof surface, and repo map.
- [AGENTS.md](../AGENTS.md): maintenance contract for agents touching this repo.
- [Methodology](../docs/methodology.md): seven-layer substrate.
- [Legal publication policy](../docs/legal-publication-policy.md): no raw copyrighted text in public repo.
- [Proof plan](../proof/README.md): claims, baselines, evals, and gate thresholds.
- [KB log](log.md): chronological updates.

## Operator and Agent Reference

- [KB maintenance contract](../docs/kb-maintenance-contract.md): operational detail behind `AGENTS.md`.
- [Front-door quality gate](../docs/front-door-quality-gate.md): what `make kb-lint` enforces, plus `make validate` and `make report`.
- [End-to-end walkthrough template](../docs/end-to-end-walkthrough-template.md): fill-in walkthrough from source to public receipt.
- [Operator roles](../docs/operator-roles.md): GM, source owner, judge, editor, canon owner, eval owner.
- [Local source shelf](../docs/local-source-shelf.md): where raw sources live and how the public KB references them.
- [Artifact definitions](../docs/artifact-definitions.md): glossary of every public-safe artifact.
- [Public writing rules](../docs/public-writing-rules.md): receipts before claims, no overclaiming, claim boundary.
- [WIP limits](../docs/wip-limits.md): per-layer caps on draft / pending artifacts.
- [Phase 0 closeout](../docs/phase-0-closeout.md): scaffold and rules closed.
- [Phase 1 closeout](../docs/phase-1-closeout.md): manifest and acquisition registry closed.
- [Phase 2 readiness](../docs/phase-2-readiness.md): first verification batch and operator checklist.

## Active Corpus

- [200-book manifest](../corpus/manifests/books-200.yaml)
- [Acquisition registry](../corpus/manifests/acquisition-registry.yaml)
- [Source ID registry — wave-1](../corpus/manifests/source-id-registry.yaml)
- [Phase 2 verification queue](../corpus/manifests/phase-2-verification-queue.yaml)
- [Manifest schema](../corpus/manifests/schema.yaml)
- [Acquisition statuses](../corpus/manifests/acquisition-statuses.yaml)
- [Publication statuses](../corpus/manifests/publication-statuses.yaml)
- [Halo-contaminated evidence vs diagnosis and validation](../corpus/claim-tension-cards/halo-contaminated-evidence-vs-diagnosis-and-validation.md) - unreviewed, non-canon claim/tension card drafted as v7 substrate pre-work.
- Status report: `make report` (output is read-only; no commits required).
- Phase 2 queue: `make phase2-queue` (prints the first verification batch).
- Boundary brief compiler: `make compile-brief BRIEF_ID=<slug> CARDS="<card_id...>"`.

## Artifact Templates

- [Book map template](../corpus/book-maps/_template.md)
- [Source card template](../corpus/source-cards/_template.md) — field guide: [source-card workflow](../docs/source-card-workflow.md)
- [Claim/tension card template](../corpus/claim-tension-cards/_template.md) — field guide: [claim/tension-card workflow](../docs/claim-tension-card-workflow.md)
- [Canon candidate template](../corpus/canon-candidates/_template.md)
- [Gate log template](../runs/gate-logs/_template.yaml)
- [Score sheet template](../runs/score-sheets/_template.md)

## Proof Surface

- [Evals README](../evals/README.md)
- [Eval lab learning memo](../docs/eval-lab-learning-memo.md) — cross-case learning notes from the contradiction-preservation surface; methodology synthesis, non-promotional.
- [Eval lab v7 pivot plan](../docs/eval-lab-v7-pivot-plan.md) - public-safe design plan for pivoting away from the v4-v6 safety/operations family before the next benchmark attempt.
- [Halo-evidence v7 eval decision](../evals/contradiction-preservation/halo-evidence-vs-diagnosis-validation-v7/eval-decision.md) - public-safe v7 pivot execution decision; partial / do_not_promote after all three judge routes failed calibration.
- [Halo-evidence v7 postmortem](../evals/contradiction-preservation/halo-evidence-vs-diagnosis-validation-v7/postmortem.md) - methodology lesson from the v7 generation pass and judge-calibration failure.
- [Halo-evidence v8 eval decision](../evals/contradiction-preservation/halo-evidence-vs-diagnosis-validation-v8/eval-decision.md) - public-safe v8 execution decision; partial / do_not_promote after generic advice matched substrate and critical controls saturated.
- [Halo-evidence v8 postmortem](../evals/contradiction-preservation/halo-evidence-vs-diagnosis-validation-v8/postmortem.md) - methodology lesson from the v8 smoke-gated run: calibration repair worked, substrate lift did not.
- [Halo-evidence v9 benchmark case](../evals/contradiction-preservation/halo-evidence-vs-diagnosis-validation-v9/case.md) - scored `do_not_promote` successor with `criteria_prompted_no_sources`, a commercial-disconfirmation C4/C5 boundary, and a pre-freeze generic-solvability probe gate.
- [Halo-evidence v10 benchmark case](../evals/contradiction-preservation/halo-evidence-vs-diagnosis-validation-v10/case.md) - scored `do_not_promote` successor with a two-sided substrate-feasibility probe, full reviewed source-card substrate packet, and strong C4-C6 lift blocked by C3 saturation.
- [Halo-evidence v11 benchmark case](../evals/contradiction-preservation/halo-evidence-vs-diagnosis-validation-v11/case.md) - scored `do_not_promote` successor with C1-C3 demoted from promotion, C4-C6 substrate/control separation, and promotion blocked by unresolved judge disagreement on `criteria_prompted_no_sources`.
- [Halo-evidence v12 benchmark case](../evals/contradiction-preservation/halo-evidence-vs-diagnosis-validation-v12/case.md) - scored `do_not_promote` successor with three pre-generation eligible judge routes, judge-disagreement smoke, and promotion blocked because `criteria_prompted_no_sources` matched the substrate.
- [Halo boundary-transfer v1 draft case](../evals/source-lineage-hostile/halo-effect-boundary-blind-measurement-v1/case.md) - source-lineage-hostile design case targeting over-application of the halo label when independent trait evidence is outside the BK-0048 mechanism; unrun and unscored.
- [Halo boundary-transfer v1 pre-freeze probe](../evals/source-lineage-hostile/halo-effect-boundary-blind-measurement-v1/pre-freeze-probe.md) - local-only readiness probe summary; failed the freeze gate because generic advice matched substrate on F1+F3+F5.
- [Locator-accuracy v1 case](../evals/bibliographic-adversary/locator-accuracy-v1/case.md) - bibliographic-adversary case testing invented card IDs, locator drift, source-claim misattribution, hidden canon drift, and unsupported citation refusal; benchmark version `locator-accuracy-v1-v1` is frozen, unrun, and unscored.
- [Locator-accuracy v1 pre-freeze probe](../evals/bibliographic-adversary/locator-accuracy-v1/pre-freeze-probe.md) - full local-only readiness probe summary; criteria and famous-source controls safely refused unsupported lineage while substrate added valid support coverage.
- [Locator-accuracy v1-v1 run packet](../evals/bibliographic-adversary/locator-accuracy-v1/run-packet.md) - frozen benchmark version; condition-packet recipes, hashes, generator settings, and freeze checklist. Not run, not judged.
- [Locator-accuracy v1-v1 judge-route pre-registration](../evals/bibliographic-adversary/locator-accuracy-v1/judge-packet/judge-route-preregistration.md) - hosted Anthropic + OpenAI primary judges, local non-Gemma backstop, calibration eligibility and disagreement policy. Frozen; calibration failed before generation.
- [Locator-accuracy v1-v1 eval decision](../evals/bibliographic-adversary/locator-accuracy-v1/eval-decision.md) - calibration-stage `do_not_promote`; hosted Anthropic and hosted OpenAI both failed exact F1-F5 anchor agreement before generation, so no benchmark outputs were generated.
- [Locator-accuracy v2 scored case](../evals/bibliographic-adversary/locator-accuracy-v2/case.md) - frozen calibration-repair successor preserving the locator-accuracy mechanical-lineage claim; 240 real model-output receipts generated, anonymised, scored by route, and reconciled aggregate-only with `do_not_promote`.
- [Locator-accuracy v2 calibration anchors](../evals/bibliographic-adversary/locator-accuracy-v2/judge-packet/calibration-anchors.md) - operator-accepted Surface 1 / Surface 1B anchors and withheld reference keys for F1-F5 plus valid support coverage; hosted Anthropic r2 and hosted OpenAI r3 passed exactly.
- [Locator-accuracy v2-v1 run packet](../evals/bibliographic-adversary/locator-accuracy-v2/run-packet.md) - frozen benchmark version; condition-packet recipes, hashes, generator settings, judge-route references, freeze checklist, generation record, OUT-NN anonymisation record, route-scoring status, and reconciliation outcome.
- [Locator-accuracy v2-v1 blind judge packet](../evals/bibliographic-adversary/locator-accuracy-v2/judge-packet/README.md) - condition-blind OUT-001 through OUT-240 packet with judge instructions, case context, rubric, calibration exercise, output-hash manifest, and blank score sheet; scored by eligible hosted routes before aggregate-only reconciliation.
- [Locator-accuracy v2-v1 judge-route pre-registration](../evals/bibliographic-adversary/locator-accuracy-v2/judge-packet/judge-route-preregistration.md) - hosted Anthropic r2 + OpenAI r3 eligible primary judges, calibration eligibility, coverage rule, and blinding rule. Frozen before generation.
- [Locator-accuracy v2-v1 Anthropic judge-score receipt](../evals/bibliographic-adversary/locator-accuracy-v2/judge-packet/judge-score-hosted_anthropic_r2.md) - public-safe hosted Anthropic r2 condition-blind scoring receipt for all 240 OUT files.
- [Locator-accuracy v2-v1 OpenAI judge-score receipt](../evals/bibliographic-adversary/locator-accuracy-v2/judge-packet/judge-score-hosted_openai_r3.md) - public-safe hosted OpenAI r3 condition-blind scoring receipt for all 240 OUT files.
- [Locator-accuracy v2-v1 eval decision](../evals/bibliographic-adversary/locator-accuracy-v2/eval-decision.md) - aggregate-only `do_not_promote`; substrate had zero failures and high support coverage, but Anthropic tripped the non-discriminating-judge guard and missed the famous-source margin.
- [Locator-accuracy v2-v1 postmortem](../evals/bibliographic-adversary/locator-accuracy-v2/postmortem.md) - methodology lesson from the mechanical-lineage near-miss and judge-discrimination guard.
- [Locator-accuracy v2-v1 judge-discrimination autopsy](../evals/bibliographic-adversary/locator-accuracy-v2/judge-discrimination-autopsy.md) - design-only follow-up explaining the Anthropic/OpenAI scoring-surface split and recommending a support-opportunity scoring repair before any v3 benchmark.
- [Locator-accuracy v2 substrate brief audit](../evals/bibliographic-adversary/locator-accuracy-v2/substrate-brief-audit.md) - local-only compiled substrate brief recipe, hash, size, and load-bearing fact audit for the frozen v2-v1 packet.
- [Locator-accuracy v2 calibration decision](../evals/bibliographic-adversary/locator-accuracy-v2/calibration-decision.md) - calibration-stage decision receipt; H-clarified hosted Anthropic r2 and hosted OpenAI r3 both passed exactly before the v2-v1 freeze.
- [Locator-accuracy v3 draft case](../evals/bibliographic-adversary/locator-accuracy-v3/case.md) - design-only successor that keeps F1-F5 as provenance-safety guardrails and adds a support-opportunity surface to distinguish safe refusal, missed support, false denial, and correct reviewed support.
- [Locator-accuracy v3 draft calibration anchors](../evals/bibliographic-adversary/locator-accuracy-v3/judge-packet/calibration-anchors.md) - draft SO0-SO3 calibration anchors; not frozen and no judge route has run.
- [Runway-lighting v5 postmortem](../evals/contradiction-preservation/normalization-vs-latent-errors-runway-lighting-v5/postmortem.md) - public-safe design lesson from the v5 machinery pass and generic-advice saturation.
- [Print-vault v6 eval decision](../evals/contradiction-preservation/normalization-vs-latent-errors-print-vault-v6/eval-decision.md) - public-safe v6 execution decision; partial / do_not_promote after generic C3/C4 saturation and one eligible scored judge.
- [Gate specs](../gates/gate-specs.yaml)
- Implemented gate scripts: `make gate-citation-lineage FILE=<path>` and
  `make gate-no-universalization FILE=<path>`.
- [Boundary tools v12 self-test](../runs/boundary-self-tests/v12-boundary-brief-vs-criteria-2026-05-25/summary.md) - tooling smoke test comparing compiled boundary brief outputs against criteria-prompt-only outputs; not benchmark evidence or canon support.
- [Registry](../registry/README.md)

## Current Open Questions

- Which of the 23 first-50 sources without local filename evidence need active acquisition?
- Which first source cards will be operator-verified?
- Which eval should be the first proof surface?
- When does the broader corpus (BK-0051 to BK-0200) get worked, and in what order?

## Authority Reminder

Book maps, source cards, claim/tension cards, and canon candidates are not canon. Canon requires explicit operator approval.
