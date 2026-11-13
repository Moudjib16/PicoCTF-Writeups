# Perceptron Train Classic 1

* **Challenge:** Perceptron Train Classic 1
* **Category:** Artificial Intelligence
* **Event:** AI Foundations
* **Difficulty:** Easy
* **Author:** LT 'syreal' Jones

---

## 1. Challenge Overview
Watch a perceptron learn in real time using the classic update rule: only misclassified points trigger updates, with no weight decay. In this variant you must find 5 successful learning rates (each reaching 100% accuracy) before the flag is revealed. Dial in a rate, trigger a run, and the interface animates each step.

**Objective:** Find 5 distinct learning rates that enable a single-layer perceptron to achieve 100% classification accuracy on a cleanly linearly separable dataset within 16 update steps.

---

## 2. Reconnaissance & Initial Analysis

### Connection / Files Provided
* **Target / Endpoint:** `http://xebec.cylabacademy.net:23269`
* **Provided Artifacts:** None — the challenge is a browser-based interactive visualizer, so there was no binary or source code to inspect

### Initial Observations
The interface plots 8 data points separated across two distinct clusters: 4 positive class points (blue) in the upper-right quadrant and 4 negative class points (orange) in the lower-left quadrant. Because the margin between the two classes is wide and linearly separable, a wide range of learning rates—from very small (`0.02`) to large (`2.09`)—can converge to `100.0%` accuracy before hitting the 16-update cap.

---

## 3. Exploitation / Step-by-Step Walkthrough

### Step 1: Testing Multiple Learning Rates
Because the dataset is cleanly separable, both small step sizes (which rotate the boundary gradually) and larger step sizes (which snap the boundary into place in just a couple of updates) succeed within 16 steps.

### Step 2: Finding 5 Successful Learning Rates
Testing five distinct values across the slider confirms `100.0%` classification accuracy on each run:

1. **`0.02` (Success):** Converged to `100.0%` accuracy (`1/5`).
2. **`0.67` (Success):** Converged to `100.0%` accuracy (`2/5`).
3. **`1.00` (Success):** Converged to `100.0%` accuracy (`3/5`).
4. **`1.5` (Success):** Converged to `100.0%` accuracy (`4/5`).
5. **`2.09` (Success):** Converged to `100.0%` accuracy (`5/5`) — after a single misclassification update on `(-3, -4) -> 0` at step 2, the parameters jumped directly to $w_1 = 7.27$, $w_2 = 7.36$, and $b = -2.09$, locking in `100.0%` accuracy for the remainder of the 16 steps.

Once all 5 successful learning rates were logged (`5/5`), the Status panel unlocked and revealed the flag.

---

## 4. Flag

```text
academy{REDACTED}