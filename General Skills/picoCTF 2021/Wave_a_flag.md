# Wave a flag

- **Platform:** CyLab Security Academy / picoCTF
- **Event:** picoCTF 2021
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** syreal

---

## 1. Challenge Overview

The challenge provides a Linux binary named `warm` and asks if you can invoke help flags for a tool or binary.

**Objective:** Make the `warm` binary executable on Linux and pass its help flag (`-h`) to retrieve the flag.

---

## 2. Reconnaissance & Initial Analysis

### Files Provided
- **Provided Artifact:** `warm` (64-bit x86-64 ELF executable)

### Initial Observations
- Running `./warm` immediately after downloading fails with `zsh: permission denied: ./warm` because files downloaded over HTTP do not have execute permissions set.
- `file warm` confirms it is a standard `ELF 64-bit LSB pie executable, x86-64` for GNU/Linux.

---

## 3. Step-by-Step Walkthrough

### Step 1: Grant Execute Permissions

Add execute permissions to the binary using `chmod`:

```bash
chmod +x warm
```

### Step 2: Run the Binary

Execute the binary without arguments to see its default prompt:

```bash
./warm
```

Output:

```text
Hello user! Pass me a -h to learn what I can do!
```

### Step 3: Invoke the Help Flag

Run the binary with the `-h` flag as instructed:

```bash
./warm -h
```

Output:

```text
Oh, help? I actually don't do much, but I do have this flag here: academy{REDACTED}
```

---

## 4. Flag

```text
academy{REDACTED}
```