#!/bin/bash
set -euo pipefail

mkdir -p /logs/verifier
MEMO="/app/output/memo.md"
ANSWER="/app/output/answer.json"

if python3 /tests/verify.py "$MEMO" "$ANSWER"; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
