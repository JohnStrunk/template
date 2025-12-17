# Auto-update Script for Copilot AI Instruction Files

A script to automatically update the `.github/instructions/`,
`.github/skills/`, and related agent/prompt files in derivative
repositories from the upstream template, merging with local changes.

## Description

When a new project is created from this template repository, it receives a
snapshot of the latest instructions, agents, prompts, and skills files. Over
time, improvements and bugfixes are made to these files in the template
repository. Projects derived from the template need a reliable way to update
their local copies to the latest upstream versions, while preserving any local
modifications.

This feature provides a script that:

- Fetches the latest versions of the relevant files from the template
  repository.
- Merges upstream changes with any local modifications, using a three-way
  merge strategy.
- Reports conflicts and provides guidance for manual resolution if needed.
- Can be run manually or integrated into CI workflows.

## Development tasks

- [ ] Determine which files and directories should be included in the update
      (e.g., `.github/instructions/`, `.github/skills/`, `AGENTS.md`,
      `CLAUDE.md`, etc.).
- [ ] Implement a script (e.g., `update-copilot-instructions.sh` or Python
      equivalent) that:
  - [ ] Identifies the upstream template repository and fetches the latest
        versions of the relevant files.
  - [ ] Performs a three-way merge for each file, using the current local
        version, the base version (from the initial clone), and the latest
        upstream version.
  - [ ] Reports any merge conflicts and provides instructions for manual
        resolution.
  - [ ] Optionally, allows for a dry-run mode to preview changes.
  - [ ] Logs all changes and actions taken.
- [ ] Add documentation to the repository on how to use the update script.
- [ ] (Optional) Integrate the script into CI workflows for automated update
      checks.

## Test plan

- Create a test repository derived from the template with local modifications to
  instruction files.
- Run the update script and verify:
  - Files are updated to match upstream when there are no local changes.
  - Local changes are preserved and merged with upstream changes when possible.
  - Merge conflicts are detected and reported clearly.
  - The script logs actions and provides clear instructions for resolving
    conflicts.
- Test dry-run mode to ensure it previews changes without modifying files.
- Test documentation for clarity and completeness.
