# Foundry Agent Call Python

Python development project with modern tooling and best practices.

## Development Setup

This project uses a dev container for consistent development environments. To get started:

1. Install [Docker](https://www.docker.com/products/docker-desktop) and [VS Code](https://code.visualstudio.com/)
2. Install the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
3. Open this folder in VS Code
4. When prompted, click "Reopen in Container" (or run the command "Dev Containers: Reopen in Container")

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
├── .devcontainer/          # Dev container configuration
├── src/                    # Source code
├── tests/                  # Test files
├── pyproject.toml         # Project configuration
└── README.md              # This file
```

## VS Code Integration

The dev container is configured with automatic formatting and linting on save. Python files will be:
- Formatted with Ruff on save
- Linted with Ruff
- Type-checked with Pylance
- Organized imports automatically

## License

MIT
