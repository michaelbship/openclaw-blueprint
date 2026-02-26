---
name: browser
description: Perform browser verification and deterministic UI actions via Playwright MCP.
---

# Browser Doctrine

Use this skill when manual exploration is insufficient or when UI verification is required.

## The Glass Box Rule
The built-in `browser` tool is for **Exploration only** (and is currently restricted). All **Verification** and **Action** must use `playwright` MCP.

## Capabilities
- **Navigation:** Deep-link to verified resources.
- **Verification:** Snapshot DOM or visual state to confirm an action was successful.
- **Orchestration:** Interact with sites that don't have APIs (e.g. niche bank portals, legacy docs).

## Guidelines
- **Snapshot First:** Always take a snapshot or read the state before clicking/typing to ensure context.
- **Traceability:** State exactly what you are doing in the browser (e.g., "Navigating to X to verify Y...").
- **Deterministic:** Prefer stable selectors over guessing positions.
