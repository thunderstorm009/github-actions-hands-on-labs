# Genuine screenshot plan

Capture in your own practice repository. The two current public captures show the course repository structure and the repository health-check run. Neither is execution of your personal practice workflow.

Learner-specific practice captures are intentionally absent until produced from the real app/terminal/GitHub run. Do not draw, synthesize, or label a conceptual UI illustration as a screenshot. The SVG illustrations live separately in `../diagrams/`.

| Filename | Application and exact page/command | What must be visible |
|---|---|---|
| `course-repository-page.png` | Chrome, public course repository home | Real repo name, public badge and lab folders; proves repository publication only. |
| `course-checks-actions-run.png` | Chrome, actual course Actions run summary | Shows green course-checks job for commit `31c732c`; not a Lab 01 practice run. |
| `01-ide-project.png` | Your IDE project/file explorer or editor | Practice project path and relevant source; no hidden credentials. |
| `02-workflow-yaml.png` | Your IDE project/file explorer or editor | Practice project path and relevant source; no hidden credentials. |
| `03-git-push-terminal.png` | Real local terminal at the stated lab directory | Command and unedited output; IDs and local usernames may be redacted. |
| `04-practice-actions-run.png` | Practice repository GitHub Actions tab → actual run → job/step | Run status and exact named job/step output; not a mocked UI. |
| `05-job-step-logs.png` | Practice repository GitHub Actions tab → actual run → job/step | Run status and exact named job/step output; not a mocked UI. |
| `06-failed-and-repaired-run.png` | Practice repository GitHub Actions tab → actual run → job/step | Run status and exact named job/step output; not a mocked UI. |

## Capture procedure

1. Perform the corresponding lab step in your own practice repository.
2. Open the exact page or terminal named in the table.
3. Capture it with the operating-system screenshot tool or a browser screenshot command.
4. Crop irrelevant desktop space only; do not alter outputs.
5. Redact tokens, secret values, emails and private repo details.
6. Add a README caption explaining which success or failure signal the screenshot demonstrates.
