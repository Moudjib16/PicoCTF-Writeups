# what's a net cat?

- **Platform:** picoCTF
- **Event:** picoCTF 2019
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** Sanjay C / Danny Tunitis

---

## 1. Challenge Overview

The challenge requires connecting to a remote service using Netcat.

**Objective:** Connect to `xebec.cylabacademy.net` on port `24109` and retrieve the flag.

---

## 2. Reconnaissance & Initial Analysis

### Connection Details
- **Host:** `xebec.cylabacademy.net`
- **Port:** `24109`
- **Tool:** `nc` (Netcat)

### Initial Observations
- The challenge provides a hostname and port.
- Netcat can establish a TCP connection to the remote service.
- No username or password is required.

---

## 3. Step-by-Step Walkthrough

### Step 1: Connect to the service

Run:

```bash
nc xebec.cylabacademy.net 24109
```

### Step 2: Read the response

The server returns:

```text
You're on your way to becoming the net cat master
academy{REDACTED}
```

The flag is included directly in the server's response.

---

## 4. Flag

```text
academy{REDACTED}
```
