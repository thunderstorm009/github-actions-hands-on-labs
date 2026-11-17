# GitHub jobs fundamentals

A workflow is triggered by an event and contains one or more jobs. Each job has an ID, a runner selected by **runs-on**, and ordered steps. Jobs without **needs** are eligible to run independently; the scheduler decides when runner capacity is available. Job definition order does not guarantee execution order.

## Runner isolation

A GitHub-hosted job runs in a fresh runner environment. A second job does not automatically see files created by the first. Check out source in each job that needs it. Transfer generated files using artifacts; transfer small scalar values using job outputs.

## Dependencies

Use **needs: job-id** or a list such as **needs: [build, test]** to express prerequisites. By default, a dependent job runs only when its required jobs succeed. If a required job fails or is skipped, dependents are skipped unless a status-aware condition deliberately changes that behavior.

## Permissions and time limits

Use the smallest workflow permissions needed, commonly **contents: read** for checkout-only jobs. Set **timeout-minutes** so a stuck process does not run indefinitely. Hosted runner OS labels such as **ubuntu-latest** can change over time; consult the official [runner image documentation](https://docs.github.com/en/actions/reference/runners/github-hosted-runners).

See the lab [README](../README.md) for complete copyable workflows and UI inspection steps. Official references: [jobs](https://docs.github.com/en/actions/using-jobs/using-jobs-in-a-workflow), [workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).
