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
# 日本語訳：del でキーと値のペアを削除する
del tel["sape"]

print(tel)  # {'jack': 4098, 'guido': 4127}
print(value)  # 4098
