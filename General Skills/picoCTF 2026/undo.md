# Undo

**Category:** General Skills  
**Difficulty:** Easy  
**Author:** Yahaya Meddy  
**Event:** picoCTF 2026 (CyLab Security Academy)  

---

## Challenge Description
> Can you reverse a series of Linux text transformations to recover the original flag? Start searching for the flag here: `nc xebec.cylabacademy.net 42558`

**Hint:**  
For text translation and character replacement, see `tr` command documentation.

---

## Reconnaissance & Analysis
Connecting to the remote service via `netcat` (`nc`) initiates an interactive five-stage text transformation challenge. At each step, the server displays the current obfuscated flag alongside a description of the last transformation applied, prompting for the exact Linux CLI command needed to undo it.

```bash
nc xebec.cylabacademy.net 42558
```

---

## Step-by-Step Solution

### Step 1: Base64 Decoding
- **Current String:** `KTdvNDE5cDA4LWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShsenJxbnBu`
- **Transformation Applied:** Base64 encoded the string.
- **Reversal Command:**
  ```bash
  base64 -d
  ```
- **Output:** `)7o419p08-fa01g@ze0sfa4eG-gk3g-ta1ferirE(lzrqnpn`

---

### Step 2: String Reversal
- **Current String:** `)7o419p08-fa01g@ze0sfa4eG-gk3g-ta1ferirE(lzrqnpn`
- **Transformation Applied:** Reversed the text.
- **Reversal Command:**
  ```bash
  rev
  ```
- **Output:** `npnqrzl(Eriref1at-g3kg-Ge4afs0ez@g10af-80p914o7)`

---

### Step 3: Restoring Underscores
- **Current String:** `npnqrzl(Eriref1at-g3kg-Ge4afs0ez@g10af-80p914o7)`
- **Transformation Applied:** Replaced underscores (`_`) with dashes (`-`).
- **Reversal Command:**
  ```bash
  tr "-" "_"
  ```
- **Output:** `npnqrzl(Eriref1at_g3kg_Ge4afs0ez@g10af_80p914o7)`

---

### Step 4: Restoring Curly Braces
- **Current String:** `npnqrzl(Eriref1at_g3kg_Ge4afs0ez@g10af_80p914o7)`
- **Transformation Applied:** Replaced curly braces (`{}`) with parentheses (`()`).
- **Reversal Command:**
  ```bash
  tr "()" "{}"
  ```
- **Output:** `npnqrzl{Eriref1at_g3kg_Ge4afs0ez@g10af_80p914o7}`

---

### Step 5: Decoding ROT13
- **Current String:** `npnqrzl{Eriref1at_g3kg_Ge4afs0ez@g10af_80p914o7}`
- **Transformation Applied:** Applied ROT13 cipher to alphabetical characters.
- **Reversal Command:**
  ```bash
  tr "A-Za-z" "N-ZA-Mn-za-m"
  ```
- **Output:** `academy{REDACTED}`

---

## Local Pipeline Verification
All five reversal stages can also be chained locally into a single Unix pipeline to verify the transformation end-to-end:

```bash
echo "KTdvNDE5cDA4LWZhMDFnQHplMHNmYTRlRy1nazNnLXRhMWZlcmlyRShsenJxbnBu" \
  | base64 -d \
  | rev \
  | tr "-" "_" \
  | tr "()" "{}" \
  | tr "A-Za-z" "N-ZA-Mn-za-m"
```

---

## Flag
```text
academy{REDACTED@}
```