# Citation-Lineage Gate

`scripts/gate_citation_lineage.py` is Anti-Slop's **deterministic** citation
gate. It checks the lower-level failure that should be mechanical and
reproducible: when an artifact names a source ID, source-card ID,
claim/tension-card ID, or local card path, that reference must resolve inside the
public KB. It does not judge whether a claim is well-supported — only whether its
citations resolve.

This gate is the operational form of the one **benchmark-supported** claim (see
`evals/bibliographic-adversary/locator-accuracy-v4/`).

## What it checks

- **source IDs** (`BK-0023`): must appear in `corpus/manifests/books-200.yaml`.
- **source-card IDs** (`BK-0023-card-001`): must resolve to a card file in
  `corpus/source-cards/`.
- **claim/tension-card IDs** (`x-vs-y` in backticks): must resolve to a
  `corpus/claim-tension-cards/` card — or to a known eval-case label (case IDs
  share the `x-vs-y` shape, so the gate knows the eval-case namespace and does
  not flag a real case reference as dangling).
- **card paths** (`corpus/source-cards/BK-0023-card-001.md`): must exist under a
  card directory.

## Usage

```sh
# Check specific files (existence mode — a reference must resolve):
python3 scripts/gate_citation_lineage.py path/to/file.md [more.md]

# Reviewed-lineage mode — additionally require every source-card reference to
# resolve to a REVIEWED card (a file's own card_id self-reference is excepted):
python3 scripts/gate_citation_lineage.py --require-reviewed path/to/file.md

# Run against a different KB checkout / fixture tree:
python3 scripts/gate_citation_lineage.py --root /path/to/kb --require-reviewed file.md

# Deterministic self-test (7 checks; no repo state needed):
python3 scripts/gate_citation_lineage.py --self-test     # or: make gate-citation-lineage-self-test
```

### Flags

- `--root DIR` — KB root that holds `corpus/` (default: the repo containing the
  script). Lets the same gate run over any checkout or a fixture tree.
- `--require-reviewed` — forward-reference / reviewed-lineage check: every
  source-card reference must resolve to a card whose `operator_review_status` is
  `reviewed`. A file's reference to its own `card_id` is excepted. A
  planned/future comparison target that is not yet a reviewed card must be named
  by its source ID (`BK-XXXX`), never by a card ID.

## Dogfood and demo (Make targets)

```sh
# Dogfood the gate over the KB's own lineage artifacts (corpus cards/maps + eval
# design/decision docs). Excludes model-outputs/ and judge-packet/outputs/, which
# are test artifacts that may cite fabricated lineage by design (that is the
# model behaviour an eval scores, not a KB defect). Fails on unresolved/unreviewed
# references:
make citation-dogfood

# Stranger-reproducible demo (no API key, network, model runtime, or raw book):
# compile_brief -> static sample corrected note -> gate -> receipt. Passes the
# good sample and fails a fabricated-citation slop sample:
make demo
```

The same commands run in CI (`.github/workflows/ci.yml`).

## Gate tiers (be precise about maturity and backing)

- **Deterministic, implemented:**
  - `citation-lineage` — *benchmark-backed* (locator-accuracy-v4). The check is
    mechanical: a reference resolves or it does not.
  - raw-text check (`scripts/check_no_raw_text.py`, `make check-raw`) — mechanical
    scan for committed raw copyrighted text.
- **Heuristic, implemented (advisory, not benchmark-backed):**
  - `no-universalization` (`scripts/gate_no_universalization.py`) — flags broad
    advice stated without nearby scope language. Catches a simple failure shape,
    not a proof that a scoped claim is right.
- **Scaffold-only (specified in `gates/gate-specs.yaml`, not yet implemented as
  scripts):** quote-limit, authority-order, source-diversity, canon-duplication,
  contradiction. The authority ladder is currently enforced by `AGENTS.md` /
  `CLAUDE.md` review, not by a gate.

## What the supported claim is — and is not

The benchmark-supported claim is narrow and mechanical: under adversarial
citation pressure, the substrate adds inspectable reviewed public-KB lineage —
the correct **card ID**, the **reviewed locator** at the granularity the card
carries, and the **supported claim**, with unsupported card IDs, pages, quotes,
false source relations, book-map evidence, and standing-canon claims refused —
where source-free prompting cannot.

It is **not** a claim about advice quality, source truth, reasoning quality, or
canon. A passing gate means the citations resolve to reviewed evidence; it does
not mean the claim is true or the advice is good. A model output is a test
artifact, never an authority; the gate promotes no canon.
