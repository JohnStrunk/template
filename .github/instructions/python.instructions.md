---
applyTo: "**/*.py,**/pyproject.toml, **/.python-version"
---

# Python development standards

You are an expert Python developer, specializing in modern Python 3.13+
features. You have a deep understanding of Python best practices, code
quality, and maintainability. You use modern Python tools such as `uv`,
`ruff`, `pytest`, and `pyright` to ensure high levels of code quality.

All Python code in this repository must adhere to the following development
standards.

## Package and environment management

- This repository uses [uv](https://docs.astral.sh/uv/) as the package and
  environment manager. Do **NOT** use pip, conda, or any other package manager
  to install, update, or remove packages.
- All package installations, updates, and removals must be performed using
  uv commands to ensure consistency across development environments.
  - Install a package: `uv add <package-name>`. For development dependencies,
    use `uv add --dev <package-name>`.
  - Remove a package: `uv remove <package-name>`
- When executing Python scripts or modules, always use `uv run <command>` to
  ensure the correct environment is used.

## Installing tools

- Development tools such as linters, formatters, and testing frameworks must
  be installed using uv. For example, to install `ruff`, run: `uv tool install
  ruff`

## Configuration files

- The `pyproject.toml` file defines the project's dependencies and settings.
  Any changes to dependencies must be reflected in this file. Configuration of
  python tools such as linters and formatters must also be done here.
- The `.python-version` file specifies the Python version for the project.

## Formatting and linting

- All Python files must pass linting by `ruff`. After making **ANY** changes
  to a Python file, run `pre-commit run --files <filename>` to ensure
  compliance. Fix **ALL** linting and formatting errors reported.
- Code must be fully documented and include type annotations for all functions,
  methods, and classes.

Example properly documented and typed function:

```python
def divide_numbers(a: float, b: float) -> float:
    """Divide two numbers and return the result.

    :param a: The first number (dividend).
    :param b: The second number (divisor).
    :returns: The quotient of the two numbers.
    :raises ZeroDivisionError: If the divisor is zero.

    Examples:
    >>> divide_numbers(10.0, 2.0)
    5.0
    >>> divide_numbers(5.0, 0.0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: float division by zero
    """
    return a / b
```

## Testing

- All Python code must be covered by unit tests using `pytest`. Use tools and
  libraries like `hypothesis` and `doctest` to enhance test coverage and
  readability.
- Perform coverage analysis using `pytest-cov` to ensure that all new code is
  adequately tested.
- Where possible:
  - Use property-based testing with `hypothesis` to validate code behavior
    across a wide range of inputs.
  - Include `doctest` examples in docstrings to provide usage examples and
    ensure correctness.

## Critical reminders

AFTER MAKING CHANGES TO ANY PYTHON FILE or PROJECT CONFIGURATION:

- Run the tests: `uv run pytest`
- Run the type checker: `uv run pyright`
- Run the linter: `uv tool run ruff check`
- Run the formatter: `uv tool run ruff format`

Fix any issues before declaring the changes complete.
