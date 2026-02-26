# RECOVERY.md — Emergency Recovery Guide

## Architecture Overview

Bob runs on OpenClaw, a persistent agent platform on your VPS.

```
~/.openclaw/
├── openclaw.json          # Runtime config (models, channels, hooks)
└── workspace/             # Bob's operational files (this directory)
    ├── AGENTS.md          # Operational rules
    ├── SOUL.md            # Personality
    ├── IDENTITY.md        # Who Bob is
    ├── USER.md            # Who you are
    ├── MEMORY.md          # Long-term memory
    ├── TOOLS.md           # Tool notes
    ├── HEARTBEAT.md       # Periodic check config
    ├── config/            # MCP server config
    ├── skills/            # Custom skills
    ├── jobs/              # Scheduled jobs
    ├── scripts/           # Utility scripts
    ├── memory/            # Daily logs
    └── outputs/           # Generated artifacts
```

## Critical Files (NEVER Delete)

| File | What Happens If Lost |
|------|---------------------|
| `~/.openclaw/openclaw.json` | Bob forgets his model config, channels, and auth tokens |
| `workspace/AGENTS.md` | Bob loses all operational rules (biggest loss) |
| `workspace/SOUL.md` | Bob loses his personality |
| `workspace/USER.md` | Bob forgets who you are |
| `workspace/MEMORY.md` | Bob loses all learned context |
| `workspace/config/mcporter.json` | Bob loses access to search tools |

## Quick Diagnostics

```bash
# Is OpenClaw running?
openclaw health

# Check gateway status
systemctl --user status openclaw-gateway

# Check logs (last 50 lines)
openclaw logs --tail 50

# Is the workspace intact?
ls ~/.openclaw/workspace/AGENTS.md

# Are MCP servers running?
mcporter daemon status
```

## Common Recovery Scenarios

### Bob Won't Start

```bash
# Check if Node.js is working
node -v   # Should be 22+

# Check if OpenClaw is installed
openclaw --version

# Try restarting
systemctl --user restart openclaw-gateway

# Check logs for errors
openclaw logs --tail 100
```

### Bob Doesn't Respond in Discord

1. Check gateway is running: `openclaw health`
2. Check Discord channel config: look in `~/.openclaw/openclaw.json` under `channels`
3. Check bot token is valid (might need regeneration in Discord Developer Portal)
4. Restart: `systemctl --user restart openclaw-gateway`

### Search Tools Not Working

```bash
# Check MCP server status
mcporter daemon status

# Restart all MCP servers
mcporter daemon restart

# Check config for API keys
cat ~/.openclaw/workspace/config/mcporter.json

# Test a specific search
mcporter call brave.brave_web_search query="test" count=1
```

### Corrupted npm / OpenClaw

```bash
# Nuclear option: reinstall OpenClaw
npm install -g openclaw@latest

# If npm itself is broken
curl -fsSL https://deb.nodesource.com/setup_22.x | bash -
apt-get install -y nodejs
npm install -g openclaw@latest
```

### Lost Workspace Files

If workspace files are corrupted but git history is intact:

```bash
cd ~/.openclaw/workspace
git log --oneline -10        # Check recent commits
git checkout -- AGENTS.md    # Restore specific file from last commit
```

If git is gone too, re-deploy from the blueprint:

```bash
# Re-run the provision script (won't overwrite existing config)
bash /tmp/provision-vps.sh
```

**Important:** This restores template files. You'll lose any customizations
Bob made to his workspace. MEMORY.md and daily logs will be reset.

## Safe Restart Script

```bash
# Always use the safe restart (detaches properly)
nohup ~/.openclaw/workspace/scripts/safe-restart.sh &
```

Never run `systemctl restart` directly from inside Bob's session — it kills
the connection mid-message.

## Getting Help

If you set up Bob using Alice:
1. Open Terminal on your Mac
2. Type `alice` (or `cd ~/blueprint && opencode`)
3. Tell Alice what's wrong — she can SSH in and diagnose

Alice has access to the same scripts and can run diagnostics remotely.
