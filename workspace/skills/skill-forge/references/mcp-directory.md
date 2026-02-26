# MCP Directory & Quality Criteria

## Where to Find MCP Servers

| Source | URL | What It Has |
|--------|-----|-------------|
| **Smithery** | smithery.ai | Curated MCP directory with ratings and reviews |
| **mcp.so** | mcp.so | MCP server registry, searchable |
| **GitHub Official** | github.com/modelcontextprotocol | Official/reference MCP servers |
| **Provider Docs** | [per service] | Check if the company publishes their own MCP |
| **npm** | npmjs.com | Search for `mcp-server-*` or `*-mcp` packages |

Always check **provider docs first** — if the company publishes their own MCP, use that.

---

## Quality Criteria

### Prefer (in order)

1. **Native/official** — Published by the service provider
2. **Well-maintained community** — Recent commits (<3 months), issues addressed
3. **High usage** — Stars, forks, npm downloads indicate reliability
4. **TypeScript/Node** — Fits the mcporter stack natively

### Avoid

- Abandoned (no commits in >6 months)
- No documentation
- Unresolved critical issues
- Requires external hosted service
- Python-only with complex deps (acceptable if only option)

---

## Evaluation Checklist

Before installing a new MCP server:

- [ ] Is there a native/official version?
- [ ] When was the last commit? (>6 months = red flag)
- [ ] Are issues being responded to?
- [ ] Does it have documentation?
- [ ] Can it run via npx or does it need global install?
- [ ] Does it need API keys? Do we have them?
- [ ] Have you tested it locally before adding to config?

---

## Decision Flow

```
Need to integrate with [Service]?
│
├─ Check: Does [Service] publish an official MCP?
│  └─ Yes → Use it
│  └─ No ↓
│
├─ Check: Is there one on Smithery/mcp.so with good ratings?
│  └─ Yes + well-maintained → Use it
│  └─ No ↓
│
├─ Check: Does [Service] have a good REST API?
│  └─ Yes → Write a script with direct API calls
│  └─ No ↓
│
└─ Manual workflow in skill instructions. Flag the gap.
```
