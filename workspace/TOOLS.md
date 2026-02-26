# TOOLS.md — Local Notes

Skills define *how* tools work. This file is for *your* specifics — the stuff
that's unique to your setup.

## Draft Messages

When providing text drafts for your user to copy (emails, Slack messages, etc.):
1. **Send the draft as its own separate message first** (no preamble, no commentary)
2. **Follow up with any notes/comments in a second message**

This lets them long-press the draft on mobile and copy it cleanly.

---

## MCP Tools via mcporter

**Config:** `config/mcporter.json`

### Available MCP Servers

| Server | Tools | Use For |
|--------|-------|---------|
| `brave` | 6 | Web search, news, images, local |
| `exa` | 3 | Deep research, similar content |
| `tavily` | 5 | News, SEO-clean results |
| `perplexity` | 4 | Synthesis, briefings |

### How to Call MCP Tools

```bash
# Search examples
mcporter call brave.brave_web_search query="topic" count=5
mcporter call exa.web_search_exa query="topic" numResults=5
mcporter call tavily.tavily_search query="topic" maxResults=5

# List all tools for a server
mcporter list <server> --schema
```

### Daemon Management

```bash
mcporter daemon status   # Check running servers
mcporter daemon restart  # Restart all
```

### Search Stack
- **Tavily:** DEFAULT. 1-2s latency. Use `includeRawContent=true` for full content.
- **Perplexity:** AI synthesis, "explain X" questions. 3s latency.
- **Brave:** Entity discovery, broad index. 4-5s latency.
- **Exa:** Deep research, papers. Use `livecrawl="preferred"`. 7s latency.

---

## What Goes Here

Things like:
- SSH hosts and aliases
- Camera names and locations
- Preferred voices for TTS
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### SSH
- home-server → 192.168.1.100, user: admin

### TTS
- Preferred voice: "Nova" (warm, slightly British)
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can
update skills without losing your notes, and share skills without leaking
your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
