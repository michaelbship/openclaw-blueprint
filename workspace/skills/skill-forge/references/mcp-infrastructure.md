# MCP Infrastructure Reference

## How the MCP Stack Works

All MCP servers run through `mcporter`, a unified CLI and daemon that manages
server lifecycles. Servers are defined in `config/mcporter.json`.

### Two Ways to Call MCPs

**Mode A: From the agent (context-aware)**
```bash
mcporter call <server>.<tool> key=value
mcporter call brave.brave_web_search query="topic" count=5
```
Full metadata, schemas, and descriptions available. ~800ms overhead.

**Mode B: From scripts (performance)**
```bash
curl -s -X POST http://127.0.0.1:<port>/rpc \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","method":"tools/call","params":{"name":"tool","arguments":{}},"id":1}'
```
~30ms round-trip. Use in gather scripts for parallel batch calls.

Both modes hit the same running process. Shared auth, caches, state.

---

## How to Add a New MCP Server

### Step 1: Find the server package
Check Smithery (smithery.ai), mcp.so, or the provider's own docs.

### Step 2: Add to mcporter config

**For npm packages (most common):**
```bash
mcporter config add <name> \
  --command "npx" \
  --arg "-y" --arg "<package-name>" \
  --env API_KEY=value \
  --persist config/mcporter.json
```

**For HTTP-based servers:**
```bash
mcporter config add <name> \
  --url "http://127.0.0.1:<port>/mcp" \
  --persist config/mcporter.json
```

### Step 3: Restart daemon
```bash
mcporter daemon restart
```

### Step 4: Verify
```bash
mcporter daemon status              # Should show new server
mcporter list <name>                # List available tools
mcporter list <name> --schema       # Full tool schemas
mcporter call <name>.<tool> ...     # Test a call
```

### Step 5: Document
Update TOOLS.md with the new server entry and invocation examples.

---

## Server Types

| Type | Config Pattern | When |
|------|---------------|------|
| **npx** | `command: "npx", args: ["-y", "package"]` | Most community MCPs |
| **Local binary** | `command: "/usr/bin/binary"` | Installed globally via npm -g |
| **HTTP** | `baseUrl: "http://127.0.0.1:PORT"` | Servers with native HTTP transport |

## Lifecycle Options

| Mode | Config | When |
|------|--------|------|
| `keep-alive` | `"lifecycle": "keep-alive"` | Frequently used servers |
| Default (on-demand) | No lifecycle key | Rarely used servers (spins up per-call) |

---

## Config File

**Location:** `config/mcporter.json`

Structure:
```json
{
  "mcpServers": {
    "<name>": {
      "description": "Human-friendly description",
      "command": "binary or npx",
      "args": ["arguments"],
      "env": { "API_KEY": "value" },
      "lifecycle": "keep-alive"
    }
  }
}
```

---

## Troubleshooting

| Problem | Check |
|---------|-------|
| Server not responding | `mcporter daemon status` — is it listed? |
| Server listed but calls fail | `mcporter daemon restart <server>` |
| All servers down | `mcporter daemon restart` |
| New server not appearing | Did you restart daemon after config change? |
