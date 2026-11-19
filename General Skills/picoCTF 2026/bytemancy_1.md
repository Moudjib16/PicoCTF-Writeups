# bytemancy 1

**Category:** General Skills  
**Difficulty:** Easy  
**Author:** LT 'syreal' Jones  
**Event:** picoCTF 2026 (CyLab Security Academy)  

---

## Challenge Description
> Can you conjure the right bytes? The program's source code can be downloaded here. Connect to the program with netcat:  
> `$ nc chatelaine.cylabacademy.net 13883`

**Hint:**  
No copy-pasta, please - use Python!

---

## Reconnaissance & Source Code Analysis
Inspecting the provided `app.py` source file reveals how the remote service validates user input:

```python
while(True):
  try:
    print('⊹──────[ BYTEMANCY-1 ]──────⊹')
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print()
    print('Send me ASCII DECIMAL 101 1751 times, side-by-side, no space.')
    print()
    print("☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐")
    print('⊹─────────────⟡─────────────⊹')
    user_input = input('==> ')
    if user_input == "\x65"*1751:
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
1. **Target Byte:** ASCII decimal `101` corresponds to hexadecimal `0x65` (`\x65`), which represents the lowercase character `'e'`.
2. **Repetition Requirement:** The program checks whether `user_input` matches `"\x65" * 1751` (a contiguous string of 1,751 `'e'` characters with no spaces or extra newlines before the end of input).
3. **Automation:** Manually typing or pasting 1,751 characters into an interactive `netcat` session is error-prone and may hit terminal line-buffer limits, so generating the payload programmatically with Python and piping it into `nc` is the cleanest approach.

---

## Solution

### Piping the Generated Payload via Python
Use Python's `-c` flag to print `"\x65" * 1751` (followed by the trailing newline required by `input()`) and pipe standard output directly into the `netcat` connection:

```bash
python -c 'print("\x65"*1751)' | nc chatelaine.cylabacademy.net 13883
```

**Output:**
```text
⊹──────[ BYTEMANCY-1 ]──────⊹
☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐

Send me ASCII DECIMAL 101 1751 times, side-by-side, no space.

☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐☉⟊☽☈⟁⧋⟡☍⟐
⊹─────────────⟡─────────────⊹
==> academy{REDACTED}
```

---

## Flag
```text
academy{REDACTED}
```