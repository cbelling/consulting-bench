#!/usr/bin/env bash
# Verify oracle solutions for Harbor L1 consulting tasks.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TASKS_DIR="$ROOT/tasks"

TASK_IDS=(
  CIP-001 CIP-002 CIP-004 CIP-007 CIP-013 CIP-014 CIP-017 CIP-020 CIP-022
  CIP-026 CIP-027 CIP-029 CIP-031 CIP-035 CIP-037 CIP-039 CIP-042 CIP-045
  CIP-049 CIP-051
)

if [[ $# -gt 0 ]]; then
  TASK_IDS=("$@")
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

  echo "==> Verifying $tid"
  docker build -t "mcb-verify-$tid" -f "$task_dir/environment/Dockerfile" "$task_dir" >/dev/null

  reward=$(docker run --rm \
    -v "$task_dir/tests:/tests:ro" \
    -v "$task_dir/solution:/solution:ro" \
    "mcb-verify-$tid" \
    bash -lc 'bash /solution/solve.sh && bash /tests/test.sh && cat /logs/verifier/reward.txt')

  if [[ "$reward" == "1" ]]; then
    echo "PASS $tid (reward=$reward)"
    ((pass++)) || true
  else
    echo "FAIL $tid (reward=$reward)"
    ((fail++)) || true
  fi
done

echo "---"
echo "Passed: $pass / $((pass + fail))"
if [[ $fail -gt 0 ]]; then
  exit 1
fi
