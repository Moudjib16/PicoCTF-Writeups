# Mod 26

- **Platform:** picoCTF
- **Event:** picoCTF 2021
- **Category:** Cryptography
- **Difficulty:** Easy
- **Author:** Pandu

---

## 1. Challenge Overview

The challenge provides a text file containing an encoded value.

**Objective:** Decode the contents of `values.txt` using ROT13 to retrieve the flag.

---

## 2. Reconnaissance & Initial Analysis

### Files Provided
- **Provided Artifact:** `values.txt`

### Initial Observations
- The challenge description mentions ROT13.
- ROT13 is a substitution cipher that shifts each letter 13 positions in the alphabet.
- The file contents need to be decoded to reveal the flag.

---

## 3. Step-by-Step Walkthrough

### Step 1: Open the file in CyberChef

Open [CyberChef](https://gchq.github.io/CyberChef/), then load or paste the contents of `values.txt` into the Input panel.

### Step 2: Apply ROT13

Search for the **ROT13** operation and add it to the Recipe panel.

CyberChef automatically decodes the input and displays the result in the Output panel.

### Step 3: Retrieve the flag

Copy the decoded output. The flag should be in the output.

---

## 4. Flag

```text
academy{REDACTED}
```
