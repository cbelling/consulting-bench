**From:** Elena Vasquez, Partner — Hospitality & Leisure
**To:** Associate case team
**Subject:** Harborlight — F&B: keep banquet or cut outlets?
**Date:** Tuesday, 11:05 AM

Team,

Harborlight's GM wants to close in-house restaurants because departmental profit is weak. Build **true contribution after shared-kitchen allocation** for banquet vs outlets.

Keep banquet and cut outlets only if banquet true contribution ≥ **$1.8M** and outlets are negative.

`/app/matter/` has departmental P&L plus a controller note on shared kitchen and banquet labor.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<keep_banquet_cut_outlets|keep_both|cut_banquet>",
  "banquet_true_contribution_millions": <float>,
  "outlet_true_contribution_millions": <float>,
  "method": "<dept profit + add-back − shared kitchen>"
}
```

True contribution = departmental profit + wrongly loaded shared kitchen − any banquet labor parked in rooms.
End with a concrete client next step—not generic risk monitoring.

Elena
