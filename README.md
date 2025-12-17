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
  - Consider enabling [Merge
    protections](https://docs.mergify.com/merge-protections/) to enable
    `Depends-On: <PR#>`, `Merge-After: <ISO 8601>`.
  - Consider enforcing the merge queue (only allowing Mergify to merge PRs) by
    [protecting the default
    branch](https://dashboard.mergify.com/queues/deployment/enforcement).
- [ ] Add a license to the project
- [ ] Update the README with project-specific information
- [ ] Update the devcontainer configuration based on the project's language
  and dev tools
- [ ] Update [Copilot setup
  workflow](.github/workflows/copilot-setup-steps.yaml) with project-specific
  tools
- [ ] Update the [Copilot instructions file](.github/copilot-instructions.md)
  with project-specific information

## Copilot Instructions Auto-Update Script

This repository includes a script to update Copilot AI instruction files from
the upstream template repository, merging with local changes.

### Usage

```bash
.github/update-copilot-instructions.sh \
  # Run update (modifies files)
.github/update-copilot-instructions.sh --dry-run \
  # Preview changes only
```

The script will fetch the latest versions of:

- `.github/instructions/`
- `.github/skills/`
- `.github/prompts/`
- `.github/agents/`
- `AGENTS.md`
- `CLAUDE.md`

For each file, a three-way merge is performed between your local version, the
base, and upstream. If a conflict occurs, a `.merged` file is created for
manual resolution. All actions are logged to the console. The script can be run
from any directory in the repository.

### Resolving Conflicts

If you see a message like `CONFLICT in <file>. See <file>.merged for manual
resolution.`, open the `.merged` file, resolve the conflict markers
(`<<<<<<<`, `=======`, `>>>>>>>`), and replace the original file with the
resolved version.

### Notes

The script requires `git`, `diff3`, and `diff` to be installed. You can
customize the upstream repository and branch by editing the script variables.
No files are modified in `--dry-run` mode.
