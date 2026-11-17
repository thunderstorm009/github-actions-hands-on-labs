# Genuine screenshot plan

Capture the called workflow graph and output only after a real run. Tag/release screenshots should show a tag/release actually created in a disposable practice repo.

These captures are intentionally absent until produced from the real app/terminal/GitHub run. Do not draw, synthesize, or label a conceptual UI illustration as a screenshot. The SVG illustrations live separately in `../diagrams/`.

| Filename | Application and exact page/command | What must be visible |
|---|---|---|
| `01-repository-layout.png` | Your IDE project/file explorer or editor | Practice project path and relevant source; no hidden credentials. |
| `02-reusable-workflow-graph.png` | Practice repository GitHub Actions tab → actual run → job/step | Run status and exact named job/step output; not a mocked UI. |
| `03-output-logs.png` | Practice repository GitHub Actions tab → actual run → job/step | Run status and exact named job/step output; not a mocked UI. |
| `04-tag-push.png` | Terminal in disposable practice repo | Tag command and successful remote update; no credentials. |
| `05-release-page.png` | Browser at local app URL or real GitHub Releases page | Actual rendered response or release/tag details. |

## Capture procedure

1. Perform the corresponding lab step in your own practice repository. 2. Open the exact page/terminal named in the table. 3. Capture the screen with your operating-system screenshot tool or browser screenshot command. 4. Crop only irrelevant desktop space; do not alter outputs. 5. Redact tokens, secret values, emails and private repo data before adding. 6. Add a caption in the lab README explaining what success/failure signal it demonstrates.
