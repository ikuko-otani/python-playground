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
