# PW Crack 2

- **Platform:** picoCTF
- **Event:** Beginner picoMini 2022
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** LT 'syreal' Jones

## 1. Challenge Overview

The challenge provides a Python password checker (`level2.py`) and an XOR-encrypted flag file (`level2.flag.txt.enc`).

**Objective:** Decode the obfuscated password check in `level2.py` and supply the password to decrypt and print the flag.

## 2. Reconnaissance & Initial Analysis

### Files Provided

* **Provided Artifacts:** `level2.py`, `level2.flag.txt.enc`

### Initial Observations

* Inspecting `level2.py` shows `level_2_pw_check()` comparing user input against four concatenated hexadecimal ASCII character codes: `chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36)`.

* Converting those hex values (`0x64` = `d`, `0x65` = `e`, `0x37` = `7`, `0x36` = `6`) reveals the plaintext password `de76`.

## 3. Step-by-Step Walkthrough

### Step 1: Inspect the Source Code

View `level2.py` to find the password comparison:

```bash
cat level2.py
```

Key snippet:

```python
if( user_pw == chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36) ):
```

### Step 2: Decode the Hex Characters

Convert the ASCII hex values (`0x64 0x65 0x37 0x36`) to text using [CyberChef](https://gchq.github.io/CyberChef/) or any other tool gives (`de76`), or evaluate the expression in Python:

```bash
python -c 'print(chr(0x64) + chr(0x65) + chr(0x37) + chr(0x36))'
```

Output:

```text
de76
```

### Step 3: Run the Script and Enter the Password

Execute `level2.py` and supply `de76` when prompted:

```bash
python level2.py
```

Input & Output:

```text
Please enter correct password for flag: de76
Welcome back... your flag, user:
academy{REDACTED}
```

## 4. Flag

```text
academy{REDACTED}
```