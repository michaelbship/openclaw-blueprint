# Skill Templates

Starter SKILL.md files for each skill type. Copy the relevant template and customize.

---

## 1. Simple Utility

Single tool, no external deps, no logic.

```yaml
---
name: tool-name
description: |
  [What it does]. Use when user asks to [trigger phrase 1] or [trigger phrase 2].
---
```

```markdown
# Tool Name

Quick one-liner:

\`\`\`bash
command --args
\`\`\`

Options:
- `--opt1` — Description
- `--opt2` — Description

Examples:
- "Do X" → `command --opt1 value`
- "Do Y" → `command --opt2 value`
```

---

## 2. MCP Orchestration

Wraps existing MCP tools with judgment and workflow.

```yaml
---
name: service-action
description: |
  Interact with [Service] for [purpose]. Use when user asks to:
  - [trigger phrase 1]
  - [trigger phrase 2]
---
```

```markdown
# Service Action Doctrine

## Prerequisites
- MCP: [server name] (via mcporter)

## Available Tools

| Tool | Use For |
|------|---------|
| `server.tool_a` | Description |
| `server.tool_b` | Description |

## Workflow
1. [Step 1]
2. [Step 2]

## Judgment Rules
- [Priority rule]
- [Format rule]

## Output Format
[Show exact format with example]
```

---

## 3. Gather-Interpret

Data collection via script + LLM analysis.

```yaml
---
name: task-name
description: |
  [What it does]. Use when user asks to [trigger] or says "[phrase]".
---
```

```markdown
# Task Name Doctrine

## Prerequisites
- Gather script: `{baseDir}/scripts/gather.sh`
- Evidence file: `data/task-name-evidence.md`

## Workflow

### Phase 1: Gather
\`\`\`bash
bash {baseDir}/scripts/gather.sh
\`\`\`

### Phase 2: Interpret
Read evidence file. Apply judgment rules below.

### Phase 3: Act
Deliver formatted output.

## Judgment Rules
- **Priority 1:** [What's most important]
- **Priority 2:** [What's next]

## Failure Recovery
- If gather script fails: [what to do]
- If MCP is down: [fallback]
```

---

## 4. Multi-Step Workflow

Complex skill with scripts, references, and multiple phases.

```yaml
---
name: workflow-name
description: |
  [What it does]. Use when user asks to:
  - [trigger 1]
  - [trigger 2]
---
```

```markdown
# Workflow Name Doctrine

## Prerequisites
- Scripts: `{baseDir}/scripts/`
- References: see [detail.md](references/detail.md)

## Workflow

### Phase 1: [Name]
[Description + commands]

### Phase 2: [Name]
[Description + commands]

## Decision Points

| Condition | Action |
|-----------|--------|
| [If X] | [Do A] |
| [If Y] | [Do B] |
```
