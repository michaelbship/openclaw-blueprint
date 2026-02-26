---
name: research
description: |
  Perform multi-layered research using the search stack (Brave, Exa, Tavily, Perplexity).
  Use when user asks to:
  - "research [topic]"
  - "look into [topic]"
  - "find out about [topic]"
  - "what's the latest on [topic]"
  - "deep dive on [topic]"
  - "investigate [topic]"
  - "compare X vs Y"
---

# Research Doctrine

Use this skill when tasked with discovery, deep dives, or news trends.

## Rule Zero: Tool Selection

**Default:** `tavily_search` with `includeRawContent: true`

Why: Fastest (1-2s) + returns full content per result. One call does the job.

### Decision Table

| Task | Primary Tool | Latency | When to Use |
|------|--------------|---------|-------------|
| General research | Tavily + `includeRawContent` | 1-2s | Default for most queries |
| Quick entity lookup | Brave | 4-5s | Need broad index, snippets OK |
| "Explain X" questions | Perplexity (`perplexity_ask`) | 3s | Question asks for synthesis, not facts |
| Deep technical / papers | Exa + `livecrawl: "preferred"` | 7s | Research papers, technical docs |
| Known URL only | web_fetch | varies | You have a specific source URL |

### Examples

**Quick fact:** "What's the current Bitcoin price?"
→ Tavily (default) — one call gives current data + sources

**Deep dive:** "Research Lightning adoption in 2025"
→ Tavily first → Exa for papers if needed

**Synthesis:** "Explain how Lightning channels work"
→ Perplexity — asks for explanation, not facts

**web_fetch is a fallback, not a default.** Use it only for known URLs or when Tavily content is insufficient.

---

## The Execution Pipeline

### Phase 1: Raw Discovery
Use the primary tool from the decision table above.
**Rule:** Do not analyze results yet. Just gather.
- Use at least 2 different search tools for important research
- Capture URLs from results — you will need them for citations

### Phase 2: Evidence Formatting
Present the findings clearly.
- Every factual claim must have a source URL
- Use `<url>` format on Discord to suppress embeds and keep links clickable
- Never wrap URLs inside markdown formatting that breaks them

### Phase 3: Synthesis
Only after showing raw evidence, perform the synthesis. Or call Perplexity if an "AI-distilled" view is requested as a separate layer.
- Clearly separate what the sources say from what you're inferring
- Flag anything uncertain

---

## Output Format (MANDATORY)

Every research response MUST end with a skill + sources block:

```
---
**Skill:** research
**Tools:** [list of search tools used]
- [Claim 1] → <source URL>
- [Claim 2] → <source URL>
```

---

## Self-Check (run before responding)
- Did I select the right tool based on the decision table?
- Did I use at least 2 search tools for important research?
- Does every specific factual claim have a source URL?
- Are all URLs bare/clickable (not inside markdown formatting)?
- Did I include the sources block at the end?
- Did I separate raw findings from my own synthesis?

---

## Failure Recovery

### MCP Server Down

| Failed Tool | Fallback | Command to Restart |
|-------------|----------|-------------------|
| Tavily | Brave or Exa | `mcporter daemon restart tavily` |
| Brave | Tavily | `mcporter daemon restart brave` |
| Exa | Tavily | `mcporter daemon restart exa` |
| Perplexity | Skip synthesis layer | `mcporter daemon restart perplexity` |

**Process:**
1. Try the fallback tool
2. If all MCPs down: `mcporter daemon restart` (restarts all)
3. Report the outage to your user

### No Results Found
1. Try a different search tool (tool diversity)
2. Broaden the query
3. Report honestly: "No relevant results found for [query]. Tried: Tavily, Exa."
