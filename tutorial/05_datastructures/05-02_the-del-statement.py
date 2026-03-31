# Chapter 5.2: The del Statement
# Ref: https://docs.python.org/3/tutorial/datastructures.html#the-del-statement

# =============================================================
# [1-1] Delete a single element by index
# del a[i]: removes the element at index i from the list (in-place)
#
# Difference from pop():
#   pop(i) → removes AND returns the value (useful when you need the value)
#   del a[i] → removes WITHOUT returning anything (use when you don't need the value)
# =============================================================

a = [-1, 1, 66.25, 333, 1234.5]
print("[1-1] original :", a)

del a[0]
print("[1-1] after del a[0] :", a)

# =============================================================
# [1-2] Delete a slice
# del a[i:j]: removes elements from index i up to (not including) j
# This is equivalent to a[i:j] = [] but more explicit and readable
# =============================================================

del a[1:3]
print("[1-2] after del a[1:3] :", a)
