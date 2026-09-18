#!/bin/bash
set -euo pipefail
mkdir -p /app/output
cat > /app/output/memo.md << 'MEMO_EOF'
We recommend go on the AeroTread passenger-narrowbody bid. Annual replacement demand is 9,600 tires and TAM is $23.04M, clearing the $20M hurdle. Cargo replacements (1,792) and the 216-tire spare pool are out of scope.

## Fleet × frequency
- 180 NB aircraft × 8 tires × (1,200 cycles / 180 landing life) = **9,600** replacements
- TAM: 9,600 × $2,400 = **$23.04M**
- Excluded: cargo 1,792 tires; spare-pool stock 216; 22 passenger widebodies; regional-jet 220-aircraft count

## Next step
Submit the NB-only bid package to the Thursday committee and lock the $2,400 ASP with procurement before cargo is added to scope.
MEMO_EOF
cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "go",
  "annual_replacements": 9600.0,
  "tam_millions": 23.04,
  "method": "fleet \u00d7 tires \u00d7 cycles / landing life"
}
JSON_EOF
