validate:
	python3 scripts/validate_manifest.py
	@if [ -f corpus/manifests/acquisition-registry.yaml ]; then \
		python3 scripts/validate_acquisition_registry.py; \
	else \
		echo "(acquisition registry not present; skipping validate_acquisition_registry.py)"; \
	fi

check-raw:
	python3 scripts/check_no_raw_text.py

kb-lint:
	python3 scripts/kb_lint.py

report:
	python3 scripts/manifest_report.py

phase2-queue:
	python3 scripts/phase2_queue.py

artifact-status:
	python3 scripts/artifact_status.py

artifact-preflight:
	python3 scripts/artifact_preflight.py

first50-queue:
	python3 scripts/first50_queue.py

packet-status:
	python3 scripts/artifact_packet_status.py

eval-lab-status:
	python3 scripts/eval_lab_status.py

eval-benchmark-readiness:
	python3 scripts/eval_benchmark_readiness.py

eval-receipt-lint:
	python3 scripts/eval_receipt_lint.py

receipt-index:
	python3 scripts/receipt_index.py

receipt-index-check:
	python3 scripts/receipt_index.py --check

new-book-map:
	python3 scripts/new_book_map.py $(SOURCE_ID)

new-source-card:
	python3 scripts/new_source_card.py $(SOURCE_ID)

new-claim:
	python3 scripts/new_claim_tension_card.py $(SLUG)

new-canon-candidate:
	python3 scripts/new_canon_candidate.py $(SLUG)

new-eval-case:
	python3 scripts/new_eval_case.py $(EVAL_TYPE) $(CASE_ID)

new-gate-log:
	python3 scripts/new_gate_log.py $(RUN_ID)

gate-citation-lineage:
	python3 scripts/gate_citation_lineage.py $(FILE)

gate-citation-lineage-self-test:
	python3 scripts/gate_citation_lineage.py --self-test

# Dogfood the deterministic citation-lineage gate over the KB's own lineage
# artifacts: every source/card reference must resolve, and (--require-reviewed)
# every source-card reference must resolve to a REVIEWED card. Scope is the
# lineage-bearing artifacts (corpus cards/maps + eval design/decision docs); it
# excludes model-outputs/ and judge-packet/outputs/, which are test artifacts
# that may cite fabricated lineage by design (that is the model behaviour an
# eval scores, not a KB defect). Fails the build on any unresolved lineage.
citation-dogfood:
	@python3 scripts/gate_citation_lineage.py --require-reviewed \
		$$(find corpus/source-cards corpus/claim-tension-cards corpus/book-maps -name '*.md') \
		$$(find evals -name '*.md' -not -path '*/model-outputs/*' -not -path '*/judge-packet/outputs/*')

# Stranger-reproducible demo of the mechanical-lineage primitive:
# compile_brief -> static sample corrected note -> gate_citation_lineage ->
# receipt. No API key, network, model runtime, or raw book required.
demo:
	python3 scripts/demo_citation_lineage.py

# Holdout-transfer smoke (holdout_smoke_not_benchmark): does the deterministic
# citation-lineage primitive transfer to a NON-benchmark-shaped corpus? Runs the
# unmodified gate over a self-contained synthetic naturalist fixture corpus via
# --root. No API key, network, model runtime, or raw book. Not a benchmark.
holdout-smoke:
	python3 scripts/holdout_smoke.py

# Package smoke: install the anti-slop-lineage CLI (pyproject.toml) into a
# throwaway isolated venv, then prove the INSTALLED console command self-tests
# and audits the holdout fixture identically to the in-tree gate. Offline; no
# network/model/API. The packaged CLI is the gate's own main() (no behaviour fork).
package-smoke:
	bash scripts/package_smoke.sh

# Agent-install smoke: exercise the INSTALL_FOR_AGENTS.md commands end-to-end in a
# throwaway venv + temp adopter repo (install, self-tests, clean PASS / fabricated
# FAIL, event SKIP/report, shipped example body). Offline; no GitHub API.
agent-install-smoke:
	bash scripts/agent_install_smoke.sh

# Adoption smoke: validate the vendorable report-mode workflow template and
# prove the underlying PR/report/receipt commands expose findings + artifacts
# while exiting 0 in report mode. Offline; no GitHub API, model, or token.
adoption-smoke:
	python3 scripts/adoption_smoke.py

# anti-slop-pr: deterministic PR-description provenance checker. Resolves the
# issue / file / test / source-card references a PR body cites against a repo or
# fixture root; stdlib-only, no GitHub API / model / network. Usage:
#   make pr-provenance ROOT=. PR=path/to/pr-body.md   (add ISSUES=file to resolve #refs)
pr-provenance:
	python3 scripts/gate_pr_provenance.py --root $(ROOT) $(if $(ISSUES),--issue-registry $(ISSUES)) $(PR)

pr-provenance-self-test:
	python3 scripts/gate_pr_provenance.py --self-test

# anti-slop-claims: generic artifact reference/receipt resolver. Uses the same
# resolver engine as anti-slop-pr for non-PR Markdown/text artifacts.
claims:
	python3 scripts/gate_claims.py --root $(ROOT) $(if $(ISSUES),--issue-registry $(ISSUES)) $(if $(DIFF),--diff $(DIFF)) $(if $(JSON),--json $(JSON)) $(ARTIFACT)

claims-self-test:
	python3 scripts/gate_claims.py --self-test

run-self-test:
	python3 scripts/anti_slop_run.py --self-test

# Synthetic checker benchmark: run the deterministic agent-claim corpus and
# write JSON + Markdown summaries. Offline; no model/API/network.
agent-claim-benchmark:
	python3 scripts/benchmark_agent_claims.py

# Public-safe report-mode audit over committed real agent/PR-body artifacts.
agent-claim-audit:
	python3 scripts/audit_agent_claim_density.py

# Launch demo: fake report FAILS with line reasons; receipt-backed report PASSES.
agent-claim-demo:
	python3 scripts/demo_agent_claim_verification.py

# Stranger-reproducible demo: a passing and an intentionally-failing PR body
# checked against a self-contained fixture root (no GitHub API, model, or network).
pr-provenance-demo:
	python3 scripts/demo_pr_provenance.py

# Dogfood: run anti-slop-pr over this repo's own (committed, public-safe) PR-body
# copies and report. Offline; always exits 0 (evidence, not a gate).
pr-provenance-dogfood:
	python3 scripts/dogfood_pr_provenance.py

# GitHub Actions event wrapper: read the PR body from a pull_request event JSON
# and run anti-slop-pr (no GitHub API; event payload + local checkout only).
pr-provenance-event-self-test:
	python3 scripts/pr_provenance_from_github_event.py --self-test

# Deterministic demo over committed fixture event payloads (clean PASS, fabricated
# FAIL, --report non-fail, non-PR SKIP, ignore-directive PASS) + a report-only run
# on a saved real PR body. Offline; no GitHub API.
pr-provenance-event-demo:
	python3 scripts/demo_pr_provenance_event.py

gate-no-universalization:
	python3 scripts/gate_no_universalization.py $(FILE)

gate-no-universalization-self-test:
	python3 scripts/gate_no_universalization.py --self-test

compile-brief:
	python3 scripts/compile_brief.py $(BRIEF_ID) $(CARDS)

compile-brief-self-test:
	python3 scripts/compile_brief.py --self-test
