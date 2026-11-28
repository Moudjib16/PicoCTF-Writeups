# First Grep

- **Platform:** picoCTF
- **Event:** picoCTF 2019
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** Alex Fulton / Danny Tunitis

## 1. Challenge Overview

The challenge provides a text file named `file` and asks if you can find the flag without looking through it manually.

**Objective:** Use `grep` to search `file` for the flag pattern (`academy{...}`) and extract only the matching string.

## 2. Reconnaissance & Initial Analysis

### Files Provided

* **Provided Artifact:** `file` (single-line text file filled with random characters)

### Initial Observations

* Manually reading through `file` is tedious due to the large wall of random noise.

* Because the entire file lacks newline breaks, running a standard `grep` prints the whole line. Combining the `-o` (only-matching) flag with a regex pattern isolates just the flag.

## 3. Step-by-Step Walkthrough

### Step 1: Extract the Flag with `grep`

Run `grep` with `-o` and a regular expression matching `academy{...}` up to the closing brace:

```bash
grep -o "academy{[^}]*}" file
```

Output:

```text
academy{REDACTED}
```

## 4. Flag

```text
academy{REDACTED}
```