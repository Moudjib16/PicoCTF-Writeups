# Shared Secrets

- **Platform:** picoCTF
- **Event:** picoCTF 2026
- **Category:** Cryptography
- **Difficulty:** Easy
- **Author:** Yahaya Meddy

---

## 1. Challenge Overview

> A message was encrypted using a shared secret... but it looks like one side of the exchange leaked something. Can you piece together the secret and get the flag? Download the message. And source code

**Hint:**
1. What do you get if you combine a public key with a known private one?

**Objective:** Rebuild the Diffie-Hellman shared secret from the leaked values and use it to decrypt the flag.

---

## 2. Reconnaissance & Initial Analysis

### Files Provided
- `message.txt`: the values from the key exchange plus the encrypted flag
- `encryption.py`: the script that produced `message.txt`

### Initial Observations

```bash
cat message.txt
```

```text
g = 2
p = 2927273144810939766701580090813587829846998218139050366191650895496341639672151115600622801622875986429173669666450605563086095565809406776099318149676703864803530494465478726922189453273460829331935414785533102652757649572940785971419755291375295328412738229475603220295990344218551730029944293124696567146516090193
A = 573064858108775587796401031506157877018348288426226470285524205679136075971072753567297355763163615870402991691187850746336169042262692610483425859830970803563824285074033597222769345556533666344979747486571381174509140455398567155637545070339870299749606406694126580709457390475875189904723414950764573551900114879
b = 310480984845844782350469929488957103404065672967681721794433968598078606678457574115948893342658016388850300951548689390362586285081923158250912861928954606683971373959652287246659410807804603053375492104235114782698335962292773627028417650732575398422905666599383548621368163602765974099546321049636858616564366046
enc = 43414346474f5b59464a7d5111415011567d16161347401b47475f
```

The important lines in `encryption.py`:

```python
g = 2
p = getPrime(1048)

a = randint(2, p-2)          # server's private key
A = pow(g, a, p)             # server's public key

b = randint(2, p-2)          # client's private key
B = pow(g, b, p)             # client's public key

shared = pow(A, b, p)        # shared secret

enc = bytes([x ^ (shared % 256) for x in flag])
```

- This is a textbook Diffie-Hellman key exchange.
- **The file leaks `b`, the client's private key.** Only public values (`g`, `p`, `A`, `B`) should ever be shared.
- The flag is XORed with a single byte: `shared % 256`.

---

## 3. Step-by-Step Walkthrough

### Step 1: Rebuild the shared secret

In Diffie-Hellman, each side combines the other side's public key with its own private key:

```text
Server:  S = B^a mod p
Client:  S = A^b mod p
```

Both give the same value, `g^(ab) mod p`. We have `A` (public) and `b` (leaked), so we can compute the secret exactly as the client did. This is what the hint means.

### Step 2: Derive the key and decrypt

The encryption uses only the lowest byte of the secret, `S % 256`, which here is `34` (`0x22`). XOR is its own inverse, so XORing the ciphertext with the same byte gives back the flag.

The script uses only the Python standard library (`encryption.py` needs `pycryptodome`, but solving doesn't):

```python
g = 2
p = 2927273144810939766701580090813587829846998218139050366191650895496341639672151115600622801622875986429173669666450605563086095565809406776099318149676703864803530494465478726922189453273460829331935414785533102652757649572940785971419755291375295328412738229475603220295990344218551730029944293124696567146516090193
A = 573064858108775587796401031506157877018348288426226470285524205679136075971072753567297355763163615870402991691187850746336169042262692610483425859830970803563824285074033597222769345556533666344979747486571381174509140455398567155637545070339870299749606406694126580709457390475875189904723414950764573551900114879
b = 310480984845844782350469929488957103404065672967681721794433968598078606678457574115948893342658016388850300951548689390362586285081923158250912861928954606683971373959652287246659410807804603053375492104235114782698335962292773627028417650732575398422905666599383548621368163602765974099546321049636858616564366046
enc = bytes.fromhex("43414346474f5b59464a7d5111415011567d16161347401b47475f")

# 1. Compute the shared secret S
S = pow(A, b, p)

# 2. Derive the single-byte XOR key (S % 256 = 34) and decrypt
key = S % 256
flag = bytes(byte ^ key for byte in enc).decode()
print(flag)
```

```bash
python script.py
```

The script prints the flag.

---

## 4. Alternative: Skip the Key Exchange Entirely

Since the key is a single byte, there are only 256 possible keys. You don't need `A`, `b` or `p` at all:

- **Known plaintext:** the flag starts with `academy{`. The first ciphertext byte is `0x43` and `a` is `0x61`, so `0x43 ^ 0x61 = 0x22 = 34`. That is the key.
- **Brute force:** try every key from 0 to 255 and keep the output that starts with `academy{`.

```python
enc = bytes.fromhex("43414346474f5b59464a7d5111415011567d16161347401b47475f")
for k in range(256):
    pt = bytes(x ^ k for x in enc)
    if pt.startswith(b"academy{"):
        print(k, pt.decode())
```

---

## 5. Flag

```text
academy{REDACTED}
```

---

## 6. Key Takeaways

- Diffie-Hellman is only secure while both private keys (`a` and `b`) stay secret. If either one leaks, anyone can compute the shared secret from the other side's public key.
- A 1048-bit secret doesn't help if only 8 bits of it are used. `shared % 256` reduces the key to 256 options, which can be brute-forced instantly.
- Single-byte XOR is not real encryption. Known plaintext (like a flag prefix) gives away the key right away. In practice, the shared secret should go through a key derivation function (for example HKDF), and the derived key should feed a real cipher such as AES-GCM.
