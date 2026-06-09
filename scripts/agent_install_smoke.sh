#!/usr/bin/env bash
# Agent-install smoke: exercises the core commands from INSTALL_FOR_AGENTS.md
# end-to-end, deterministically and offline.
#
#   1. install the package into a throwaway venv  (simulates the documented
#      `pip install "anti-slop-lineage @ git+..."` — see BOUNDARY below)
#   2. installed self-tests: anti-slop-pr --self-test, anti-slop-pr-event --self-test,
#      anti-slop-claims --self-test, anti-slop-run --self-test
#   3. in a temp "adopter repo": a clean PR body PASSES, a fabricated one FAILS
#   4. the event wrapper SKIPs a non-PR event and reports in report mode
#   5. the shipped templates/example-pr-body.md resolves against this repo
#
# BOUNDARY: the raw-URL `git+https://...` install needs network and is NOT tested
# here; this smoke installs the SAME package from the in-tree checkout (`pip
# install .`), which is byte-identical to what the git URL resolves to. Offline;
# no GitHub API, model, or network beyond pip's local build.

set -u
REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP="$(mktemp -d -t anti-slop-agent-smoke-XXXXXX)"
VENV="$TMP/venv"; LOG="$TMP/install.log"; ADOPTER="$TMP/adopter"
cleanup() { rm -rf "$TMP" "$REPO/build" "$REPO/scripts/anti_slop_lineage.egg-info"; }
trap cleanup EXIT

echo "== Anti-Slop agent-install smoke =="
echo "Repo: $REPO ; temp: $TMP"

# 1. install (isolated; offline fallback) — mirrors scripts/package_smoke.sh
python3 -m venv --system-site-packages "$VENV" || { echo "FAIL: venv"; exit 1; }
BIN="$VENV/bin"
if ! "$BIN/python" -m pip install --quiet "$REPO" >"$LOG" 2>&1; then
  "$BIN/python" -m pip install --no-build-isolation --quiet "$REPO" >>"$LOG" 2>&1 \
    || { echo "FAIL: install"; tail -20 "$LOG"; exit 1; }
fi
for c in anti-slop-pr anti-slop-pr-event anti-slop-claims anti-slop-run; do
  [ -x "$BIN/$c" ] || { echo "FAIL: $c not installed"; exit 1; }
done

# 2. installed self-tests
"$BIN/anti-slop-pr" --self-test >/dev/null 2>&1; a=$?
"$BIN/anti-slop-pr-event" --self-test >/dev/null 2>&1; b=$?
"$BIN/anti-slop-claims" --self-test >/dev/null 2>&1; h=$?
"$BIN/anti-slop-run" --self-test >/dev/null 2>&1; i=$?

# 3. temp adopter repo: clean body PASS, fabricated body FAIL
mkdir -p "$ADOPTER/docs"
printf '# Doc\n\nhi\n' > "$ADOPTER/docs/guide.md"
printf 'Updates `docs/guide.md`.\n' > "$ADOPTER/clean.md"
printf 'Adds `docs/ghost.md` (never created).\n' > "$ADOPTER/fab.md"
"$BIN/anti-slop-pr" --root "$ADOPTER" "$ADOPTER/clean.md" >/dev/null 2>&1; c=$?
"$BIN/anti-slop-pr" --root "$ADOPTER" "$ADOPTER/fab.md" >/dev/null 2>&1; d=$?

# 4. event wrapper: non-PR SKIP, and report mode on a fabricated PR event
printf '{"ref":"refs/heads/main","commits":[]}\n' > "$TMP/push.json"
printf '{"pull_request":{"number":1,"body":"Adds `docs/ghost.md`."}}\n' > "$TMP/pr.json"
"$BIN/anti-slop-pr-event" --event "$TMP/push.json" --event-name push --root "$ADOPTER" >/dev/null 2>&1; e=$?
"$BIN/anti-slop-pr-event" --event "$TMP/pr.json" --event-name pull_request --root "$ADOPTER" --report >/dev/null 2>&1; f=$?

# 5. shipped example body resolves against this repo
"$BIN/anti-slop-pr" --root "$REPO" "$REPO/templates/example-pr-body.md" >/dev/null 2>&1; g=$?

echo "[1] anti-slop-pr --self-test            -> exit $a (expect 0)"
echo "[2] anti-slop-pr-event --self-test      -> exit $b (expect 0)"
echo "[2b] anti-slop-claims --self-test       -> exit $h (expect 0)"
echo "[2c] anti-slop-run --self-test          -> exit $i (expect 0)"
echo "[3] adopter clean PR body               -> exit $c (expect 0 PASS)"
echo "[4] adopter fabricated PR body          -> exit $d (expect 1 FAIL)"
echo "[5] event wrapper non-PR event          -> exit $e (expect 0 SKIP)"
echo "[6] event wrapper --report (fabricated) -> exit $f (expect 0 advisory)"
echo "[7] shipped templates/example-pr-body   -> exit $g (expect 0 PASS)"

if [ "$a" -eq 0 ] && [ "$b" -eq 0 ] && [ "$h" -eq 0 ] && [ "$i" -eq 0 ] && [ "$c" -eq 0 ] && [ "$d" -eq 1 ] \
   && [ "$e" -eq 0 ] && [ "$f" -eq 0 ] && [ "$g" -eq 0 ]; then
  echo "AGENT-INSTALL SMOKE PASSED: the INSTALL_FOR_AGENTS.md commands install and behave as documented."
  exit 0
fi
echo "AGENT-INSTALL SMOKE FAILED (a=$a b=$b h=$h i=$i c=$c d=$d e=$e f=$f g=$g)."
exit 1
