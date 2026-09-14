#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "value_created_millions": -0.8,
  "hurdle_millions": 10,
  "decision": "no-go",
  "rationale": "Net value of -$0.8M misses the $10M hurdle\u2014no-go."
}
ORACLE_EOF
