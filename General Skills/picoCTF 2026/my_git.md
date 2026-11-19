# MY GIT

**Category:** General Skills  
**Difficulty:** Easy  
**Author:** Darkraicg492  
**Event:** picoCTF 2026 (CyLab Security Academy)  

---

## Challenge Description
> I have built my own Git server with my own rules! You can clone the challenge repo using the command below.  
> `git clone ssh://git@chatelaine.cylabacademy.net:44743/git/challenge.git`  
> Here's the password: `f64d4005`  
> Check the README to get your flag!

---

## Reconnaissance & Analysis
Cloning the repository over SSH using the provided credentials and inspecting `README.md` reveals a custom server-side hook restriction:

```bash
git clone ssh://git@chatelaine.cylabacademy.net:44743/git/challenge.git
cd challenge
cat README.md
```

**`README.md` contents:**
```markdown
# MyGit

### If you want the flag, make sure to push the flag!

Only flag.txt pushed by `root:root@academy` will be updated with the flag.

GOOD LUCK!
```

Because Git stores commit metadata (`user.name` and `user.email`) purely from local client configuration without cryptographic verification by default, a server hook checking the commit author's name and email can be bypassed by spoofing the local repository's Git identity.

---

## Step-by-Step Solution

### 1. Impersonate the `root` Author Identity
Configure the local repository's Git username and email to match `root:root@academy`:

```bash
git config user.name "root"
git config user.email "root@academy"
```

### 2. Create and Stage `flag.txt`
Create `flag.txt` in the working directory and stage it for commit:

```bash
echo > flag.txt
git add flag.txt
```

### 3. Commit and Push to Trigger the Remote Hook
Commit the new file under the spoofed `root` author identity and push to `master`:

```bash
git commit -m "added flag"
git push
```

Upon pushing with the password `f64d4005`, the remote hook validates the author metadata and prints the flag directly in the remote output:

```text
remote: Author matched and flag.txt found in commit...
remote: Congratulations! You have successfully impersonated the root user
remote: Here's your flag: academy{REDACTED}
```

---

## Key Takeaway
Git commit author fields (`user.name` and `user.email`) are arbitrary strings set by the client and cannot be trusted for authentication or authorization. Enforcing commit authorship requires cryptographic verification such as GPG or SSH commit signing (`git commit -S`).

---

## Flag
```text
academy{REDACTED}
```