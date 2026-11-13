# Perceptron Train Hole in Middle

* **Challenge:** Perceptron Train Hole in Middle
* **Category:** Artificial Intelligence
* **Event:** AI Foundations
* **Difficulty:** Easy
* **Author:** LT 'syreal' Jones

---

## 1. Challenge Overview
Watch a perceptron learn in real time on a "hole in the middle" pattern: positive points surround one negative center point. The classic perceptron update rule still applies (only misclassified points trigger updates, with no weight decay), but this shape is not linearly separable by a single line. Reach 88.9% accuracy to reveal the flag.

**Objective:** Tune the learning rate of a single-layer perceptron so it reaches the maximum possible 88.9% accuracy on a ring-with-center dataset within 16 steps.

---

## 2. Reconnaissance & Initial Analysis

### Connection / Files Provided
* **Target / Endpoint:** `http://chatelaine.cylabacademy.net:18721`
* **Provided Artifacts:** None — the challenge is a browser-based interactive visualizer, so there was no binary or source code to inspect

### Initial Observations
The interface plots 9 data points: 8 outer points arranged in a ring belonging to the positive class (blue) and 1 center point at `(0, 0)` belonging to the negative class (orange). Because a single-layer perceptron only draws a single straight decision boundary, it cannot enclose the center point and can correctly classify at most 8 out of 9 points (88.9% accuracy) by pushing the line outside the entire ring.

---

## 3. Exploitation / Step-by-Step Walkthrough

### Step 1: Tuning the Learning Rate
Unlike the XOR/XNOR layouts where the boundary needed to sit between opposing corners, here the perceptron needs larger parameter updates to push the decision boundary completely past the outer ring of positive points within the 16-step limit.

* **Player action:** Set the **Learning rate** to `0.90` and click **Run training**
* **Result:** The larger learning rate allows the bias and weights to shift rapidly enough to clear the outer positive points before hitting the 16-update cap.

### Step 2: Converging to 88.9% Accuracy
Over 12 steps, the decision boundary shifts toward the bottom-left edge of the plot:

* **Steps 1–5:** Starting from initial misclassifications on `(0, 3) -> 1` and `(2, -2) -> 1`, the model adjusts its weights to $w_1 = 2.80$, $w_2 = -0.10$, and $b = 1.80$, reaching `55.6%` accuracy.
* **Step 12:** By step 12 (`sample 3`), the parameters settle at $w_1 = 1.00$, $w_2 = 0.80$, and $b = 4.50$, reaching `88.9%` accuracy.

With the boundary line pushed outside all 8 outer blue points, all positive points are classified correctly while only the center orange point `(0, 0)` is misclassified—achieving 8/9 (`88.9%`) accuracy and revealing the flag in the Status panel.

---

## 4. Flag

```text
academy{REDACTED}