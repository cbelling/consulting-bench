**From:** James Park, Partner — Logistics
**To:** Associate case team
**Subject:** Parceline — dim-weight net after small-shipper churn
**Date:** Tuesday, 7:50 AM

Team,

Parceline can switch from actual-weight billing to dim-weight (bill the max of actual vs dim). Build **year-1 net** = incremental billed pounds × rate − small-shipper churn.

Implement if net ≥ **$8M**. Do not bill dim pounds on top of actual — only the increment. Ignore the oversized-subset average in the ops footnote.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<implement|hold>",
  "year1_net_millions": <float>,
  "incremental_lb_billions": <float>,
  "method": "<parcels × (dim − actual) × rate − churn>"
}
```

Incremental pounds = parcels × (average dim − average actual). Multiply by $/lb. Subtract churn on small-shipper revenue.
End with a concrete client next step—not generic risk monitoring.

James
