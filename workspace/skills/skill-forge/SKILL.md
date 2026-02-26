---
name: skill-forge
description: |
  Guide the creation, validation, and packaging of OpenClaw skills.
  Use when user wants to create a new skill, improve an existing skill,
  or says "build a skill for X", "create a skill that...", or "make a skill".
---

# Skill Forge Doctrine

Build skills that are concise, well-structured, and leverage existing tools.

**Core principle:** Lean on what exists. Only build new integrations when necessary.

---

## Workflow

### Phase 1: Discover

Product owner mindset. Ask focused questions, don't overwhelm.

1. **Trigger** — "What would you say to activate this? 1-3 phrases."
2. **Friction** — "What do you do today? What's slow or broken?"
3. **Output** — "What do you want back? Format? Where should it go?"
4. **Guardrails** — "What should it never do? Any hard constraints?"

**Output of this phase:** Problem statement, trigger phrases, success criteria, constraints.

Only proceed to Phase 2 after you have clear answers.

---

### Phase 2: Research Tools

Use the `research` skill to find what exists before building anything new.

1. **What tools/APIs solve this problem?** — Search the web for existing solutions
2. **What MCP servers exist?** — Check Smithery, mcp.so, official repos
3. **What's already installed locally?** — Run `mcporter daemon status` and check config
4. **Evaluate quality** — Native > well-maintained community > build our own

Read [mcp-directory.md](references/mcp-directory.md) for where to search and quality criteria.
Read [mcp-infrastructure.md](references/mcp-infrastructure.md) for how the MCP stack works and how to add new servers.

---

### Phase 3: Decide

**Integration decision:**

| What You Found | Action |
|----------------|--------|
| Already in mcporter config | Orchestrate it from the skill |
| Good native MCP exists | Install via mcporter, then orchestrate |
| Good community MCP (well-maintained) | Evaluate quality, install if it passes |
| Good API exists but no MCP | Write a script with direct API calls |
| Nothing exists | Manual workflow in skill instructions; flag the gap |

**Structure decision:**

| Complexity | Structure | When to Use |
|------------|-----------|-------------|
| Simple | SKILL.md only | Single tool, no logic needed |
| MCP Orchestration | SKILL.md + tool guidance | Wraps existing MCP tools with judgment |
| Gather-Interpret | SKILL.md + scripts + evidence | Data collection + LLM analysis |
| Multi-Step | SKILL.md + scripts + references | Complex workflow with variants |

Read [patterns.md](references/patterns.md) for design patterns.

---

### Phase 4: Write

1. **Name** — hyphen-case, <64 chars, verb-led (e.g., `email-scan`, `deploy-check`)
2. **Description** — Must include WHAT it does AND WHEN to use it (trigger phrases)
3. **Body** — Quick start first, then link to references/ for deep detail. Imperative form.
4. **Keep SKILL.md under 500 lines**

**Progressive disclosure:**
- SKILL.md = overview + navigation (loaded when triggered)
- references/ = deep docs (loaded on-demand when needed)
- scripts/ = deterministic code (executed, not loaded into context)
- assets/ = output files (used in output, not loaded for reasoning)

Read [templates.md](references/templates.md) for starter files.

---

### Phase 5: Validate

Run the validation script:

```bash
python3 {baseDir}/scripts/validate_skill.py <skill-folder>
```

Also manually verify:
- [ ] Description includes trigger phrases
- [ ] SKILL.md under 500 lines
- [ ] No info duplicated between SKILL.md and references/
- [ ] All referenced files exist
- [ ] Scripts tested and working
- [ ] Uses existing tools/MCPs where possible
- [ ] Good/bad output examples included
- [ ] Self-Check section includes skill footer declaration

Read [quality-checklist.md](references/quality-checklist.md) for the full checklist.

---

### Phase 6: Deliver

1. Show the user the skill structure and key files
2. Install to `skills/<skill-name>/`
3. Offer to test with a real query
4. Iterate based on results

---

## Freedom Level Guide

| Level | When | How |
|-------|------|-----|
| High | Multiple valid approaches | Text instructions in SKILL.md |
| Medium | Preferred pattern exists | Pseudocode or parameterized scripts |
| Low | Fragile, must be exact | Specific scripts with narrow parameters |
