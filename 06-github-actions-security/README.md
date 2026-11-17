# Optional Lab 06 — GitHub Actions Security, Secrets and Permissions

Configure workflows to do only what they need. `GITHUB_TOKEN` is a short-lived, repository-scoped credential; actions may access it through context even when it is not visibly passed. Permissions at workflow/job level narrow access. Secrets are encrypted at rest but become available to steps that reference them; masking is not a defense against intentional transformations or exfiltration.

## Estimated time

| Activity | Duration |
|---|---:|
| Threat concepts | 35 min |
| Configure workflow/settings | 30 min |
| Exercises | 45 min |
| Inspect and debug | 25 min |
| Review and cleanup | 15 min |
| **Total** | **2 h 30 min** |

Prerequisite: Lab 01 and admin access to a practice repo. Copy the example workflow. Observe that it declares `contents: read`, scopes job permissions and checks a dummy secret only for presence. Never echo its value. To test, set a fake value as repository secret `DEMO_VALUE`; remove it after. The workflow must not print the value.

Topics to investigate: repository and environment secrets, environment protection rules/approvals, fork PR restrictions, untrusted expressions/script injection, action SHA pinning, dependency updates and OIDC short-lived cloud identity. `pull_request_target` runs with base-repository trust; never combine it with checking out and executing untrusted fork code. Compare the deliberately dangerous shape in GitHub's security guidance rather than running it.

Exercises: narrow permission; configure a dummy secret; add a protected environment without deploying. Challenges: audit every action and justify permissions; replace a vulnerable string interpolation in shell with an environment variable. Questions: why least privilege? What does masking fail to guarantee? Why are fork PRs different? What is action SHA pinning? What problem does OIDC solve? Debug exercise: remove required contents read and inspect checkout error, then restore. Integration: safe read-only PR workflow and gated deployment design using fake credentials. Hints: quote shell variables, don't expose values, keep secret access out of PR tests.

Security: never use production secrets for this exercise. `pull_request_target` risks, script injection and self-hosted runner host access can turn untrusted input into credential theft. Remove dummy secret after practice. Further reading: [security hardening](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions), [token permissions](https://docs.github.com/en/actions/tutorials/authenticate-with-github_token), [secure pull_request_target](https://docs.github.com/en/actions/reference/security/securely-using-pull_request_target), [OIDC](https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect). Continue to [Lab 07](../07-reusable-workflows-and-releases/README.md).

## Screenshot index

Use genuine, redacted screenshots for permissions, dummy secret presence check and environment approval settings. Never show the secret value.
