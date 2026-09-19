**From:** Marcus Williams, Partner — Travel & Transportation
**To:** Associate case team
**Subject:** NorthAir — run-rate margin vs $500M board ask
**Date:** Tuesday, 5:40 PM

Team,

NorthAir reports $8.308B cost on 62B ASMs. The $180M fuel-hedge loss is **one-time**. Labor steps up **4.0%** next year on the labor share.

Board wants **$500M** run-rate operating profit. Say whether run-rate gets there.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<enough|more_cuts>",
  "runrate_cost_billions": <float>,
  "runrate_profit_millions": <float>,
  "gap_to_500_millions": <float>,
  "method": "<reported cost − hedge + labor step; vs revenue>"
}
```

Labor = 31% of reported cost. Run-rate cost = reported − $0.180B hedge + 4% of labor. Revenue = $8.550B.
End with a concrete client next step—not generic risk monitoring.

Marcus
