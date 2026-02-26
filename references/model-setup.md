# Model Setup Guide

This guide is for Alice to read and relay conversationally. Do NOT show
this file to the user directly. Walk them through it step by step.

## The Decision

Bob needs a paid model. There are two options:

### Option 1: Claude Max (Recommended)

- **Cost:** $100/month flat rate
- **What it is:** Anthropic's unlimited Claude access plan
- **Why it's best:** Flat rate means Bob can think as much as he needs.
  No surprise bills. No usage anxiety. Best model quality.
- **Signup:** https://console.anthropic.com
- **Steps:**
  1. Go to console.anthropic.com
  2. Create an account (email + password)
  3. Subscribe to the Max plan ($100/month)
  4. Go to API Keys → Create Key
  5. Copy the key (starts with `sk-ant-`)
  6. IMPORTANT: Save this key somewhere safe. You can't see it again.

### Option 2: OpenRouter (Budget Alternative)

Only offer this if the user pushes back on $100/month.

- **Cost:** $10-20/month pay-per-use (typical usage)
- **What it is:** API gateway that routes to Claude and other models
- **Why it's cheaper:** Pay only for what you use
- **Trade-off:** Per-message costs, slightly higher latency
- **Signup:** https://openrouter.ai
- **Steps:**
  1. Go to openrouter.ai
  2. Create an account
  3. Add credits ($20 to start)
  4. Go to Keys → Create Key
  5. Copy the key (starts with `sk-or-`)

## What NOT to Do

- **Never recommend OpenAI models.** They are too restrictive for
  OpenClaw's agentic workflows. Tool use breaks, refusals are common.
- **Never try to use Zen models.** Zen is OpenCode-only (Alice's world).
  OpenClaw does not support Zen models.
- **Never skip this step.** Bob cannot function without a model key.

## The Cost Pitch

If the user hesitates on cost, frame it this way:

"Compare to what people pay for AI tools that don't even talk to each
other: Superhuman $30 + Granola $19 + Notion AI $10 + Motion $34 +
Perplexity $20 = $113/month for five separate tools. Bob replaces
the need for most of these AND he gets smarter over time."

## After Getting the Key

- Store a note in MEMORY.md: "Model: Claude Max" or "Model: OpenRouter"
- Do NOT store the actual API key in any file in the repo
- You'll use the key during Phase 4 when configuring Bob on the VPS
