---
applyTo: "**"
---

# This repository uses pre-commit

This repository uses the `pre-commit` tool to enforce code quality and
consistency checks before each commit. It is essential to ensure that all
pre-commit hooks pass successfully before finalizing any commit.

Before committing changes, you must follow these guidelines:

- Always run [lint-all.sh](../lint-all.sh) prior to committing to catch any
  issues early. You must fix any issues identified by this linting process.
  You will not be able to commit until all issues are resolved.
- When you run `git commit`, carefully check the return code of the command. If
  any pre-commit checks fail, the commit will not be successful. You must fix
  the issues and re-attempt the commit.
- After pre-commit hooks make changes to your staged files, you must re-stage
  those files before re-attempting the commit.
- You must repeat this process until the commit is successful. Note that since
  your commit has failed, you do not have a previous commit to "fix" (so don't
  use `--amend` or `--no-edit`).
- When committing changes, ensure that your commit messages cover all changes
  being committed, not just changes to fix pre-commit issues.
