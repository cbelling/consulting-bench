**From:** Olivia Grant, Partner — Financial Services
**To:** Associate case team
**Subject:** ClearBank — BNPL net vs $8M hurdle
**Date:** Tuesday, 4:00 PM

Team,

ClearBank can put BNPL on checkout. Build **year-1 net** = GMV × (take-rate − loss − opex) − revolving-NII cannibal.

Launch only if net ≥ **$8M**. Do not report take-rate × GMV as profit.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<launch|no-go>",
  "bnpl_contribution_millions": <float>,
  "year1_net_millions": <float>,
  "method": "<GMV × spread − revolving cannibal>"
}
```

Spread = take-rate − loss rate − opex rate. Cannibal = 18% of $40M revolving NII.
End with a concrete client next step—not generic risk monitoring.

Olivia
