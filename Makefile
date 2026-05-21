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
