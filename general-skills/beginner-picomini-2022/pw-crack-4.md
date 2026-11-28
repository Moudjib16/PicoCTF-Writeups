# PW Crack 4

- **Platform:** picoCTF
- **Event:** Beginner picoMini 2022
- **Category:** General Skills
- **Difficulty:** Medium
- **Author:** LT 'syreal' Jones

---

## 1. Challenge Overview

The challenge provides a Python password checker (`level4.py`), an MD5 password hash file (`level4.hash.bin`), and an XOR-encrypted flag file (`level4.flag.txt.enc`).

**Objective:** Automate testing the 100 candidate passwords listed inside `level4.py` against `level4.hash.bin` to decrypt and retrieve the flag.

---

## 2. Reconnaissance & Initial Analysis

### Files Provided
* **Provided Artifacts:** `level4.py`, `level4.hash.bin`, `level4.flag.txt.enc`

### Initial Observations
* Similar to `PW Crack 3`, `level4.py` hashes user input with MD5 and compares the digest against `level4.hash.bin`.
* At the bottom of `level4.py`, `pos_pw_list` contains 100 candidate 4-character hex strings—too many to test manually, making a Python `for` loop the ideal approach.

---

## 3. Step-by-Step Walkthrough

### Step 1: Modify `level4.py` to Iterate Over `pos_pw_list`

Update `level_4_pw_check` to accept a password argument directly instead of prompting via `input()`, and add a `for` loop at the bottom of the script (after `pos_pw_list` is defined) to test every candidate:

```python
def level_4_pw_check(pw):
    user_pw_hash = hash_pw(pw)

    if( user_pw_hash == correct_pw_hash ):
        print("Welcome back... your flag, user:")
        decryption = str_xor(flag_enc.decode(), pw)
        print(decryption)
        return True
    print("That password is incorrect")

# ... pos_pw_list definition ...

for pw in pos_pw_list:
    if level_4_pw_check(pw):
        break
```

### Step 2: Execute the Modified Script

Run `level4.py` to iterate through the candidate list until the matching hash decrypts the flag:

```bash
python level4.py
```

Output:

```text
Welcome back... your flag, user:
academy{REDACTED}
```

---

## 4. Flag

```text
academy{REDACTED}
```