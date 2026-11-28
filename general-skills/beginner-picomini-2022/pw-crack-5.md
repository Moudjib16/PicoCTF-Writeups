# PW Crack 5

- **Platform:** picoCTF
- **Event:** Beginner picoMini 2022
- **Category:** General Skills
- **Difficulty:** Medium
- **Author:** LT 'syreal' Jones

## 1. Challenge Overview

The challenge provides a Python password checker (`level5.py`), an MD5 password hash file (`level5.hash.bin`), an XOR-encrypted flag file (`level5.flag.txt.enc`), and a wordlist file (`dictionary.txt`).

**Objective:** Perform a dictionary attack by iterating through all candidate passwords in `dictionary.txt`, hashing each one with MD5 until it matches `level5.hash.bin`, and decrypting the flag.

## 2. Reconnaissance & Initial Analysis

### Files Provided

* **Provided Artifacts:** `level5.py`, `level5.hash.bin`, `level5.flag.txt.enc`, `dictionary.txt`

### Initial Observations

* Unlike `PW Crack 3` and `PW Crack 4` where candidate passwords were embedded inside the Python script, `PW Crack 5` provides an external wordlist (`dictionary.txt`) containing 65,536 possible 4-character hex passwords.

* Modifying `level_5_pw_check()` to read `dictionary.txt` line-by-line allows testing all candidates in a single Python execution within milliseconds.

## 3. Step-by-Step Walkthrough

### Step 1: Modify `level5.py` to Iterate Over `dictionary.txt`

Update `level_5_pw_check()` to open `dictionary.txt`, strip the newline from each entry, compute its MD5 digest, and decrypt the flag once `correct_pw_hash` is matched:

```python
def level_5_pw_check():
    with open("dictionary.txt", "r") as file:
        for line in file:
            user_pw = line.strip()
            user_pw_hash = hash_pw(user_pw)
            if user_pw_hash == correct_pw_hash:
                print("Welcome back... your flag, user:")
                decryption = str_xor(flag_enc.decode(), user_pw)
                print(decryption)
                return
```

### Step 2: Execute the Modified Script

Run `level5.py` to crack the password and print the decrypted flag:

```bash
python level5.py
```

Output:

```text
Welcome back... your flag, user:
academy{REDACTED}
```

## 4. Flag

```text
academy{REDACTED}
```