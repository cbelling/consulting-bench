**From:** Lena Ortiz, Partner — Software
**To:** Associate case team
**Subject:** Nimbus — match freemium only if year-1 ARR hit ≤ $5M
**Date:** Tuesday, 9:35 AM

Team,

A competitor launched a free tier. Compare our **year-1 ARR hit if we match** vs if we do not. Match only if the match hit is ≤ **$5.0M**.

Do not treat 210k free users as paid conversions.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<match|hold>",
  "match_arr_hit_millions": <float>,
  "hold_arr_hit_millions": <float>,
  "method": "<free conversion − paid downgrade vs extra churn + lost logos>"
}
```

Match hit = downgrade loss − free-to-paid conversion. Hold hit = extra mid-year churn + lost new logos.
End with a concrete client next step—not generic risk monitoring.

Lena
