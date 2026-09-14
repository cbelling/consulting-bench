#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "net_benefit_millions": 0.22,
  "hurdle_millions": 1,
  "decision": "no-go",
  "rationale": "Net benefit $0.22M is below the $1M hurdle\u2014no-go."
}
ORACLE_EOF
