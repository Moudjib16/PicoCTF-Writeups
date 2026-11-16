# strings it

* **Platform:** CyLab Security Academy / picoCTF
* **Event:** picoCTF 2019
* **Category:** General Skills
* **Difficulty:** Easy
* **Author:** Sanjay C / Danny Tunitis

## 1. Challenge Overview

The challenge provides a binary file named `strings` and asks if you can locate the flag inside it without executing the program.

**Objective:** Extract readable ASCII strings from the `strings` binary and filter for the flag format (`academy{...}`).

## 2. Reconnaissance & Initial Analysis

### Files Provided

* **Provided Artifact:** `strings` (compiled executable binary)

### Initial Observations

* Compiled binaries store hardcoded text literals (such as prompts, error messages, and flags) in readable character sequences inside their data sections.
* Using the Linux `strings` utility extracts printable character sequences directly from the file without running it.

## 3. Step-by-Step Walkthrough

### Step 1: Extract and Filter Strings

Run `strings` on the provided binary and pipe the output to `grep` to search case-insensitively for the `academy` flag prefix:

```bash
strings strings | grep -i "academy"
```

Output:

```text
academy{REDACTED}
```

## 4. Flag

```text
academy{REDACTED}
```