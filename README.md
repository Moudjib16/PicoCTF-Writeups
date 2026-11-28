# picoCTF Writeups

Step-by-step writeups for [picoCTF](https://picoctf.org/) challenges, explaining the reasoning, tools and key takeaways behind each solve.

![Writeups](https://img.shields.io/badge/writeups-55-blue)
![Last commit](https://img.shields.io/github/last-commit/Moudjib16/PicoCTF-Writeups)
![picoCTF](https://img.shields.io/badge/platform-picoCTF-orange)

---

## About

I write these to learn, not just to collect flags. Each writeup walks through how I approached the challenge, why the solution works, and what the challenge teaches about real-world security.

The challenges are solved through **picoCTF** and the **CyLab Security Academy**. Academy instances use the flag format `academy{...}` instead of `picoCTF{...}`, which is why you'll see both in these writeups.

## Progress

<!-- Updated automatically by .github/workflows/writeups.yml -->
<!-- progress:start -->
| Category | Solved |
|---|---|
| [General Skills](#general-skills) | 27 |
| [AI Foundations](#ai-foundations) | 16 |
| [Cryptography](#cryptography) | 8 |
| [Web Exploitation](#web-exploitation) | 3 |
| [Forensics](#forensics) | 1 |
| **Total** | **55** |
<!-- progress:end -->

---

## General Skills

| Challenge | Event | Difficulty | Technique |
|---|---|---|---|
| [2warm](general-skills/picoctf-2019/2warm.md) | picoCTF 2019 | Easy | Decimal to binary conversion |
| [Bases](general-skills/picoctf-2019/bases.md) | picoCTF 2019 | Easy | Base64 decoding |
| [First Grep](general-skills/picoctf-2019/first-grep.md) | picoCTF 2019 | Easy | Searching a file with `grep` and regex |
| [strings it](general-skills/picoctf-2019/strings-it.md) | picoCTF 2019 | Easy | `strings` + `grep` on a binary |
| [Warmed Up](general-skills/picoctf-2019/warmed-up.md) | picoCTF 2019 | Easy | Number base conversion in CyberChef |
| [what's a net cat?](general-skills/picoctf-2019/whats-a-net-cat.md) | picoCTF 2019 | Easy | Connecting to a service with `nc` |
| [Obedient Cat](general-skills/picoctf-2021/obedient-cat.md) | picoCTF 2021 | Easy | Reading a file with `cat` |
| [Python Wrangling](general-skills/picoctf-2021/python-wrangling.md) | picoCTF 2021 | Medium | Running a Python decryption script |
| [Tab, Tab, Attack](general-skills/picoctf-2021/tab-tab-attack.md) | picoCTF 2021 | Easy | Tab completion through nested directories |
| [Wave a flag](general-skills/picoctf-2021/wave-a-flag.md) | picoCTF 2021 | Easy | `chmod +x` and program help flags |
| [PW Crack 1](general-skills/beginner-picomini-2022/pw-crack-1.md) | Beginner picoMini 2022 | Easy | Hardcoded password in source |
| [PW Crack 2](general-skills/beginner-picomini-2022/pw-crack-2.md) | Beginner picoMini 2022 | Easy | Deobfuscating a password check |
| [PW Crack 3](general-skills/beginner-picomini-2022/pw-crack-3.md) | Beginner picoMini 2022 | Medium | Matching candidate passwords to an MD5 hash |
| [PW Crack 4](general-skills/beginner-picomini-2022/pw-crack-4.md) | Beginner picoMini 2022 | Medium | Automating a 100-candidate hash check |
| [PW Crack 5](general-skills/beginner-picomini-2022/pw-crack-5.md) | Beginner picoMini 2022 | Medium | MD5 dictionary attack |
| [Super SSH](general-skills/picoctf-2024/super-ssh.md) | picoCTF 2024 | Easy | SSH basics |
| [bytemancy 0](general-skills/picoctf-2026/bytemancy-0.md) | picoCTF 2026 | Easy | ASCII decimal to characters |
| [bytemancy 1](general-skills/picoctf-2026/bytemancy-1.md) | picoCTF 2026 | Easy | Generating a long payload with Python |
| [MY GIT](general-skills/picoctf-2026/my-git.md) | picoCTF 2026 | Easy | Spoofing a git author to trigger a push hook |
| [Password Profiler](general-skills/picoctf-2026/password-profiler.md) | picoCTF 2026 | Easy | OSINT-based wordlist, SHA-1 matching |
| [Piece by Piece](general-skills/picoctf-2026/piece-by-piece.md) | picoCTF 2026 | Easy | Rejoining split files, password-protected ZIP |
| [ping-cmd](general-skills/picoctf-2026/ping-cmd.md) | picoCTF 2026 | Easy | OS command injection |
| [Printer Shares](general-skills/picoctf-2026/printer-shares.md) | picoCTF 2026 | Easy | Enumerating SMB shares with `smbclient` |
| [SUDO MAKE ME A SANDWICH](general-skills/picoctf-2026/sudo-make-me-a-sandwich.md) | picoCTF 2026 | Easy | Abusing `sudo` permissions |
| [Undo](general-skills/picoctf-2026/undo.md) | picoCTF 2026 | Easy | Reversing layered text transforms (Base64, reverse, ROT13) |
| [Big Zip](general-skills/picogym-exclusive/big-zip.md) | picoGym Exclusive | Easy | Recursive `grep` |
| [Log Hunt](general-skills/picomini-cmu-africa/log-hunt.md) | picoMini by CMU-Africa | Easy | Extracting and deduplicating flag fragments from logs |

## AI Foundations

| Challenge | Event | Difficulty | Technique |
|---|---|---|---|
| [Assistant or Agent?](artificial-intelligence/ai-foundations/assistant-or-agent.md) | AI Foundations | Easy | AI assistants vs agents, guardrails, human-in-the-loop |
| [Trust But Verify](artificial-intelligence/ai-foundations/trust-but-verify.md) | AI Foundations | Easy | Verifying AI-generated stats, code and citations |
| [Neuron Meet 0](artificial-intelligence/ai-foundations/neuron-meet-0.md) | AI Foundations | Easy | Steering a 1D perceptron to output ASCII bits |
| [Neuron Meet 2D-0](artificial-intelligence/ai-foundations/neuron-meet-2d-0.md) | AI Foundations | Easy | Steering a 2D perceptron to output ASCII bits |
| [Neuron Express 0](artificial-intelligence/ai-foundations/neuron-express-0.md) | AI Foundations | Easy | Probing a hidden 1D perceptron's boundary |
| [Neuron Express 2D-0](artificial-intelligence/ai-foundations/neuron-express-2d-0.md) | AI Foundations | Easy | Probing a hidden 2D perceptron's boundary |
| [Perceptron Play 1D Alpha](artificial-intelligence/ai-foundations/perceptron-play-1d-alpha.md) | AI Foundations | Easy | Hand-tuning weight and bias in 1D |
| [Perceptron Play Alpha](artificial-intelligence/ai-foundations/perceptron-play-alpha.md) | AI Foundations | Easy | Hand-tuning a 2D decision boundary |
| [Perceptron Play Naught](artificial-intelligence/ai-foundations/perceptron-play-naught.md) | AI Foundations | Easy | Hand-tuning a 2D decision boundary |
| [Perceptron Train Classic 0](artificial-intelligence/ai-foundations/perceptron-train-classic-0.md) | AI Foundations | Easy | Learning rate tuning on separable data |
| [Perceptron Train Classic 1](artificial-intelligence/ai-foundations/perceptron-train-classic-1.md) | AI Foundations | Easy | Finding several working learning rates |
| [Perceptron Train Classic 2 Alpha](artificial-intelligence/ai-foundations/perceptron-train-classic-2-alpha.md) | AI Foundations | Easy | Finding several working learning rates |
| [Perceptron Train XOR](artificial-intelligence/ai-foundations/perceptron-train-xor.md) | AI Foundations | Easy | XOR is not linearly separable |
| [Perceptron Train XNOR](artificial-intelligence/ai-foundations/perceptron-train-xnor.md) | AI Foundations | Easy | XNOR is not linearly separable |
| [Perceptron Train 3-Bit Parity](artificial-intelligence/ai-foundations/perceptron-train-3-bit-parity.md) | AI Foundations | Easy | Parity is not linearly separable |
| [Perceptron Train Hole in Middle](artificial-intelligence/ai-foundations/perceptron-train-hole-in-middle.md) | AI Foundations | Easy | Limits of a linear boundary on ring data |

## Cryptography

| Challenge | Event | Difficulty | Technique |
|---|---|---|---|
| [13](cryptography/picoctf-2019/13.md) | picoCTF 2019 | Easy | ROT13 |
| [The Numbers](cryptography/picoctf-2019/the-numbers.md) | picoCTF 2019 | Easy | A1Z26 letter-number cipher |
| [Mod 26](cryptography/picoctf-2021/mod-26.md) | picoCTF 2021 | Easy | ROT13 |
| [interencdec](cryptography/picoctf-2024/interencdec.md) | picoCTF 2024 | Easy | Double Base64 + Caesar shift |
| [EVEN RSA CAN BE BROKEN???](cryptography/picoctf-2025/even-rsa-can-be-broken.md) | picoCTF 2025 | Easy | Even RSA modulus, factoring N = 2 × q |
| [hashcrack](cryptography/picoctf-2025/hashcrack.md) | picoCTF 2025 | Easy | Cracking unsalted MD5 / SHA hashes |
| [Shared Secrets](cryptography/picoctf-2026/shared-secrets.md) | picoCTF 2026 | Easy | Leaked Diffie-Hellman key, single-byte XOR |
| [StegoRSA](cryptography/picoctf-2026/stegorsa.md) | picoCTF 2026 | Easy | RSA key hidden in JPEG metadata, OpenSSL |

## Web Exploitation

| Challenge | Event | Difficulty | Technique |
|---|---|---|---|
| [Insp3ct0r](web-exploitation/picoctf-2019/insp3ct0r.md) | picoCTF 2019 | Easy | Reading client-side HTML, CSS and JS |
| [where are the robots](web-exploitation/picoctf-2019/where-are-the-robots.md) | picoCTF 2019 | Easy | `robots.txt` disclosure |
| [Old Sessions](web-exploitation/picoctf-2026/old-sessions.md) | picoCTF 2026 | Easy | Session hijacking with a leaked token |

## Forensics

| Challenge | Event | Difficulty | Technique |
|---|---|---|---|
| [Enhance!](forensics/picoctf-2022/enhance.md) | picoCTF 2022 | Medium | Reading text hidden in SVG XML |

---

## Repository Layout

Each writeup lives under its category, then the event it comes from:

```text
category/
└── event/
    └── challenge-name.md
```

For example: `cryptography/picoctf-2026/shared-secrets.md`.

## Writeup Format

New writeups follow the [writeup template](templates/writeup-template.md). Older ones use a shorter version of it.

1. **Challenge Overview:** the official description and the objective
2. **Reconnaissance & Initial Analysis:** files, endpoints and first observations
3. **Hypotheses & Testing:** what I suspected and how I checked it
4. **Step-by-Step Walkthrough:** commands, scripts and output
5. **Failed Attempts & Lessons:** what didn't work and why
6. **Flag & Verification**
7. **Tools & Techniques**
8. **Key Takeaways & Remediation:** the concept, root cause and how to prevent it
9. **References & Resources**

## Disclaimer

Flags are **redacted on purpose**. These writeups are meant to help you learn, so try each challenge yourself first and come back if you get stuck.

All challenges belong to picoCTF / Carnegie Mellon University. This repository is not affiliated with them.


## Contact

Found a mistake or have a better solution? Open an [issue](https://github.com/Moudjib16/PicoCTF-Writeups/issues), or contact me on GitHub at [@Moudjib16](https://github.com/Moudjib16).
