# Leaderboard

Consulting Bench records Harbor job summaries under [`evals/`](../evals).
The current Partner-50 / terminus-2 / Modal scoreboard:

| Set | Run | Pass | Mean | Cost |
|-----|-----|------|------|------|
| Pre-harden (31 stub graders) | Sequential n=1 | 43/50 | 0.86 | $1.04 |
| Pre-harden (31 stub graders) | Concurrent n=20 | 45/50 | 0.90 | $0.93 |
| **Hardened-v1 (all checkable)** | Concurrent n=20 | **26/50** | **0.52** | **$0.73** |

Hardened-v1: 0 errors; all 24 fails still have a passing local oracle.
Pre-harden sequential/concurrent JSON lives under
`evals/full-bench-deepseek-v4.1-flash-*-results.json`.

This folder is the Terminal-Bench-style place for public leaderboard data.
A multi-model pass and a static site live on a separate branch
(`cursor/four-model-leaderboard-0618`).
