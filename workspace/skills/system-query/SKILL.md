---
name: system-query
description: |
  Find information about how your operational system works — tools, models,
  configuration, skills, memory, and agent setup. Use when user asks:
  - "how does X work in our system"
  - "what model am I running"
  - "what tools do we have"
  - "what skills exist"
  - "what's in memory about X"
  - "how is X configured"
  - "check workspace"
---

# System Query

Use this skill to answer questions about how your operational system works.
This covers tools, models, configuration, skills, memory, and agent setup.

## Workspace Map

Don't read every file. Route to the right one based on what's being asked.

### Always-Injected (already in your context every turn)

| File | What's there | You already have it |
|------|-------------|-------------------|
| `TOOLS.md` | Tool awareness + invocation patterns | Yes — just reference it |
| `AGENTS.md` | Operating instructions, behavioral rules | Yes — just reference it |
| `SOUL.md` | Persona, tone, boundaries | Yes — just reference it |
| `USER.md` | Who your user is | Yes — just reference it |
| `IDENTITY.md` | Agent's name, vibe | Yes — just reference it |
| `HEARTBEAT.md` | Heartbeat checklist | Yes — just reference it |

**If the answer is in one of these files, don't re-read it. It's already in context.**

### Session-Start (loaded once per session)

| File | What's there | How to access |
|------|-------------|---------------|
| `MEMORY.md` | Curated operational state, decisions, preferences | Read the file |
| `memory/YYYY-MM-DD.md` | Daily logs (today + yesterday auto-loaded) | Read by date |

### On-Demand (load when needed)

| File | What's there | How to access |
|------|-------------|---------------|
| `skills/*/SKILL.md` | Domain doctrine for specific tasks | Read the specific skill |
| `config/mcporter.json` | MCP server configuration | Read the file |
| `~/.openclaw/openclaw.json` | Agent runtime config (models, channels) | Read the file |

### Key Reference Table

| Question | Read this |
|----------|-----------|
| "What model am I running?" | `~/.openclaw/openclaw.json` → `models` section |
| "What MCP servers are configured?" | `config/mcporter.json` |
| "What happened yesterday?" | `memory/YYYY-MM-DD.md` for yesterday's date |
| "What skills exist?" | `ls skills/` then read specific SKILL.md files |
| "What's configured?" | `config/mcporter.json` + `~/.openclaw/openclaw.json` |

---

## Related Skills

- `system-update`: When the answer to the query leads to a change
- `research`: When the answer is on the web, not in your workspace
