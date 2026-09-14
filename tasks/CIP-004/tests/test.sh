#!/bin/bash
set -euo pipefail

mkdir -p /logs/verifier
OUTPUT="/app/output/answer.json"

if python3 /tests/verify.py "$OUTPUT"; then
  echo 1 > /logs/verifier/reward.txt
else
  echo 0 > /logs/verifier/reward.txt
fi
