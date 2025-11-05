# Foundry Agent Call Python

A Python client for calling Azure AI Foundry agents with default Azure credentials.

## Development Setup

### Using Dev Container (Recommended)

This project uses a dev container for consistent development environments:

1. **Open in Dev Container**
   - Install [Docker](https://www.docker.com/products/docker-desktop) and [VS Code](https://code.visualstudio.com/)
   - Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
   - Open this folder in VS Code
   - When prompted, click "Reopen in Container" (or run the command "Dev Containers: Reopen in Container")

2. **Install Dependencies** (inside the dev container)

```bash
pip install -r requirements.txt
```

3. **Configure Azure Connection**

Create a `config.json` file with your Azure AI Foundry endpoint and agent ID:

```json
{
  "endpoint": "https://YOUR-PROJECT.services.ai.azure.com/api/projects/YOUR-PROJECT-NAME",
  "agent_id": "asst_YOUR_AGENT_ID"
}
```

4. **Authenticate with Azure**

Use device code flow (recommended for dev containers):

```bash
az login --use-device-code
```

5. **Run the Example**

```bash
python ./example.py
```

The example provides two options:
- **Option 1**: Simple chat (single message)
- **Option 2**: Multi-turn conversation

## Development Tools

This project uses modern Python tooling:

- **Ruff**: Fast Python linter and formatter (replaces flake8, isort, black)
- **mypy**: Static type checker
- **pytest**: Testing framework
- **pytest-cov**: Code coverage reports

## Running Tests

```bash
pytest
```

With coverage:

```bash
pytest --cov=. --cov-report=html
```

## Code Quality

Format code with Ruff:

```bash
ruff format .
```

Lint code:

```bash
ruff check .
```

Auto-fix issues:

```bash
ruff check --fix .
```

Type checking:

```bash
mypy .
```

## Project Structure

```
.
├── .devcontainer/              # Dev container configuration
├── foundry_agent_caller.py     # Main client library
├── example.py                  # Example usage
├── config.json                 # Azure configuration (create this)
├── requirements.txt            # Python dependencies
├── pyproject.toml             # Project configuration
└── README.md                  # This file
```

## VS Code Integration

The dev container is configured with automatic formatting and linting on save. Python files will be:
- Formatted with Ruff on save
- Linted with Ruff
- Type-checked with Pylance
- Organized imports automatically

## License

MIT
