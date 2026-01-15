# codespace-test

## Development Container

This workspace includes a devcontainer for .NET 10, Node 22.12.0, and Python 3.12.

### Use in GitHub Codespaces or VS Code

- Open the folder in VS Code and when prompted, "Reopen in Container".
- Or, in Codespaces, it will automatically build using [.devcontainer/devcontainer.json](.devcontainer/devcontainer.json).

### Verify tool versions inside the container

Run these commands in the container terminal to confirm versions:

```bash
dotnet --info
node -v
python --version
```

### Notes

- .NET 10 SDK packages are available on Ubuntu feeds; the devcontainer uses features to install dotnet-sdk-10.0.
- Node is installed via the Dev Containers Node feature (nvm) at 22.12.0.
- Python is installed via the Dev Containers Python feature at 3.12.
