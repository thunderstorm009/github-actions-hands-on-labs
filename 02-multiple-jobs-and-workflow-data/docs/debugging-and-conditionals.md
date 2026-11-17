# Debugging and conditionals

Start with the workflow graph, locate the first failed job, then open the first failing step. Compare exact job IDs, step IDs, output keys, artifact names, paths, and conditional expressions.

## Status functions

- **success()**: prior relevant work succeeded.
- **failure()**: prior relevant work failed.
- **always()**: evaluate even after failure or cancellation.
- **cancelled()**: the run/job was cancelled.

Dependent jobs have an implicit success condition. A job-level **if: always()** can permit a diagnostic/report job to run after a failed dependency. A step-level **if: failure()** can print diagnostics after failure. The workflow remains failed; do not hide a real failure with continue-on-error or broad conditions.

## Common debugging order

1. Check the graph: failed, skipped, or cancelled?
2. Open the first red job and first failing step.
3. Read the command output and compare names/paths.
4. Check whether a needed producer completed.
5. Repair one issue, commit, push, and inspect the next run.

Run the intentional failure workflow manually only. It is expected to finish red. See [GitHub status-check expressions](https://docs.github.com/en/actions/learn-github-actions/expressions#status-check-functions).
