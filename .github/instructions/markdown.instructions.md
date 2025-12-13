---
applyTo: "**/*.md"
---

# Formatting and linting for Markdown files

All Markdown files in this repository must conform to the following formatting
and linting standards:

- All Markdown files must pass linting by markdownlint. After making **ANY**
  changes to a markdown file, run `pre-commit run --files <filename>` to
  ensure compliance. Fix **ALL** linting errors reported.
- Line length must not exceed 80 characters, with the exception of code blocks
  and tables.
- The proper style is defined by the markdownlint rules configured in
  [markdownlint-config.yaml](../.github/markdownlint-config.yaml). Review this
  file prior to making changes to ensure compliance with the defined rules.
