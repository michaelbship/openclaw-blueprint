---
name: artifact-writer
description: |
  Create, iterate, and publish documents as persistent artifacts.
  Use when user asks to:
  - "write a report"
  - "draft a [document]"
  - "create a doc"
  - "put together a [summary]"
  - "iterate on [document]"
  - "write this up"
  - "study and analyze [topic]"
  - "breakdown this content"
  Deep-dive analysis and breakdowns should ALWAYS create a document,
  not a long chat message.
---

# Artifact Writer

Use this skill to create, publish, and iterate on documents. The workflow:
write a file, commit it, share it, take feedback, update, repeat.

## Prerequisites

You need a target directory for artifacts. By default, use `outputs/` in
your workspace. If your user has a knowledge base repo configured, write
there instead.

---

## The Workflow

### Step 0: Check for Existing Artifact

Before creating a new file:
1. Check recent conversation for a `**Skill:** artifact-writer` footer with a file path
2. If found, skip to Step 5 (iterate on that file)
3. If not found, check the destination folder
4. If a related file exists, confirm: edit existing or create new?

This prevents creating v1, v2, v3 of the same document.

### Step 1: Determine Destination

| Content Type | Default Destination |
|-------------|---------------------|
| Reports, summaries, analysis | `outputs/` |
| Project-specific artifacts | `outputs/` (or user-configured repo) |
| Temporary drafts | `outputs/` |

### Step 2: Write the File

**Filename convention:** `{YYYY-MM-DD}-{title-slug}.md`

Example: `2026-02-20-weekly-research-summary.md`

**Frontmatter template:**

```yaml
---
title: "Document Title"
date: 2026-02-20
type: report
author: bob
tags:
  - type/report
generated_at: 2026-02-20T18:00:00Z
---
```

Write the document body after the frontmatter. Use clear markdown
structure with headings, lists, and tables as appropriate.

### Step 3: Commit (if in a git repo)

```bash
git add {path-to-file}
git commit -m "feat: {brief description}"
git push origin main
```

### Step 4: Share with User

Tell the user where the file is. If it's in a git repo with a web UI,
provide the URL. Otherwise, provide the file path.

### Step 5: Accept Feedback and Iterate

When your user gives feedback:
1. Edit the file based on feedback
2. Commit and push if in a git repo
3. Let the user know it's updated
4. Repeat until satisfied

**Important:** Re-read this skill on each iteration. Don't work from
memory of the workflow.

---

## Frontmatter Templates by Type

### Report / Summary
```yaml
---
title: "Weekly Summary — Feb 17-21"
date: 2026-02-21
type: report
author: bob
tags:
  - type/report
generated_at: 2026-02-21T10:00:00Z
---
```

### Technical Doc
```yaml
---
title: "Feature Architecture"
date: 2026-02-20
type: architecture
author: bob
tags:
  - type/architecture
generated_at: 2026-02-20T18:00:00Z
---
```

---

## Self-Check

Before reporting a document as ready:

- Did I check for an existing artifact first?
- Does the file have proper frontmatter (title, date, type)?
- Is the filename in `{YYYY-MM-DD}-{title-slug}.md` format?
- Did I write to the correct destination?
- Is the document in clean, scannable markdown?
- Did I declare skill usage in the footer? (`**Skill:** artifact-writer · **File:** <path>`)

---

## Related Skills

- `research`: Load when external web research is needed as input
- `system-query`: Load when you need to find info in your own workspace
