# PW Crack 1

- **Platform:** picoCTF
- **Event:** Beginner picoMini 2022
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** LT 'syreal' Jones

## 1. Challenge Overview

The challenge provides a Python password checker (`level1.py`) and an XOR-encrypted flag file (`level1.flag.txt.enc`).

**Objective:** Inspect `level1.py` to find the hardcoded password and supply it to decrypt and print the flag.

## 2. Reconnaissance & Initial Analysis

### Files Provided

* **Provided Artifacts:** `level1.py`, `level1.flag.txt.enc`

### Initial Observations

* Reading `level1.py` reveals the `level_1_pw_check()` function, which checks the user's input directly against a plaintext string (`if( user_pw == "8713"):`).

* Once matched, the script XOR-decrypts `level1.flag.txt.enc` using `"8713"` as the key.

## 3. Step-by-Step Walkthrough

### Step 1: Inspect the Source Code

View the contents of `level1.py` to locate the password check:

```bash
cat level1.py
```

Key snippet:

```python
if( user_pw == "8713"):
```

### Step 2: Run the Script and Enter the Password

Execute `level1.py` with Python and enter `8713` when prompted:

```bash
python level1.py
```

Input & Output:

```text
Please enter correct password for flag: 8713
Welcome back... your flag, user:
academy{REDACTED}
```

## 4. Flag

```text
academy{REDACTED}
```