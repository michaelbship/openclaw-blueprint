# Discord Setup Guide

This guide is for Alice to read and relay conversationally. Do NOT show
this file to the user directly. Walk them through it step by step.

## What We're Doing

Setting up a Discord bot so the user can talk to Bob from Discord on
their phone, desktop, or browser. This takes about 5 minutes.

## Prerequisites

- User needs a Discord account (free)
- User needs a Discord server (they can create one for free)

If they don't have Discord: "Discord is a free messaging app. Download
it at discord.com, create an account, and create a server — just click
the + button on the left sidebar. Name it whatever you want."

## Step-by-Step

### Step 1: Open the Developer Portal

Go to: https://discord.com/developers/applications

"Open this link in your browser. You may need to log in with your
Discord account."

### Step 2: Create a New Application

- Click "New Application" (top right, blue button)
- Name it "Bob" (or whatever they want)
- Click "Create"

### Step 3: Create the Bot

- In the left sidebar, click "Bot"
- The bot is created automatically with the application
- Under "Token", click "Reset Token" then "Yes, do it!"
- Copy the token — it looks like a long string (~70 characters with
  two dots in it, like: `MTQ2...abc.GhK...xyz.Rq8...def`)
- IMPORTANT: "Copy this token and paste it here. You can't see it
  again after you leave this page."

### Step 4: Enable Privileged Gateway Intents

Still on the Bot page, scroll down to "Privileged Gateway Intents":
- Turn ON: Presence Intent
- Turn ON: Server Members Intent
- Turn ON: Message Content Intent
- Click "Save Changes"

"These permissions let Bob read and respond to messages. Without them,
Bob can see the channel but can't read what you type."

### Step 5: Generate the Invite Link

- In the left sidebar, click "OAuth2"
- Click "URL Generator"
- Under SCOPES, check: `bot`
- Under BOT PERMISSIONS, check:
  - Send Messages
  - Read Message History
  - Embed Links
  - Attach Files
  - Add Reactions
- Copy the generated URL at the bottom

### Step 6: Add Bot to Server

- Open the copied URL in your browser
- Select your server from the dropdown
- Click "Authorize"
- Complete the CAPTCHA

"Bob should now appear in your server's member list (he'll be offline
until we configure him on the VPS)."

### Step 7: Get the Channel ID

- In Discord, go to User Settings (gear icon) → Advanced → turn on
  "Developer Mode"
- Go back to your server
- Right-click the channel where you want Bob to listen
- Click "Copy Channel ID"

"Paste that channel ID here. It's a long number like 1234567890123456."

## What Alice Does Next

With the bot token and channel ID:

```bash
# SSH into the VPS and configure Discord
ssh root@[VPS_IP] "openclaw channels add discord --token '[BOT_TOKEN]' --channel '[CHANNEL_ID]'"
```

If the above command is interactive or fails, fall back to direct config:

```bash
ssh root@[VPS_IP] "openclaw channels add discord"
# Then follow prompts, or edit the config file directly
```

## Verification

After configuring:
1. Send a message in the Discord channel: "Hey Bob, are you there?"
2. Bob should respond within 10-30 seconds
3. If no response, check: `ssh root@[VPS_IP] "openclaw health"`

## Common Problems

**Bot appears offline in Discord:**
- Check that the gateway is running: `openclaw health`
- Check channel config: `cat ~/.openclaw/config/channels.json`
- Restart: `openclaw restart`

**Bot is online but doesn't respond:**
- Make sure Message Content Intent is enabled (Step 4)
- Make sure the channel ID is correct
- Check logs: `openclaw logs --tail 50`

**"Missing Permissions" error:**
- Re-invite the bot with the correct permissions (Step 5-6)
- Make sure the bot's role has permission to read/send in the channel

**Token doesn't work:**
- Tokens can only be viewed once. If lost, reset it (Step 3)
- Make sure you copied the full token (no extra spaces)
