# Warmed Up

- **Platform:** picoCTF
- **Event:** picoCTF 2019
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** Sanjay C / Danny Tunitis

---

## 1. Challenge Overview

The challenge asks for the decimal representation of the hexadecimal value `0x3D`.

**Objective:** Decode the provided Base64 input in CyberChef, then convert the resulting value to decimal.

---

## 2. Solution

### Step 1: Decode the Base64 input

Open [CyberChef](https://gchq.github.io/CyberChef/), paste the provided input, and add the **From HEX** operation.

### Step 2: Convert the result to decimal

Add the **To Decimal** operation after **From HEX** in the recipe.

The decimal result is:

```text
61
```

---

## 3. Flag

```text
academy{REDACTED}
```
