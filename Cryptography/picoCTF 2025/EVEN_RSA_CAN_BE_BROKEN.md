# EVEN RSA CAN BE BROKEN???

- **Platform:** picoCTF
- **Event:** picoCTF 2025
- **Category:** Cryptography
- **Difficulty:** Easy
- **Author:** Michael Crotty

---

## 1. Challenge Overview

> This service provides you an encrypted flag. Can you decrypt it with just N & e?

**Hints:**
1. How much do we trust randomness?
2. Notice anything interesting about N?
3. Try comparing N across multiple requests

**Objective:** Recover the plaintext flag from an RSA ciphertext using only the public key `(N, e)`.

---

## 2. Reconnaissance & Initial Analysis

### Files Provided
- **Provided Artifact:** A challenge instance. Connecting to it prints `N`, `e` and the ciphertext `c`.

### Initial Observations

The service gave me these values (they change with every instance):

```text
N = 15424048554547657957921856435660559273370524290746504055028692839882927120239817554031457747034773646915346242572002915658908465982480390093888128692136154
e = 65537
c = 2877202933090238740815690001242684594293297236980539773342785377906815641843713276876288143364314918667041921790796270480127476908822745412379706196805377
```

- `e = 65537` is the standard public exponent, so there's nothing unusual there.
- **`N` ends in `4`, so it is even.** A proper RSA modulus is the product of two large odd primes, so it is always odd. An even `N` means one of its prime factors is `2`.

---

## 3. Step-by-Step Walkthrough

### Step 1: Factor N

RSA is secure only because factoring `N = p × q` is hard. Here it's trivial:

```text
p = 2
q = N / 2
```

You can check that `q` is prime (for example with `sympy.isprime`). It is a 512-bit prime. The hints point at the cause: the key generator's "random" prime choice isn't random enough, and one of the primes ends up being `2`. If you compare `N` across several requests, look for a factor they share. You can find a shared factor with `gcd(N1, N2)`.

### Step 2: Compute the private key

With both factors known, the private key is ordinary RSA math:

```text
phi(N) = (p - 1)(q - 1) = q - 1
d      = e^-1 mod phi(N)
```

### Step 3: Decrypt

The script uses only the Python standard library:

```python
N = 15424048554547657957921856435660559273370524290746504055028692839882927120239817554031457747034773646915346242572002915658908465982480390093888128692136154
e = 65537
c = 2877202933090238740815690001242684594293297236980539773342785377906815641843713276876288143364314918667041921790796270480127476908822745412379706196805377

p = 2
q = N // 2
assert p * q == N

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)          # modular inverse (Python 3.8+)
m = pow(c, d, N)

print(m.to_bytes((m.bit_length() + 7) // 8, "big").decode())
```

```bash
python solve.py
```

The script prints the flag. Paste in the `N` and `c` from your own instance, because they're different every time.

---

## 4. Flag

```text
academy{REDACTED}
```

---

## 5. Key Takeaways

- An RSA modulus must be odd. If `N` is even, `2` is a factor and the key is broken immediately.
- RSA security depends on the quality of the primes. A weak or buggy prime generator breaks the scheme no matter how big the key is.
- Before reaching for heavier tools like RsaCtfTool or factordb, check `N` for simple flaws: small factors, a factor shared between keys (`gcd(N1, N2)`), or `p` and `q` that are too close together.
