**From:** Daniel Cho, Partner — Consumer & Retail
**To:** Associate case team
**Subject:** Cartly — 3P vs 1P on the home-goods category
**Date:** Wednesday, 8:30 AM

Team,

Cartly can flip home-goods from 1P to 3P. Compare **category contribution** under 1P vs 3P after returns, ads, and fulfillment.

Flip to 3P only if 3P contribution exceeds 1P by ≥ **$8M**.

The marketplace GM quotes take-rate × GMV and stops. That is incomplete.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<flip_3p|keep_1p>",
  "onep_contribution_millions": <float>,
  "threep_contribution_millions": <float>,
  "method": "<1P margin after returns/fulfill vs take-rate + ads − 3P costs>"
}
```

1P = GMV × (gross margin − return rate × landed cost share) − fulfillment. 3P = GMV × take-rate + ads − 3P ops − referral leakage.
End with a concrete client next step—not generic risk monitoring.

Daniel
