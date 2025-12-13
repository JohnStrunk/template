#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "pyyaml>=6.0.3",
# ]
# ///
import os
import re

import yaml

# Directory to search for SKILL.md files
SKILLS_DIR = os.path.join(".github", "skills")

# Markdown table header
TABLE_HEADER = "| **name** | **description** | **Instructions link** |"
TABLE_DIVIDER = "| ------ | ----- | ----- |"


def extract_name_description(filepath: str) -> tuple[str | None, str | None]:
    """Extract 'name' and 'description' from YAML frontmatter using PyYAML."""
    with open(filepath, "r", encoding="utf-8") as f:
        content: str = f.read()
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None, None
    frontmatter: str = match.group(1)
    try:
        meta = yaml.safe_load(frontmatter)
    except Exception:
        return None, None
    name = meta.get("name") if isinstance(meta, dict) else None
    description = meta.get("description") if isinstance(meta, dict) else None
    return name, description


def find_skill_md_files(base_dir: str) -> list[str]:
    """Recursively find all SKILL.md files under base_dir."""
    skill_files: list[str] = []
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file == "SKILL.md":
                rel_path: str = os.path.relpath(os.path.join(root, file), ".")
                skill_files.append(rel_path)
    return skill_files


def main() -> None:
    skill_files: list[str] = find_skill_md_files(SKILLS_DIR)
    rows: list[str] = []
    skill_rows: list[tuple[str, str, str]] = []
    for skill_file in skill_files:
        name, description = extract_name_description(skill_file)
        if not name and not description:
            continue
        rel_skill_path = os.path.relpath(skill_file, SKILLS_DIR)
        parts = rel_skill_path.split(os.sep)
        subpackage = ":".join(parts[:-2]) if len(parts) > 2 else ""
        display_name = f"{subpackage}:{name}" if subpackage else name
        rel_path: str = os.path.relpath(skill_file, ".")
        link: str = f"[{rel_path}](../{rel_path})".replace("\\", "/")
        skill_rows.append((display_name or "", description or "", link))

    # Sort rows alphabetically by display_name (case-insensitive)
    skill_rows.sort(key=lambda row: row[0].lower())
    rows = [f"| {name} | {desc} | {lnk} |" for name, desc, lnk in skill_rows]
    table = "\n".join([TABLE_HEADER, TABLE_DIVIDER] + rows)

    # Path to the instructions file
    instructions_path = os.path.join(
        os.path.dirname(__file__), "skills.instructions.md"
    )
    with open(instructions_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Replace the table between markers
    start_marker = "<!-- TABLE START -->"
    end_marker = "<!-- TABLE END -->"
    pattern = re.compile(
        rf"({re.escape(start_marker)})(.*?)(\s*{re.escape(end_marker)})",
        re.DOTALL,
    )
    new_content = pattern.sub(f"{start_marker}\n{table}\n{end_marker}", content)

    with open(instructions_path, "w", encoding="utf-8") as f:
        f.write(new_content)


if __name__ == "__main__":
    main()
