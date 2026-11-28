# interencdec

- **Platform:** picoCTF
- **Event:** picoCTF 2024
- **Category:** Cryptography
- **Difficulty:** Easy
- **Author:** NGIRIMANA Schadrack

---

## 1. Challenge Overview

> Can you get the real meaning from this file.

**Hint:** Engaging in various decoding processes is of utmost importance

**Objective:** Peel back each layer of encoding in `enc_flag` until the flag appears.

---

## 2. Reconnaissance & Initial Analysis

### Files Provided
- **Provided Artifact:** `enc_flag`

### Initial Observations

```bash
cat enc_flag
```

```text
YidhR3BvYTJ4MFpudHFhR3g2YUhsZmF6TnFlVGwzWVROclh6Z3lNalF6TURrM2ZRPT0nCg==
```

- The character set (`A-Z`, `a-z`, `0-9`) and the trailing `==` padding point to Base64.
- The hint says "various decoding processes", so there is likely more than one layer.

---

## 3. Step-by-Step Walkthrough

### Step 1: First Base64 decode

```bash
base64 -d enc_flag
```

```text
b'aGpoa2x0ZntqaGx6aHlfazNqeTl3YTNrXzgyMjQzMDk3fQ=='
```

The output is wrapped in `b'...'`, which is how Python prints a bytes object. The challenge author printed the bytes instead of decoding them to a string. The part inside the quotes is another Base64 string (note the `==` again).

### Step 2: Second Base64 decode

Strip the `b'` and `'` and decode what is left. I pasted `aGpoa2x0ZntqaGx6aHlfazNqeTl3YTNrXzgyMjQzMDk3fQ==` into [CyberChef](https://gchq.github.io/CyberChef/) with the **From Base64** operation. The result has the shape of a flag, but the letters are scrambled:

```text
hjhkltf{...}
```

Digits, underscores and braces are unchanged, and only the letters are shifted. That points to a Caesar cipher.

### Step 3: Find the Caesar shift

The flag should start with `academy`. Comparing the first letter:

- `h` → `a` is a shift of 7 back, which is the same as 19 forward (26 − 7 = 19).

Checking the rest of the prefix confirms it: `j` → `c`, `k` → `d`, `l` → `e`, `t` → `m`, `f` → `y`.

### Step 4: Apply ROT19

Add the **ROT13** operation in CyberChef after **From Base64** and set the amount to `19`. The output is the flag.

### Alternative: one shell pipeline

The whole chain also works in a single command:

```bash
base64 -d enc_flag | cut -d"'" -f2 | base64 -d | tr 'a-zA-Z' 't-za-sT-ZA-S'
```

- `cut -d"'" -f2` keeps only the text between the single quotes, dropping the `b'...'` wrapper.
- `tr 'a-zA-Z' 't-za-sT-ZA-S'` maps `a` → `t`, `b` → `u`, and so on, which is ROT19.

---

## 4. Flag

```text
academy{REDACTED}
```

---

## 5. Key Takeaways

- Encodings are often stacked. Decode one layer, look at the output, and decide on the next step.
- A `b'...'` wrapper is a Python bytes repr, not part of the data. Remove it before decoding further.
- When only the letters look wrong and the structure (`{`, `_`, digits) is intact, think Caesar/ROT. A known flag prefix gives you the shift right away.
