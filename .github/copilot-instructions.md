# Instructions for AI coding assistants

## Project architecture

The major features and architectural decisions for this project are documented
in the [`design/`](../design/) directory. Each feature and decision is captured
in a separate markdown file. These documents serve as a reference for
understanding the rationale behind various design choices and provide context
for future development.
**All changes must be consistent with these documents.**

Before making architectural changes or adding new features:

- Review all existing decision records and feature descriptions in the `design/`
  directory to ensure consistency and avoid duplication.
- If requirements or instructions from the user are ambiguous or incomplete,
  ask clarifying questions before proceeding.
- All new architectural decisions must be documented using the MADR template by
  running `design/new-record.sh -m "<title>"`.

## File linting

After making changes to any files in this repository, ensure that all linting
checks pass. Use the script [`.github/lint-all.sh`](lint-all.sh) to check for
problems. If any issues are found, fix them, and re-run the script. Continue to
iterate until no issues are found. **This must be done any time files are
modified and before telling the user that changes are complete.**

All markdown files must comply with markdownlint rules (line length,
formatting, etc.).
