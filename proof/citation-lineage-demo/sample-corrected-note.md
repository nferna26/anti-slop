<!--
SAMPLE / PLACEHOLDER output for the citation-lineage demo. This is NOT a model
run and NOT a benchmark artifact: it is a static, hand-written stand-in for a
corrected note, used so `make demo` can exercise the deterministic
citation-lineage gate without any API key, network, model runtime, or raw book.
It cites only reviewed public-KB source cards at their reviewed locators, and
names (refuses) an unsupported request. The gate should PASS this file.
-->

# Sample Corrected Note (placeholder)

Corrected note:

- The halo effect — that a general impression of a company's overall performance
  drives how observers rate its specific attributes — is supported by
  `BK-0048-card-001` (Chapter 4).
- Rumelt's strategy kernel (a diagnosis, a guiding policy, and coherent action)
  is supported by `BK-0001-card-001` (Chapter 5).

Removed / unsupported:

- A requested page-117 locator and verbatim quote for the strategy kernel: the
  reviewed card carries a Chapter 5 locator only, so the page and quote are not
  supported and are refused.

Supported lineage:

- `BK-0048-card-001`, Chapter 4 — halo-effect mechanism.
- `BK-0001-card-001`, Chapter 5 — strategy kernel.
