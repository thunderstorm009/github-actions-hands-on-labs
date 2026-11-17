# Job outputs and artifacts

## Outputs: small values

1. Give a step a stable ID.
2. Append name=value to the runner-provided file at $GITHUB_OUTPUT.
3. Map the step output in the producing job's outputs.
4. Read it in a dependent job with needs.producer.outputs.name.

Outputs are useful for a short version string, label, or boolean-like value. Do not use them to transfer files or secrets.

## Artifacts: files

Use actions/upload-artifact to persist selected files after one job ends and actions/download-artifact in another job. The artifact name must match; the consumer must wait for the producer. Artifact retention follows repository policy and can be shortened with retention-days.

Artifacts are not a secret store. Never upload tokens, private keys, environment files, or sensitive reports.

## Summary: readable Markdown

Append Markdown to $GITHUB_STEP_SUMMARY to display a concise report on the run summary page. Keep detailed command output in logs and downloadable files in artifacts. See [workflow commands](https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions) and [storing workflow data](https://docs.github.com/en/actions/using-workflows/storing-workflow-data-as-artifacts).
