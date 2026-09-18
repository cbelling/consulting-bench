**From:** Emily Chen, Partner — Industrial
**To:** Associate case team
**Subject:** Sensoria IoT — spin EBITDA after captive transfer leakage
**Date:** Monday, 11:00 AM

Team,

Corporate wants to spin Sensoria IoT. Build **standalone EBITDA** after losing most parent transfer revenue.

Spin only if standalone EBITDA ≥ **$4.0M**. The CIM treats $17M parent transfers as lasting third-party sales.

Deliverables by **Wednesday 5 PM**:
1. `/app/output/memo.md` — one-page memo with the recommendation and the key number in paragraph one.
2. `/app/output/answer.json`:

```json
{
  "decision": "<spin|no-spin>",
  "standalone_ebitda_millions": <float>,
  "kept_transfer_gm_millions": <float>,
  "method": "<external GM + surviving transfer GM − standalone opex>"
}
```

Keep 40% of transfer at 18% GM (arm's length). Lose 60% of transfer entirely. External GM stays 34%. Subtract standalone opex.
End with a concrete client next step—not generic risk monitoring.

Emily
