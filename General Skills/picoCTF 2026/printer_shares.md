# Printer Shares

* **Category:** General Skills
* **Difficulty:** Easy
* **Author:** Janice He
* **Event:** picoCTF 2026

## 1. Challenge Overview

> *"Oops! Someone accidentally sent an important file to a network printer—can you retrieve it from the print server? The printer is on 17398."*
> *"you can try `$ nc -vz chatelaine.cylabacademy.net 17398`"*

**Hints:**
1. *Knowing how SMB protocol works would be helpful!*
2. *`smbclient` and `smbutil` are good tools*

We are given a target hostname (`chatelaine.cylabacademy.net`) and a non-standard port (`17398`) running an SMB (Server Message Block) service simulating a network print/file server.

## 2. Step-by-Step Solution

### Step 1: Verifying Connectivity
First, we check that the target server and custom port are reachable using Netcat (`nc`):

```bash
nc -vz chatelaine.cylabacademy.net 17398
# Output: Connection to chatelaine.cylabacademy.net (18.190.79.158) 17398 port [tcp/*] succeeded!
```

* **Why this works:** `-v` enables verbose output and `-z` performs a zero-I/O port scan, confirming the TCP handshake succeeds without hanging on an interactive prompt.

### Step 2: Enumerating SMB Shares
Knowing from the hints that the service speaks SMB, we use `smbclient` to list available network shares on the custom port (`-p 17398`):

```bash
smbclient -L 18.190.79.158 -p 17398
```

When prompted for a password (`Password for [WORKGROUP\athena]:`), pressing **Enter** (blank password) initiates an anonymous/guest session and reveals the available shares:

```text
        Sharename       Type      Comment
        ---------       ----      -------
        shares          Disk      Public Share With Guests
        IPC$            IPC       IPC Service (Samba 4.19.5-Ubuntu)
```

* **Key Observation:** The `shares` disk share explicitly notes `"Public Share With Guests"`, meaning no valid user credentials are required to browse or download files.

### Step 3: Connecting to the Share & Retrieving the Flag
We connect directly to `//18.190.79.158/shares` on port `17398` using `-N` (no password prompt):

```bash
smbclient //18.190.79.158/shares -p 17398 -N
```

Inside the interactive `smb: \>` prompt, listing the directory contents with `ls` reveals two files:

```text
smb: \> ls
  .                                   D        0  Wed Sep 23 08:02:25 2026
  ..                                  D        0  Wed Sep 23 08:02:25 2026
  dummy.txt                           N     1142  Wed Sep 23 01:59:21 2026
  flag.txt                            N       37  Wed Sep 23 08:02:25 2026
```

#### Troubleshooting `smbclient` Interactive Commands
* **`cat flag.txt` / `cta dummy.txt`:** Fails with `command not found` because `smbclient` uses an FTP-like command set rather than a full POSIX shell.
* **`print flag.txt`:** Fails with `NT_STATUS_ACCESS_DENIED` because the `print` command attempts to submit a print job to a printer queue, whereas `shares` is configured as a read-only `Disk` share.
* **`get flag.txt`:** Downloads the remote file to our local working directory cleanly:

```text
smb: \> get flag.txt
getting file \flag.txt of size 37 as flag.txt (0.0 KiloBytes/sec) (average 0.0 KiloBytes/sec)
smb: \> get dummy.txt
getting file \dummy.txt of size 1142 as dummy.txt (0.1 KiloBytes/sec) (average 0.1 KiloBytes/sec)
smb: \> exit
```

### Step 4: Reading the Flag Locally
Once downloaded to our local machine, we read `flag.txt`:

```bash
cat flag.txt
# Output: academy{REDACTED}
```

*(Note: `dummy.txt` simply contains standard "Lorem Ipsum / Far far away" placeholder text as a decoy.)*

## 3. Flag

```text
academy{REDACTED}
```

## 4. Alternative Tools & Methods

### Alternative 1: Viewing Files Without Downloading (`more` or `!`)
Inside `smbclient`, you can read small text files directly without saving them permanently:
* Use the built-in `more` command:
  ```text
  smb: \> more flag.txt
  ```
* Or execute local shell commands via `!` after downloading:
  ```text
  smb: \> get flag.txt
  smb: \> !cat flag.txt
  ```

### Alternative 2: One-Liner Non-Interactive Download
You can pass commands directly to `smbclient` using `-c` to download `flag.txt` in a single command:

```bash
smbclient //chatelaine.cylabacademy.net/shares -p 17398 -N -c "get flag.txt" && cat flag.txt
```

## 5. Key Takeaways & Security Lessons

1. **Disable Anonymous/Guest SMB Access:** Allowing unauthenticated guest access (`Public Share With Guests`) on Samba or Windows file/print servers exposes sensitive documents to anyone who can reach the port.
2. **Security Through Obscurity Is Not Enough:** Running SMB on a non-standard port (`17398` instead of `445`) does not protect an unauthenticated share once discovered via service enumeration.
3. **Interactive Protocol Shells:** Tools like `smbclient` and `ftp` use protocol-specific commands (`get`, `put`, `mget`, `more`) rather than standard bash utilities (`cat`). Running `help` inside unfamiliar CLI clients quickly reveals supported actions.