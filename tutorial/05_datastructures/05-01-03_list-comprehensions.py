# Chapter 5.1.3: List Comprehensions
# Ref: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

# =============================================================
# [1-1] Basic structure: for-loop vs list comprehension
# List comprehension syntax: [expression for item in iterable]
# Tutorial's first example: build a list of squares
# =============================================================

# --- Approach 1: traditional for-loop with append ---
squares_loop = []
for x in range(10):
    squares_loop.append(x**2)
print("[1-1] for-loop    :", squares_loop)

# --- Approach 2: map() with lambda ---
squares_map = list(map(lambda x: x**2, range(10)))
print("[1-1] map+lambda  :", squares_map)

# --- Approach 3: list comprehension (most Pythonic) ---
squares_lc = [x**2 for x in range(10)]
print("[1-1] list comp   :", squares_lc)

# All three produce identical results
print("[1-1] all equal?  :", squares_loop == squares_map == squares_lc)

# =============================================================
# [1-2] Expression can be any valid Python expression
# =============================================================

# Absolute values
absolute = [abs(x) for x in range(-5, 6)]
print("[1-2] abs values  :", absolute)

# String methods
words = ["hello", "WORLD", "Python"]
lowered = [w.lower() for w in words]
print("[1-2] lowered     :", lowered)

# =============================================================
# [2-1] Filtering with a condition: [expr for item in iter if condition]
#
# Structure: the 'if' clause acts as a filter — only items satisfying
#            the condition are included in the output list
# =============================================================

# Tutorial example: squares of non-multiples of 3
vec = [-4, -2, 0, 2, 4]

# Filter: keep only non-negative values
non_negative = [x for x in vec if x >= 0]
print("[2-1] non-negative:", non_negative)

# Apply both filter and transformation in one expression
doubled_positive = [x * 2 for x in vec if x > 0]
print("[2-1] doubled pos :", doubled_positive)

# =============================================================
# [2-2] Tutorial example: combining filter + function call
# =============================================================

# Apply abs(), then keep all results
abs_values = [abs(x) for x in vec]
print("[2-2] abs of vec  :", abs_values)

# Combine: filter negatives, then take absolute value
abs_negatives = [abs(x) for x in vec if x < 0]
print("[2-2] abs of neg  :", abs_negatives)

# =============================================================
# [2-3] PITFALL: 'if' position matters — filter vs ternary
#
# [expr if cond else alt  for x in iter]  <- ternary: ALL items included
# [expr                   for x in iter if cond]  <- filter: items removed
# =============================================================

nums = range(10)

# Filter: only even numbers (some items are REMOVED)
evens_filter = [x for x in nums if x % 2 == 0]
print("[2-3] filter evens:", evens_filter)

# Ternary: ALL items kept, but odd ones are replaced with 0
evens_ternary = [x if x % 2 == 0 else 0 for x in nums]
print("[2-3] ternary evens:", evens_ternary)

# =============================================================
# [3-1] Multiple 'for' clauses: Cartesian product
#
# Tutorial example: combine elements from two lists
# Note: the order of 'for' clauses matches the order in a nested for-loop
# =============================================================

# Equivalent nested for-loop:
# result = []
# for x in [1, 2, 3]:
#     for y in [3, 1, 4]:
#         if x != y:
#             result.append((x, y))
combs = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print("[3-1] combinations:", combs)
# [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# =============================================================
# [3-2] Tutorial example: flatten a matrix (list of lists)
# This pattern appears often in backend data transformation
# =============================================================
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Flatten: iterate over rows, then over each element in the row
flat = [num for row in matrix for num in row]
print("[3-2] flat matrix :", flat)
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# =============================================================
# [3-3] The subexpression can reference variables from earlier 'for' clauses
# =============================================================

# Pairs where second element is double the first
pairs = [(x, x * 2) for x in range(1, 6)]
print("[3-3] doubled pairs:", pairs)
# [(1, 2), (2, 4), (3, 6), (4, 8), (5, 10)]

# =============================================================
# [4-1] Calling functions and methods in a list comprehension
# Any callable can appear in the expression or the condition
# =============================================================


# Apply a user-defined function
def celsius_to_fahrenheit(c: float) -> float:
    # Convert Celsius temperature to Fahrenheit
    return c * 9 / 5 + 32


temps_c = [0, 20, 37, 100]
temps_f = [celsius_to_fahrenheit(c) for c in temps_c]
print("[4-1] temps_f     :", temps_f)

# =============================================================
# [4-2] List comprehension as an argument to another function
# Common in production: pass directly to sum(), max(), join(), etc.
# =============================================================

total = sum(x**2 for x in range(10))  # generator expression inside sum()
print("[4-2] sum of squares:", total)  # 285

joined = ", ".join(w.upper() for w in ["hello", "world"])
print("[4-2] joined        :", joined)

# =============================================================
# [4-3] Nested list comprehension — transpose a matrix
#
# Tutorial example: transpose rows and columns
# Equivalent to: [[row[i] for row in matrix] for i in range(3)]
# =============================================================

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# Transpose using nested list comprehension
transposed = [[row[i] for row in matrix] for i in range(4)]
print("[4-3] transposed  :")
for row in transposed:
    print("  ", row)
# [1, 5, 9]
# [2, 6, 10]
# [3, 7, 11]
# [4, 8, 12]

# Note: in production, prefer zip(*matrix) for transposing
transposed_zip = list(zip(*matrix))
print("[4-3] zip transpose:", transposed_zip)
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)]
