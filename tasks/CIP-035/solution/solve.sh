#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "operating_profit_millions": -7.8,
  "decision": "no-go",
  "rationale": "Year-3 OP is -$7.8M; expansion fails profitability gate\u2014no-go."
}
ORACLE_EOF
