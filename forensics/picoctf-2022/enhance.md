# Enhance!

- **Platform:** picoCTF
- **Event:** picoCTF 2022
- **Category:** Forensics
- **Difficulty:** Medium
- **Author:** LT 'syreal' Jones

## 1. Challenge Overview

The challenge provides an image file (`drawing.flag.svg`) and asks you to find the hidden flag inside it.

**Objective:** Inspect the SVG image file—either by examining its underlying XML source code or zooming into its vector elements—to recover the split flag text and combine it.

## 2. Reconnaissance & Initial Analysis

### Files Provided

* **Provided Artifact:** `drawing.flag.svg` (Scalable Vector Graphics image)

### Initial Observations

* Unlike raster images (such as PNG or JPEG), `.svg` files are plain-text XML documents that define shapes, paths, and `<text>` elements mathematically.

* Because SVG graphics scale infinitely without losing quality, microscopic text (`font-size:0.00352781px`) hidden inside the drawing can be read either by zooming in with a vector editor or by reading the raw XML tags directly.

* Inside the `<tspan>` tags, the flag characters are split across multiple lines with spaces between them, requiring the pieces to be joined together.

## 3. Step-by-Step Walkthrough

### Method 1: Inspect XML Source in VS Code

Open `drawing.flag.svg` in Visual Studio Code (`code drawing.flag.svg`). Searching (`Ctrl+F`) for `<tspan` or the flag characters reveals the `<text>` block containing the split pieces of the flag, which can be concatenated together.

### Method 2: Filter XML Tags with `grep`

Use `grep` in the terminal to search for flag patterns and XML tags in `drawing.flag.svg`:

```bash
grep -iE "academy\{|picoCTF\{|flag\{|CTF\{|base64|<" drawing.flag.svg
```

Output snippet:

```xml
    <text
       id="text3723"><tspan
         id="tspan3748">a </tspan><tspan
         id="tspan3754">c </tspan><tspan
         id="tspan3756">a </tspan><tspan
         id="tspan3758">d </tspan><tspan
         id="tspan3760">e </tspan><tspan
         id="tspan3762">m </tspan><tspan
         id="tspan3764">y { 3 n h 4 n </tspan><tspan
         id="tspan3752">c 3 d _ R E D A C T E D }</tspan></text>
```

### Method 3: Extract Printable Content with `strings`

Run `strings` on the SVG file to dump all readable text and inspect the `<tspan>` elements at the bottom:

```bash
strings drawing.flag.svg
```

### Method 4: Zoom In with Inkscape

Open `drawing.flag.svg` in **Inkscape** and zoom all the way into the center of the drawing (`+` key) until the `0.00352781px` text elements become readable on the canvas.

## 4. Flag

```text
academy{REDACTED}
```