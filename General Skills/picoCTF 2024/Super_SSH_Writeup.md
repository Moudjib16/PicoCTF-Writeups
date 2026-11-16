# Super SSH

- **Platform:** picoCTF
- **Event:** picoCTF 2024
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** Jeffery John

---

## 1. Challenge Overview

The challenge provides SSH connection details and a password.

**Objective:** Connect to `xebec.cylabacademy.net` as `ctf-player` on port `27873` and retrieve the flag.

---

## 2. Reconnaissance & Initial Analysis

### Connection Details
- **Host:** `xebec.cylabacademy.net`
- **Port:** `27873`
- **Username:** `ctf-player`
- **Password:** `fa1a82ad`

### Initial Observations
- The challenge requires an SSH connection.
- The server uses a non-default port (`27873`), so it must be specified with `-p`.
- The password is provided in the challenge description.

---

## 3. Step-by-Step Walkthrough

### Step 1: Connect to the server

Run:

```bash
ssh ctf-player@xebec.cylabacademy.net -p 27873
```

### Step 2: Accept the server fingerprint

On the first connection, SSH may ask whether to trust the server's host key.

Enter:

```text
yes
```

### Step 3: Enter the password

When prompted, enter:

```text
fa1a82ad
```

The password will not appear on the screen while typing. This is normal for SSH.

### Step 4: Read the flag

After successfully logging in, the remote shell opens and it will automaticlly display the flag

---

## 4. Flag

```text
academy{REDACTED}
```
