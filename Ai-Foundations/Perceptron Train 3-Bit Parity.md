# Perceptron Train 3-Bit Parity

* **Challenge:** Perceptron Train 3-Bit Parity
* **Category:** Artificial Intelligence
* **Event:** AI Foundations
* **Difficulty:** Easy
* **Author:** LT 'syreal' Jones

---

## 1. Challenge Overview
Watch a perceptron learn in real time on 3-bit parity data using the classic update rule: only misclassified points trigger updates, with no weight decay. This challenge extends the same idea into 3 dimensions, and the frontend renders the points in 3D space. Because parity is not linearly separable by one plane, a single perceptron cannot hit 100% accuracy. Reach 75% accuracy to reveal the flag.

**Objective:** Tune the learning rate of a single-layer perceptron so its separating plane achieves the theoretical maximum 75% accuracy on a 3D parity dataset within 16 update steps.

---

## 2. Reconnaissance & Initial Analysis

### Connection / Files Provided
* **Target / Endpoint:** `http://chatelaine.cylabacademy.net:25578`
* **Provided Artifacts:** None — the challenge is a browser-based interactive 3D visualizer, so there was no binary or source code to inspect

### Initial Observations
The interface renders the 8 vertices of a cube in 3D space at coordinates $(\pm 2, \pm 2, \pm 2)$ representing 3-bit parity: 4 points with odd parity belong to the positive class (blue) and 4 points with even parity belong to the negative class (orange). Because adjacent corners alternate classes, no single flat plane ($w_1 x_1 + w_2 x_2 + w_3 x_3 + b = 0$) can separate all 8 points—the best possible performance for a single perceptron is 6 out of 8 points (`75.0%` accuracy).

---

## 3. Exploitation / Step-by-Step Walkthrough

### Step 1: Testing Learning Rate Bounds
Testing a very small learning rate shows that the plane shifts too slowly within the 16-update budget:

* **`0.02` (Failed):** Weight and bias updates are too small to reposition the separating plane to a 6-of-8 split before hitting the 16-step cap.

### Step 2: Converging to 75% Accuracy
Increasing the learning rate to `1.05` enables larger parameter updates that quickly orient the plane in 3D space:

* **Player action:** Set the **Learning rate** to `1.05` and click **Run training**
* **Step 1:** Evaluates `(-2, -2, -2) -> 0` (predicted `0`, error `0`), keeping initial parameters at $w_1 = 1.00$, $w_2 = 1.00$, $w_3 = 1.00$, $b = 0.00$ (`25.0%` accuracy).
* **Step 2:** Evaluates `(-2, -2, 2) -> 1` (predicted `0`, error `1`), updating parameters to $w_1 = -1.10$, $w_2 = -1.10$, $w_3 = 3.10$, $b = 1.05$ (`50.0%` accuracy).
* **Step 3:** Evaluates `(-2, 2, -2) -> 1` (predicted `0`, error `1`), updating parameters to $w_1 = -3.20$, $w_2 = 1.00$, $w_3 = 1.00$, $b = 2.10$ (`50.0%` accuracy).
* **Step 4:** Evaluates `(-2, 2, 2) -> 0` (predicted `1`, error `-1`), updating parameters to $w_1 = -1.10$, $w_2 = -1.10$, $w_3 = -1.10$, $b = 1.05$ (`75.0%` accuracy).

By step 4 (`sample 4`), the plane $-1.10x_1 - 1.10x_2 - 1.10x_3 + 1.05 = 0$ slices off a corner of the cube, classifying 6 out of 8 points (`75.0%` accuracy) and revealing the flag in the Status panel.

---

## 4. Flag

```text
academy{REDACTED}