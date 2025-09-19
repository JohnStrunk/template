# Project template

This is a template to serve as a starting point for new repos.

## Features

- Pre-configured CI/CD pipeline that runs pre-commit and ensures that the
  devcontainer builds successfully.
- A basic devcontainer setup
- Mergify configuration to enable merging of PRs. See
  [.github/mergify.yml](.github/mergify.yml) for details.
- Renovate configuration to keep dependencies up to date. See
  [.github/renovate.json5](.github/renovate.json5) for details.
- Pre-commit configuration to ensure code quality. See
  [.pre-commit-config.yaml](.pre-commit-config.yaml) for details.
- Configuration files for GitHub Copilot to help with code generation
  and editing, including custom prompts:
  - `/enhance-instructions`: Enhance the AI agent's instructions based on the
    conversation history
  - `/feature <title>`: Generate a feature specification
  - `/madr <title>`: Generate a new architectural decision record

## New project checklist

- [ ] Adjust the Mergify configuration to customize the merge conditions
- [ ] Add a license to the project
- [ ] Update the README with project-specific information
- [ ] Update the devcontainer configuration based on the project's language
  and dev tools
- [ ] Update [Copilot setup
  workflow](.github/workflows/copilot-setup-steps.yaml) with project-specific
  tools
- [ ] Update the [Copilot instructions file](.github/copilot-instructions.md)
  with project-specific information
