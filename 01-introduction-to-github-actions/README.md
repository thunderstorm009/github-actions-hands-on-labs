# Lab 01 — Introduction to GitHub Actions

Your first automated workflow checks out code, inspects the runner and reports results in GitHub. Actions is GitHub's automation platform: an event such as a push starts a workflow, which schedules jobs on runners. CI repeatedly checks changes; CD automates delivery or deployment. A workflow is YAML; jobs contain ordered steps; steps call actions or shell commands.

## Estimated time

| Activity | Duration |
|---|---:|
| Concepts | 25 min |
| Environment setup | 20 min |
| Workflow implementation | 35 min |
| Push and inspect | 20 min |
| Debugging | 20 min |
| Practice | 20 min |
| **Total** | **2 h 20 min** |

Beginners may need longer, especially for Git setup.

## Objectives and concepts

Recognize events (`push`, `pull_request`, manual `workflow_dispatch`), workflow files, YAML indentation, jobs, steps, runners, `runs-on`, expressions, contexts, environment variables, conditions, logs and exit codes. `ubuntu-latest` is a moving label whose hosted image changes over time; use a fixed label when reproducibility matters. GitHub-hosted runners are temporary remote machines, unlike your VS Code terminal. Self-hosted runners are machines you manage and secure (Lab 04).

```mermaid
flowchart LR
  A[Push to main / PR / manual] --> B[GitHub schedules job]
  B --> C[Ubuntu hosted runner]
  C --> D[checkout action]
  D --> E[Shell steps]
  E --> F[Logs and exit status in Actions tab]
```

## Prerequisites

Git, VS Code, GitHub account and internet. Follow [Start Here](../docs/START-HERE.md). On macOS/Linux use Terminal; on Windows use PowerShell or Git Bash. Create a *separate* practice repository named `github-actions-lab`; do not edit/push this course repo for exercises.

## Implementation

### Step 01 — Create and clone a practice repository

**Objective:** make a personal remote to receive your experiment. **Where:** GitHub website, then your computer terminal. Create an empty repository, then clone it. **Command:** `git clone https://github.com/YOUR-USERNAME/github-actions-lab.git` then `cd github-actions-lab`; **Working directory:** the parent folder for the clone. **Expected output:** `Cloning into 'github-actions-lab'...`; exact progress differs. Open the folder in VS Code (**File → Open Folder**), then **Terminal → New Terminal**. Run `git config --global user.name "Your Name"` and `git config --global user.email "you@example.com"`; these configure identity on your computer (choose the email you want on commits). `git config --get user.name` and `git config --get user.email` verify them. To avoid changing global config, run those commands without `--global` inside this practice repository. **Troubleshooting:** ensure the GitHub repository is empty and your account can authenticate. **Next:** create workflow path.

### Step 02 — Create the workflow file

**Objective:** put the sample under the required repository path. **Where:** VS Code Explorer; use New Folder twice to create `.github/workflows`, then New File. **File path:** `.github/workflows/basic-checkout.yml` relative to your *practice repository root*. **Content to paste:** copy the complete [`basic-checkout.yml`](.github/workflows/basic-checkout.yml) shown below. The hidden `.github` directory is normal; type the leading dot.

```yaml
name: Basic checkout
on:
  push:
    branches: [main]
  pull_request:
  workflow_dispatch:
permissions:
  contents: read
jobs:
  inspect:
    name: Inspect the repository on Ubuntu
    runs-on: ubuntu-latest
    steps:
      - name: Check out this commit
        uses: actions/checkout@v6
      - name: List repository files
        run: ls -la
      - name: Show system and tool versions
        run: |
          echo "Runner OS: $RUNNER_OS"
          uname -a
          node --version
          python3 --version
          git --version
      - name: Set and read a custom environment variable
        env:
          LAB_GREETING: Hello from the workflow
        run: echo "$LAB_GREETING"
      - name: Run only on main branch
        if: github.ref == 'refs/heads/main'
        run: echo "This run is on main"
```

