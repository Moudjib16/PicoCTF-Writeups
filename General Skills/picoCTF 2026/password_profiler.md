# Password Profiler

* **Category:** General Skills
* **Difficulty:** Easy
* **Author:** Yahaya Meddy
* **Event:** picoCTF 2026

## 1. Challenge Overview

> *"We intercepted a suspicious file from a system, but instead of the password itself, it only contains its SHA-1 hash. Using OSINT techniques, you are provided with personal details about the target. Your task is to leverage this information to generate a custom password list and recover the original password by matching its hash."*

**Provided files:**

* `userinfo.txt` — personal details about the target
* `hash.txt` — the SHA-1 hash of the real password
* `check_password.py` — a script that hashes candidate passwords and compares them to `hash.txt`

**Objective:** Use the target's personal details to build a small, targeted wordlist (rather than a huge generic one), and find the single password in it that matches the given SHA-1 hash.

## 2. Step-by-Step Solution

### Step 1: Looking at What's Provided

```text
ls
check_password.py           hash.txt            userinfo.txt
```

```text
cat userinfo.txt
First Name: Alice
Surname: Johnson
Nickname: AJ
Birthdate: 15-07-1990
Partner's Name: Bob
Child's Name: Charlie
```

* **Key Observation:** This is exactly the kind of personal information (name, nickname, birthdate, partner, child) that people base their passwords on — and it's exactly the input a password-profiling tool like **CUPP** (Common User Passwords Profiler) is built to turn into a wordlist.

### Step 2: Generating a Targeted Wordlist with CUPP

CUPP interviews you for personal details about a target and builds a custom wordlist from the combinations people actually use (name + birth year, nickname + special chars, leetspeak substitutions, etc.) instead of brute-forcing every possible string.

```bash
cd cupp
python cupp.py -i
```

Answering the interactive prompts with the details from `userinfo.txt`:

```text
> Enter the first name: Alice
> Enter the surname: Johnson
> Enter the nickname: AJ
> Enter birthdate (DDMMYYYY): 15071990
> Enter partner's name: Bob
> Enter partner's nickname: 
> Enter partner's birthdate: 
> Enter child's name: Charlie
> Enter child's nickname: 
> Enter child's birthdate: 
> Do you want to add some key words about the victim? Y/[N]: N
> Do you want to add special chars at the end of words? Y/[N]: Y
> Do you want to add some random numbers at the end of words? Y/[N]: Y
> Do you want to add some common passwords? Y/[N]: N
```

This produces a wordlist file (`alice.txt`), built from combinations of the name, surname, nickname, birthdate, and the partner/child names, with extra special characters and random numbers appended to variations of each word.

### Step 3: Reading `check_password.py`

Before plugging anything in, it's worth checking what the cracking script actually does:

```python
#!/usr/bin/env python3
import hashlib

HASH_FILE = "hash.txt"
WORDLIST_FILE = "passwords.txt" # wordlist that was generated using CUPP

def load_hash():
    with open(HASH_FILE, "r") as f:
        return f.read().strip()

def crack_password(target_hash):
    with open(WORDLIST_FILE, "r", encoding="utf-8", errors="ignore") as f:
        for password in f:
            password = password.strip()
            if hashlib.sha1(password.encode()).hexdigest() == target_hash:
                return password
    return None

if __name__ == "__main__":
    target_hash = load_hash()
    result = crack_password(target_hash)
    if result:
        print(f"Password found: academy{{{result}}}")
    else:
        print("No match found.")
```

* **Key Observation:** The script hardcodes its wordlist path as `passwords.txt` (the comment even confirms it's meant to hold a CUPP-generated list), reads `hash.txt` for the target SHA-1 digest, and does a straightforward dictionary attack — hash each candidate line, compare to the target, stop on the first match. It also wraps whatever password it finds in `academy{...}` to build the final flag, so the wordlist only needs to contain the raw password, not the flag format.

### Step 4: Swapping the Wordlist for `check_password.py`

Since the script reads candidate passwords from `passwords.txt` specifically, the CUPP-generated list has to be dropped in under that exact filename:

```bash
mv alice.txt passwords.txt
```

### Step 5: Cracking the Hash

```bash
python check_password.py
```

```text
Password found: academy{REDACTED}
```

The script hashed each line of `passwords.txt` with SHA-1 and compared it against `hash.txt` until it found a match — one of the CUPP-generated combinations of "alice", "AJ", and the birth year happened to be the real password.

## 3. Flag

```text
academy{REDACTED}
```

## 4. Alternative Tools & Methods

### Alternative 1: Manual Wordlist with a One-Liner Cracker
Without CUPP, the same idea can be done by hand: build a small list of likely combinations from the `userinfo.txt` fields (name, nickname, birth year, leetspeak swaps) and check each one against the hash directly in Python:

```python
import hashlib

target = open("hash.txt").read().strip()
candidates = ["alice", "aliceaj", "aliceaj1990", "aliceaj7515", "AJalice90"]

for word in candidates:
    if hashlib.sha1(word.encode()).hexdigest() == target:
        print("Found:", word)
        break
```

### Alternative 2: Other Profiling Wordlist Generators
Tools like **CeWL** (scrapes words from a website) or **Mentalist** (GUI-based mangling rules) solve the same OSINT-to-wordlist problem as CUPP, and could build an equivalent list from the same personal details.

### Alternative 3: Feed the List Straight to Hashcat/John
Instead of the challenge's custom `check_password.py`, the same `passwords.txt` wordlist generated by CUPP could be fed directly into a cracking tool:

```bash
hashcat -m 100 -a 0 hash.txt passwords.txt    # mode 100 = SHA-1
```

## 5. Key Takeaways & Lessons

1. **OSINT narrows the search space:** A generic wordlist with millions of entries is slow and may still miss a personalized password. Feeding real personal details (name, nickname, birthdate, family names) into a profiler like CUPP produces a small, highly relevant list that's far more likely to contain the actual password.
2. **People reuse predictable patterns:** Names, nicknames, birth years, and appended numbers or special characters are extremely common password-construction habits — which is exactly what makes them crackable once an attacker has a little personal information.
3. **Match the tool's expected input:** The provided `check_password.py` only reads from `passwords.txt`, so the generated wordlist had to be renamed/moved into place before the script could use it — a reminder to check a tool's expected filenames and inputs before assuming it isn't working.
