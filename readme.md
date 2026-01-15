# codespace-test

This repository gives customers a minimal devcontainer (Python 3.12, Node 22, .NET 10) plus a GitHub Codespace to validate proxy behavior, port forwarding, and package downloads. Use it to confirm that outbound calls (pip/npm/nuget) and forwarded ports work end-to-end before onboarding larger projects.

![Codespace start menu](_images/codespace-start.png)

## 1) Fork this repo

- Open https://github.com/alexander-kastil/codespace-test.
- Select Fork (top right) and create the fork under your organization or user account.

## 2) Start a Codespace from the fork

- In your fork, choose Code ➜ Codespaces ➜ Create codespace on master (this uses [.devcontainer/devcontainer.json](.devcontainer/devcontainer.json)).
- Wait for the container build to finish; VS Code in the browser will open automatically inside the Codespace.
- Optional: If you prefer the desktop client, click the green “Open in VS Code” button once the Codespace is ready.

## 3) Quick proxy sanity checks

- Open a terminal in the Codespace and run: `python --version`, `node -v`, `dotnet --info` to confirm tool access through your proxy.
- Install something trivial to verify downloads through the proxy, e.g.: `pip install httpx` and `npm install left-pad` (the cache should populate without 407/timeout errors).

## 4) Run the bundled Python 3.12 REST tester

1. Go to the app folder and create a local venv (optional but recommended):
   ```bash
   cd src/python-tester
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
2. Install deps: `pip install -r requirements.txt`
3. Start the app: `uvicorn app:app --host 0.0.0.0 --port 8000`
4. Forward port 8000 when prompted.
5. Open [src/python-tester/test-rest-call.http](src/python-tester/test-rest-call.http) in VS Code (REST client) and send the requests to `/` and `/health` using the forwarded URL. This confirms proxyed downloads and port forwarding.

If anything fails (timeouts, 407, no forwarded URL), copy the error text so we can troubleshoot quickly.
