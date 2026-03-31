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
# [1, 66.25, 333, 1234.5]

# =============================================================
# [1-2] Delete a slice
# del a[i:j]: removes elements from index i up to (not including) j
# This is equivalent to a[i:j] = [] but more explicit and readable
# =============================================================

del a[1:3]
print("[1-2] after del a[1:3] :", a)
# [1, 1234.5]

# =============================================================
# [1-3] Clear the entire list with del a[:]
# del a[:]: removes ALL elements from the list (in-place)
#
# Equivalent to a.clear(), but del a[:] also works on slices of other sequences
# =============================================================
b = [1, 2, 3, 4, 5]
print("[2-3] before del b[:] :", b)
del b[:]
print("[2-3] after  del b[:] :", b)
# []

# =============================================================
# [1-4] Delete the variable itself
# del a: removes the variable binding; accessing 'a' afterwards raises NameError
#
# Pitfall: del a is NOT the same as a = []
#   del a   → the name 'a' no longer exists in the namespace
#   a = []  → 'a' still exists, but now points to an empty list
# =============================================================

c = [10, 20, 30]
print("[2-4] before del c :", c)
del c
try:
    print(c)
except NameError as err:
    print("[2-4] NameError after del c :", err)
# NameError: name 'c' is not defined

# =============================================================
# [2-1] Delete a key from a dictionary
# del d[key]: removes the key-value pair from the dict; raises KeyError if not found
#
# In FastAPI/backend work, this pattern appears when cleaning up response dicts
# before returning to the client (though Pydantic models are usually preferred).
# =============================================================

user = {"id": 1, "name": "Alice", "password": "secret123"}
print("[3-1] before del :", user)


del user["password"]
print("[3-1] after del user['password'] :", user)
# {"id": 1, "name": "Alice"}

# KeyError example — catch so the script doesn't crash
try:
    del user["email"]
except KeyError as err:
    print("[3-1] KeyError after del :", err)

# =============================================================
# [2-2] Delete with a step slice (extended slicing)
# del a[::step]: removes every nth element from the list
# =============================================================

d = list(range(10))
print("[3-2] original :", d)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

del d[::2]
print("[3-2] after del d[::2] :", d)
# [1, 3, 5, 7, 9]
