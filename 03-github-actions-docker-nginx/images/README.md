# Lab 03 visual asset index

The lab intentionally uses two distinct kinds of visuals:

- **Concept diagrams** explain architecture, data flow, or Docker relationships.
- **Screenshot prompt cards** are clearly labeled instructions for capturing genuine evidence after a learner performs a step. They are not screenshots and do not prove execution.

The main [Lab 03 README](../README.md) places these visuals beside their related instructions. Historical useful diagrams are retained even where a newer diagram is now the primary visual.

## Architecture

| Asset | What it teaches |
|---|---|
| [system-architecture.svg](architecture/system-architecture.svg) | Separate secret-free pull-request CI and trusted Docker Hub publishing lanes. |
| [nginx-http-flow.svg](architecture/nginx-http-flow.svg) | Browser request, NGINX listener, document root, index file, and response. |
| [image-container-lifecycle.svg](architecture/image-container-lifecycle.svg) | Dockerfile build, reusable image, running container, stop, and remove. |
| [local-port-mapping.svg](architecture/local-port-mapping.svg) | Host port 8000 forwarding to container port 80. |

## Implementation

| Asset | What it teaches |
|---|---|
| [project-structure.svg](implementation/project-structure.svg) | The files learners create in their practice repository and which are Docker build inputs. |
| [dockerfile-build-context.svg](implementation/dockerfile-build-context.svg) | Build context, `.dockerignore`, Dockerfile instructions, copy destinations, and image result. |
| [nginx-config-map.svg](implementation/nginx-config-map.svg) | How the NGINX config directives and Dockerfile copy destinations work together. |

## Workflow diagrams

| Asset | What it teaches |
|---|---|
| [github-actions-ci-flow.svg](workflows/github-actions-ci-flow.svg) | Pull request → hosted runner → checkout/build → HTTP test → cleanup. |
| [dockerhub-secret-handling.svg](workflows/dockerhub-secret-handling.svg) | Secret boundary from GitHub repository settings to the Docker login action. |
| [dockerhub-publish-flow.svg](workflows/dockerhub-publish-flow.svg) | Build and test before login, then push `latest` and commit-SHA tags. |
| [complete-cicd-journey.svg](workflows/complete-cicd-journey.svg) | Full developer-to-registry journey with distinct CI and publish triggers. |

## Troubleshooting

| Asset | What it teaches |
|---|---|
| [first-failure-diagnostic.svg](troubleshooting/first-failure-diagnostic.svg) | Inspect the earliest failing stage, gather container diagnostics, fix, and rerun. |

## Preserved diagrams from earlier Lab 03 versions

These are kept to preserve existing learning material. The README links the ones that add detail at the relevant steps. Where an older illustration differs from the current implementation, the README identifies it and points to the current source files as authoritative.

| Asset | Notes |
|---|---|
| [browser-nginx-request-flow.svg](diagrams/browser-nginx-request-flow.svg) | Earlier browser and NGINX request illustration. |
| [container-networking.svg](diagrams/container-networking.svg) | Restored from Git history; explains local and runner network boundaries. |
| [docker-architecture.svg](diagrams/docker-architecture.svg) | Earlier Dockerfile → image → container illustration. |
| [docker-build-run-lifecycle.svg](diagrams/docker-build-run-lifecycle.svg) | Restored from Git history; build and run lifecycle. |
| [ghcr-publishing-flow.svg](diagrams/ghcr-publishing-flow.svg) | Historical optional GHCR illustration. This Lab 03 publishes to Docker Hub; this diagram is not its publishing workflow. |
| [github-actions-docker-ci.svg](diagrams/github-actions-docker-ci.svg) | Restored from Git history; CI build and HTTP check sequence. |
| [port-mapping.svg](diagrams/port-mapping.svg) | Restored from Git history; host/container port mapping. |
| [runner-docker-engine.svg](diagrams/runner-docker-engine.svg) | Restored from Git history; hosted runner and its Docker engine. |
| [step-container-inspect-cleanup.svg](diagrams/step-container-inspect-cleanup.svg) | Earlier status, log, and cleanup command illustration. |
| [step-dockerfile-anatomy.svg](diagrams/step-dockerfile-anatomy.svg) | Earlier Dockerfile illustration, authored for an older image tag; use the README's current Dockerfile as source of truth. |
| [step-local-docker-commands.svg](diagrams/step-local-docker-commands.svg) | Earlier local build/run/test command illustration. |
| [step-runner-http-check.svg](diagrams/step-runner-http-check.svg) | Earlier runner smoke-test illustration. |

## Instructional screenshot prompts

The [screenshot capture guide](screenshots/README.md) lists all 19 prompt cards, says exactly which application/page or command to capture, and identifies the visible evidence to show. Every card is named `PLACEHOLDER-...` and visually labeled as a placeholder. Replace a card reference with a genuine, sanitized screenshot only after completing that step. Never create synthetic terminal output, workflow status, Docker Hub state, or editor captures.
