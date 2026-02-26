# Skill Design Patterns

Distilled best practices from Anthropic, OpenAI, and OpenClaw architecture.

---

## From Anthropic

### Progressive Disclosure
Skills load in 3 levels to manage context efficiently:
- **Level 1:** Metadata (name + description) — always visible (~100 words)
- **Level 2:** SKILL.md body — loaded when skill triggers (<5k words ideal)
- **Level 3:** Referenced files — loaded on-demand by the bot as needed

### Description = Trigger
The `description` field is THE primary mechanism for when a skill loads.
- Include WHAT the skill does
- Include WHEN to use it (exact trigger phrases and contexts)
- All "when to use" info goes in the description, NOT in the body

### Concise is Key
The context window is a public good. Skills share it with system prompt, conversation history, other skills, and the actual request.
- Keep SKILL.md under 500 lines
- Challenge each piece: "Does the bot really need this explanation?"
- Prefer concise examples over verbose explanations
- Move deep detail to references/ files

### Structure
```
skill-name/
├── SKILL.md           # Overview + navigation (loaded when triggered)
├── references/        # Deep docs (loaded on-demand)
└── scripts/           # Code (executed, not loaded into context)
```

### Degrees of Freedom
Match specificity to the task's fragility:
- **High freedom:** Multiple valid approaches, context-dependent decisions
- **Medium freedom:** Preferred pattern exists, some variation OK
- **Low freedom:** Fragile operations, consistency critical, exact sequence required

---

## From OpenAI

### Few-Shot Examples
Include good and bad output examples in SKILL.md.

### Define Output Format
Use structured formats: markdown tables, emoji-sectioned bullet lists, JSON schemas, templates with placeholders.

### Reflection
Have the model check its own work: "Verify against the checklist before completing."

---

## From OpenClaw Architecture

### Skill Execution Pipeline
Each skill follows a 4-layer execution model:
- **Gathering:** Deterministic script fetches data via MCP
- **Evidence:** Immutable markdown file with structured facts
- **Interpretation:** LLM reads evidence + SKILL.md, applies judgment
- **Action:** Deliver output or execute tool calls

Not every skill needs all 4 layers. Simple skills skip gathering/evidence.

### MCP as Contracts
- Skills orchestrate MCP tools; they don't duplicate API logic
- MCP bridges absorb API complexity and present stable interfaces

### Glass Box Transparency
- Evidence files show raw inputs (auditable)
- Skills encode judgment rules (debuggable)
- No hidden heuristics in opaque scripts

---

## Anti-Patterns to Avoid

- "When to Use This Skill" section in the body (belongs in description)
- README.md, CHANGELOG.md in skill folder
- Duplicating info in SKILL.md AND references/
- SKILL.md over 500 lines
- Building new integration when existing one works
- Vague description like "Helps with X"
- Loading scripts into context instead of executing them

---

## Multi-Phase Workflow Patterns

### The "Display Then Confirm" Trap

**Problem:** If a skill has separate "Display" and "Confirm" phases, the LLM will often stop at Display.

**Good:** Merge display and action into one phase. Use enforcement language: "MANDATORY:", "Always end with:", "Never complete without:"
