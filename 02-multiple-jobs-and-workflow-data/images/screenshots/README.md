# Genuine screenshot capture guide

The repository contains conceptual diagrams, not GitHub execution screenshots. Capture images only after running workflows in your separate practice repository. Never recreate GitHub UI as an illustration and label it a screenshot. Do not include secrets, account email, private repository details, or personal access tokens.

| Suggested filename | Exact page or action | Learning evidence |
|---|---|---|
| workflow-files-in-editor.png | Any IDE, open practice repo root and .github/workflows/multiple-jobs.yml | Correct root folder and readable YAML; hide unrelated desktop content. |
| parallel-job-graph.png | Practice repo → Actions → Multiple jobs and workflow data → run summary | Actual graph showing prepare and parallel-check independent, report dependent. |
| prepare-output-and-upload.png | Same run → prepare job logs | Output step and successful lab-result artifact upload. |
| report-download-and-summary.png | Same run → report job logs, then run summary | Download step, report contents, rendered Markdown summary. |
| matrix-variants.png | Actions → Python matrix → actual run graph | Three execution names and selected Python version logs. |
| intentional-failure.png | Actions → manually triggered conditional workflow | Red fails-on-purpose job and diagnostic step; run is intentionally red. |
| repaired-success.png | Main workflow after restoring a deliberately broken example | New successful run after repair. |
| final-integration-graph.png | Practice repo → final challenge run | Real dependency graph and job summaries. |

Capture with the operating system screenshot utility or browser screenshot feature. Crop irrelevant desktop area only; do not alter text/status or synthesize interface elements. Redact private data before committing. Place screenshots beside matching README instructions. These captures are learner-generated evidence and should not be committed unless they contain no personal or private information.
