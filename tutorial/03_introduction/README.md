## 3.1.1 Numbers

- `//` is floor division, and `%` gives the remainder.
- `len` is frequently used later to get the length of a list.
- Assignment operators can be used.

## 3.1.2 Strings

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

## 3.1.3 Lists

- Indexing and slicing are the same idea as strings: use `lst[i]`, `lst[-1]`, `lst[a:b]`, `lst[a:b:c]` to access ranges efficiently.
- Use `len`, `sum`, `max`, `min` on lists to quickly compute aggregates, a common pattern in array problems.
- Modify lists in place with `append`, `+=`, and slice assignment (`lst[a:b] = [...]`) to insert, replace, or delete ranges without extra lists.
- Be careful with references: `b = a` shares the **same** list, while `b = a[:]` makes a shallow copy; this matters for side effects in helper functions.
- Work comfortably with nested lists (matrices), using `lst[i][j]` access and nested loops for 2D problems.

## 3.2 First steps towards programming

- Practiced the Fibonacci sequence with a while loop and multiple assignment.
- Observed how truthiness works for numbers and sequences in while conditions.
- Experimented with the print function, especially the `end` keyword argument.
