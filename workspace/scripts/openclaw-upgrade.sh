#!/bin/bash
# OpenClaw Safe Upgrade Script
#
# Safely upgrades OpenClaw to the latest version:
# 1. Commits and pushes workspace changes
# 2. Stops gateway
# 3. Upgrades npm package
# 4. Restarts gateway
# 5. Reports status
#
# Usage: nohup scripts/openclaw-upgrade.sh &

set -e

WORKSPACE="$HOME/.openclaw/workspace"
LOG="/tmp/openclaw-upgrade-$(date +%Y%m%d-%H%M%S).log"

log() {
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG"
}

log "=== OpenClaw Upgrade Started ==="

# Step 1: Save workspace state
log "Step 1: Saving workspace state..."
if [ -d "$WORKSPACE/.git" ]; then
  cd "$WORKSPACE"
  if ! git diff --quiet 2>/dev/null || ! git diff --cached --quiet 2>/dev/null; then
    git add -A
    git commit -m "auto: pre-upgrade snapshot $(date +%Y-%m-%d)" 2>/dev/null || true
    log "  Workspace changes committed"
  else
    log "  No uncommitted changes"
  fi
fi

# Step 2: Record current version
OLD_VERSION=$(openclaw --version 2>/dev/null || echo "unknown")
log "Step 2: Current version: $OLD_VERSION"

# Step 3: Stop gateway
log "Step 3: Stopping gateway..."
systemctl --user stop openclaw-gateway 2>/dev/null || true
sleep 2

# Step 4: Upgrade
log "Step 4: Upgrading OpenClaw..."
npm install -g openclaw@latest 2>&1 | tee -a "$LOG"

NEW_VERSION=$(openclaw --version 2>/dev/null || echo "unknown")
log "  New version: $NEW_VERSION"

# Step 5: Restart gateway
log "Step 5: Restarting gateway..."
systemctl --user start openclaw-gateway
sleep 3

# Step 6: Verify
if systemctl --user is-active openclaw-gateway &>/dev/null; then
  log "Step 6: Gateway is running"
  log "=== Upgrade Complete: $OLD_VERSION → $NEW_VERSION ==="
else
  log "Step 6: WARNING — Gateway failed to start!"
  log "  Check logs: openclaw logs --tail 50"
  log "  Attempting restart..."
  systemctl --user restart openclaw-gateway
  sleep 3
  if systemctl --user is-active openclaw-gateway &>/dev/null; then
    log "  Recovery successful"
  else
    log "  FAILED — Manual intervention needed"
    log "  Try: npm install -g openclaw@$OLD_VERSION"
  fi
fi

log "Log saved to: $LOG"
