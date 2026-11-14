# Neuron Meet 2D-0

* **Challenge:** Neuron Meet 2D-0
* **Category:** Artificial Intelligence
* **Event:** AI Foundations
* **Difficulty:** Easy
* **Author:** LT 'syreal' Jones

---

## 1. Challenge Overview
Probe a 2D perceptron over the network. Send it pairs of numbers (x, y) and watch whether the neuron fires or not. Use those responses to figure out the decision boundary, then line up the last eight outputs to read the ASCII for p (01110000) and you'll earn the flag.

**Objective:** Probe a hidden 2D perceptron ($w_1 x + w_2 y + b \ge 0$) within the $[-10.0, 10.0]$ input bounds—without repeating the exact same $(x, y)$ pair back-to-back—to produce the 8-bit sequence `01110000` (ASCII `'p'`) and reveal the flag.

---

## 2. Reconnaissance & Initial Analysis

### Connection / Files Provided
* **Target / Endpoint:** `nc xebec.cylabacademy.net 13520`
* **Provided Artifacts:** None — the challenge is an interactive black-box perceptron service over netcat, so there was no binary or source code to inspect

### Initial Observations
* The neuron evaluates $w_1 x + w_2 y + b \ge 0$, returning `1` ("Perceptron fires!") when non-negative and `0` ("Perceptron stays quiet.") otherwise.
* Inputs must lie within $[-10.0, 10.0]$, and consecutive queries cannot repeat the exact same $(x, y)$ coordinates.
* Probing near the origin (`0 0`, `1 0`, `0 1`, `1 1`, `2 1`) consistently keeps the neuron quiet (`0`), while probing larger positive coordinates (`6 7`, `7 8`, `8 9`) triggers it (`1`), indicating positive weights with a negative bias threshold shifted away from the origin.

---

## 3. Exploitation / Step-by-Step Walkthrough

### Step 1: Mapping the Quiet (`0`) and Firing (`1`) Regions
By testing points in the first quadrant, we identify distinct coordinates on both sides of the linear decision boundary:
* **Quiet inputs (`0`):** `(0, 0)`, `(1, 0)`, `(0, 1)`, `(1, 1)`, and `(2, 1)` all fall below the firing threshold ($w_1 x + w_2 y + b < 0$).
* **Firing inputs (`1`):** `(6, 7)`, `(7, 8)`, and `(8, 9)` all exceed the firing threshold ($w_1 x + w_2 y + b \ge 0$).

### Step 2: Sequencing Inputs to Emit `01110000`
Using distinct valid coordinates for every step to satisfy the no-consecutive-repeat rule, we feed eight inputs matching the target binary pattern `01110000`:

1. **`0 0` $\rightarrow$ `0`** (`0`)
2. **`6 7` $\rightarrow$ `1`** (`01`)
3. **`7 8` $\rightarrow$ `1`** (`011`)
4. **`8 9` $\rightarrow$ `1`** (`0111`)
5. **`1 0` $\rightarrow$ `0`** (`01110`)
6. **`0 1` $\rightarrow$ `0`** (`011100`)
7. **`1 1` $\rightarrow$ `0`** (`0111000`)
8. **`2 1` $\rightarrow$ `0`** (`01110000`)

Once the rolling 8-output buffer matches `01110000` (ASCII `'p'`), the server prints the flag.

---

## 4. Flag

```text
academy{REDACTED}