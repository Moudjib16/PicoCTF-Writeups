# StegoRSA

- **Platform:** picoCTF
- **Event:** picoCTF 2026
- **Category:** Cryptography / Steganography
- **Difficulty:** Easy
- **Author:** Yahaya Meddy

---

## 1. Challenge Overview

> *"A message has been encrypted using RSA. The public key is gone… but someone might have been careless with the private key. Can you recover it and decrypt the message? Download the flag and image."*

We are provided with two files:
1. `flag.enc` — An RSA-encrypted binary file containing the flag.
2. `image.jpg` — A standard JPEG image that supposedly hides or leaks the RSA private key.

---

## 2. Step-by-Step Solution

### Step 1: Inspecting Image Metadata
Because the prompt hints that *"someone might have been careless with the private key"* and provides an image file, the first logical step in steganography/forensics challenges is to inspect the file's EXIF metadata (comments, author fields, descriptions, etc.).

Using `exiftool`, we extract the `Comment` tag in binary/raw mode (`-b`) and redirect it to a file:

```bash
exiftool -b -Comment image.jpg > private.key
```

* **Why this works:** JPEG files support arbitrary text strings in their header segments (specifically the `COM` marker). Creators often hide keys, hints, or base64/hex payloads here. Using `-b` ensures `exiftool` outputs the exact raw data without truncating or formatting line breaks.

---

### Step 2: Decoding the Hex-Encoded Key
Inspecting the extracted `private.key` reveals a continuous string of hexadecimal characters:

```bash
cat private.key
# Output: 2d2d2d2d2d424547494e2050524956415445204b45592d2d2d2d2d0a4d...
```

Recognizing the `2d2d2d2d2d` prefix as `-----` in ASCII, we convert the hex dump back into standard ASCII text using `xxd`:

```bash
xxd -r -p private.key > decode.key
```

* **Why these flags:** 
  * `-r` tells `xxd` to reverse the operation (convert hex to binary/text).
  * `-p` specifies plain postscript/continuous hex dump style (no line numbers or ASCII sidebar).

Checking `decode.key` confirms we now have a valid PEM-formatted PKCS#8 RSA Private Key:

```text
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCxGCNdItl8tylV
...
XysrXGk3ukcuQhRjTpBQ1v4=
-----END PRIVATE KEY-----
```

---

### Step 3: Decrypting the Flag (and Troubleshooting OpenSSL)

Initially, attempting to decrypt `flag.enc` using the raw hex file (`private.key`) or the legacy `rsautl` command results in OpenSSL errors:

```bash
openssl rsautl -decrypt -in flag.enc -out flag.txt -inkey private.key
# Warning: The command rsautl was deprecated in version 3.0. Use 'pkeyutl' instead.
# Error: Could not find or decode private key from private.key
```

**Why it failed:**
1. `private.key` was still hex-encoded rather than decoded PEM (`decode.key`).
2. `rsautl` is deprecated in OpenSSL 3.0+ in favor of the modern `pkeyutl` utility.

Running `openssl pkeyutl` with the properly decoded PEM key (`decode.key`) succeeds cleanly:

```bash
openssl pkeyutl -decrypt -inkey decode.key -in flag.enc -out decrypted_message.txt
```

Reading the output file reveals the flag:

```bash
cat decrypted_message.txt
# Output: academy{REDACTED}
```

---


## 3. Alternative Tools & Methods

If you do not have `exiftool`, `xxd`, or `openssl` installed, you can achieve the exact same result using standard Linux utilities or Python:

### Alternative 1: Extracting Metadata without `exiftool`
* **`strings`:** Since the key was stored as ASCII hex inside the JPEG header, running `strings image.jpg | head -n 20` will immediately display the hex string near the top of the file.
* **`exiv2`:** Running `exiv2 -p c image.jpg` prints only the JPEG comment field.
* **`binwalk` / Hex Editors (`xxd`, `hexdump`):** Viewing the first few hundred bytes of `image.jpg` reveals the `FF FE` (JPEG Comment) marker followed directly by the hex string.

### Alternative 2: Decoding Hex without `xxd`
* **Python:**
  ```bash
  python3 -c "open('decode.key', 'wb').write(bytes.fromhex(open('private.key').read().strip()))"
  ```
* **`sed` + `printf` / `perl`:**
  ```bash
  perl -pe 's/([0-9a-f]{2})/chr(hex($1))/gie' private.key > decode.key
  ```

### Alternative 3: Decrypting RSA without `openssl` CLI
You can decrypt `flag.enc` programmatically using Python's `cryptography` or `pycryptodome` libraries:

```python
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5

# Load the PEM private key
with open("decode.key", "rb") as key_file:
    private_key = RSA.import_key(key_file.read())

# Load the ciphertext
with open("flag.enc", "rb") as enc_file:
    ciphertext = enc_file.read()

# Decrypt using PKCS#1 v1.5 padding (OpenSSL's default)
cipher = PKCS1_v1_5.new(private_key)
plaintext = cipher.decrypt(ciphertext, sentinel=None)

print(plaintext.decode())
```

---

## 4. Key Takeaways & Security Lessons

1. **Metadata Hygiene:** Image files frequently carry hidden metadata (EXIF, XMP, COM markers). Never store credentials, API tokens, or cryptographic keys inside media files, even if obfuscated in hex or base64.
2. **Encoding vs. Encryption:** Hexadecimal encoding (`2d2d2d...`) is not encryption—it provides zero confidentiality and can be reversed instantly once discovered.
3. **OpenSSL Modernization:** In modern Linux distributions running OpenSSL 3.x+, always prefer `openssl pkeyutl` over legacy commands like `rsautl`.


## 5. Flag

```text
academy{REDACTED}
```

---