**If this PR adds or changes a Consulting Bench task, complete the checklist.
Otherwise, delete the task section.**

## Task checklist

- [ ] `python3 scripts/validate_task_fields.py` passes
- [ ] `bash scripts/verify_oracles_local.sh <kebab-slug>` returns reward `1`
- [ ] All behavior checked in `tests/verify.py` is described in `instruction.md`
- [ ] All behavior described in `instruction.md` is checked by the verifier
- [ ] Matter files do not precompute the answer
- [ ] The oracle in `solution/solve.sh` was reviewed by a human

## Summary

<!-- What changed and why. -->
