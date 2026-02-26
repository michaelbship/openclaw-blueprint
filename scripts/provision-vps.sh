#!/bin/bash
set -e

echo ""
echo "  Bob — VPS Setup"
echo "  ==============="
echo ""

# --- System Updates ---
echo "[1/6] Updating system packages..."
export DEBIAN_FRONTEND=noninteractive
apt-get update -qq
apt-get upgrade -y -qq

# --- Install Node.js 22+ ---
echo "[2/6] Installing Node.js..."
if command -v node &>/dev/null && [ "$(node -v | sed 's/v//' | cut -d. -f1)" -ge 22 ]; then
  echo "  Node.js $(node -v) already installed"
else
  curl -fsSL https://deb.nodesource.com/setup_22.x | bash - >/dev/null 2>&1
  apt-get install -y -qq nodejs
  echo "  Node.js $(node -v) installed"
fi

# --- Install git ---
echo "[3/6] Installing git..."
if command -v git &>/dev/null; then
  echo "  git already installed"
else
  apt-get install -y -qq git
  echo "  git installed"
fi

# --- Install OpenClaw ---
echo "[4/6] Installing OpenClaw..."
if command -v openclaw &>/dev/null; then
  echo "  OpenClaw already installed ($(openclaw --version 2>/dev/null || echo 'unknown version'))"
else
  npm install -g openclaw 2>/dev/null
  echo "  OpenClaw installed"
fi

# --- Deploy Workspace ---
echo "[5/6] Deploying workspace..."
WORKSPACE="$HOME/.openclaw/workspace"
TEMP_DIR=$(mktemp -d)

# Clone the blueprint repo to a temp location
git clone --depth 1 https://github.com/michaelbship/openclaw-blueprint "$TEMP_DIR/blueprint" 2>/dev/null

# Create workspace directory
mkdir -p "$WORKSPACE"

# Copy only workspace/ contents (Bob's world) into the actual workspace
if [ -d "$TEMP_DIR/blueprint/workspace" ]; then
  cp -r "$TEMP_DIR/blueprint/workspace/"* "$WORKSPACE/" 2>/dev/null || true
  cp -r "$TEMP_DIR/blueprint/workspace/".[!.]* "$WORKSPACE/" 2>/dev/null || true
  echo "  Workspace files deployed to $WORKSPACE"
else
  echo "  ERROR: workspace/ directory not found in blueprint repo"
  rm -rf "$TEMP_DIR"
  exit 1
fi

# Clean up temp clone
rm -rf "$TEMP_DIR"

# Initialize a fresh git repo in the workspace (Bob's own history)
if [ ! -d "$WORKSPACE/.git" ]; then
  git -C "$WORKSPACE" init -q
  git -C "$WORKSPACE" add -A
  git -C "$WORKSPACE" commit -m "Initial workspace deployment" -q
  echo "  Git initialized in workspace"
fi

# --- Create outputs directory ---
echo "[6/6] Finalizing..."
mkdir -p "$WORKSPACE/outputs"

echo ""
echo "  ======================="
echo "  Setup complete!"
echo "  ======================="
echo ""
echo "  Workspace: $WORKSPACE"
echo ""
echo "  Next step: Run openclaw onboard to configure your model and start Bob."
echo ""
echo "  Example:"
echo "    openclaw onboard --workspace $WORKSPACE"
echo ""
