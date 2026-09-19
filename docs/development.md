# Development notes

Durable helpers in `scripts/` are for running and checking the bench, not
rewriting tasks:

```bash
python3 scripts/validate_task_fields.py
bash scripts/verify_oracles_local.sh
```

Edit task folders under `tasks/` by hand. After a change, run the validators
above (and `harbor run -p tasks/<TASK-ID> -a oracle` if Docker is available).

Recorded Harbor jobs live under `evals/`. Bundled run configs live under
`configs/` (Terminal-Bench style). Modal wrappers in `scripts/`
(`run_dry_run.sh`, `run_full_bench_concurrent.sh`,
`run_full_bench_sequential.sh`, `run_hardened_bench_concurrent.sh`) point
at those recorded job configs.

## Scope

- Management consulting only; all matter is synthetic
- Partner-memo Harbor tasks only (memo + JSON sidecar)
