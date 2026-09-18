**From:** Elena Vasquez, Partner — Transportation & Leisure
**To:** Associate case team
**Subject:** SkyWing bag fee $30→$40 — raise or hold?
**Date:** Tuesday, 11:30 AM

Team,

SkyWing plans to raise checked-bag fees from **$30 to $40** (8M bags/yr). Marketing cites elasticity **−0.4**; revenue management warns **−1.0**. Spill to competitors affects **20M passengers** at **$40 contribution** each (0.5% vs 1.2% scenarios). Variable cost is **$6/bag**.

Model **both** elasticity/spill combinations in `/app/matter/` and recommend whether to raise.

Deliverables by **Wednesday 3 PM**:
1. `/app/output/memo.md` (recommendation in paragraph one).
2. `/app/output/answer.json`:

```json
{
  "decision": "<raise|hold>",
  "incremental_profit_millions_optimistic": <float>,
  "incremental_profit_millions_pessimistic": <float>,
  "method": "<bag-fee elasticity and spill model>"
}
```

Show both scenarios. End with a concrete pricing next step.

Elena
