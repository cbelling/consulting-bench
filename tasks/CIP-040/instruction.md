**From:** Marcus Chen, Partner — Consumer & Retail
**To:** Associate case team
**Subject:** Harvest & Co — bid only if syn-adjusted ROIC ≥ 13%
**Date:** Monday, 11:40 AM

Team,

We can bid $180M for Harvest & Co (organic snacks). Build **year-3 syn-adjusted ROIC** = (NOPAT + after-tax synergies − stranded HQ) / (EV + stranded integration cash).

Bid only if ROIC ≥ **13%**. Banker materials capitalize revenue synergies that ops has not diligence-confirmed.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<bid|walk>",
  "year3_roic_pct": <float>,
  "after_tax_synergies_millions": <float>,
  "method": "<(NOPAT + syn − stranded) / (EV + integration cash)>"
}
```

Use only cost synergies ops confirmed. Tax rate 25%. Do not use the banker's $22M revenue synergy.
End with a concrete client next step—not generic risk monitoring.

Marcus
