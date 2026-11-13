# Perceptron Train Classic 2 Alpha

* **Challenge:** Perceptron Train Classic 2 Alpha
* **Category:** Artificial Intelligence
* **Event:** AI Foundations
* **Difficulty:** Easy
* **Author:** LT 'syreal' Jones

---

## 1. Challenge Overview
Watch a perceptron learn in real time using the classic update rule: only misclassified points trigger updates, with no weight decay. In this variant you must find 5 successful learning rates (each reaching 100% accuracy) before the flag is revealed. The dataset is still linearly separable, but it is less toy-like and the separation is less obvious. Dial in a rate, trigger a run, and the interface animates each step.

**Objective:** Find 5 distinct learning rates that enable a single-layer perceptron to achieve 100% classification accuracy on a linearly separable dataset within the 16-update cap.

---

## 2. Reconnaissance & Initial Analysis

### Connection / Files Provided
* **Target / Endpoint:** `http://xebec.cylabacademy.net:44102`
* **Provided Artifacts:** None — the challenge is a browser-based interactive visualizer, so there was no binary or source code to inspect

### Initial Observations
The interface plots 12 data points distributed across the plane—6 belonging to the positive class (blue) in the upper-right region and 6 belonging to the negative class (orange) in the lower-left region. Unlike the XOR/XNOR or ring datasets, this distribution is linearly separable (100% accuracy is achievable). However, because training stops after 16 updates, very small learning rates fail to shift the decision boundary far enough in time, whereas moderate-to-large learning rates converge to a clean separation.

---

## 3. Exploitation / Step-by-Step Walkthrough

### Step 1: Testing Learning Rate Bounds
Testing a very small learning rate shows that the model runs out of its 16-update budget before the line can separate the two classes:

* **`0.02` (Failed):** Step sizes are too small to move the decision boundary across the gap within 16 updates.

### Step 2: Finding 5 Successful Learning Rates
Increasing the learning rate allows the weights ($w_1, w_2$) and bias ($b$) to adjust rapidly enough to separate all 12 points (`100.0%` accuracy) within the 16-step limit:

1. **`2.2` (Success):** Converged to `100.0%` accuracy (`1/5`).
2. **`1.49` (Success):** Converged to `100.0%` accuracy (`2/5`).
3. **`0.99` (Success):** Converged to `100.0%` accuracy (`3/5`).
4. **`3.03` (Success):** Converged to `100.0%` accuracy (`4/5`).
5. **`0.67` (Success):** Converged to `100.0%` accuracy (`5/5`) — by step 16 (`sample 4`), the parameters settled at $w_1 = 1.67$, $w_2 = 1.68$, and $b = -1.34$, cleanly dividing all blue and orange points.

Once all 5 successful learning rates were logged (`5/5`), the Status panel unlocked and revealed the flag.

---

## 4. Flag

```text
academy{REDACTED}