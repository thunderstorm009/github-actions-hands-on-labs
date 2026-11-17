# Genuine screenshot plan

Capture the actual local build, `docker ps`/logs and browser at localhost:8080. Separately capture the Actions runner curl step. Runner-localhost output is not a laptop browser screenshot.

These captures are intentionally absent until produced from the real app/terminal/GitHub run. Do not draw, synthesize, or label a conceptual UI illustration as a screenshot. The SVG illustrations live separately in `../diagrams/`.

| Filename | Application and exact page/command | What must be visible |
|---|---|---|
| `01-vscode-file-tree.png` | Your IDE project/file explorer or editor | Practice project path and relevant source; no hidden credentials. |
| `02-docker-build-terminal.png` | Real local terminal at the stated lab directory | Command and unedited output; IDs and local usernames may be redacted. |
| `03-docker-ps-and-logs.png` | Real local terminal at the stated lab directory | Command and unedited output; IDs and local usernames may be redacted. |
| `04-local-nginx-browser.png` | Browser at local app URL or real GitHub Releases page | Actual rendered response or release/tag details. |
| `05-actions-http-smoke-test.png` | Practice repository GitHub Actions tab → actual run → job/step | Run status and exact named job/step output; not a mocked UI. |

## Capture procedure

1. Perform the corresponding lab step in your own practice repository. 2. Open the exact page/terminal named in the table. 3. Capture the screen with your operating-system screenshot tool or browser screenshot command. 4. Crop only irrelevant desktop space; do not alter outputs. 5. Redact tokens, secret values, emails and private repo data before adding. 6. Add a caption in the lab README explaining what success/failure signal it demonstrates.
