---
name: model-config-manager
description: |
  Add or update model providers and aliases on your OpenClaw instance.
  Use when user asks to:
  - "Add [provider] provider with models..."
  - "Set up [provider] with aliases..."
  - "Configure [provider] models..."
  - "Add these models from [provider]..."
  Automatically researches provider docs, checks for alias conflicts, and deploys safely.
---

# Model Config Manager

Add model providers and aliases to your OpenClaw instance via natural language.

## Quick Start

User: "Add Groq provider with their fast models, sensible aliases"

Agent will:
1. Research Groq's available models
2. Check existing aliases
3. Generate non-conflicting aliases
4. Show plan, get approval + API key
5. Deploy

---

## Workflow

### Phase 1: Understand Request

Extract from user's request:
- **Provider:** Which provider (groq, together, fireworks, custom)?
- **Models:** Specific models or category ("fast models", "all")?
- **API Key:** User has it, or need to find it?

**MANDATORY:** Ask for any missing info before proceeding.

---

### Phase 2: Research Provider

Use the `research` skill to discover:

1. **API Documentation** — Base URL, auth method, rate limits
2. **Available Models** — Model IDs, context windows, capabilities, pricing
3. **OpenClaw Integration** — Check if `api: "openai-completions"` works (most do)

**Output of this phase:** Provider config with model list.

---

### Phase 3: Discover Current State

Check current config:

```bash
python3 -c "import json; d=json.load(open('$HOME/.openclaw/openclaw.json')); print('Providers:', list(d['models']['providers'].keys())); print('Aliases:', list(d['agents']['defaults']['models'].keys()))"
```

**Extract:**
- Existing providers (avoid duplicates)
- Existing aliases (avoid conflicts)

---

### Phase 4: Plan

Generate the plan and show user:

```
Will add:
  Provider: groq (X models)
  Aliases:
    groq70 → groq/llama-3.3-70b-versatile
    groq8 → groq/llama-3.1-8b-instant
  Existing aliases preserved: [list a few]

API key: [where to get it or "already have it"]
```

**MANDATORY:** Get user approval before deploying.

---

### Phase 5: Deploy

Execute via the scripts:

```bash
python3 {baseDir}/scripts/deploy_config.py \
  --provider-json '[config]' \
  --api-key [KEY] \
  --aliases '[alias mapping]'
```

The scripts enforce:
- Protected keys preserved (tokens, bindings, hooks)
- Backup created before changes
- JSON validation before write

---

### Phase 6: Verify

After deploy:
1. Check gateway is active
2. Verify provider appears in config
3. Test one alias if possible: `/model [alias]`

---

## Protected Keys

The scripts NEVER modify these:
- `channels.discord.token`
- `channels.telegram.botToken`
- `gateway.auth.token`
- `bindings`
- `hooks`

---

## Failure Recovery

| Failure | Action |
|---------|--------|
| Research fails | Ask user for provider docs URL |
| Alias conflict | Generate alternative aliases, show options |
| Deploy fails | Backup exists, show rollback command |
| Gateway won't restart | Check logs, offer restore from backup |

**Rollback:**
```bash
cp ~/.openclaw/openclaw.json.bak.[timestamp] ~/.openclaw/openclaw.json
systemctl --user restart openclaw-gateway
```
