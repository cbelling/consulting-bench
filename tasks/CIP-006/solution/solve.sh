#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend go on Pixelate India entry. Annual smartphone sell-out is 186.2M units and TAM is $31.3B, inside the 160–200M unit gate. The 220M sell-in and 2.5-year tablet cycle are rejected.

## Build
- Users: 1.42B × 68% × 54% = **521.4M**
- Replacements: 521.4 / 3.1 = **168.2M**
- Plus first-time 18.0M = **186.2M** units
- TAM: 186.2M × $168 = **$31.3B**

## Next step
File the India entry IC memo with sell-out (not sell-in) as the official TAM and commission a 6-city replacement-cycle diary.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "go",
  "annual_units_millions": 186.201,
  "tam_billions": 31.282,
  "method": "users / replacement cycle + first-time"
}
JSON_EOF
