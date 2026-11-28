# Neuron Express 0

- **Platform:** picoCTF
- **Event:** AI Foundations
- **Category:** Artificial Intelligence
- **Difficulty:** Easy
- **Author:** LT 'syreal' Jones

---

## 1. Challenge Overview
Probe a 1D perceptron over the network. Send it integers and watch whether the neuron fires or not. Use those responses to figure out the underlying weight and bias, then submit your guess with the `TEST` command to earn the flag.

**Objective:** Probe a hidden 1D perceptron ($w \cdot x + b \ge 0$) within the $[-10, 10]$ integer input bounds to determine its decision boundary, then submit a matching weight and bias pair via `TEST w b` that reproduces the perceptron's outputs for every integer in range.

---

## 2. Reconnaissance & Initial Analysis

### Connection / Files Provided
- **Target / Endpoint:** `nc chatelaine.cylabacademy.net 46826`
- **Provided Artifacts:** None — the challenge is an interactive black-box perceptron service over netcat, so there was no binary or source code to inspect.

### Initial Observations
- The neuron evaluates $w \cdot x + b \ge 0$, returning `1` ("Perceptron fires!") when non-negative and `0` ("Perceptron stays quiet.") otherwise.
- Inputs must be integers within $[-10, 10]$ (up to 128 queries), and guesses are evaluated via `TEST w b` across all 21 integers in the range.
- Because the activation function is a 1D linear threshold, any $(w, b)$ pair that shares the exact same firing threshold over the integers $[-10, 10]$ produces identical outputs and passes validation.

---

## 3. Exploitation / Step-by-Step Walkthrough

### Step 1: Determining Orientation and Narrowing the Interval
By probing initial anchor points on the integer line, we establish the sign of the weight $w$ and bracket the transition point:
- **`0` $\rightarrow$ `0` (quiet):** Confirms $b < 0$.
- **`1` $\rightarrow$ `0` (quiet):** Confirms $w + b < 0$.
- **`5` $\rightarrow$ `1` (fires):** Confirms $5w + b \ge 0$, proving $w > 0$ and placing the firing threshold $T$ inside $\{2, 3, 4, 5\}$.
- **`TEST 1 -5` $\rightarrow$ Failed:** A threshold at $x = 5$ did not match all integers in $[-10, 10]$, ruling out $T = 5$ and narrowing the threshold to $T \in \{2, 3, 4\}$.

### Step 2: Binary Search for the Exact Threshold
Testing the midpoint $x = 3$ isolates the exact integer transition point $T$:
- If `3` fires (`1`), probing `2` distinguishes between $T = 2$ (if `2` fires) and $T = 3$ (if `2` stays quiet).
- If `3` stays quiet (`0`), the threshold is guaranteed to be $T = 4$.

### Step 3: Parameterizing and Submitting the Guess
Once the smallest firing integer $T$ is identified, setting $w = 1$ and $b = -T$ yields:

$$1 \cdot x - T \ge 0 \iff x \ge T$$

Submitting `TEST 1 -<T>` matches the hidden perceptron's output across every integer in $[-10, 10]$ and prints the flag.

---

## 4. Flag

```text
academy{REDACTED}