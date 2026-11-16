# Tab, Tab, Attack

- **Platform:** CyLab Security Academy / picoCTF
- **Event:** picoCTF 2021
- **Category:** General Skills
- **Difficulty:** Easy
- **Author:** syreal

---

## 1. Challenge Overview

The challenge provides a ZIP archive (`Addadshashanammu.zip`) containing deeply nested directories and long filenames, highlighting how terminal tab completion speeds up navigation.

**Objective:** Extract `Addadshashanammu.zip`, navigate through the nested directory structure using tab completion, and execute the compiled binary inside to retrieve the flag.

---

## 2. Reconnaissance & Initial Analysis

### Files Provided
- **Provided Artifact:** `Addadshashanammu.zip`

### Initial Observations
- Extracting the archive reveals a multi-level nested directory hierarchy (`Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku`).
- Inside the deepest directory are a C source file (`fang-of-haynekhtnamet.c`) and its pre-compiled Linux executable (`fang-of-haynekhtnamet`).

---

## 3. Step-by-Step Walkthrough

### Step 1: Extract the Archive

Unzip `Addadshashanammu.zip`:

```bash
unzip Addadshashanammu.zip
```

### Step 2: Navigate Using Tab Completion

Use `cd` with `Tab` auto-completion to traverse the nested folders down to `Ularradallaku`:

```bash
cd Addadshashanammu/Almurbalarammi/Ashalmimilkala/Assurnabitashpi/Maelkashishi/Onnissiralis/Ularradallaku
```

### Step 3: Execute the Binary

List the files and run the `fang-of-haynekhtnamet` executable:

```bash
./fang-of-haynekhtnamet
```

Output:

```text
*ZAP!* academy{REDACTED}
```

---

## 4. Flag

```text
academy{REDACTED}
```