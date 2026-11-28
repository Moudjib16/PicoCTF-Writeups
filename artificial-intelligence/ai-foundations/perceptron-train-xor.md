# Perceptron Train XOR

- **Platform:** picoCTF
- **Event:** AI Foundations
- **Category:** Artificial Intelligence
- **Difficulty:** Easy
- **Author:** LT 'syreal' Jones

---

## 1. Challenge Overview
Watch a perceptron learn in real time on XOR data using the classic update rule: only misclassified points trigger updates, with no weight decay. Because XOR is not linearly separable, a single perceptron cannot hit 100% accuracy. Reach 75% accuracy to prove you understand the limitation and reveal the flag.

**Objective:** Tune the learning rate of a single-layer perceptron so it reaches the maximum possible 75% accuracy on XOR data within 16 steps.

---

## 2. Reconnaissance & Initial Analysis

### Connection / Files Provided
* **Target / Endpoint:** `http://chatelaine.cylabacademy.net:48035`
* **Provided Artifacts:** None — the challenge is a browser-based interactive visualizer, so there was no binary or source code to inspect

### Initial Observations
The interface plots four points in an XOR configuration: `(-2, 2)` and `(2, -2)` as one class (blue), and `(-2, -2)` and `(2, 2)` as the other (orange). Because a single-layer perceptron only draws a single straight decision boundary, it can separate at most 3 out of 4 points (75% accuracy). If the learning rate is set too high, the boundary overshoots and oscillates without settling.

---

## 3. Exploitation / Step-by-Step Walkthrough

### Step 1: Tuning the Learning Rate
Lowering the learning rate prevents the weights from oscillating wildly across the plot when misclassified points trigger updates.

* **Player action:** Set the **Learning rate** to `0.02` and click **Run training**
* **Result:** The perceptron makes small, controlled adjustments to its weights ($w_1, w_2$) and bias ($b$) rather than overshooting.

### Step 2: Converging to 75% Accuracy
Within just two update steps, the decision boundary settles into a valid 3-of-4 split:

* **Step 1:** Evaluates `(-2, -2) -> 0` (predicted `1`, error `-1`), updating parameters to $w_1 = 1.04$, $w_2 = -0.96$, $b = -0.02$ (`50.0%` accuracy).
* **Step 2:** Evaluates `(2, 2) -> 0` (predicted `1`, error `-1`), updating parameters to $w_1 = 1.00$, $w_2 = -1.00$, $b = -0.04$ (`75.0%` accuracy).

At 75% accuracy, the boundary isolates `(2, 2)` from the other three points, hitting the target threshold and revealing the flag in the Status panel.

---

## 4. Flag

```text
academy{REDACTED}
```