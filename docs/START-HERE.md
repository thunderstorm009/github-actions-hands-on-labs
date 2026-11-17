# Start Here

Welcome. Follow the course in order; you do not need prior Actions experience. Learning material lives in this repository, while your experiments belong in a separate repository you own.

## 1. Install and verify tools

Install [Git](https://git-scm.com/downloads), [VS Code](https://code.visualstudio.com/download), and create a [GitHub account](https://github.com/signup). On macOS/Linux, open Terminal; on Windows, open PowerShell. Run `git --version`. Install Docker Desktop only before Labs 03/05; verify with `docker --version` and `docker info` (Docker Desktop must be running). Install Python 3.11+ for Lab 05 and verify `python --version` (Windows may use `py --version`).

## 2. Clone the course and open it

In a terminal, choose a parent folder, then run:

```sh
git clone https://github.com/thunderstorm009/github-actions-hands-on-labs.git
cd github-actions-hands-on-labs
code .
```

If `code` is unavailable, open VS Code and choose **File → Open Folder**. The Explorer lists course files. Use **Terminal → New Terminal** to run commands. See [VS Code setup](VS-CODE-SETUP.md).

## 3. Create a separate practice repository

On GitHub, use **New repository**, name it `github-actions-lab`, choose public or private, and do not initialize it with a README if you plan to push an existing local folder. Copy the practice files of the current lab to a separate folder, open that folder in VS Code, and in its terminal run `git init -b main`, `git add .`, `git commit -m "Start lab 01"`, then add your repository URL with `git remote add origin https://github.com/YOUR-USERNAME/github-actions-lab.git` and push using `git push -u origin main`. Replace the username. Do not point this practice clone at the course remote.

For Lab 01, the checked-in sample is under `01-introduction-to-github-actions/`. Copy its `.github/workflows/basic-checkout.yml` into the root of your practice repository under `.github/workflows/`. Workflows must be in that exact path relative to a repository root.

## 4. Learn, run, inspect

Read the lab from top to bottom. Each command says where and in which folder to run it. Push the workflow, open your practice repository on GitHub, select **Actions**, open the run, then select a job and step to read logs. Follow the verification and troubleshooting sections before moving on. Mark progress in the root README or `docs/PROGRESS.md` locally; these notes need not be pushed.
