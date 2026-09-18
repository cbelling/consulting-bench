# Development notes

These generators rewrite slices in place. After the L1/L3 generators, re-run
the hardener so spoilers stay stripped and bands stay tight.

```bash
python3 scripts/generate_partner_tasks.py
python3 scripts/generate_l3_partner_tasks.py
python3 scripts/generate_hardened_stubs.py   # 31 formerly stub L2/L3 cases
python3 scripts/tighten_existing_graders.py  # strip spoilers + tighten the other 19
python3 scripts/validate_task_fields.py
bash scripts/verify_oracles_local.sh
```

Recorded Harbor jobs live under `evals/`. Bundled run configs live under
`configs/` (Terminal-Bench style). Helper wrappers in `scripts/` still point
at the JSON jobs in `evals/` so existing dry-run and full-bench commands
keep working.

## Scope

- Management consulting only; all matter is synthetic
- Partner-memo Harbor tasks only (memo + JSON sidecar)
