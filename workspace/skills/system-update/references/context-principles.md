# Context Engineering Principles

How to write effective always-injected context for AI agents. These principles
are distilled from Anthropic's research and real-world experience.

Sources:
- Anthropic "Building Effective Agents" (Dec 2024)
- Anthropic "Writing Effective Tools for Agents" (Sep 2025)
- Anthropic "Effective Context Engineering for AI Agents" (Sep 2025)

---

## The Progressive Disclosure Model

Not everything belongs in always-injected context. Context is a finite resource
with diminishing returns — every token depletes the agent's attention budget.

| Layer | When loaded | What belongs here | Cost |
|-------|------------|-------------------|------|
| **TOOLS.md** | Every turn | Awareness + concrete invocation pattern | Paid every turn |
| **MEMORY.md** | Session start | Operational state, decisions, preferences | Paid once per session |
| **Skills** | On demand (description match) | Domain-specific doctrine | Paid only when triggered |
| **Reference docs** | On demand (explicit read) | Deep architecture, design principles | Paid only when needed |

**Rule of thumb:** For each piece of information, ask: "Can the agent discover
this on its own?" If yes, don't put it in always-injected context. Let the agent
load it just-in-time.

**Must be always-injected (agent cannot discover on its own):**
- That a capability exists
- The exact invocation pattern (what to type)
- 2-3 verified examples of the most common operations

**Should NOT be always-injected (agent can discover just-in-time):**
- Full parameter schemas (discoverable via `mcporter list --schema`)
- Domain-specific doctrine (discoverable via skills)
- Architecture details (ports, service names)

---

## The Right Altitude

From Anthropic's context engineering research:

> "The right altitude is the Goldilocks zone between two common failure modes."

**Too prescriptive:** Hardcoding complex brittle if-else logic in prompts.
Creates fragility and maintenance burden.

**Too vague:** High-level guidance that "falsely assumes shared context."
The agent can't act on abstract descriptions.

**Right altitude:** Specific enough to guide behavior (concrete commands),
flexible enough to provide heuristics rather than rigid rules.

---

## Principles Summary

1. **Write at the agent's interface layer.** If the agent uses `exec`, show shell
   commands. If the agent has native tools, show tool call syntax. Never describe
   tools at a different abstraction layer than what the agent can execute.

2. **Verified examples only.** Unverified examples mislead models more than no
   examples at all. Test every example before putting it in a description.

3. **Junior developer test.** Could a new hire read this and immediately do the
   right thing? If not, rewrite it.

4. **Every line earns its slot.** Context is finite. Each line in always-injected
   context must either establish awareness or provide a concrete action pattern.

5. **Progressive disclosure.** Put awareness + invocation pattern in TOOLS.md.
   Put full schemas behind a discovery command. Put domain doctrine in skills.
   Put deep docs in reference files.

6. **Concrete beats abstract.** When context sources compete, the one with
   copy-pasteable commands wins over the one with descriptions or tables.

7. **Curate ruthlessly.** Remove outdated info on every update. Context rot
   degrades performance across all models.
