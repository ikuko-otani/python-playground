# Chapter 5.5: Dictionaries
# Ref: https://docs.python.org/3/tutorial/datastructures.html#dictionaries


# ============================================================
# Block 1: Creating dictionaries and basic operations
# ============================================================

# Create a dictionary with initial key-value pairs
tel: dict[str, int] = {"jack": 4098, "sape": 4139}

# Add a new key-value pair
tel["guido"] = 4127

# Access a value by key (raises KeyError if not found)
value = tel["jack"]

# Delete a key-value pair with del
del tel["sape"]

print(tel)  # {'jack': 4098, 'guido': 4127}
print(value)  # 4098


# ============================================================
# Block 2: Safe access with get(), key existence check with in
# ============================================================

# Use get() to avoid KeyError — returns None or a default value
result_none = tel.get("irv")  # key does not exist -> None
result_default = tel.get("irv", 0)  # key does not exist -> 0

# Check if a key exists using the in keyword
is_guido_in = "guido" in tel
is_jack_out = "jack" not in tel

print(result_none)  # None
print(result_default)  # 0
print(is_guido_in)  # True
print(is_jack_out)  # False


# ============================================================
# Block 3: Listing keys with list() and sorted()
# ============================================================

# list(d) returns keys in insertion order
keys_list = list(tel)

# sorted(d) returns keys in sorted order
keys_sorted = sorted(tel)

print(keys_list)  # ['jack', 'guido']
print(keys_sorted)  # ['guido', 'jack']


# ============================================================
# Block 4: Building dictionaries with dict() constructor
# ============================================================

# Build from a list of (key, value) tuples
tel2 = dict([("sape", 4139), ("guido", 4127), ("jack", 4098)])

# Build using keyword arguments (keys must be valid identifiers)
tel3 = dict(sape=4139, guido=4127, jack=4098)

print(tel2)  # {'sape': 4139, 'guido': 4127, 'jack': 4098}
print(tel3)  # {'sape': 4139, 'guido': 4127, 'jack': 4098}


# ============================================================
# Block 5: Dict comprehension
# ============================================================

# Create a dict mapping numbers to their squares
squares: dict[int, int] = {x: x**2 for x in (2, 4, 6)}

# Practical example: invert a dictionary (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
inverted: dict[int, str] = {v: k for k, v in original.items()}

print(squares)  # {2: 4, 4: 16, 6: 36}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
