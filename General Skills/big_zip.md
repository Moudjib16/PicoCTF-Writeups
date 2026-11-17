# Big Zip

* **Platform:** CyLab Security Academy / picoCTF

* **Category:** General Skills

* **Difficulty:** Easy

* **Author:** LT 'syreal' Jones

## 1. Challenge Overview

The challenge provides a ZIP archive (`big-zip-files.zip`) containing numerous nested directories and text files, and asks you to unzip it and find the flag.

**Objective:** Extract `big-zip-files.zip` and recursively search through all extracted directories and files using `grep` to locate the flag.

## 2. Reconnaissance & Initial Analysis

### Files Provided

* **Provided Artifact:** `big-zip-files.zip`

### Initial Observations

* Extracting `big-zip-files.zip` creates a `big-zip-files` directory packed with many subfolders and text files, making manual inspection impractical.

* Running `grep` directly on a directory without recursive flags fails with `grep: big-zip-files: Is a directory`. Passing `-r` (recursive) instructs `grep` to search every file across all subdirectories.

## 3. Step-by-Step Walkthrough

### Step 1: Extract the Archive

Unzip `big-zip-files.zip`:

```
unzip big-zip-files.zip

```

### Step 2: Recursively Search for the Flag

Run `grep` with `-rn` (recursive search with line numbers) across the `big-zip-files` directory for the `academy` flag prefix:

```
grep -rn "academy" big-zip-files

```

Output:

```
big-zip-files/folder_pmbymkjcya/folder_cawigcwvgv/folder_ltdayfmktr/folder_fnpfclfyee/whzxrpivpqld.txt:1:information on the record will last a billion years. Genes and brains and books encode academy{REDACTED}

```

## 4. Flag

```
academy{REDACTED}

```