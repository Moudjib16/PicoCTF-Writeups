# Piece by Piece

* **Category:** General Skills
* **Difficulty:** Easy
* **Author:** Yahaya Meddy
* **Event:** picoCTF 2026

## 1. Challenge Overview

> *"After logging in, you will find multiple file parts in your home directory. These parts need to be combined and extracted to reveal the flag."*
> *`ssh -p 21689 ctf-player@chatelaine.cylabacademy.net`*

**Objective:** Log in over SSH, join the split file parts back into one ZIP archive, extract it with the password given in the instructions, and read the flag.

## 2. Step-by-Step Solution

### Step 1: Logging In & Looking Around

```bash
ssh -p 21689 ctf-player@chatelaine.cylabacademy.net
```

```text
ctf-player@academy-chall$ ls
instructions.txt  part_aa  part_ab  part_ac  part_ad  part_ae
```

There are five files named `part_aa` to `part_ae`. This naming is the default output of the `split` command, so they are chunks of one larger file.

### Step 2: Reading the Instructions

```text
ctf-player@academy-chall$ cat instructions.txt
Hint:

- The flag is split into multiple parts as a zipped file.
- Use Linux commands to combine the parts into one file.
- The zip file is password protected. Use this "supersecret" password to extract the zip file.
- After unzipping, check the extracted text file for the flag.
```

* **Key Observation:** The parts must be joined into a ZIP, and the password is `supersecret`.

### Step 3: A Failed Attempt on a Single Part

Running `unzip` on the first part alone fails:

```text
ctf-player@academy-chall$ unzip part_aa
  End-of-central-directory signature not found.  Either this file is not
  a zipfile, or it constitutes one disk of a multi-part archive.
```

`unzip` looks for the *end-of-central-directory* record at the end of the file, and that record is only in the last chunk. A single part is just a slice of the archive, so it can't be opened alone.

### Step 4: Combining the Parts

`cat` with a glob joins the files in alphabetical order (`aa`, `ab`, `ac`, `ad`, `ae`), which is the order `split` created them:

```bash
cat part_* > flag.zip
```

### Step 5: Extracting the Archive

```text
ctf-player@academy-chall$ unzip flag.zip
Archive:  flag.zip
[flag.zip] flag.txt password: supersecret
 extracting: flag.txt
```

```text
ctf-player@academy-chall$ cat flag.txt
academy{REDACTED}
```

## 3. Flag

```text
academy{REDACTED}
```

## 4. Alternative Tools & Methods

### Alternative 1: Explicit Part Order
If the glob order could be wrong, list the files by name:

```bash
cat part_aa part_ab part_ac part_ad part_ae > flag.zip
```

### Alternative 2: Pass the Password on the Command Line
```bash
unzip -P supersecret flag.zip
```

### Alternative 3: Verify the Archive First
```bash
file flag.zip        # should say: Zip archive data
unzip -l flag.zip    # lists contents without extracting
```

## 5. Key Takeaways & Lessons

1. **`split` and `cat` are inverses:** `split` cuts a file into `xaa`, `xab`, ... chunks (here with the prefix `part_`), and `cat part_*` puts them back together. The shell sorts glob matches alphabetically, which matches the order `split` used.
2. **Check the file type:** A "file part" is not a valid file on its own. Only the joined file is a real ZIP, which is why `unzip part_aa` failed.
3. **Read the instructions:** The password was given in `instructions.txt`, so no cracking was needed.
