# Visual coverage audit

This checklist distinguishes conceptual drawings and annotated output illustrations from genuine screenshots. All diagrams are original editable SVGs. The diagrams are embedded beside relevant explanations in each lab README; `images/README.md` inventories files without duplicating a gallery at the lesson end.

| Lab | Architecture/concepts | File/configuration | Execute/verify/debug | Genuine screenshot status |
|---|---|---|---|---|
| 01 Introduction | Event/workflow/runner Mermaid, runner comparison, lifecycle | Practice path, Explorer sequence, YAML anatomy illustrations | Git sequence, Actions navigation map, success/failure paths | Real public repository page and course-check run summary. Learner `basic-checkout.yml` run, logs and failure remain capture cards. |
| 02 Multiple jobs | Job dependency graph | Parallel scheduling, `$GITHUB_OUTPUT`, artifact/summary, matrix/status illustrations | Workflow instructions state graph/log locations and expected values | Lab-specific graph, artifacts, matrix and summary captures remain capture cards. |
| 03 Docker + NGINX | Docker image/container and browser request/port diagrams | Dockerfile and `.dockerignore` anatomy | Build/run commands, curl/browser/log/cleanup, runner smoke-test illustrations | Local Docker/browser and lab Actions captures remain capture cards. |
| 04 Self-hosted runner | Control plane/host boundary and trust diagram | Settings navigation, label/token-safe setup illustrations | Online/idle dispatch, job assignment, removal lifecycle | Practice Settings, job logs and removal captures remain capture cards; token never shown. |
| 05 CRUD pipeline | Flask components, CRUD/API flows, database/test diagrams | Project tree and Python environment commands | Verified local pytest/Ruff illustration, API/Docker and CI workflow illustrations | API, Docker and lab-specific Actions captures remain capture cards. |
| 06 Security | Permission, secret, PR trust, least privilege, OIDC | Read-only and dummy-secret configuration illustrations | Safe/insecure pattern comparison and secret presence check | Redacted Settings and practice workflow captures remain capture cards. |
| 07 Reuse/releases | Caller/callee, input/output, action and release diagrams | `workflow_call` contract and `action.yml` annotation | Tag/release command illustration and expected output instructions | Practice run and actual release captures remain capture cards; no release is claimed. |

## Actual capture provenance

- `01-introduction-to-github-actions/images/screenshots/course-repository-page.png` is a real Chrome headless capture of the public repository page.
- `01-introduction-to-github-actions/images/screenshots/course-checks-actions-run.png` is a real Chrome headless capture of the public run summary at [run 44068246516](https://github.com/thunderstorm009/github-actions-hands-on-labs/actions/runs/44068246516). GitHub's public page showed the successful job graph; the run's Jobs API independently showed each test, lint, SVG and link-validation step completed successfully. This validates the course repository, not any lab workflow in a learner's practice repository.
- Lab 05's pytest and Ruff output illustration reflects commands actually run locally. It is explicitly not a screenshot and not GitHub execution evidence.

All other screenshot cards state the target application/page/command, required visible signal and capture procedure. A missing genuine capture is labeled as unavailable rather than simulated.
