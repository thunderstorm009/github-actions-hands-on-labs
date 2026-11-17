# Lab visual asset index

Lab 02 uses two complementary visual categories.

- **Conceptual diagrams:** explain architecture, dependencies, and data flow. The current README embeds Mermaid diagrams beside the explanations, and editable source is listed below.
- **Instructional images:** preserved SVG code/step illustrations show implementation details. Labeled screenshot capture cards explain precisely which genuine editor or Actions UI evidence to capture. They are placeholders, not screenshots.

## Editable Mermaid source

| Source | Topic |
|---|---|
| [Job and runner isolation](architecture/job-runner-isolation.mmd) | Workflow hierarchy and separate workspaces |
| [Parallel jobs and dependencies](architecture/parallel-and-needs.mmd) | prepare, parallel-check, report |
| [Final integration architecture](architecture/final-integration.mmd) | Integration challenge dependencies |
| [Step and job outputs](implementation/output-data-flow.mmd) | GITHUB_OUTPUT to downstream job |
| [Artifact lifecycle](implementation/artifact-lifecycle.mmd) | Upload, isolated runners, download |
| [Logs, summary and artifacts](implementation/log-summary-artifact.mmd) | Purpose of three output mechanisms |
| [Matrix expansion](workflows/matrix-expansion.mmd) | Python matrix variants |
| [Status functions](workflows/status-functions.mmd) | Failure, success, always, skipped job |
| [Concurrency and timeouts](workflows/concurrency-timeout.mmd) | Cancellation and bounded jobs |
| [Push to Actions lifecycle](workflows/push-to-actions.mmd) | Local Git through Actions inspection |
| [Debugging decision tree](troubleshooting/debugging-decision-tree.mmd) | First-failure investigation |

## Preserved instructional SVG illustrations

| Image | Learning use |
|---|---|
| [Workflow/jobs YAML anatomy](diagrams/step-workflow-jobs.svg) | Read a workflow and its job/step hierarchy |
| [Multiple job architecture](diagrams/multiple-job-architecture.svg) | Relate course files, runner jobs, and artifacts |
| [Parallel jobs](diagrams/parallel-jobs.svg) | Visualize independent checks and a dependent report |
| [Sequential needs](diagrams/sequential-needs.svg) | See prerequisite ordering |
| [Output passing](diagrams/workflow-output-passing.svg) | Trace output expressions |
| [Artifact lifecycle](diagrams/artifact-lifecycle.svg) | Understand file upload/download across runners |
| [Artifact and summary implementation](diagrams/step-artifact-summary.svg) | Connect a generated file, artifact, and summary |
| [Matrix strategy](diagrams/matrix-strategy.svg) | Read a matrix definition and expanded jobs |
| [Matrix/status illustration](diagrams/step-matrix-status.svg) | Compare matrix executions and status checks |
| [Parallel graph (legacy generalized example)](diagrams/job-dependency-graph.svg) | Supplemental fan-in graph with different example job names |

## Screenshot capture prompts

Each SVG in [screenshots](screenshots/) named PLACEHOLDER is explicitly a placeholder card, not a screenshot. The exact page, evidence, file name, and capture integrity rules are in the [genuine screenshot guide](screenshots/README.md).

Genuine GitHub Actions, editor, and terminal screenshots are not currently included because no learner practice-run evidence is available. Do not treat diagrams or placeholder cards as proof of a successful run.
