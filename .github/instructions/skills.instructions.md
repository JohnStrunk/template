---
applyTo: "**"
---

# Skills

Skills are special abilities that you can use to better assist users with
specific types of requests. Each skill has its own unique functionality and
must be invoked when a user asks for something that falls within the skill's
domain.

When a user makes a request, you must determine if any of the available skills
are relevant to the request. If a skill is applicable, you must use it to
generate your response. Only if no skills are relevant can you respond using
just your general knowledge and capabilities.

If there's even a slight chance that a skill is relevant to the user's
request, you must read the skill's instructions before deciding. Do this for
all skills that look like they are even remotely related to the user's
request. **If a skill is relevant, you must use it.**

Here are the skills currently available to you, a short description of each
skill, and a link to the full instructions for that skill:

<!-- TABLE START -->
| **name** | **description** | **Instructions link** |
| ------ | ----- | ----- |
| dad-joke | How to tell a dad joke. Use this skill to respond with a dad joke when prompted. | [../skills/dad-joke/SKILL.md](../skills/dad-joke/SKILL.md) |
| superpowers:brainstorming | Use when creating or developing, before writing code or implementation plans - refines rough ideas into fully-formed designs through collaborative questioning, alternative exploration, and incremental validation. Don't use during clear 'mechanical' processes | [../skills/superpowers/brainstorming/SKILL.md](../skills/superpowers/brainstorming/SKILL.md) |
| superpowers:executing-plans | Use when partner provides a complete implementation plan to execute in controlled batches with review checkpoints - loads plan, reviews critically, executes tasks in batches, reports for review between batches | [../skills/superpowers/executing-plans/SKILL.md](../skills/superpowers/executing-plans/SKILL.md) |
| superpowers:finishing-a-development-branch | Use when implementation is complete, all tests pass, and you need to decide how to integrate the work - guides completion of development work by presenting structured options for merge, PR, or cleanup | [../skills/superpowers/finishing-a-development-branch/SKILL.md](../skills/superpowers/finishing-a-development-branch/SKILL.md) |
| superpowers:root-cause-tracing | Use when errors occur deep in execution and you need to trace back to find the original trigger - systematically traces bugs backward through call stack, adding instrumentation when needed, to identify source of invalid data or incorrect behavior | [../skills/superpowers/root-cause-tracing/SKILL.md](../skills/superpowers/root-cause-tracing/SKILL.md) |
| superpowers:systematic-debugging | Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes - four-phase framework (root cause investigation, pattern analysis, hypothesis testing, implementation) that ensures understanding before attempting solutions | [../skills/superpowers/systematic-debugging/SKILL.md](../skills/superpowers/systematic-debugging/SKILL.md) |
| superpowers:test-driven-development | Use when implementing any feature or bugfix, before writing implementation code - write the test first, watch it fail, write minimal code to pass; ensures tests actually verify behavior by requiring failure first | [../skills/superpowers/test-driven-development/SKILL.md](../skills/superpowers/test-driven-development/SKILL.md) |
| superpowers:using-git-worktrees | Use when starting feature work that needs isolation from current workspace or before executing implementation plans - creates isolated git worktrees with smart directory selection and safety verification | [../skills/superpowers/using-git-worktrees/SKILL.md](../skills/superpowers/using-git-worktrees/SKILL.md) |
| superpowers:verification-before-completion | Use when about to claim work is complete, fixed, or passing, before committing or creating PRs - requires running verification commands and confirming output before making any success claims; evidence before assertions always | [../skills/superpowers/verification-before-completion/SKILL.md](../skills/superpowers/verification-before-completion/SKILL.md) |
| superpowers:writing-plans | Use when design is complete and you need detailed implementation tasks for engineers with zero codebase context - creates comprehensive implementation plans with exact file paths, complete code examples, and verification steps assuming engineer has minimal domain knowledge | [../skills/superpowers/writing-plans/SKILL.md](../skills/superpowers/writing-plans/SKILL.md) |
<!-- TABLE END -->

- If you read a skill's instructions, say: "📖 **Read instructions for
  skill:** skill-name 📖".
- If you decide a skill is relevant, say: "✅ **Decided to use skill:**
  skill-name ✅".
- If you decide a skill is not relevant, say: "❌ **Decided not to use skill:**
  skill-name (reason for not using) ❌".

When using a skill, make sure to follow the specific instructions provided for
that skill. Each skill may have its own guidelines for how to format
responses, what kind of content to include, and any other special
considerations. Make sure you follow those instructions carefully. **Use todo
items to track any steps required by the skill instructions.** It is very
important that you adhere to the instructions for each skill to ensure you are
using it correctly.
