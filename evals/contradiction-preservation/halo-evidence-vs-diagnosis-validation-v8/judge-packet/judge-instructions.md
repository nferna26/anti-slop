---
artifact: judge-packet-instructions
case_id: halo-evidence-vs-diagnosis-validation-v8
benchmark_version: halo-evidence-vs-diagnosis-validation-v8-smoke-2
condition_blinded: true
calibration_smoke_only: true
---

# Judge Instructions

This is a calibration-smoke packet for halo-evidence-vs-diagnosis-validation-v8. No v8 model outputs exist yet.

Return exactly eight anchor rows in this format:

```text
[ANCHOR-A] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-B] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-C] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-D] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-E] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-F] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-G] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
[ANCHOR-H] C1=PASS C2=PASS C3=PASS C4=PASS C5=PASS C6=PASS TOTAL=6
```

The operator will compare your verdicts with withheld references. For v8 smoke
eligibility, C3-C6 must match exactly on eligibility anchors, totals must be
arithmetic, and the dependency rule must hold. C1/C2 are scored but non-gating.
