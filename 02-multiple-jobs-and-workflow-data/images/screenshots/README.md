# Genuine screenshot capture guide

This lab deliberately separates conceptual diagrams, illustrative SVGs, placeholder cards, and genuine screenshots. The files named PLACEHOLDER-*.svg are capture prompts only: they do not depict GitHub, an IDE, a log, or a workflow result. Replace none of these with a mocked interface. Capture genuine evidence in your own practice repository and save sanitized screenshots beside the cards.

| Suggested genuine image | Where to capture | What the screenshot must show |
|---|---|---|
| workflow-files-in-editor.png | Any IDE/editor; open the practice repo and .github/workflows/multiple-jobs.yml | Real project path, trigger, jobs, and readable YAML indentation. |
| practice-repository-structure.png | Any IDE/editor Explorer or file pane | Root .github/workflows and examples paths. |
| parallel-job-graph.png | Practice repo → Actions → Multiple jobs and workflow data → successful run summary | Actual graph showing prepare and parallel-check independent, report dependent. |
| dependency-job-logs.png | Same run → open prepare, parallel-check, and report jobs | Actual statuses and dependency behavior; execution order may vary. |
| output-step-and-consumer.png | Open prepare output step, then report output consumer step | Step runs and downstream log prints Hello from prepare. |
| artifact-upload-download.png | Open prepare upload-artifact step and report download-artifact step | Both successful logs and matching lab-result name. |
| job-summary-page.png | Return to the actual run summary page | Rendered Workflow data report and report file contents. |
| matrix-variants.png | Actions → Python matrix → actual run graph and one job log | All configured Python variants and the interpreter printed by one. |
| conditional-failure.png | Manually run Conditional jobs and status functions; inspect graph and observer logs | Intentionally red fails-on-purpose job, failure diagnostic, skipped success-only step, and summary. |
| failure-and-repair.png | Capture one intentionally broken main workflow run and the later repaired run | Two distinct, genuine captures showing first failure and successful repair. |
| final-integration-graph.png | Run integration-challenge.yml in practice repo → Actions | Actual prepare, lint, build, test matrix, report graph and run summary. |

Capture with your OS screenshot tool or browser screenshot feature. The practice repo can be public or a private repo you control; if private, confirm screenshots do not leak names, IDs, or code you should not share. Crop irrelevant desktop space only. Do not paint over, synthesize, or alter the status/log content. Redact private data before adding a capture to a public pull request.

Place each real PNG beside the corresponding placeholder and update the lab README to show the genuine PNG with a caption. Keep the PLACEHOLDER card only if no screenshot is available; label it as a prompt, never as evidence. See the [visual asset index](../README.md) for the distinction between diagrams and instructional imagery.
