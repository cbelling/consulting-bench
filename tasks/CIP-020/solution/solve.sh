#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "primary_leak": "churn",
  "monthly_churn_pct": 4.2,
  "rationale": "CAC is flat; rising churn is destroying net retention and is the leak\u2014not acquisition unit cost."
}
ORACLE_EOF