**Code explanation:** `on` selects events; `workflow_dispatch` adds a Run workflow button. `permissions` limits the automatic `GITHUB_TOKEN` to read repository contents. `jobs.inspect` is an ID; `runs-on` chooses the runner. `checkout@v6` downloads the triggering commit into the remote runner workspace (the action's current version is checked against its official release page when this course was prepared; use maintained releases). Each `run` is a shell command. `|` preserves a multiline script. `env` sets a value for one step. `github.ref` is a context; `if` skips the final step outside main. Failed commands generally return nonzero exit codes, failing the step/job.

### Step 03 — Commit and push

**Where:** VS Code integrated terminal. **Working directory:** practice repository root (`pwd` or PowerShell `Get-Location`). Execute:

```sh
git status
git add .github/workflows/basic-checkout.yml
git commit -m "Add basic GitHub Actions workflow"
git push -u origin main
```

**Example output:** status lists the new file as untracked; commit reports one file changed; push reports `main -> main`. Names and commit IDs vary. If the branch is `master`, rename with `git branch -M main` before pushing. Git identity missing? rerun the config commands from Step 01. **Security:** never put credentials in workflow YAML or print environment variables wholesale.

### Step 04 — Inspect the run

**Where:** browser, your practice repo → **Actions** → **Basic checkout** → newest run → `Inspect the repository on Ubuntu` → individual step. A push to `main` creates a run; a pull request also creates a run. GitHub's runner runs the commands remotely. Success is a green check and each step marked completed. The file listing and OS/tool versions appear in their logs; timestamps and versions may vary because `ubuntu-latest` moves. **Verification:** use the Actions job graph and compare each step to the YAML. A missing workflow usually means wrong path, extension, branch or no push. Confirm Actions is enabled and that workflow is in the repository's default branch.

### Step 05 — Practice a controlled failure

In the practice repo, temporarily change `node --version` to `node --version-invalid`, commit and push. The version step fails and later steps are skipped. Read the first red step's log, restore the command, commit and push again. This demonstrates failure through exit status; don't create a failure in a production workflow.

## Detailed outputs and screenshots

**Example output** for the version step includes `Runner OS: Linux`, a kernel string, Node/Python/Git version lines and `Hello from the workflow`. These are illustrative and vary by runner image. In Actions, event name and commit SHA identify the trigger and code revision. `images/` includes a screenshot index with explicit placeholders: no real GitHub execution screenshot is supplied in this source checkout, so none is presented as evidence. Capture your own screenshots of Explorer, YAML, terminal, run graph, step logs and failure/success in your practice repository.

## Exercises

**Guided:** (1) Add `date -u` on the runner. (2) Add `df -h` to display disk space. (3) Add `echo "Repo: ${{ github.repository }}"`. Hints: add a named step under `steps`; expressions use `${{ }}`. **Independent:** add a manual-only workflow step gated on `github.event_name`; show runner OS and repository name. **Concept questions:** What starts a workflow? Where does `run` execute? What does checkout do? Why can `ubuntu-latest` change? What indicates command failure? **Debugging:** intentionally misspell `runs-on`, inspect the annotation, restore it. **Integration challenge:** build a workflow triggered by push, PR and manual dispatch that prints repo, branch/ref and UTC date, with `contents: read`. **Solutions:** `date -u`, `df -h`, and `echo "Repo: ${{ github.repository }}"`; manual gate `if: github.event_name == 'workflow_dispatch'`. Do not print secrets or dump contexts wholesale.

## Troubleshooting, security and cleanup

Workflow absent: check `.github/workflows/*.yml`, branch filters, push, Actions tab/settings. `node` missing: confirm Linux hosted runner label. YAML error: spaces and indentation. A local command works but runner fails: they are different environments. Do not enable verbose debug logging that could expose values; add targeted safe diagnostics. This lab creates no long-lived infrastructure; optionally delete the practice repository after saving your notes.

## Further reading and next lab

[Actions overview](https://docs.github.com/en/actions), [workflow syntax](https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax), [hosted runners](https://docs.github.com/en/actions/how-tos/manage-runners/github-hosted-runners), [checkout releases](https://github.com/actions/checkout/releases). Continue to [Lab 02](../02-multiple-jobs-and-workflow-data/README.md) to coordinate jobs and move data.
