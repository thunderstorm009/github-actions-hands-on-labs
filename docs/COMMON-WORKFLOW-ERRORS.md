# Common workflow errors

- **Workflow missing:** file is not under `.github/workflows/`, extension is invalid, or the change was not pushed to the expected repository/branch. Confirm Actions is enabled.
- **YAML parse error:** align indentation with spaces; check colons, quoting and list markers.
- **No runs appear:** check the event filters and branch name; `workflow_dispatch` requires the workflow on the default branch and a manual run from Actions.
- **Command not found:** verify runner OS and installed tools; a local tool is not automatically available on the runner.
- **Permission denied:** declare only the specific `permissions` required; repo settings may restrict token rights.
- **Artifact not found:** ensure upload completed, artifact name matches, and downloader job depends on uploader.
- **Docker daemon unavailable locally:** start Docker Desktop and check `docker info`.
- **Self-hosted job queued:** runner must be online and match all requested labels.

Inspect the first failing step and consult [debugging](WORKFLOW-DEBUGGING.md).
