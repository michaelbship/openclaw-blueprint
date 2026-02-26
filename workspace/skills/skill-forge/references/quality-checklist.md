# Quality Checklist

Run through this before delivering a skill.

---

## Must Have

- [ ] **Name:** hyphen-case, <64 chars, verb-led or noun-phrase
- [ ] **Description:** includes WHAT it does AND WHEN to use it (trigger phrases)
- [ ] **SKILL.md under 500 lines**
- [ ] **No duplicate info** — content lives in SKILL.md OR references/, not both
- [ ] **All referenced files exist** — every link in SKILL.md points to a real file
- [ ] **Scripts tested and working** — if scripts/ exists, each script runs without errors
- [ ] **Uses existing tools where possible** — checked mcporter config before building new

---

## Should Have

- [ ] **Quick start section** — immediate actionable code or command
- [ ] **Good vs bad output examples** — shows what success and failure look like
- [ ] **Failure recovery** — what to do when MCP is down, script fails, data is empty
- [ ] **Imperative form** — "Run the script" not "You should run the script"
- [ ] **Mandatory completion enforced** — if skill must end with confirmation/action, uses MANDATORY language

---

## Nice to Have

- [ ] **Homepage URL** — for external tools/services
- [ ] **Links to related skills** — if this skill composes with others

---

## Anti-Patterns (Never Do)

- Extra docs files (no README.md, CHANGELOG.md, INSTALL.md)
- "When to Use" in body (all trigger info belongs in the description field)
- Over 500 lines (split into references/)
- Vague description ("Helps with X")
- Building what exists (always check installed MCPs first)
- Loading scripts into context (scripts are executed, not read)
- Separate display and confirm phases (merge them)
