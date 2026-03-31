# ch05_1_3_tuples_and_sequences.py
# Chapter 5.3: Tuples and Sequences
# Ref: https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

# =============================================================
# [1-1] Creating tuples
# A tuple consists of values separated by commas.
# Unlike lists, tuples are immutable — you cannot change elements after creation.
# =============================================================

t = 12345, 54321, "hello!"
print("[1-1] tuple t:", t)  # (12345, 54321, 'hello!')
print("[1-1] t[0]:", t[0])  # 12345
print("[1-1] type(t):", type(t))  # <class 'tuple'>

# Tuples can be nested
u = t, (1, 2, 3, 4, 4)
print("[1-1] nested tuple u:", u)
# ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))

# =============================================================
# [1-2] Tuples are immutable — mutation raises TypeError
# Pitfall: beginners often confuse tuple immutability with deep immutability.
# =============================================================

try:
    t[0] = 88888
except TypeError as err:
    print("[1-2] TypeError (expected):", err)
    # 'tuple' object does not support item assignment

# Tuples CAN contain mutable objects — the container is immutable, not the contents
mutable_in_tuple = ([1, 2], [3, 4])
mutable_in_tuple = ([1, 2], [3, 4])
mutable_in_tuple[0].append(99)  # This works! The list inside is still mutable
print("[1-2] mutable inside tuple:", mutable_in_tuple)
# ([1, 2, 99], [3, 4])

# =============================================================
# [2-1] Empty tuple and single-element tuple
# Empty tuple: use ()
# Single-element tuple: MUST have a trailing comma  ← common pitfall!
# =============================================================

empty = ()
print("[2-1] empty tuple:", empty, "| len:", len(empty))  # () | 0

single = ("hello",)  # trailing comma is required — without it, it's just a string
not_a_tuple = "hello"

print("[2-1] single-element tuple:", single, "| type:", type(single))
# ('hello',) | <class 'tuple'>

# =============================================================
# [2-2] Sequence types: tuple, list, range — shared operations
# All sequence types support: indexing, slicing, len(), in, +, *
# =============================================================

seq_tuple = (10, 20, 30, 40, 50)
seq_list = [10, 20, 30, 40, 50]

print("[2-2] tuple slice [1:3]:", seq_tuple[1:3])  # (20, 30)
print("[2-2] tuple slice [1:3]:", seq_list[1:3])  # [20, 30]
print("[2-2] 30 in tuple:", 30 in seq_tuple)  # True
print("[2-2] tuple + tuple:", seq_tuple + (60, 70))  # (10, 20, 30, 40, 50, 60, 70)

# =============================================================
# [3-1] Tuple packing — values are "packed" into a tuple automatically
# タプルパッキング：値が自動的にタプルにまとめられる
# =============================================================

packed = 1, 2, 3
print("[3-1] packed:", packed, "| type:", type(packed))

# =============================================================
# [3-2] Sequence unpacking — the reverse of packing
# The number of variables on the left must match the number of elements.
# =============================================================

point = (10, 20, 30)
x, y, z = point
print("[3-2] unpacked:", x, y, z)

# Works with any sequence type (list, string, range)
a, b, c = [100, 200, 300]
print("[3-2] list unpack:", a, b, c)

first, *rest = [1, 2, 3, 4, 5]
print("[3-2] starred unpack — first:", first, "| rest:", rest)
# 1 | [2, 3, 4, 5]

# ValueError when counts don't match
try:
    p, q = (1, 2, 3)
except ValueError as err:
    print("[3-2] ValueError (expected):", err)
    # too many values to unpack (expected 2, got 3)

# =============================================================
# [3-3] Practical pattern: swap variables without a temp variable
# This is idiomatic Python; interviewers love to see this.
# =============================================================

a, b = 10, 20
print("[3-3] before swap: a =", a, "| b =", b)
a, b = b, a
print("[3-3] after swap : a =", a, "| b =", b)

# =============================================================
# [3-4] Tuple unpacking in loops — common in real backend code
# =============================================================

pairs = [(1, "apple"), (2, "banana"), (3, "cherry")]
for idx, fruit in pairs:
    print(f"[3-4] {idx}: {fruit}")
