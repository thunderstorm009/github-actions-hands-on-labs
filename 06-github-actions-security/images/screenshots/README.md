# Genuine screenshot plan

Capture permission configuration and the secret presence-only log. Never include the dummy value itself. Redact repository and identity details if desired.

These captures are intentionally absent until produced from the real app/terminal/GitHub run. Do not draw, synthesize, or label a conceptual UI illustration as a screenshot. The SVG illustrations live separately in `../diagrams/`.

| Filename | Application and exact page/command | What must be visible |
|---|---|---|
| `01-read-only-permissions.png` | Practice repository Settings page | Relevant setting; redact private info and all secret/token values. |
| `02-dummy-secret-presence-only.png` | Practice repository GitHub Actions tab → actual run → job/step | Run status and exact named job/step output; not a mocked UI. |
| `03-environment-protection.png` | Practice repository Settings page | Relevant setting; redact private info and all secret/token values. |
| `04-read-only-pr-run.png` | Practice repository GitHub Actions tab → actual run → job/step | Run status and exact named job/step output; not a mocked UI. |

## Capture procedure

1. Perform the corresponding lab step in your own practice repository. 2. Open the exact page/terminal named in the table. 3. Capture the screen with your operating-system screenshot tool or browser screenshot command. 4. Crop only irrelevant desktop space; do not alter outputs. 5. Redact tokens, secret values, emails and private repo data before adding. 6. Add a caption in the lab README explaining what success/failure signal it demonstrates.
