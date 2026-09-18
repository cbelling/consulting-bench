#!/usr/bin/env bash
# Verify oracle solutions without Harbor/Docker (local smoke test).
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TASKS_DIR="$ROOT/tasks"
TMP_ROOT=$(mktemp -d)
trap 'rm -rf "$TMP_ROOT"' EXIT

TASK_IDS=(
  CIP-001 CIP-002 CIP-004 CIP-007 CIP-013 CIP-014 CIP-017 CIP-020 CIP-022
  CIP-026 CIP-027 CIP-029 CIP-031 CIP-035 CIP-037 CIP-039 CIP-042 CIP-045
  CIP-049 CIP-051
)

# Partner-delegated Harbor slice (memo.md + answer.json, 4-check verifier)
PARTNER_TASK_IDS=(
  CIP-054 CIP-063 CIP-075 CIP-089 CIP-098
)

# Hard L3 partner-delegated frontier probe (COD-57)
L3_PARTNER_TASK_IDS=(
  CIP-015 CIP-021 CIP-028 CIP-044 CIP-050 CIP-052 CIP-055 CIP-066 CIP-093 CIP-099
)

if [[ $# -gt 0 ]]; then
  TASK_IDS=("$@")
  PARTNER_TASK_IDS=()
  L3_PARTNER_TASK_IDS=()
fi

pass=0
fail=0

for tid in "${TASK_IDS[@]}"; do
  task_dir="$TASKS_DIR/$tid"
  sandbox="$TMP_ROOT/$tid"
  mkdir -p "$sandbox/app/output" "$sandbox/app/matter" "$sandbox/logs/verifier"

  cp -r "$task_dir/matter/"* "$sandbox/app/matter/" 2>/dev/null || true
  cp "$task_dir/tests/verify.py" "$sandbox/verify.py"
  cp "$task_dir/tests/test.sh" "$sandbox/test.sh"
  cp "$task_dir/solution/solve.sh" "$sandbox/solve.sh"

  (
    cd "$sandbox"
    # Rewrite paths for local sandbox
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

COMBINED_PARTNER_IDS=("${PARTNER_TASK_IDS[@]}" "${L3_PARTNER_TASK_IDS[@]}")
for tid in "${COMBINED_PARTNER_IDS[@]}"; do
  task_dir="$TASKS_DIR/$tid"
  sandbox="$TMP_ROOT/$tid"
  mkdir -p "$sandbox/app/output" "$sandbox/app/matter" "$sandbox/logs/verifier"

  cp -r "$task_dir/matter/"* "$sandbox/app/matter/" 2>/dev/null || true
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
