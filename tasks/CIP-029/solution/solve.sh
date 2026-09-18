#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "npv_millions": -9.6,
  "decision": "no-go",
  "rationale": "NPV is -$9.6M; value-destructive\u2014no-go."
}
ORACLE_EOF
