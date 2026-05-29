<!--
SAMPLE / PLACEHOLDER "slop" output for the citation-lineage demo. This is a
deliberate negative fixture: a static, hand-written stand-in for a corrected
note that cites a card ID that does not exist in the public KB. It is NOT a
model run and NOT a benchmark artifact. The deterministic citation-lineage gate
should FAIL this file (unresolved reference), demonstrating that the gate
catches a fabricated citation. It lives under proof/ and is intentionally
outside the corpus/ + evals/ dogfood scope.
-->

# Sample Slop Note (placeholder; intentionally fails the gate)

Corrected note:

- The strategy kernel is supported by `BK-9999-card-001` (Chapter 5).

This cites `BK-9999-card-001`, a card ID that does not resolve to any reviewed
public-KB source card. The deterministic citation-lineage gate flags it as an
unresolved reference.
