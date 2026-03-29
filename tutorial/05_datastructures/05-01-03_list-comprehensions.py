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
