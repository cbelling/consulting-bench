**From:** Priya Nair, Partner — Media
**To:** Associate case team
**Subject:** Streamhouse — ad-lite net vs $25M hurdle
**Date:** Monday, 1:00 PM

Team,

Streamhouse wants a $12.99 ad-lite tier (35% take; rest stay at $15.99). Finance's exhibit ignores ad-lite churn. Product's exhibit ignores ad ARPU.

Launch only if net revenue vs base ≥ **$25M**.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<launch|hold>",
  "net_vs_base_millions": <float>,
  "ad_revenue_millions": <float>,
  "method": "<mix of prices + ad ARPU − 4% ad-lite churn>"
}
```

Base = 4.2M × $15.99 × 12. New = ad-lite subs × ($12.99+$4.80) × 12 × (1−4% churn) + stay × $15.99 × 12.
End with a concrete client next step—not generic risk monitoring.

Priya
