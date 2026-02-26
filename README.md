# AI Agent Blueprint

A battle-tested AI agent configuration. ~$4,000 and hundreds of hours
of iteration, given away for free.

## What This Is

Everything you need to run a personal AI agent that remembers everything,
researches the web, builds new capabilities for itself, and runs 24/7
on your own server.

## Setup (3 Pastes)

Open Terminal on your Mac (Cmd+Space → "Terminal" → Enter), then:

**1. Install the setup agent:**
```
curl -fsSL https://opencode.ai/install | bash && echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && export PATH="$HOME/.local/bin:$PATH"
```

**2. Launch it:**
```
opencode
```

**3. Paste this into the text box:**
```
Clone https://github.com/michaelbship/openclaw-blueprint to ~/blueprint, then read BOOTSTRAP.md and follow it step by step. You are Alice.
```

Alice wakes up and handles everything from here. No cost. No API key.

## What Happens Next

1. Alice introduces herself and asks your name
2. Alice shows you what an AI agent can do (free demo)
3. Alice helps you deploy Bob — your permanent agent on a $4/month server
4. Alice connects Discord so you can talk to Bob from anywhere
5. Alice sets up web research capabilities
6. Bob runs 24/7. Alice becomes your rescue tool.

## What's Inside

- **BOOTSTRAP.md** — Alice's setup playbook
- **workspace/AGENTS.md** — Battle-tested operational rules (300+ hours of iteration)
- **9 custom skills** — Research, Skill Forge, Artifact Writer, and more
- **Memory architecture** — Solves the "AI amnesia" problem
- **Self-expanding system** — The agent builds its own capabilities

## The Architecture

**Alice** runs locally via [OpenCode](https://opencode.ai) (free). She's your
setup assistant and mechanic.

**Bob** runs on a VPS via [OpenClaw](https://openclaw.ai). He's your permanent
agent — always on, always learning.

They never share files at runtime. Alice deploys Bob's workspace to the VPS,
then steps back. Bob takes it from there.

## Cost

| Component | Cost |
|-----------|------|
| Alice (OpenCode) | Free |
| VPS (Hetzner CX22) | ~$4/month |
| Bob's brain (Claude Max) | $100/month |
| Search APIs (Tavily, Brave, Exa) | Free tiers |

Total: ~$104/month for a personal AI agent that runs 24/7.

## License

MIT
