#!/bin/bash
# verify-bob.sh — Health check for Bob's deployment
# Alice runs this after provisioning to verify everything is working.

echo ""
echo "  Bob — Health Check"
echo "  =================="
echo ""

WORKSPACE="$HOME/.openclaw/workspace"
PASS=0
FAIL=0

check() {
  local label="$1"
  local result="$2"
  if [ "$result" = "ok" ]; then
    echo "  [OK]   $label"
    PASS=$((PASS + 1))
  else
    echo "  [FAIL] $label"
    FAIL=$((FAIL + 1))
  fi
}

# Check OpenClaw installed
if command -v openclaw &>/dev/null; then
  check "OpenClaw installed" "ok"
else
  check "OpenClaw installed" "fail"
fi

# Check Node.js version
if command -v node &>/dev/null && [ "$(node -v | sed 's/v//' | cut -d. -f1)" -ge 22 ]; then
  check "Node.js 22+" "ok"
else
  check "Node.js 22+" "fail"
fi

# Check workspace exists
if [ -d "$WORKSPACE" ]; then
  check "Workspace directory" "ok"
else
  check "Workspace directory" "fail"
fi

# Check critical files
for file in AGENTS.md SOUL.md IDENTITY.md TOOLS.md HEARTBEAT.md; do
  if [ -f "$WORKSPACE/$file" ]; then
    check "$file" "ok"
  else
    check "$file" "fail"
  fi
done

# Check skills directory
SKILL_COUNT=$(find "$WORKSPACE/skills" -name "SKILL.md" 2>/dev/null | wc -l | tr -d ' ')
if [ "$SKILL_COUNT" -ge 5 ]; then
  check "Skills ($SKILL_COUNT found)" "ok"
else
  check "Skills ($SKILL_COUNT found, expected 9)" "fail"
fi

# Check config
if [ -f "$WORKSPACE/config/mcporter.json" ]; then
  check "MCP config" "ok"
else
  check "MCP config" "fail"
fi

# Check OpenClaw gateway
if command -v openclaw &>/dev/null; then
  if openclaw health &>/dev/null; then
    check "Gateway running" "ok"
  else
    check "Gateway running (not started yet — normal before onboard)" "fail"
  fi
fi

echo ""
echo "  Results: $PASS passed, $FAIL failed"
echo ""

if [ "$FAIL" -eq 0 ]; then
  echo "  Everything looks good!"
else
  echo "  Some checks failed. Alice will help fix these."
fi
echo ""
