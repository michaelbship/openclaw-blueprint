# Inbox Check

Read the evidence file and triage unread emails.

## Priority Levels

- **P1 (Urgent):** Contains urgency keywords (urgent, asap, action required,
  deadline, eod, critical). Notify immediately.
- **P2 (Important):** From known contacts, needs a response today.
- **P3 (Low):** Newsletters, notifications, FYI emails. Ignore unless asked.

## Rules

- Only notify for P1 and P2
- If nothing is P1/P2: reply `HEARTBEAT_OK` (silent, no notification)
- For P1: include sender, subject, and one-line summary
- For P2: batch into a short list
- Never include full email bodies — just enough to decide if action is needed
