# Set up your editor and terminal

VS Code is the screenshots-first walkthrough, but it is optional. The repository is made of plain text, YAML, Python, Docker and Markdown files. Any IDE or editor that can open a folder, create nested files and run terminal commands can complete the labs. Examples include VS Code, PyCharm, IntelliJ IDEA, Visual Studio, Vim/Neovim and other editors. Install a relevant language/YAML extension when your editor supports one; extensions improve feedback but are not needed to run the project.

## Open the project

Open the repository folder using your editor's **Open Folder/Open Project** command. The project/file explorer should show lab folders. Create folders relative to a lab's practice-repository root. For workflows, preserve `.github/workflows/` exactly. Some file explorers hide dot-folders; enable hidden files or create `.github` by typing the full name.

## Use a terminal

VS Code: **Terminal → New Terminal**. Other IDEs may offer **Terminal**, **Console** or **Run** panels. A system terminal works too: open it at the practice folder. Run `pwd` (macOS/Linux/Git Bash) or `Get-Location` (PowerShell) before commands to confirm location. Select bash/zsh, PowerShell or another shell as directed by a lab; the code itself is not tied to VS Code.

## Edit and inspect

Use Explorer/project pane to create files, select a file to edit and save before running. YAML uses spaces and consistent indentation; do not use tabs. An IDE's Problems panel can show syntax and lint errors. The terminal is the authoritative place to run `git`, Python and Docker commands. GitHub Actions logs are viewed in a browser under the practice repository's **Actions** tab, independent of the local IDE.

Recommended optional VS Code extensions are in `.vscode/extensions.json`: YAML, Docker, GitHub Actions, Python and Markdown. Equivalent plugins may help in other IDEs.
