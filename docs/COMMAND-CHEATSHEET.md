# Command cheatsheet

| Task | macOS/Linux/Git Bash | Windows PowerShell |
|---|---|---|
| Show folder | `pwd` | `Get-Location` |
| List files | `ls -la` | `Get-ChildItem -Force` |
| Make folders | `mkdir -p .github/workflows` | `New-Item -ItemType Directory -Force .github/workflows` |
| Git version | `git --version` | `git --version` |
| Status | `git status` | `git status` |
| Stage and commit | `git add . && git commit -m "message"` | `git add .; git commit -m "message"` |
| Push | `git push -u origin main` | `git push -u origin main` |

Run Git commands from the practice repository root unless directed otherwise. Never paste tokens into commands that may be saved in shell history.
