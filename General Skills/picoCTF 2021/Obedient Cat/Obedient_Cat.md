# Obedient Cat

- **Platform:** picoCTF
- **Event:** picoCTF 2021
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** syreal

---

## 1. Challenge Overview

The challenge provides a file containing a flag in plaintext.

**Objective:** Download the file and read its contents to retrieve the flag.

---

## 2. Reconnaissance & Initial Analysis

### Files Provided
- **Provided Artifact:** `flag`
- **Target / Endpoint:** Download link on the challenge page.

### Initial Observations
- The description says the flag is stored "in-the-clear".
- The file has no extension, but this does not prevent reading its contents.
- No service interaction or exploitation is required.

---

## 3. Step-by-Step Walkthrough

### Step 1: Download the file

Download the `flag` file from the picoCTF challenge page.

### Step 2: Read the file

Run:

```bash
cat flag
```

The command prints the file contents directly to the terminal.

### Step 3: Retrieve the flag

The supplied file contains:

```text
academy{REDACTED}
```

---

## 4. Flag

```text
academy{REDACTED}
```

**Note:** The supplied file contains an `academy{...}` flag rather than the usual `picoCTF{...}` format.
