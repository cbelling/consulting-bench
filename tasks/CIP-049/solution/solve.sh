#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/answer.json << 'ORACLE_EOF'
{
  "forward_ebitda_millions": 9.5,
  "entry_multiple": 8,
  "equity_check_millions": 30.4,
  "limit_millions": 70,
  "decision": "go",
  "rationale": "Forward EBITDA 9.5 * 8x = $76M EV exceeds $70M limit\u2014go."
}
ORACLE_EOF
