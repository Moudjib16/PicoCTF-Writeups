# bytemancy 0

- **Platform:** picoCTF
- **Event:** picoCTF 2026
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** LT 'syreal' Jones

---

## Challenge Description
> Can you conjure the right bytes? The program's source code can be downloaded here. Connect to the program with netcat:  
> `$ nc xebec.cylabacademy.net 15933`

---

## Reconnaissance & Source Code Analysis
Inspecting the provided `app.py` source file reveals how the remote service validates user input:

```python
while(True):
  try:
    print('⊹──────[ BYTEMANCY-0 ]──────⊹')
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print()
    print('Send me ASCII DECIMAL 101, 101, 101, side-by-side, no space.')
    print()
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print('⊹─────────────⟡─────────────⊹')
    user_input = input('==> ')
    if user_input == "\x65\x65\x65":
      print(open("./flag.txt", "r").read())
      break
    else:
      print("That wasn't it. I got: " + str(user_input))
      print()
      print()
      print()
  except Exception as e:
    print(e)
    break
```

Key observations from the code:
1. **Target Byte:** ASCII decimal `101` corresponds to hexadecimal `0x65` (`\x65`), which is the lowercase character `'e'`.
2. **Repetition Requirement:** The program compares `user_input` to `"\x65\x65\x65"`, which is just the string `"eee"`. The challenge text says "101, 101, 101, side-by-side, no space", so the input is three `'e'` characters in a row.
3. **No automation needed:** Unlike bytemancy 1, the payload is only three characters long, so it can be typed straight into the `netcat` prompt.

---

## Solution

### Typing the Payload Directly
Connect with `netcat` and type `eee` at the `==>` prompt:

```bash
nc xebec.cylabacademy.net 15933
```

**Output:**
```text
⊹──────[ BYTEMANCY-0 ]──────⊹
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐

Send me ASCII DECIMAL 101, 101, 101, side-by-side, no space.

☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
⊹─────────────⟡─────────────⊹
==> eee
academy{REDACTED}
```

### One-Liner Alternative
The same payload can be piped in with Python (this is the approach needed for bytemancy 1):

```bash
python -c 'print("\x65"*3)' | nc xebec.cylabacademy.net 15933
```

---

## Flag
```text
academy{REDACTED}
```
