# Lab 03 genuine screenshot guide

This directory contains SVG cards named PLACEHOLDER. They are instructional capture prompts, not screenshots and not proof that any command or workflow ran. No GitHub UI, Docker Hub page, editor, terminal, or successful result is fabricated.

After completing the step in your own practice repository, capture a real screen with your operating-system screenshot tool or browser capture feature. Save the PNG beside this guide using the suggested filename. Replace the placeholder image reference in the README with the genuine image only after reviewing it. Never capture a password, token, secret value, private key, or credential file.

| Suggested capture | Open this exact place | Show this evidence |
|---|---|---|
| 01-github-repository.png | GitHub → New repository | Repository creation and chosen public/private visibility. |
| 02-clone-repository.png | Terminal at projects parent | Real git clone command and completion. |
| 03-project-structure.png | IDE project pane at practice root | Dockerfile, nginx.conf, website and .github/workflows paths. |
| 04-edit-index-html.png | Editor → website/index.html | Page heading and NGINX_DOCKER_HUB_LAB_READY marker. |
| 05-edit-nginx-config.png | Editor → nginx.conf | Port 80, document root, index, /healthz and location block. |
| 06-write-dockerfile.png | Editor → Dockerfile | Base image, config/site COPY, EXPOSE and foreground CMD. |
| 07-docker-build.png | Terminal at practice root | Real docker build command and successful completion/tag. |
| 08-run-container.png | Terminal after docker run | Real container ID or docker ps status/port mapping. |
| 09-browser-page.png | Browser → http://localhost:8000 | Rendered page and unique marker. |
| 10-container-logs-status.png | Terminal after docker ps and docker logs lab-nginx | Actual Up state, published port and request log. |
| 11-workflow-files.png | Editor → .github/workflows | Both workflow files and branch triggers. |
| 12-configure-secrets.png | Practice repo Settings → Secrets and variables → Actions | Names only: DOCKER_USERNAME and DOCKER_PASSWORD. Never reveal values. |
| 13-dockerhub-repository.png | Docker Hub → Repositories → mynginx | Repository name and visibility; do not capture token panels. |
| 14-actions-ci-run.png | Practice repo Actions → Docker NGINX CI → real run | Event, status, job graph and test result. |
| 15-actions-step-logs.png | Real CI run → Build/Verify/Cleanup step | Actual runner output and HTTP assertion. |
| 16-dockerhub-publish.png | Real trusted main publish run → push step | Successful tags/push without credentials visible. |
| 17-dockerhub-tags.png | Docker Hub → mynginx → Tags | Actual latest and commit-SHA tags. |
| 18-pull-and-run.png | Terminal and browser → localhost:8001 | Real pull/run command and rendered page. |
| 19-troubleshooting.png | Real failed run and later repaired run | First error step and separate successful repair run. |

Crop irrelevant desktop area only. Do not redraw, synthesize, or alter terminal output or status indicators. Redact private account or repository information before a screenshot is committed publicly. Add a caption beside the image in the lab README explaining what success or failure signal it demonstrates.
