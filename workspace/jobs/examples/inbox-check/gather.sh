#!/bin/bash
# Inbox Check — Gather Phase
# Checks for unread emails and flags urgent ones.
#
# Customize: Replace the example commands below with your actual
# email data source (Google MCP, etc.)

set -e

source "$(dirname "$0")/../../config.conf"

EVIDENCE_FILE="${DATA_DIR:-/tmp}/inbox-check-evidence.md"
mkdir -p "$(dirname "$EVIDENCE_FILE")"

cat > "$EVIDENCE_FILE" << 'EOF'
# Inbox Check Evidence

## Unread Emails (Last 2 Hours)
<!-- Replace with actual email data -->
<!-- Example: mcporter call google.search_gmail_messages query="is:unread newer_than:2h" -->
No email data configured yet. Set up Google MCP to enable.

## Flagged / Urgent
<!-- Replace with urgency filter -->
<!-- Example: filter for keywords: urgent, asap, action required, deadline -->
No urgency filter configured yet.
EOF

echo "Evidence written to $EVIDENCE_FILE"
