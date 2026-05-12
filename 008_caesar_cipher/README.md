# Day 8: 🕵️ Caesar Cipher

## Overview

An encoder/decoder that shifts letters while preserving spaces and punctuation.

This project is part of my **100 Days of Code: Python Bootcamp** progress.

---

## Concepts practiced

- functions with parameters
- return values
- lists
- modulo arithmetic
- while loops
- string building

---

## Files

| File | Purpose |
|---|---|
| `main.py` | The final Caesar Cipher app. |
| `art.py` | The console logo. |
| `section_code.py` | Function parameter practice snippets. |

---

## How to run

From this folder:

```bash
python main.py
```

Or from the repo root:

```bash
cd 008_caesar_cipher
python main.py
```

---

## Example run

```text
Type 'encode' to encrypt, type 'decode' to decrypt: encode
Type your message: hello world
Type the shift number: 5
Here is your 'encoded' message: mjqqt btwqi
```

---

## What I learned

- How modulo wraps letters from z back to a.
- How one function can handle both encode and decode.
- How to keep non-letter characters unchanged.

---

## Future improvements

- Validate direction input.
- Handle uppercase while preserving original casing.
- Use `string.ascii_lowercase` instead of a manual alphabet list.

---

[⬅ Back to main repo](../README.md)
