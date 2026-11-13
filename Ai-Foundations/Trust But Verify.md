# Trust But Verify

* **Challenge:** Trust But Verify
* **Category:** Artificial Intelligence
* **Event** AI Foundations
* **Difficulty:** Easy
* **Author:** LT 'syreal' Jones

---

## 1. Challenge Overview
Play through an AI ethics interactive fiction where confident AI outputs can be wrong, subtly wrong, or almost-right. Verify claims, code, and citations to learn practical habits for safe AI-assisted work.

**Objective:** Always verify AI-generated output (statistics, code, citations) before trusting and acting on it.

---

## 2. Reconnaissance & Initial Analysis

### Connection / Files Provided
* **Target / Endpoint:** `nc xebec.cylabacademy.net 32263`
* **Provided Artifacts:** None — the challenge is a narrative-driven interactive fiction, so there was no binary or source to inspect

### Initial Observations
The game follows Ren, a junior at Westbrook High, and his AI study companion ARIA. Across three scenes, ARIA produces outputs that are confident but wrong, subtly wrong, or almost-right. The player must decide when to trust and when to verify.

---

## 3. Exploitation / Step-by-Step Walkthrough

### Step 1: The Statistic (Scene 1)
Ren is working on a science fair proposal about ocean plastic and needs a strong opening statistic.

* **Player choice:** `B) Ask ARIA for the exact source link before using it`
* **Result:** ARIA could not locate the source document and admitted it likely generated a plausible-sounding citation rather than a real one (a hallucination). The statistic itself may also have been inaccurate.

### Step 2: The Code (Scene 2)
ARIA offers to write a Python script for a bar chart of ocean plastic input over time.

* **Player choice:** `B) Read through it carefully before running`
* **Result:** Ren spotted the suspicious `+ 1` in the average calculation (`sum(data) / len(years) + 1`). ARIA could not explain why it was there. Ren removed it before running the code, which brought the correct average to 10.83.

### Step 3: The Citation (Scene 3)
ARIA composes a closing argument citing a 2021 study by Dr. Heather Leslie at Vrije Universiteit Amsterdam linking microplastics to human blood.

* **Player choice:** `B) Verify it anyway`
* **Result:** The study was real, but the publication year was actually 2022 (not 2021), and the finding was described as preliminary rather than confirmed.

---

## 4. Flag

```text
academy{REDACTED}
```

---

## 5. Key Takeaways & Remediation
* **Root Cause / Concept:** AI hallucination — models can produce confident-sounding but fabricated or subtly incorrect outputs (fake citations, phantom code changes, misremembered facts).
* **Lesson Learned / Fix:** "Trust but verify." Always ask for sources, read code before running it, and verify details independently. Verification isn't about distrust — it's about making your work bulletproof.
