#!/bin/bash
set -euo pipefail
mkdir -p /app/output

cat > /app/output/memo.md << 'MEMO_EOF'
We recommend **no-go** on Chemora's solo US lithium processing entry. Engineering reality ($24M base case EBITDA, $32M with expected policy incentive) misses the $150M IRR hurdle by 5×, even with IRA upside. The consultant's $60M EBITDA assumes aspirational 35% efficiency; our plant design achieves 28%, yielding $1,200/tonne margin vs consultant $3,000/tonne.

## EBITDA scenarios vs $150M hurdle (L3 conflicting exhibits)

| View | Margin $/tonne | Annual EBITDA | vs $150M hurdle |
|------|----------------|---------------|-----------------|
| A: Consultant (aspirational) | $3,000 | $60M | ❌ Miss by 2.5× |
| B: Engineering base | $1,200 | **$24M** | ❌ Miss by 6× |
| C: With IRA incentive (100%) | $2,000 | $40M | ❌ Miss by 3.75× |
| C: Expected (50% prob) | $1,600 | **$32M** | ❌ Miss by 4.7× |

Market: 200kt 2028 US demand × 10% share = 20kt. 

Even the bull consultant case ($60M) clears only 40% of the IRR hurdle. Engineering truth at $1,200/tonne margin ($24M base, $32M expected with uncertain policy incentive) misses by 80%.

To hit $150M at engineering margin would require 62.5% US market share (125kt)—infeasible for a new entrant.

## Recommended path
Pursue **strategic partnership** with a cathode manufacturer (co-located facility) to split $900M CapEx and secure 50kt+ offtake contract. This would 2.5× scale (from 20kt to 50kt) and improve unit economics via integration, potentially clearing hurdle at $1,800+/tonne blended margin.

## Next step
Engage three target cathode OEMs (LG Energy, CATL US JV, Panasonic) for 90-day exclusivity on joint venture structuring before abandoning the opportunity.
MEMO_EOF

cat > /app/output/answer.json << 'JSON_EOF'
{
  "decision": "no-go",
  "base_case_annual_ebitda_millions": 24.0,
  "with_incentive_annual_ebitda_millions": 32.0,
  "hurdle_annual_ebitda_millions": 150.0,
  "method": "market × share × engineering margin with policy incentive scenarios, reconciling consultant vs engineering conflict"
}
JSON_EOF
