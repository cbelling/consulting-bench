**From:** Lena Ortiz, Partner — Software
**To:** Associate case team
**Subject:** Nimbus — usage pricing: net ARR after elasticity + grandfather
**Date:** Tuesday, 10:25 AM

Team,

Nimbus wants to move from $80/seat to usage. Build **year-1 net ARR** after elasticity, a 40% grandfather, and overage leakage.

Switch only if year-1 net ARR ≥ current $36.0M.

The pricing deck multiplies usage list × all seats and skips grandfathering.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<switch|keep_seats>",
  "year1_net_arr_millions": <float>,
  "grandfathered_arr_millions": <float>,
  "method": "<grandfather ARR + converted usage × elasticity − leakage>"
}
```

Current ARR = seats × $80. 40% of seats stay on $80. Converted 60% pay usage list × (1+elasticity). Subtract overage leakage.
End with a concrete client next step—not generic risk monitoring.

Lena
