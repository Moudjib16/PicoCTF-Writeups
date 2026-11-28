# Python Wrangling

- **Platform:** picoCTF
- **Event:** picoCTF 2021
- **Category:** General Skills
- **Difficulty:** Medium
- **Author:** LT 'syreal' Jones

## 1. Challenge Overview

The challenge provides a Python encryption/decryption script (`ende.py`), a password file (`password.txt`), and an encrypted flag file (`flag.txt.en`).

**Objective:** Run `ende.py` in decryption mode on `flag.txt.en` using the password stored in `password.txt` to recover the flag.

## 2. Reconnaissance & Initial Analysis

### Files Provided

* **Provided Artifacts:** `ende.py`, `flag.txt.en`, `password.txt`

### Initial Observations

* Inspecting `password.txt` reveals the decryption key string (`563e47ddeaf84eca8b2a31201381a898`).
* Running `python ende.py` without arguments displays its usage syntax: `Usage: ende.py (-e/-d) [file]`, showing that `-d` is used for decryption.

## 3. Step-by-Step Walkthrough

### Step 1: Retrieve the Password

Read the contents of `password.txt`:

```bash
cat password.txt
```

Output:

```text
563e47ddeaf84eca8b2a31201381a898
```

### Step 2: Check Script Usage

Invoke `ende.py` with Python to confirm the required command-line flags:

```bash
python ende.py
```

Output:

```text
Usage: ende.py (-e/-d) [file]
```

### Step 3: Decrypt the Flag File

Run `ende.py` with the `-d` flag targeting `flag.txt.en`, and supply the password when prompted:

```bash
python ende.py -d flag.txt.en
```

Input & Output:

```text
Please enter the password: 563e47ddeaf84eca8b2a31201381a898
academy{REDACTED}
```

## 4. Flag

```text
academy{REDACTED}
```