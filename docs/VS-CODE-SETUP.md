# VS Code setup

Open a folder with **File → Open Folder**. The Explorer on the left shows repository files; click a file to edit. Create a directory or file with the Explorer's New Folder/New File buttons. YAML workflow files belong below `.github/workflows/` at the repository root.

Choose **Terminal → New Terminal**. The prompt shows the current folder; run `pwd` (macOS/Linux/Git Bash) or `Get-Location` (PowerShell) before commands. Use the terminal dropdown to select PowerShell, Command Prompt, bash or zsh. Commands are shell-specific when noted in a lab.

Recommended extensions are listed in `.vscode/extensions.json`: YAML, Docker, GitHub Actions, Python and Markdown. YAML uses two spaces per indentation level. Red underlines and Problems view help find syntax errors, but GitHub's workflow parser is the final check. Use Source Control to inspect changes; use terminal Git commands in the labs to learn what each operation does. To inspect remote execution, open the repository's **Actions** tab in a browser and drill into a run, job and step.
