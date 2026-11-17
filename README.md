# GitHub Actions Hands-On Labs

*Learn GitHub Actions from your first workflow to real-world CI/CD pipelines.*

A practical, step-by-step course for building and understanding automation on GitHub. Every example is original; illustrative outputs are labeled and screenshots of real runs are not fabricated.

## Start learning

New to the repository? Begin with [Start Here](docs/START-HERE.md), then work through the five core labs in order. Estimated core time: **14–18 hours**. Optional advanced labs add **4.5–5.5 hours**. Beginners may need extra time to install tools and repeat exercises.

| Lab | Topic | Time | Level | Path |
|---|---|---:|---|---|
| 01 | Introduction to GitHub Actions | 2–2.5 h | Beginner | [Open Lab 01](01-introduction-to-github-actions/README.md) |
| 02 | Multiple Jobs and Workflow Data | 2.5–3 h | Beginner–Intermediate | [Open Lab 02](02-multiple-jobs-and-workflow-data/README.md) |
| 03 | GitHub Actions with Docker and NGINX | 3–3.5 h | Intermediate | [Open Lab 03](03-github-actions-docker-nginx/README.md) |
| 04 | Self-Hosted GitHub Actions Runner | 2.5–3 h | Intermediate–Advanced | [Open Lab 04](04-self-hosted-github-actions-runner/README.md) |
| 05 | Building a CRUD Application CI/CD Pipeline | 4–5 h | Advanced | [Open Lab 05](05-crud-application-cicd/README.md) |

### Optional advanced path

| Lab | Topic | Time | Path |
|---|---|---:|---|
| 06 | Security, Secrets and Permissions | 2–2.5 h | [Open Lab 06](06-github-actions-security/README.md) |
| 07 | Reusable Workflows, Custom Actions and Releases | 2.5–3 h | [Open Lab 07](07-reusable-workflows-and-releases/README.md) |

## What you will build and learn

Start with a push-triggered workflow; then orchestrate jobs and artifacts, test a Dockerized NGINX website, operate a safely isolated self-hosted runner, and build/test/package a Flask CRUD API. Advanced labs cover least privilege, reusable workflows, composite actions and releases. You will learn events, runners, YAML, expressions, logs, matrices, caching, testing, secrets and safe automation.

## Prerequisites

A computer, internet access, Git, VS Code and a GitHub account. Docker is required for Lab 03 and the container part of Lab 05. No paid cloud account is needed. See [setup from zero](docs/START-HERE.md), [VS Code setup](docs/VS-CODE-SETUP.md), and the [roadmap](docs/LEARNING-ROADMAP.md).

## Progress

- [ ] Lab 01
- [ ] Lab 02
- [ ] Lab 03
- [ ] Lab 04
- [ ] Lab 05
- [ ] Optional Lab 06
- [ ] Optional Lab 07

## Use the course safely

This repository is the course material. For hands-on pushes, make a **separate personal practice repository** and copy or recreate the lab files there. Never push learner changes into the course repository. Read [security best practices](docs/SECURITY-BEST-PRACTICES.md) before using secrets or self-hosted runners.

## Navigate

- [Command cheatsheet](docs/COMMAND-CHEATSHEET.md) · [YAML quick reference](docs/YAML-QUICK-REFERENCE.md)
- [Workflow debugging](docs/WORKFLOW-DEBUGGING.md) · [Common errors](docs/COMMON-WORKFLOW-ERRORS.md)
- [Glossary](docs/GITHUB-ACTIONS-GLOSSARY.md) · [Lab template](docs/templates/LAB-TEMPLATE.md)
- [Contributing](CONTRIBUTING.md) · [Tasks](TASKS.md)

Lab pages include diagrams and a screenshot index. Repository screenshots are labeled placeholders until captured from real executions; no placeholder claims to show a successful run. Official [GitHub Actions documentation](https://docs.github.com/en/actions) is the technical source of truth.

## Contribute

Found a confusing step or want to add a challenge? Start with [CONTRIBUTING.md](CONTRIBUTING.md), reproduce commands in a clean practice repository, and include genuine evidence or a clearly labeled placeholder.
