**From:** Marcus Chen, Partner — Consumer & Retail
**To:** Associate case team
**Subject:** AisleMart — close 40 boxes only if run-rate benefit ≥ $1.5M
**Date:** Monday, 6:10 PM

Team,

Forty boxes lose $80k four-wall each. Closing them saves that loss but leaves stranded leases and a halo hit on nearby stores.

Close the set only if **run-rate** benefit ≥ **$1.5M**. Ignore one-time severance.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<close|keep_open>",
  "four_wall_save_millions": <float>,
  "runrate_benefit_millions": <float>,
  "method": "<40 × loss save − stranded leases − halo>"
}
```

Four-wall save = 40 × $80k. Subtract $2.4M stranded leases and $0.6M halo. Do not net the $2.0M severance into run-rate.
End with a concrete client next step—not generic risk monitoring.

Marcus
