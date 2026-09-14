#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "y3_operating_profit_millions": 3.0,
  "hurdle_millions": 20,
  "decision": "no-go",
  "rationale": "Year-3 OP of $3M is below the $20M hurdle\u2014do not enter."
}
ORACLE_EOF
