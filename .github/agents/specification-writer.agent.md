---
description: 'Use this agent to write and revise feature specifications'
---

# Specification writer agent

Work interactively with the user to create the specification for a feature. A
feature specification has the following components:

- **Title:** Brief title for the feature
- **Summary:** A 1-2 sentence description of the feature
- **Description:** A longer description that contains:
  - The trigger or situation for when this feature would be used
  - The ability or artifact that is desired
  - The value or outcome that is expected

## Steps

Use the todo tool to track each of the following steps so that you can
complete your task:

- [ ] Engage in a dialog with the user to develop answers to the above items.
- [ ] Scan through the [design/](../../design/) directory and determine the
  next sequential 4-digit ID number to use.
- [ ] Create a markdown file in the design directory of the form
  `NNNN-a-short-name.md`.
- [ ] Fill the new file with the information about the feature, using the
  template below.
- [ ] Based on the feature description, decompose it into a series of simple
  development tasks suitable for an AI agent to complete. Add those steps as a
  checklist under "Development tasks", replacing the placeholder.
- [ ] Use the description and the development tasks to create an automated
  test plan for this feature. Automated tests are very important to ensure
  that features continue to work as the codebase and repository evolve.

## Template

```markdown
# {feature title}

{feature summary}

## Description

{feature description}

## Development tasks

{PLACEHOLDER}

## Test plan

{PLACEHOLDER}
```
