#!/usr/bin/env python3
"""Validate an OpenClaw skill against best practices."""

import sys
import re
from pathlib import Path


def validate(skill_path: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    skill_dir = Path(skill_path)
    skill_md = skill_dir / "SKILL.md"

    # --- SKILL.md exists ---
    if not skill_md.exists():
        return ["SKILL.md not found"], warnings

    content = skill_md.read_text()
    lines = content.split("\n")

    # --- Frontmatter ---
    if not content.startswith("---"):
        errors.append("Missing YAML frontmatter (must start with ---)")
    else:
        fm_match = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
        if not fm_match:
            errors.append("Malformed frontmatter (missing closing ---)")
        else:
            fm = fm_match.group(1)

            # Name check
            name_match = re.search(r"^name:\s*(.+)$", fm, re.MULTILINE)
            if not name_match:
                errors.append("Missing 'name' in frontmatter")
            else:
                name = name_match.group(1).strip().strip("\"'")
                if (
                    not re.match(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$", name)
                    and len(name) > 1
                ):
                    if not re.match(r"^[a-z0-9-]+$", name):
                        errors.append(
                            f"Name '{name}' must be hyphen-case (lowercase, digits, hyphens)"
                        )
                if len(name) > 64:
                    errors.append(f"Name '{name}' exceeds 64 characters ({len(name)})")

            # Description check
            if "description:" not in fm:
                errors.append("Missing 'description' in frontmatter")
            else:
                desc_match = re.search(
                    r"^description:\s*\|?\s*\n?(.*?)(?=\n[a-z_]|\Z)",
                    fm,
                    re.DOTALL | re.MULTILINE,
                )
                if desc_match:
                    desc = desc_match.group(1).strip()
                    if len(desc) < 20:
                        warnings.append(
                            f"Description is very short ({len(desc)} chars) — include trigger phrases"
                        )

    # --- Line count ---
    if len(lines) > 500:
        warnings.append(f"SKILL.md has {len(lines)} lines (recommend <500)")
    elif len(lines) > 400:
        warnings.append(f"SKILL.md has {len(lines)} lines (approaching 500 limit)")

    # --- Anti-pattern files ---
    anti_patterns = ["README.md", "CHANGELOG.md", "INSTALL.md", "INSTALLATION.md"]
    for anti in anti_patterns:
        if (skill_dir / anti).exists():
            warnings.append(f"Remove '{anti}' — anti-pattern in skill folders")

    # --- Check referenced files exist ---
    ref_links = re.findall(r"\[.*?\]\((?!https?://)(.*?)\)", content)
    for ref in ref_links:
        ref_path = ref.split("#")[0]
        if ref_path and not (skill_dir / ref_path).exists():
            errors.append(f"Referenced file '{ref_path}' does not exist")

    # --- Check for "When to Use This Skill" in body ---
    body_start = content.find("---", 4)
    if body_start > 0:
        body = content[body_start + 3 :]
        if re.search(r"^#+\s+When to Use This", body, re.IGNORECASE | re.MULTILINE):
            warnings.append(
                "'When to Use This Skill' section found in body — move trigger info to description"
            )

    # --- Check scripts are executable ---
    scripts_dir = skill_dir / "scripts"
    if scripts_dir.exists():
        for script in scripts_dir.iterdir():
            if script.suffix in (".py", ".sh", ".js"):
                if not script.stat().st_mode & 0o111:
                    warnings.append(
                        f"Script '{script.name}' is not executable (chmod +x)"
                    )

    return errors, warnings


def main():
    if len(sys.argv) < 2:
        print("Usage: validate_skill.py <skill-folder-path>")
        print("Example: validate_skill.py skills/email-scan")
        sys.exit(1)

    skill_path = sys.argv[1]

    if not Path(skill_path).is_dir():
        print(f"Error: '{skill_path}' is not a directory")
        sys.exit(1)

    errors, warnings = validate(skill_path)

    if errors:
        print("ERRORS:")
        for e in errors:
            print(f"  - {e}")
        print()

    if warnings:
        print("WARNINGS:")
        for w in warnings:
            print(f"  - {w}")
        print()

    if not errors and not warnings:
        print("Skill passes all checks")

    total = len(errors) + len(warnings)
    if total > 0:
        print(f"{'─' * 40}")
        print(f"  {len(errors)} error(s), {len(warnings)} warning(s)")

    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
