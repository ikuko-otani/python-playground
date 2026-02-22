# Chapter 3 Notes
## 01 Numbers
- `//` is floor division, and `%` gives the remainder.
- `len` is frequently used later to get the length of a list.
- Assignment operators can be used.

## 02 Strings
###  String Basics
- Strings are sequences of characters, created with single (`'`), double (`"`) or triple quotes (`'''` / `"""`).
- Triple quotes allow multi-line strings and include both quote types without escaping.

### Escape Sequences
- Use backslash `\` for special characters:  
  - `\n` newline, `\t` tab, `\\` backslash, `\'` single quote, `\"` double quote, `\r` carriage return, `\v` vertical tab, `\f` form feed, `\b` backspace, `\a` bell, `\0` null, `\uXXXX` Unicode (e.g., `\u03A9` for Ω).
- Raw strings (`r"..."`) ignore escape sequences.

### String Operations
- Concatenation: `"Hello" + " " + "World"`.
- Multiplication: `"Ha" * 3` → `"HaHaHa"`.
- Adjacent string literals are automatically concatenated.
- Use **f-strings** (`f"Value: {variable}"`) for fast, readable formatting.

### String Indexing and Slicing
- Indexing starts at 0.  
  Example: `"Python"[0]` → `'P'`, `"Python"[-1]` → `'n'`.
- Slicing: `"Python"[1:4]` → `'yth'`.  
- Omitting indices:  
  - `[:3]` → first three chars.  
  - `[3:]` → from index 3 onward.  
  - `[::-1]` → reversed string.
- Step slicing: `"Python"[::2]` → `'Pto'` (every second character).

### String Methods
- Split and Join: `.split()`, `' '.join(list)`.
- Replace: `.replace(old, new)`.
- Search: `.find(substring)` returns index or `-1` if not found.

### Iterating Over Strings
- `for char in "Hello":` — iterates over characters.

