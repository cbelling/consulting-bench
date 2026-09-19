#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend build. 24-month cash is $6.16M for the 14-person team including the 4-month dead-time payroll, versus $14.9M cash for the Helio acqui-hire. Option rollover is not cash.

## Cash-out
- Acqui-hire: 9.0 + 4.8 + 1.1 = **$14.9M** (exclude $6.0M equity face)
- Build: 14 × $0.220M × 2.0 years = **$6.16M** (pay through dead-time)
- Board $5.13M skips 4 months; $9.0M Helio skip ignores retention.

## Next step
Stand up the 14-person requisition this Friday and withdraw the Helio LOI.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "build",
  "acqui_hire_cash_24m_millions": 14.9,
  "build_cash_24m_millions": 6.16,
  "method": "close cash + retention + integration vs loaded 24-month build burn"
}
JSON_EOF
