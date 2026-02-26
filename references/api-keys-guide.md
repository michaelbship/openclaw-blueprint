# Search API Keys Guide

This guide is for Alice to read and relay conversationally. Do NOT show
this file to the user directly. Walk them through one API at a time.

## Overview

Bob uses multiple search engines for research. Each has a free tier.
Set them up one at a time — don't overwhelm the user.

Order: Tavily first (most useful), then Brave, then Exa (optional).

## Tavily (Do This First)

**What it is:** AI-optimized search engine. Returns clean, structured
results perfect for AI agents. This is Bob's primary search tool.

**Cost:** Free tier — 1,000 searches/month (plenty for personal use)

**Signup:**
1. Go to: https://tavily.com
2. Click "Get API Key" or "Sign Up"
3. Create an account (email + password)
4. The API key is shown on the dashboard
5. Copy it — starts with `tvly-`

**Key format:** `tvly-` followed by alphanumeric characters

## Brave Search

**What it is:** Privacy-focused web search. Good complement to Tavily —
different results, different strengths.

**Cost:** Free tier — 2,000 searches/month

**Signup:**
1. Go to: https://brave.com/search/api/
2. Click "Get Started"
3. Choose the "Free" plan
4. Create an account
5. Copy the API key from the dashboard
6. Starts with `BSA`

**Key format:** `BSA` followed by alphanumeric characters

## Exa (Optional)

**What it is:** Semantic search — finds content by meaning, not just
keywords. Great for finding similar articles, research papers, niche
topics.

**Cost:** Free tier — 1,000 searches/month

**Signup:**
1. Go to: https://exa.ai
2. Click "Get API Key" or "Sign Up"
3. Create an account
4. Copy the API key from the dashboard

**Key format:** Alphanumeric string

## Configuring on the VPS

After getting each key, Alice updates Bob's MCP config via SSH:

```bash
# Read current config
ssh root@[VPS_IP] "cat ~/.openclaw/workspace/config/mcporter.json"

# Update config with real keys (use sed or edit directly)
# Alice handles this — the user just provides the keys
```

The config file is at `~/.openclaw/workspace/config/mcporter.json`.
Each search server has an `env` section where the API key goes.

## Testing

After all keys are configured:

1. Restart MCP servers: `ssh root@[VPS_IP] "openclaw restart"`
2. Ask Bob in Discord: "Research the latest developments in [topic]"
3. Bob should cite sources from multiple search engines
4. If a specific engine fails, check its key in mcporter.json

## Common Problems

**"API key invalid" errors:**
- Keys are case-sensitive. Check for extra spaces.
- Some keys take a few minutes to activate after creation.
- Try the key in a browser: `curl -H "X-API-Key: [KEY]" https://api.tavily.com/health`

**Bob doesn't use search:**
- Make sure mcporter.json is properly formatted (valid JSON)
- Restart after config changes: `openclaw restart`
- Check that the MCP server names match what Bob's skills expect

**Free tier limits:**
- 1,000 Tavily + 2,000 Brave + 1,000 Exa = 4,000 searches/month
- More than enough for personal use
- If hitting limits, consider Tavily's paid plan ($50/mo for 10,000)
