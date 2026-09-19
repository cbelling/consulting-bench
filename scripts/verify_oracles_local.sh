#!/usr/bin/env bash
# Verify partner-memo oracle solutions locally (no Harbor/Docker).
# Default: all 50 partner-delegated tasks. Pass kebab slugs or CIP IDs
# (for example restinn-weekend-pricing or CIP-054) to check a subset.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TASKS_DIR="$ROOT/tasks"
TMP_ROOT=$(mktemp -d)
trap 'rm -rf "$TMP_ROOT"' EXIT

resolve_task_id() {
  python3 - "$ROOT" "$1" <<'PY'
import sys
from pathlib import Path

root = Path(sys.argv[1])
sys.path.insert(0, str(root / "scripts"))
from task_slugs import folder_slug

print(folder_slug(sys.argv[2]))
PY
}

if [[ $# -gt 0 ]]; then
  TASK_IDS=()
  for raw in "$@"; do
    TASK_IDS+=("$(resolve_task_id "$raw")")
  done
else
  mapfile -t TASK_IDS < <(find "$TASKS_DIR" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | sort)
fi

pass=0
fail=0

for tid in "${TASK_IDS[@]}"; do
  task_dir="$TASKS_DIR/$tid"
  if [[ ! -d "$task_dir" ]]; then
    echo "FAIL $tid — directory missing"
    ((fail++)) || true
    continue
  fi

  sandbox="$TMP_ROOT/$tid"
  mkdir -p "$sandbox/app/output" "$sandbox/app/matter" "$sandbox/logs/verifier"

  if [[ -d "$task_dir/environment/matter" ]]; then
    cp -r "$task_dir/environment/matter/"* "$sandbox/app/matter/" 2>/dev/null || true
  else
    cp -r "$task_dir/matter/"* "$sandbox/app/matter/" 2>/dev/null || true
  fi
  cp "$task_dir/tests/verify.py" "$sandbox/verify.py"
  cp "$task_dir/tests/test.sh" "$sandbox/test.sh"
  cp "$task_dir/solution/solve.sh" "$sandbox/solve.sh"

  (
    cd "$sandbox"
    sed 's|/app/|./app/|g; s|/tests/verify.py|./verify.py|g; s|/logs/verifier|./logs/verifier|g' solve.sh > solve_local.sh
    sed 's|/app/|./app/|g; s|/tests/verify.py|./verify.py|g; s|/logs/verifier|./logs/verifier|g' test.sh > test_local.sh
    chmod +x solve_local.sh test_local.sh
    bash solve_local.sh
    bash test_local.sh
  )

  reward=$(cat "$sandbox/logs/verifier/reward.txt")
  if [[ "$reward" == "1" ]]; then
    echo "PASS $tid"
    ((pass++)) || true
  else
    echo "FAIL $tid (reward=$reward)"
    ((fail++)) || true
  fi
done

echo "---"
echo "Passed: $pass / $((pass + fail))"
[[ $fail -eq 0 ]]
