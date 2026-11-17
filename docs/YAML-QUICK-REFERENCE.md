# YAML quick reference

```yaml
name: Example
on:
  push:
    branches: [main]
  workflow_dispatch:
permissions:
  contents: read
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v6
      - name: Say hello
        run: echo "Hello, ${{ github.repository }}"
```

Indentation defines nesting; use spaces, never tabs. `on` declares events, `jobs` contains independently scheduled jobs, `steps` run in order inside a job. `uses` calls an action; `run` executes shell commands. `${{ ... }}` evaluates an Actions expression. Quote YAML strings that contain punctuation or values that might be parsed as booleans. Pin actions to reviewed full commit SHAs for sensitive production workflows; version tags are easier for teaching and updates. See [official syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax).
