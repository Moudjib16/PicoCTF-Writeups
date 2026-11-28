# hashcrack

- **Platform:** picoCTF
- **Event:** picoCTF 2025
- **Category:** Cryptography
- **Difficulty:** Easy
- **Author:** Nana Ama Atombo-Sackey

---

## 1. Challenge Overview

> A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?

**Hint:** Tried using any hash cracking tools?

**Objective:** Recover the plaintext behind a series of unsalted password hashes the server presents, revealing the secret.

---

## 2. Reconnaissance & Initial Analysis

### Files Provided
- **Provided Artifact:** A network service, reached with `nc chatelaine.cylabacademy.net 41130` (the port changes per instance).

### Initial Observations

Connecting to the service prints a hash and asks for the password behind it. Two more hashes follow once each one is answered.

You can usually tell the hash type from its length in hex characters:

| Length | Bits | Likely algorithm |
|--------|------|------------------|
| 32     | 128  | MD5              |
| 40     | 160  | SHA-1            |
| 64     | 256  | SHA-256          |

None of these hashes are salted, so each one can be looked up in a precomputed table or recovered quickly with a wordlist.

---

## 3. Step-by-Step Walkthrough

The server presents three hashes in turn, one per algorithm:

1. a 32-character MD5 hash,
2. a 40-character SHA-1 hash,
3. a 64-character SHA-256 hash.

### Using CrackStation (what I did)

[CrackStation](https://crackstation.net/) looks a hash up in a large precomputed table and returns the plaintext. I pasted each hash in turn, read back the recovered password, and typed it into the service. All three were common, well-known passwords, so each resolved instantly.

After the third hash the server confirms the secret:

```text
Correct! You've cracked the SHA-256 hash with a secret found.
The flag is: academy{REDACTED}
```

### Alternative: crack offline with hashcat or John the Ripper

If you'd rather not use a website, all three plaintexts live in the `rockyou.txt` wordlist.

**hashcat** (`-m` selects the hash mode — `0` MD5, `100` SHA-1, `1400` SHA-256):

```bash
hashcat -m 0    <md5_hash>    rockyou.txt
hashcat -m 100  <sha1_hash>   rockyou.txt
hashcat -m 1400 <sha256_hash> rockyou.txt
```

**John the Ripper** (put each hash in its own file):

```bash
john --format=raw-md5    --wordlist=rockyou.txt md5.txt
john --format=raw-sha1   --wordlist=rockyou.txt sha1.txt
john --format=raw-sha256 --wordlist=rockyou.txt sha256.txt
john --show --format=raw-md5 md5.txt
```

You can confirm a recovered password by hashing it yourself and comparing:

```bash
printf '%s' 'the_password' | sha256sum
```

---

## 4. Flag

```text
academy{REDACTED}
```

---

## 5. Key Takeaways

- Hash length is a quick way to guess the algorithm (32 hex for MD5, 40 for SHA-1, 64 for SHA-256). `hashid` or `hash-identifier` can confirm it.
- A stronger hash algorithm does not protect a weak password. The SHA-256 value fell just as fast as the MD5 one, because the weakness is the password, not the algorithm.
- Real systems avoid this with slow, salted password hashes (bcrypt, scrypt, Argon2), which defeat precomputed tables and make wordlist attacks far more expensive.
