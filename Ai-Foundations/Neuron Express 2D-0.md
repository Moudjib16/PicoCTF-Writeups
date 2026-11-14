# Neuron Express 2D-0

- **Challenge:** Neuron Express 2D-0
- **Category:** Artificial Intelligence
- **Event:** AI Foundations
- **Difficulty:** Easy
- **Author:** LT 'syreal' Jones

---

## 1. Challenge Overview
Probe a 2D perceptron over the network. Send integer pairs $(x, y)$ and observe whether the neuron fires or stays quiet, then deduce integer weights and bias that reproduce the perceptron's outputs across the entire grid.

**Objective:** Probe a hidden 2D perceptron ($w_1 \cdot x + w_2 \cdot y + b \ge 0$) within the $[-10, 10] \times [-10, 10]$ integer grid to determine its decision boundary, then submit matching integer parameters via `TEST w1 w2 b` that agree with the target perceptron on all $21 \times 21 = 441$ integer input pairs.

---

## 2. Reconnaissance & Initial Analysis

### Connection / Files Provided
- **Target / Endpoint:** `nc xebec.cylabacademy.net 41549`
- **Provided Artifacts:** None — the challenge is an interactive black-box perceptron service over netcat, so there was no binary or source code to inspect.

### Initial Observations
- The neuron evaluates $w_1 \cdot x + w_2 \cdot y + b \ge 0$ using integer weights and bias, returning `1` ("Perceptron fires!") when non-negative and `0` ("Perceptron stays quiet.") otherwise.
- Input pairs $(x, y)$ must be integers in $[-10, 10]$ (up to 128 queries), and candidate parameters are submitted via `TEST w1 w2 b`.
- When a `TEST` submission fails, the server prints a $21 \times 21$ visual mismatch grid (`X` = mismatch, `.` = match) across $x \in [-10, 10]$ and $y \in [-10, 10]$, revealing the exact geometry of the true decision boundary.

---

## 3. Exploitation / Step-by-Step Walkthrough

### Step 1: Bracketing the Decision Boundary via Probing
Probing anchor points across the 2D plane isolates how $x$ and $y$ affect activation:
- **`(0, 0)` $\rightarrow$ `0` (quiet)** and **`(5, 5)` $\rightarrow$ `1` (fires):** Places the decision boundary between the origin and $(5, 5)$.
- **`(2, 2)` $\rightarrow$ `0`** and **`(3, 3)` $\rightarrow$ `1`:** Narrows the transition along the diagonal.
- **`(2, 3)` $\rightarrow$ `0`** vs. **`(3, 2)` $\rightarrow$ `1`:** Increasing $x$ from `2` to `3` triggers firing even when $y$ decreases, indicating $w_1 > w_2$.
- **`(3, -10)` $\rightarrow$ `1`** vs. **`(2, 10)` $\rightarrow$ `0`:** Even at the extreme $y = -10$, $x = 3$ still fires; even at $y = 10$, $x = 2$ stays quiet. This proves the decision boundary is independent of $y$ ($w_2 = 0$), forming a vertical line between $x = 2$ and $x = 3$.

### Step 2: Using the Mismatch Grid to Align the Threshold
- **`TEST 3 0 0` $\rightarrow$ Failed (63 mismatches):** A boundary at $x \ge 0$ mismatched 3 vertical columns of 21 points each ($x \in \{0, 1, 2\}$).
- **`TEST 3 0 -2` $\rightarrow$ Failed (42 mismatches):** Shifting the boundary to $x \ge 1$ narrowed the mismatch to 2 vertical columns ($x \in \{1, 2\}$).

### Step 3: Parameterizing and Submitting the Solution
To keep the perceptron quiet for all $x \le 2$ and fire for all $x \ge 3$ with $w_1 = 3$ and $w_2 = 0$, the integer bias $b$ must satisfy:

$$3(2) + b < 0 \quad \text{and} \quad 3(3) + b \ge 0 \implies -9 \le b \le -7$$

Submitting `TEST 3 0 -7` ($3x - 7 \ge 0 \iff x \ge 3$) matches the hidden perceptron's output across all 441 integer grid points and prints the flag.

---

## 4. Flag

```text
academy{REDACTED}