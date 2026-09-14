#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "enterprise_value_millions": 560.0,
  "seller_ask_millions": 400,
  "decision": "go",
  "rationale": "EV of $560M (80 * 7x) exceeds $400M ask\u2014go."
}
ORACLE_EOF
