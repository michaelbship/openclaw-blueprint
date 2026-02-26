#!/bin/bash
# Morning Briefing — Gather Phase
# Collects calendar and weather data for the LLM to interpret.
#
# Customize: Replace the example commands below with your actual
# data sources (Google Calendar MCP, weather API, etc.)

set -e

source "$(dirname "$0")/../../config.conf"

EVIDENCE_FILE="${DATA_DIR:-/tmp}/morning-briefing-evidence.md"
mkdir -p "$(dirname "$EVIDENCE_FILE")"

cat > "$EVIDENCE_FILE" << 'EOF'
# Morning Briefing Evidence

## Calendar
<!-- Replace with actual calendar data -->
<!-- Example: mcporter call google.list_calendar_events ... -->
No calendar data configured yet. Set up Google MCP to enable.

## Weather
<!-- Replace with actual weather data -->
<!-- Example: curl -s "wttr.in/YourCity?format=j1" -->
No weather data configured yet. Add a weather API or use wttr.in.

## Unread Priority Emails
<!-- Replace with actual email check -->
<!-- Example: mcporter call google.search_gmail_messages query="is:unread" -->
No email data configured yet. Set up Google MCP to enable.
EOF

echo "Evidence written to $EVIDENCE_FILE"
