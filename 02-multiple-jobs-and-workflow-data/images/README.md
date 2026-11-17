# Lab visual asset index

The main [lab README](../README.md) embeds conceptual Mermaid diagrams beside the corresponding explanation. Editable Mermaid source files are grouped by purpose below. The retained SVGs are original teaching illustrations, not execution screenshots.

| Source | Topic |
|---|---|
| [Job and runner isolation](architecture/job-runner-isolation.mmd) | Workflow hierarchy and separate workspaces |
| [Parallel jobs and dependencies](architecture/parallel-and-needs.mmd) | prepare, parallel-check, report |
| [Final integration architecture](architecture/final-integration.mmd) | Integration challenge dependencies |
| [Step and job outputs](implementation/output-data-flow.mmd) | GITHUB_OUTPUT to downstream job |
| [Artifact lifecycle](implementation/artifact-lifecycle.mmd) | Upload, isolated runners, download |
| [Logs, summary and artifacts](implementation/log-summary-artifact.mmd) | Purpose of three output mechanisms |
| [Matrix expansion](workflows/matrix-expansion.mmd) | Python matrix variants |
| [Status functions](workflows/status-functions.mmd) | Failure, success, always and skipped job |
| [Concurrency and timeouts](workflows/concurrency-timeout.mmd) | Cancellation and bounded jobs |
| [Push to Actions lifecycle](workflows/push-to-actions.mmd) | Local Git through Actions inspection |
| [Debugging decision tree](troubleshooting/debugging-decision-tree.mmd) | First-failure investigation |

Retained SVG illustrations:

- [Parallel jobs](diagrams/parallel-jobs.svg)
- [Artifact and job summary](diagrams/step-artifact-summary.svg)
- [Matrix and status functions](diagrams/step-matrix-status.svg)
- [Output flow](diagrams/step-output-flow.svg)

No GitHub Actions execution screenshots are included. Use the [genuine screenshot guide](screenshots/README.md) after running the examples in your own practice repository.
