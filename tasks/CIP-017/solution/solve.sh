#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "dominant_driver": "ticket_and_parts_margin",
  "volume_change_pct": 11.0,
  "ticket_parts_margin_change_millions": 48.0,
  "summary": "Profit gain is dominated by higher ticket and parts margin (+$48M), not visit volume alone."
}
ORACLE_EOF
