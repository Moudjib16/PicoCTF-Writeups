# Log Hunt

* **Category:** General Skills
* **Difficulty:** Easy
* **Author:** Yahaya Meddy
* **Event:** picoMini by CMU-Africa

## 1. Challenge Overview

> *"Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag? Download the logs and figure out the full flag from the fragments."*

**Objective:** Find the flag fragments in `server.log`, remove the repeats, and join the pieces in the right order.

## 2. Step-by-Step Solution

### Step 1: Finding the Fragments

The log is too long to read line by line, so the first step is to search for lines that mention the flag. Every leaked piece is tagged with `FLAGPART`:

```bash
grep "FLAGPART" server.log
```

```text
[1990-08-09 10:00:10] INFO FLAGPART: academy{us3_
[1990-08-09 10:02:55] INFO FLAGPART: y0urlinux_
[1990-08-09 10:05:54] INFO FLAGPART: sk1lls_
[1990-08-09 10:05:55] INFO FLAGPART: sk1lls_
[1990-08-09 10:10:54] INFO FLAGPART: cedfa5fb}
[1990-08-09 10:10:58] INFO FLAGPART: cedfa5fb}
[1990-08-09 10:11:06] INFO FLAGPART: cedfa5fb}
[1990-08-09 11:04:27] INFO FLAGPART: academy{us3_
[1990-08-09 11:04:29] INFO FLAGPART: academy{us3_
[1990-08-09 11:04:37] INFO FLAGPART: academy{us3_
[1990-08-09 11:09:16] INFO FLAGPART: y0urlinux_
[1990-08-09 11:09:19] INFO FLAGPART: y0urlinux_
[1990-08-09 11:12:40] INFO FLAGPART: sk1lls_
[1990-08-09 11:12:45] INFO FLAGPART: sk1lls_
[1990-08-09 11:16:58] INFO FLAGPART: cedfa5fb}
...
```

### Step 2: Understanding the Pattern

* **Key Observation:** Only four distinct fragments exist, and they always appear in the same cycle: the piece starting with `academy{`, then the middle pieces, then the piece ending with `}`. The cycle repeats about once an hour, and each piece may be logged two or three times in a row.

So the flag is the four unique fragments, in the order they first appear.

### Step 3: Rebuilding the Flag in One Command

```bash
grep -oP 'FLAGPART: \K.*' server.log | awk '!seen[$0]++' | tr -d '\n'; echo
```

* `grep -oP 'FLAGPART: \K.*'` prints only the text after `FLAGPART: ` (`\K` drops everything matched before it from the output).
* `awk '!seen[$0]++'` keeps each line the first time it appears and drops later copies, **without changing the order**.
* `tr -d '\n'` joins the pieces into a single line, and `echo` adds a final newline.

```text
academy{REDACTED}
```

## 3. Flag

```text
academy{REDACTED}
```

## 4. Alternative Tools & Methods

### Alternative 1: `uniq` on the First Cycle
`uniq` removes only *adjacent* duplicates, which handles the back-to-back repeats. Taking the first four results gives one full cycle:

```bash
grep "FLAGPART" server.log | awk '{print $NF}' | uniq | head -n 4 | tr -d '\n'; echo
```

### Alternative 2: Read It by Eye
With only a few dozen matching lines, reading the first cycle of the `grep` output and copying the four pieces by hand works too.

### A Trap to Avoid: `sort -u`
`sort -u` removes duplicates, but it also sorts the pieces alphabetically and loses the original order:

```text
academy{us3_
cedfa5fb}
sk1lls_
y0urlinux_
```

Joined together, this is not the flag. The order of the fragments matters, so use a method that keeps it.

## 5. Key Takeaways & Lessons

1. **`grep` first:** In a large log, search for a keyword (`FLAG`, `flag`, `academy{`) before reading anything.
2. **Removing duplicates while keeping order:** `awk '!seen[$0]++'` keeps the first copy of each line in its original position. `uniq` only removes adjacent repeats, and `sort -u` changes the order.
3. **Use the flag format:** The piece starting with `academy{` comes first and the piece ending with `}` comes last, which helps confirm the order.
