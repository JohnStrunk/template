# Instructions for AI coding assistants

The following instructions **MUST** be followed by any AI coding assistant
when making changes to this repository.

## Project architecture

The major features and architectural decisions for this project are documented
in the [`design/`](../design/) directory. Each feature and decision is captured
in a separate markdown file. These documents serve as a reference for
understanding the rationale behind various design choices and provide context
for future development.
**All changes must be consistent with these documents.**

Before making changes to the repository or adding new code:

- Review all existing decision records and feature descriptions in the `design/`
  directory. Changes and additions must align with these documents.
- If requirements or instructions from the user are ambiguous or incomplete,
  ask clarifying questions before proceeding.

## Committing changes

This repository uses the `pre-commit` tool to enforce linting and other checks
with each commit. When generating git commits, it is essential to verify the
return code from the `git commit` command. If ANY pre-commit checks fail, that
means the commit has failed. The issues must be fixed and the commit re-tried.

When generating commits:

- Attempt to commit the changes, using an appropriate commit message that
  accurately describes all outstanding changes that are about to be committed.
- Evaluate the return code. If the commit succeeded, stop. Othwise, continue.
- Examine the output of the pre-commit tests and fix the issues that
  pre-commit surfaced.
- Repeat this entire procedure until the commit is successful. NOTE: Since
  your commit has failed, you do not have a previous commit to "fix" (so don't
  use "--amend" or "--no-edit").
