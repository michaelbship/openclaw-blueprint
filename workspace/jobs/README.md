# Jobs — Scheduled Tasks

Jobs follow a **gather + interpret** pattern:

1. `gather.sh` — Deterministic script that collects data (API calls, file reads, etc.)
2. `prompt.md` — Instructions for the LLM to interpret the gathered data

The runner (`run-job.sh`) orchestrates both phases.

## How It Works

```
Cron → run-job.sh <job-name>
         ├── gather.sh    (collects data, writes to evidence file)
         └── prompt.md    (LLM reads this + evidence, takes action)
```

## Creating a Job

1. Create a directory: `jobs/<job-name>/`
2. Add `gather.sh` (make it executable: `chmod +x gather.sh`)
3. Add `prompt.md` with interpretation instructions
4. Set up a cron entry to call `run-job.sh <job-name>`

## Example Cron Entries

```bash
# Morning briefing at 7:00 AM
0 7 * * * bash ~/.openclaw/workspace/jobs/run-job.sh morning-briefing

# Inbox check every 2 hours during work hours
0 9,11,13,15,17 * * 1-5 bash ~/.openclaw/workspace/jobs/run-job.sh inbox-check
```

## Key Principle

The **gather script** is deterministic — it always collects the same type of
data. The **LLM** provides judgment — it decides what's important and what
action to take. This separation makes jobs reliable and debuggable.
