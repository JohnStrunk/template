---
applyTo: "**/pyproject.toml, **/.python-version"
description: "Standards for configuring Python project files"
---

# Standards for Python project configuration files

This repository uses `pyproject.toml` and `.python-version` files to manage
Python project settings and dependencies.

## Configuration files

- The `pyproject.toml` file defines the project's dependencies and settings.
  Any changes to dependencies must be reflected in this file. Configuration of
  python tools such as linters and formatters must also be done here.
- The `.python-version` file specifies the Python version for the project.
  This will be used by `uv` to create the appropriate environment.

## Type checking configuration

- Pyright is used for static type checking in this repository.
- Below is the recommended configuration for Pyright to be included in the
  `pyproject.toml` file under the `[tool.pyright]` section:

```toml
[tool.pyright]
# https://microsoft.github.io/pyright/#/configuration
deprecateTypingAliases = true
enableReachabilityAnalysis = true
include = ["."]
reportUnnecessaryTypeIgnoreComment = true
typeCheckingMode = "strict"
useLibraryCodeForTypes = true
verboseOutput = true
```

## Linting and formatting configuration

- Ruff is used for linting and formatting Python code in this repository.
- Below is the recommended configuration for Ruff to be included in the
  `pyproject.toml` file:

```toml
[tool.ruff.format]
docstring-code-format = true
indent-style = "space"
quote-style = "double"

[tool.ruff.lint]
# https://docs.astral.sh/ruff/rules/
select = [
    "D",     # Pydocstyle
    "DOC",   # Pydoclint
    "E101",  # Pycodestyle: mixed spaces and tabs
    "E4",    # Pycodestyle: Imports
    "E7",    # Pycodestyle: misc
    "E9",    # Pycodestyle: error
    "F",     # Pyflakes
    "FAST",  # FastAPI-specific
    "I",     # isort
    "PL",    # pylint
    "RUF",   # Ruff-specific
    "UP",    # Pyupgrade
    "W",     # Pycodestyle: warning
]
pydocstyle.convention = "pep257"

[tool.ruff.lint.per-file-ignores]
# Ignore magic value (PLR2004) in test files
"*_test.py" = ["PLR2004"]
"test_*.py" = ["PLR2004"]
```

## Testing configuration

- Pytest is used for testing Python code in this repository, along with
  `pytest-cov` for coverage reporting.
- Below is the recommended configuration for Pytest to be included in the
  `pyproject.toml` file:

```toml
[tool.coverage.html]
directory = "htmlcov"

[tool.coverage.report]
# Regexes for lines to exclude from consideration
exclude_lines = [
    # Have to re-enable the standard pragma
    "pragma: no cover",
    # Don't complain about missing debug-only code:
    "def __repr__",
    "if self.debug",
    # Don't complain if tests don't hit defensive assertion code:
    "raise AssertionError",
    "raise NotImplementedError",
    # Don't complain if non-runnable code isn't run:
    "if 0:",
    "if __name__ == .__main__.:",
    # Don't complain about abstract methods, they aren't run:
    "@(abc.)?abstractmethod",
]
omit = ["*_test.py", "test_*.py"]  # Omit test files from coverage report

[tool.coverage.run]
branch = true   # Enable branch coverage
source = ["."]  # Source code directories

[tool.coverage.xml]
output = "coverage.xml"

[tool.pytest.ini_options]
addopts = [
    "-rA -q",
    "--doctest-modules",  # Run doctests in docstrings
    "--cov=.",
    "--cov-config=.coveragerc",
    "--cov-report=html",
    "--cov-report=term",
    "--cov-report=xml",
]
filterwarnings = [
    "error",  # Treat all warnings as errors
]
```
