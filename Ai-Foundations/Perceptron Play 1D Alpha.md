# Perceptron Play 1D Alpha

* **Challenge:** Perceptron Play 1D Alpha
* **Category:** Artificial Intelligence
* **Event:** AI Foundations
* **Difficulty:** Easy
* **Author:** LT 'syreal' Jones

---

## 1. Challenge Overview
Play with the weight and bias of a 1D perceptron on a number line. Adjust the parameters until every labeled point is classified correctly and you will earn the flag.

**Objective:** Manually adjust the weight ($w$) and bias ($b$) of a 1D single-layer perceptron via an interactive terminal playground so its threshold cleanly separates all 6 labeled points on the number line.

---

## 2. Reconnaissance & Initial Analysis

### Connection / Files Provided
* **Target / Endpoint:** `nc chatelaine.cylabacademy.net 13272`
* **Provided Artifacts:** None — the challenge is an interactive ASCII perceptron playground over netcat, so there was no binary or source code to inspect

### Initial Observations
Running `POINTS` displays the coordinates and target classes for all 6 points along the 1D number line:
* **Class `0`:** `(-4)`, `(-2)`, `(+0)` — all sit at $x \le 0$.
* **Class `1`:** `(+2)`, `(+3)`, `(+4)` — all sit at $x \ge +2$.

The default parameters ($w = 1, b = 0$) place the decision boundary ($w \cdot x + b = 0$) directly at $x = 0$. Because an activation of `0` triggers a `1` prediction, the point at `(+0)` is misclassified (`x`). Shifting the threshold into the gap between `0` and `+2` (at $x = +1$) separates all points cleanly.

---

## 3. Exploitation / Step-by-Step Walkthrough

### Step 1: Testing Bias Directions
Testing positive and negative parameters demonstrates how the bias shifts the decision boundary along the number line:
* **`SET 1 1`:** Shifts the boundary left to $x = -1$, still leaving `(+0)` misclassified (`x`) with an activation of `+1`.
* **`SET -1 -1`:** Keeps the boundary at $x = -1$ but flips the weight sign, inverting predictions so that 5 out of 6 points are misclassified (`x`).

### Step 2: Shifting the Threshold to $x = +1$ & Verifying
Keeping $w = 1$ and setting $b = -1$ moves the decision boundary ($x - 1 = 0$) directly to $x = +1$:
* **Player command:** `SET 1 -1`
* **Result:** All class `0` points (`-4`, `-2`, `+0`) evaluate to negative activations (`-5`, `-3`, `-1`, predicted `0`) and all class `1` points (`+2`, `+3`, `+4`) evaluate to positive activations (`1`, `2`, `3`, predicted `1`), eliminating all misclassified (`x`) markers on the number line.
* **Player command:** `CHECK`
* **Result:** Confirms 100% classification across all 6 points and prints the flag.

---

## 4. Flag

```text
academy{REDACTED}