#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "incremental_profit_millions": -3.0,
  "decision": "cut_nights",
  "rationale": "Night shift incremental profit is -$3M; cut nights\u2014do not allocate fixed overhead."
}
ORACLE_EOF
