#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "implied_value_millions": 177.5,
  "bid_millions": 180,
  "decision": "marginal",
  "rationale": "Implied value ~$177.5M vs $180M bid is marginal\u2014710 sites * $250K * 10x \u2248 $177.5M."
}
ORACLE_EOF
