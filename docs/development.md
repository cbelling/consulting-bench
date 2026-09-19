# Development notes

Durable helpers in `scripts/` are for running and checking the bench, not
rewriting tasks:

```bash
python3 scripts/validate_task_fields.py
bash scripts/verify_oracles_local.sh
```

Edit task folders under `tasks/` by hand. After a change, run the validators
above (and `harbor run -p tasks/restinn-weekend-pricing -a oracle` if Docker
is available).

Recorded Harbor jobs live under `evals/`. Those JSON files still name the
folders as `CIP-XXX` because that is what the runs used. Live tasks now use
kebab-case slugs (`restinn-weekend-pricing`). Bundled run configs live under
`configs/` (Terminal-Bench style). Modal wrappers in `scripts/`
(`run_dry_run.sh`, `run_full_bench_concurrent.sh`,
`run_full_bench_sequential.sh`, `run_hardened_bench_concurrent.sh`) point
at those recorded job configs.

## Scope

- Management consulting only; all matter is synthetic
- Partner-memo Harbor tasks only (memo + JSON sidecar)
