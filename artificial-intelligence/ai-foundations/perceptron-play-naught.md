# Perceptron Play Naught

- **Platform:** picoCTF
- **Event:** AI Foundations
- **Category:** Artificial Intelligence
- **Difficulty:** Easy
- **Author:** LT 'syreal' Jones

---

## 1. Challenge Overview
The points would be inseparable in just the x-dimension, but each point now has a new y-value so the set becomes linearly separable in 2D. Watch the ASCII plot update in real time as you tweak the perceptron weights and bias. Separate the labeled points with a single line to earn the flag.

**Objective:** Manually adjust the weights ($w_1, w_2$) and bias ($b$) of a 2D single-layer perceptron via an interactive terminal playground so its linear decision boundary cleanly separates all 7 labeled points.

---

## 2. Reconnaissance & Initial Analysis

### Connection / Files Provided
* **Target / Endpoint:** `nc chatelaine.cylabacademy.net 27657`
* **Provided Artifacts:** None — the challenge is an interactive ASCII perceptron playground over netcat, so there was no binary or source code to inspect

### Initial Observations
Running `POINTS` displays the coordinates and target classes for all 7 points:
* **Class `0`:** `(-4, -1)`, `(+0, -1)`, `(+2, -1)` — all sit at $y = -1$ (below the x-axis).
* **Class `1`:** `(-1, +2)`, `(+0, +2)`, `(+3, +1)`, `(+4, +2)` — all sit at $y \ge +1$ (above the x-axis).

While the points overlap horizontally along the $x$-axis (making them inseparable in 1D), they are completely separated vertically along the $y$-axis by the line $y = 0$. The default parameters ($w_1 = 1, w_2 = -1, b = 0$) draw a diagonal boundary ($x - y = 0$) that misclassifies 4 out of 7 points.

---

## 3. Exploitation / Step-by-Step Walkthrough

### Step 1: Inspecting the Dataset Layout
Using the `POINTS` command reveals that every class `1` point has a positive $y$-coordinate and every class `0` point has a negative $y$-coordinate. Setting $w_1 = 0$, $w_2 = 1$, and $b = 0$ turns the perceptron activation function ($w_1 x + w_2 y + b$) into simply $y$, placing the decision boundary directly along the horizontal x-axis ($y = 0$).

### Step 2: Updating Weights & Verifying Classification
* **Player command:** `SET 0 1 0`
* **Result:** All class `0` points evaluate to an activation of `-1` (predicted `0`) and all class `1` points evaluate to positive activations of `1` or `2` (predicted `1`), eliminating all misclassified (`x`) markers on the ASCII plot.
* **Player command:** `CHECK`
* **Result:** Confirms 100% classification across all 7 points and prints the flag.

---

## 4. Flag

```text
academy{REDACTED}