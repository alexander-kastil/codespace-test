# DevContainer and Codespace Proxy Testing

This repository gives customers a minimal devcontainer (Python 3.12, Node 22, .NET 10) plus a GitHub Codespace to validate proxy behavior, port forwarding, and package downloads. Use it to confirm that outbound calls (pip/npm/nuget) and forwarded ports work end-to-end before onboarding larger projects.

## About DevContainers and Codespaces

Dev Containers define a reproducible development environment as code, so every contributor gets the same tools, runtimes, extensions, and settings without local setup drift.

> Note: If you wish you can examine the [.devcontainer/devcontainer.json](./.devcontainer/devcontainer.json).

GitHub Codespaces builds that environment in the cloud, letting new team members open the repo and start coding in minutes—no local installs required. Prebuilds can cache image creation and dependency installs to make the very first launch even faster. 

Together they reduce “works on my machine” issues, speed onboarding, and simplify collaboration across platforms.

[Codespaces Docs](https://docs.github.com/en/codespaces)

[DevContainers Docs](https://code.visualstudio.com/docs/devcontainers/containers)

## Forking and starting a Codespace (visual guide):

- Fork the repo (top right) to your org/user.

  ![Fork entry point](_images/fork-repo.png)

- Pick the fork owner/org and confirm. ![Fork dialog choose owner](_images/create-fork.png)

- In your fork, open Code ➜ Codespaces ➜ Create codespace on master to launch the devcontainer. ![Create Codespace on master](_images/codespace-start.png).
  
- On the first launch, Codespaces will build the container image and install dependencies. This may take several minutes.

- Then test package management and port forwarding:

  ```bash
  cd src/python-tester
  python -m venv .venv
  source .venv/bin/activate
  pip install -r requirements.txt
  uvicorn app:app --host 0.0.0.0 --port 8000
  ```

- Forward port 8000 when prompted.
- Use [src/python-tester/test-rest-call.http](src/python-tester/test-rest-call.http) to hit `/` via `Send Request`

  ![app-testing](./_images/port-forwarding.png)
