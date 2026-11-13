# Perceptron Train Classic 0

* **Challenge:** Perceptron Train Classic 0
* **Category:** Artificial Intelligence
* **Event:** AI Foundations
* **Difficulty:** Easy
* **Author:** LT 'syreal' Jones

---

## 1. Challenge Overview
Watch a perceptron learn in real time using the classic update rule: only misclassified points trigger updates, with no weight decay. This dataset is intentionally gentle, so many learning rates still converge quickly. Dial in a rate, trigger a run, and the interface will animate each step until every point is classified correctly.

**Objective:** Tune the learning rate of a single-layer perceptron so it reaches 100% classification accuracy on a cleanly linearly separable dataset within 16 update steps.

---

## 2. Reconnaissance & Initial Analysis

### Connection / Files Provided
* **Target / Endpoint:** `http://chatelaine.cylabacademy.net:19393`
* **Provided Artifacts:** None — the challenge is a browser-based interactive visualizer, so there was no binary or source code to inspect

### Initial Observations
The interface plots 8 data points cleanly separated into two clusters: 4 positive class points (blue) in the upper-right quadrant and 4 negative class points (orange) in the lower-left quadrant. Because the dataset is cleanly linearly separable, a single straight decision boundary can easily classify all 8 points (`100.0%` accuracy) without needing aggressive parameter jumps.

---

## 3. Exploitation / Step-by-Step Walkthrough

### Step 1: Tuning the Learning Rate
A small learning rate allows the perceptron to smoothly rotate its initial decision boundary into the wide margin between the two clusters without overshooting.

* **Player action:** Set the **Learning rate** to `0.02` and click **Run training**
* **Result:** The model makes gradual, stable updates to its weights ($w_1, w_2$) and bias ($b$) across the training steps.

### Step 2: Converging to 100% Accuracy
Within 13 update steps, the decision boundary settles into a clean separation:

* **Steps 1–5:** Starting from $w_1 = 1.00$, $w_2 = -1.00$, and $b = 0.00$ (`50.0%` accuracy), misclassifications on `(-3, -4) -> 0`, `(-2, -3) -> 0`, and `(3, 4) -> 1` nudge the weights to $w_1 = 1.16$, $w_2 = -0.78$, and $b = -0.02$, raising accuracy to `75.0%`.
* **Step 13:** By step 13 (`sample 5`), the parameters converge to $w_1 = 1.20$, $w_2 = -0.72$, and $b = 0.00$, reaching `100.0%` accuracy.

With all 4 blue points on one side of the line and all 4 orange points on the other, the Status panel confirms `100.0%` accuracy within the 16-step limit and reveals the flag.

---

## 4. Flag

```text
academy{REDACTED}