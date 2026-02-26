---
name: system-update
description: |
  Update your operational context — tools, memory, skills, configuration, or
  agent identity. Routes information to the correct file in the correct format.
  Use when user says:
  - "remember this"
  - "update tools" or "update memory"
  - "commit to memory" or "save this"
  - "add this capability"
  - "change your identity/personality"
  - "write this down"
  Confirms before modifying identity files (AGENTS.md, SOUL.md, IDENTITY.md).
  Delegates to model-config-manager for model changes and skill-forge for new skills.
---

# System Update

Use this skill to persist information to the correct location in the correct
format. This is how you maintain your own operational brain.

---

## Step 1: Route

Decide where the information belongs. If your user specifies a file, follow
the instruction. If not, route based on what's being stored.

| What's being stored | Destination | Why there |
|---|---|---|
| Tool or capability awareness | `TOOLS.md` | Always-injected. You see it every turn. |
| Operational decision, lesson, preference | `MEMORY.md` (under relevant section) | Loaded at session start. Persists across sessions. |
| Something that happened today | `memory/YYYY-MM-DD.md` | Daily log. Append-only. Raw context. |
| Process doctrine for a domain | `skills/<name>/SKILL.md` | Delegate to `skill-forge`. |
| Model or provider configuration | Delegate to `model-config-manager` | Specialized skill with safety checks. |
| New skill creation | Delegate to `skill-forge` | Specialized skill with validation. |
| Agent identity, personality, behavioral rules | `AGENTS.md`, `SOUL.md`, or `IDENTITY.md` | **Confirm before writing.** Show proposed changes first. |
| Who the user is | `USER.md` | **Confirm before writing.** |
| Heartbeat checklist | `HEARTBEAT.md` | Keep it short to limit token burn. |

---

## Step 2: Format

Each destination has different rules. The core principle:

> Write at the agent's actual interface layer. If a junior developer couldn't
> read what you wrote and immediately do the right thing, rewrite it.

### TOOLS.md (highest stakes — you see this every turn)

**Rules:**
- Every line earns its slot. Context is a finite resource.
- When adding a new tool, add BOTH: a discovery entry AND at least one
  verified, copy-pasteable invocation example.
- Never write an example you haven't tested.

**Test before writing:** "Could someone copy-paste this command and get a result?"

### MEMORY.md (operational state — loaded at session start)

**Rules:**
- Scannable: headers + bullets, no prose paragraphs.
- Operational state only — things you need to function.
- Curate on each update: remove outdated info, consolidate duplicates.
- Not a dumping ground. Ask: "Will future-me need this at session start?"

### memory/YYYY-MM-DD.md (daily log — append-only)

**Rules:**
- Timestamped entries, most recent at bottom.
- Raw context: what happened, what was decided, what to follow up on.
- Don't curate — this is the raw log. Curation happens in MEMORY.md.

### AGENTS.md, SOUL.md, IDENTITY.md (identity — confirm first)

**Rules:**
- **Always show proposed changes to your user before writing.**
- These files shape your behavior on every future turn.
- Changes are high-impact: a bad edit affects every interaction.
- Format: match the existing structure of the file. Don't reorganize.

For the full principles on writing effective always-injected context,
read: `{baseDir}/references/context-principles.md`

---

## Self-Check

Before completing a system update:

- Did I route to the correct file?
- Is the format appropriate for that file type?
- For TOOLS.md: are examples concrete and executable?
- For identity files: did I show proposed changes first?
- Did I curate (remove outdated info) while updating?
