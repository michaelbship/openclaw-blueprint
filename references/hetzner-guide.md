# Hetzner VPS Guide

This guide is for Alice to read and relay conversationally. Do NOT show
this file to the user directly. Walk them through it step by step.

## What We're Doing

Setting up a small cloud server (VPS) where Bob will run 24/7. This is
Bob's home — a computer in a data center that's always on, even when
your laptop is closed.

**Cost:** ~$4/month (less than a coffee)

## Step 1: Create a Hetzner Account

1. Go to: https://console.hetzner.cloud/
2. Click "Register" and create an account
3. You'll need a credit card for verification
4. Verify your email

"This is like signing up for any online service. The credit card is
for the ~$4/month server cost."

## Step 2: Create a New Project

1. After logging in, click "+ New Project"
2. Name it "bob" (or whatever you want)
3. Click into the project

## Step 3: Set Up SSH Key

Before creating the server, Alice needs to check for an SSH key.

```bash
# Alice checks for existing SSH key
ls ~/.ssh/id_*.pub 2>/dev/null

# If no key exists, generate one:
ssh-keygen -t ed25519 -C "bob-vps" -f ~/.ssh/id_ed25519 -N ""

# Show the public key for the user to copy:
cat ~/.ssh/id_ed25519.pub
```

"I need to set up a secure connection to your server. Let me check
if you already have an SSH key..."

After getting the public key content:
1. In the Hetzner project, go to Security → SSH Keys
2. Click "Add SSH Key"
3. Paste the public key Alice showed
4. Name it "my-mac" or similar

## Step 4: Create the Server

1. Click "Add Server" (big blue button)
2. **Location:** Choose the closest to you
   - US East Coast → Ashburn
   - US West Coast → Hillsboro
   - Europe → Falkenstein, Nuremberg, or Helsinki
   - "Pick whichever is closest to where you live"
3. **Image:** Ubuntu 24.04
4. **Type:** Shared vCPU → x86
   - CX22: 2 vCPU, 4 GB RAM — ~$4/month (recommended)
   - "This is plenty for Bob. He's efficient."
5. **Networking:** Leave defaults (Public IPv4 + IPv6)
6. **SSH Key:** Select the key you just added
7. **Name:** "bob" (or whatever they want)
8. Click "Create & Buy Now"

"It takes about 30 seconds to spin up. You'll see an IP address
when it's ready — paste that here."

## Step 5: Get the IP Address

The server page shows the IP address (something like 203.0.113.42).

"Copy that IP address and paste it here. I'll test the connection."

## What Alice Does Next

```bash
# Test SSH connection
ssh -o StrictHostKeyChecking=accept-new root@[IP] "echo 'Connection OK'"

# If this fails, common causes:
# - Wrong SSH key (check Step 3)
# - Server still starting (wait 30 seconds, retry)
# - Firewall (Hetzner's default allows SSH — shouldn't be an issue)
```

Then Alice proceeds with provision-vps.sh (Phase 4 of BOOTSTRAP.md).

## Alternative Providers

If Hetzner doesn't work (region restrictions, payment issues):

**DigitalOcean:**
- https://digitalocean.com
- Create Droplet → Ubuntu 24.04 → Basic → $6/month (cheapest)
- Same SSH key process
- Similar UI

**Linode (Akamai):**
- https://linode.com
- Create Linode → Ubuntu 24.04 → Shared CPU → $5/month
- Same SSH key process

**Vultr:**
- https://vultr.com
- Deploy Instance → Ubuntu 24.04 → Regular → $6/month

The provision-vps.sh script works on any Ubuntu 24.04 server regardless
of provider. Only the server creation steps differ.

## Common Problems

**"Permission denied (publickey)":**
- The SSH key on the server doesn't match your local key
- Check: `ssh -v root@[IP]` to see which key it's trying
- Fix: Add the correct public key in Hetzner console → SSH Keys

**"Connection timed out":**
- Server might still be starting (wait 1-2 minutes)
- Check server status in Hetzner console (should be "Running")
- Try: `ping [IP]` to check if it's reachable

**"Connection refused":**
- SSH service might not be running (rare on fresh Ubuntu)
- Use Hetzner's web console (click "Console" on server page) to debug

**Server costs more than expected:**
- Make sure you chose CX22 (not a larger plan)
- Hetzner charges hourly — you can delete and recreate anytime
- Snapshots and backups cost extra (skip for now)
