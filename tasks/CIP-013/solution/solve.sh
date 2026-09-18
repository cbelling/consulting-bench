#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "delta_profit_millions": -86.0,
  "primary_driver": "fuel",
  "fuel_share_of_decline_pct": 70.0,
  "recommendation": "Prioritize fuel hedging and network fuel-efficiency; fuel explains ~70% of the $86M profit decline."
}
ORACLE_EOF
