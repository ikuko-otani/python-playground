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
