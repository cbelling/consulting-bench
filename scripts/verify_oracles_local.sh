#!/usr/bin/env bash
# Verify partner-memo oracle solutions locally (no Harbor/Docker).
# Default: all 50 partner-delegated tasks. Pass CIP IDs to check a subset.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TASKS_DIR="$ROOT/tasks"
TMP_ROOT=$(mktemp -d)
trap 'rm -rf "$TMP_ROOT"' EXIT

DEFAULT_TASK_IDS=(
  CIP-003 CIP-005 CIP-006 CIP-010 CIP-012 CIP-015 CIP-016 CIP-018 CIP-019 CIP-021
  CIP-025 CIP-028 CIP-030 CIP-032 CIP-033 CIP-034 CIP-038 CIP-040 CIP-041 CIP-043
  CIP-044 CIP-050 CIP-052 CIP-053 CIP-054 CIP-055 CIP-057 CIP-059 CIP-062 CIP-063
  CIP-064 CIP-066 CIP-067 CIP-070 CIP-075 CIP-076 CIP-077 CIP-079 CIP-084 CIP-085
  CIP-087 CIP-089 CIP-090 CIP-091 CIP-093 CIP-096 CIP-097 CIP-098 CIP-099 CIP-100
)

if [[ $# -gt 0 ]]; then
  TASK_IDS=("$@")
else
  TASK_IDS=("${DEFAULT_TASK_IDS[@]}")
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
