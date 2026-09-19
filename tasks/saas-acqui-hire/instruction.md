**From:** Nina Patel, Partner — Software
**To:** Associate case team
**Subject:** Nimbus — acqui-hire Helio vs 14-person build
**Date:** Monday, 5:10 PM

Team,

Nimbus needs an observability module in 24 months. Compare **24-month cash out** of acqui-hiring Helio vs building 14 engineers, including dead-time before the build team is productive.

Choose the cheaper 24-month cash path. A board slide treats Helio equity as free.

Exhibits in `/app/matter/`.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<acqui_hire|build>",
  "acqui_hire_cash_24m_millions": <float>,
  "build_cash_24m_millions": <float>,
  "method": "<cash + retention + dead-time loaded build cost>"
}
```

Acqui-hire cash = close cash + 24-month retention + integration. Build = loaded cost × 14 × 24 months, plus 4 months of unproductive dead-time at the same burn.
End with a concrete client next step—not generic risk monitoring.

Nina
