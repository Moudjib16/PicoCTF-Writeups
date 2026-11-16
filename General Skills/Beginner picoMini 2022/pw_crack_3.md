# PW Crack 3

* **Platform:** CyLab Security Academy / picoCTF

* **Event:** Beginner picoMini 2022

* **Category:** General Skills

* **Difficulty:** Medium

* **Author:** LT 'syreal' Jones

## 1. Challenge Overview

The challenge provides a Python password checker (`level3.py`), an MD5 password hash file (`level3.hash.bin`), and an XOR-encrypted flag file (`level3.flag.txt.enc`).

**Objective:** Inspect `level3.py` to find the list of 7 candidate passwords and identify which one matches `level3.hash.bin` to decrypt and print the flag.

## 2. Reconnaissance & Initial Analysis

### Files Provided

* **Provided Artifacts:** `level3.py`, `level3.hash.bin`, `level3.flag.txt.enc`

### Initial Observations

* Unlike previous levels, `level3.py` does not store the password in plaintext; instead, it hashes user input with MD5 (`hash_pw(user_pw)`) and compares the raw digest against `level3.hash.bin`.

* At the bottom of `level3.py`, a comment and list (`pos_pw_list`) explicitly provide the 7 possible passwords: `["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]`.

## 3. Step-by-Step Walkthrough

### Step 1: Inspect the Source Code

View `level3.py` to locate the candidate password list:

```bash
cat level3.py
```

Key snippet:

```python
pos_pw_list = ["8799", "d3ab", "1ea2", "acaf", "2295", "a9de", "6f3d"]
```

### Step 2: Test the Candidate Passwords

Run `level3.py` and test the candidate passwords from `pos_pw_list` until `a9de` matches the MD5 digest in `level3.hash.bin`:

```bash
python level3.py
```

Input & Output:

```text
Please enter correct password for flag: a9de
Welcome back... your flag, user:
academy{REDACTED}
```

## 4. Flag

```text
academy{REDACTED}
```