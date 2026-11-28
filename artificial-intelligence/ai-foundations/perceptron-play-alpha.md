# Perceptron Play Alpha

- **Platform:** picoCTF
- **Event:** AI Foundations
- **Category:** Artificial Intelligence
- **Difficulty:** Easy
- **Author:** LT 'syreal' Jones

---

## 1. Challenge Overview
Play with the weights and bias of a 2D perceptron while watching an ASCII plot update in real time. Tune the parameters so that the decision boundary separates all of the labeled points and you will earn the flag.

**Objective:** Manually adjust the weights ($w_1, w_2$) and bias ($b$) of a 2D single-layer perceptron via an interactive terminal playground so its linear decision boundary cleanly separates all 6 labeled points.

---

## 2. Reconnaissance & Initial Analysis

### Connection / Files Provided
* **Target / Endpoint:** `nc chatelaine.cylabacademy.net 32037`
* **Provided Artifacts:** None — the challenge is an interactive ASCII perceptron playground over netcat, so there was no binary or source code to inspect

### Initial Observations
Running `POINTS` displays the coordinates and target classes for all 6 points:
* **Class `0`:** `(-3, -2)`, `(-1, -1)`, `(-4, -2)` — all sit in the lower-left quadrant where $x + y < 0$.
* **Class `1`:** `(+3, +1)`, `(+2, +2)`, `(+1, +3)` — all sit in the upper-right quadrant where $x + y = +4$.

The default parameters ($w_1 = 1, w_2 = -1, b = 0$) draw a boundary along $x - y = 0$, which cuts straight through both clusters and misclassifies `(-1, -1)` and `(+1, +3)`. Rotating the line 90 degrees to $x + y = 0$ separates the two quadrants cleanly.

---

## 3. Exploitation / Step-by-Step Walkthrough

### Step 1: Testing the Inverse Orientation
Setting negative weights (`SET -1 -1 0`) aligns the boundary along $x + y = 0$, but inverts the class predictions:
* **Player command:** `SET -1 -1 0`
* **Result:** Every point is misclassified (`x`) because the class `0` points produce positive activations (`2`, `5`, `6`) while the class `1` points produce negative activations (`-4`).

### Step 2: Flipping the Weights & Verifying Classification
Flipping the signs of both weights (`SET 1 1 0`) keeps the boundary along $x + y = 0$ while inverting the activation signs:
* **Player command:** `SET 1 1 0`
* **Result:** All class `0` points evaluate to negative activations (`-5`, `-2`, `-6`, predicted `0`) and all class `1` points evaluate to `+4` (predicted `1`), eliminating all misclassified (`x`) markers on the ASCII plot.
* **Player command:** `CHECK`
* **Result:** Confirms 100% classification across all 6 points and prints the flag.

---

## 4. Flag

```text
academy{REDACTED}