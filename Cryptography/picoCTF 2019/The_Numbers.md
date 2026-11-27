# The Numbers

- **Platform:** picoCTF
- **Event:** picoCTF 2019
- **Category:** Cryptography
- **Difficulty:** Easy
- **Author:** Danny

---

## 1. Challenge Overview

> The numbers... what do they mean?

**Objective:** Work out what the numbers in the provided image stand for and decode them into the flag.

---

## 2. Reconnaissance & Initial Analysis

### Files Provided
- **Provided Artifact:** `the_numbers.png`

### Initial Observations

I opened the image in Inkscape:

```bash
inkscape the_numbers.png
```

The numbers are in plain sight in the image:

```text
16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }
```

- The `{ }` braces suggest a flag format, so the 7 numbers before them are probably `PICOCTF`.
- Every number is between 1 and 26, which matches the letters of the alphabet.

---

## 3. Step-by-Step Walkthrough

### Step 1: Identify the cipher

This is an A1Z26 cipher. Each number is a letter's position in the alphabet: `A = 1`, `B = 2`, ..., `Z = 26`.

The prefix confirms it: `16 9 3 15 3 20 6` → `P I C O C T F`.

### Step 2: Decode the numbers

Map each number back to its letter. A short Python one-liner does it:

```bash
python -c "s='16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }';print(''.join(chr(64+int(t)) if t.isdigit() else t for t in s.split()))"
```

`chr(64 + n)` turns `1` into `A` (ASCII 65), `2` into `B`, and so on. The braces pass through unchanged.

You can also use CyberChef's **A1Z26 Cipher Decode** operation.

### Step 3: Retrieve the flag

The output is the flag in uppercase `PICOCTF{...}` format.

---

## 4. Flag

```text
PICOCTF{REDACTED}
```

---

## 5. Key Takeaways

- A1Z26 replaces each letter with its position in the alphabet. It has no key, so it only hides text and gives no security.
- A known flag prefix such as `PICOCTF` is a quick way to confirm a guess about the cipher.
- The decoded flag is uppercase because the numbers carry no case information.
