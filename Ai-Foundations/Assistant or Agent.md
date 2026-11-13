# Assistant or Agent?

* **Challenge:** Assistant or Agent?
* **Category:** Artificial Intelligence
* **Event:** AI Foundations
* **Difficulty:** Easy
* **Author:** LT 'syreal' Jones

---

## 1. Challenge Overview
Return to Westbrook High in this playful AI ethics interactive fiction. Learn when an AI assistant should advise, when an AI agent should act, and how permissions, guardrails, and review checkpoints keep autonomous actions safe.

**Objective:** Distinguish between passive AI assistant workflows and tool-using AI agent workflows, applying appropriate permissions, guardrails, and human-in-the-loop checkpoints across three event-planning scenarios.

---

## 2. Reconnaissance & Initial Analysis

### Connection / Files Provided
* **Target / Endpoint:** `nc chatelaine.cylabacademy.net 44981`
* **Provided Artifacts:** None — the challenge is a narrative-driven interactive fiction, so there was no binary or source code to inspect

### Initial Observations
Set one week after the science fair adventure in 2031, Ren is preparing Westbrook High's Community Cleanup Night with his AI companion ARIA. Across three scenarios—volunteer scheduling, poster fact-checking, and snack ordering—the player decides whether to use ARIA strictly as a chat-based **assistant** (generating drafts/plans for manual execution) or as an **agent** (taking multi-step actions with tools under strict guardrails and approval rules).

---

## 3. Exploitation / Step-by-Step Walkthrough

### Step 1: The Schedule Switcheroo (Scene 1)
Ren needs to schedule 27 volunteers within ten minutes while accounting for special teacher requests, after-soccer availability, and a cleaning product allergy.

* **Player choice:** `A) Use ARIA as an assistant: ask for a scheduling strategy, then assign shifts yourself`
* **Result:** ARIA drafts a clean scheduling process (grouping by availability, placing constraints first, then filling preferences), and Ren assigns the shifts manually so no unverified messages go out by accident.

### Step 2: The Source Scavenger Hunt (Scene 2)
Ren needs three reliable facts (local litter impact, safe disposal guidance, and volunteer safety tips) for a cleanup poster.

* **Player choice:** `B) Ask agent-mode ARIA to browse approved sites, collect citations, and attach a verification bundle`
* **Result:** Using browsing tools and memory, ARIA pulls quotes and link snapshots from pre-approved sources into an evidence packet complete with per-claim confidence notes.

### Step 3: The Snack Budget Boss Fight (Scene 3)
Principal Vega allocated a strict $120 budget for event snacks, and Ren still needs money left over to print maps.

* **Player choice:** `B) Let agent-mode ARIA place the order with guardrails: $120 cap, approved stores, and confirmation required for substitutions`
* **Result:** ARIA handles the order autonomously within boundaries, pauses to ask Ren for approval when an item is out of stock, and completes the purchase under budget at `$119.42`.

---

## 4. Flag

```text
academy{REDACTED}
```

---

## 5. Key Takeaways & Remediation
* **Root Cause / Concept:** Assistants vs. Agents — an **AI assistant** generates text, plans, and drafts in chat while leaving real-world execution to the user, whereas an **AI agent** uses tools, memory, and planning to take direct actions in external systems.
* **Lesson Learned / Fix:** Match autonomy to risk. Grant agents narrow tool scopes, hard constraints (such as budget limits and approved source lists), and human-in-the-loop approval checkpoints before executing high-impact or irreversible actions.