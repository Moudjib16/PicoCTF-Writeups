# Neuron Meet 0

- **Platform:** picoCTF
- **Event:** AI Foundations
- **Category:** Artificial Intelligence
- **Difficulty:** Easy
- **Author:** LT 'syreal' Jones

---

## 1. Challenge Overview
Probe a 1D perceptron over the network. Send it numbers and watch whether the neuron fires or not. Use those responses to figure out the decision boundary, then line up the last eight outputs to read the ASCII for p (01110000) and you'll earn the flag.

**Objective:** Probe a hidden 1D perceptron ($w \cdot x + b \ge 0$) within the $[-10.0, 10.0]$ input bounds—without repeating the exact same number back-to-back—to produce the 8-bit sequence `01110000` (ASCII `'p'`) and reveal the flag.

---

## 2. Reconnaissance & Initial Analysis

### Connection / Files Provided
* **Target / Endpoint:** `nc xebec.cylabacademy.net 33663`
* **Provided Artifacts:** None — the challenge is an interactive black-box perceptron service over netcat, so there was no binary or source code to inspect

### Initial Observations
* The neuron evaluates $w \cdot x + b \ge 0$, returning `1` ("Perceptron fires!") when non-negative and `0` ("Perceptron stays quiet.") otherwise.
* Inputs must lie within $[-10.0, 10.0]$, and consecutive queries cannot repeat the exact same value.
* Probing `0` and `1` keeps the neuron quiet (`0`), while probing `2`, `3`, and `4` causes it to fire (`1`), indicating a positive weight with a threshold between `1` and `2`.

---

## 3. Exploitation / Step-by-Step Walkthrough

### Step 1: Mapping the Quiet (`0`) and Firing (`1`) Regions
By probing integer values along the number line, we identify distinct inputs on both sides of the firing threshold:
* **Quiet inputs (`0`):** `0`, `1`, `-1`, `-2`, and `-3` all fall below the firing threshold ($w \cdot x + b < 0$).
* **Firing inputs (`1`):** `2`, `3`, and `4` all exceed the firing threshold ($w \cdot x + b \ge 0$).

### Step 2: Sequencing Inputs to Emit `01110000`
Using distinct valid numbers for every step to satisfy the no-consecutive-repeat rule, we feed eight inputs matching the target binary pattern `01110000`:

1. **`0` $\rightarrow$ `0`** (`0`)
2. **`3` $\rightarrow$ `1`** (`01`)
3. **`2` $\rightarrow$ `1`** (`011`)
4. **`4` $\rightarrow$ `1`** (`0111`)
5. **`1` $\rightarrow$ `0`** (`01110`)
6. **`-1` $\rightarrow$ `0`** (`011100`)
7. **`-2` $\rightarrow$ `0`** (`0111000`)
8. **`-3` $\rightarrow$ `0`** (`01110000`)

Once the rolling 8-output buffer matches `01110000` (ASCII `'p'`), the server prints the flag.

---

## 4. Flag

```text
academy{REDACTED}