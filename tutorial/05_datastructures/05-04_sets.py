# Chapter 5.4: Sets
# Ref: https://docs.python.org/3/tutorial/datastructures.html#sets

# =============================================================
# [1-1] Creating sets — two ways
# 1) set() constructor from an iterable (e.g., string, list)
# 2) curly-brace literal {a, b, c}
# =============================================================

# Tutorial's official basket example
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print("[1-1] basket set:", basket)
# Output: {'pear', 'apple', 'banana', 'orange'}  ← duplicates removed, order NOT guaranteed

# Membership test — O(1) average, much faster than list's O(n)
print("[1-1] 'orange' in basket:", "orange" in basket)  # True
print("[1-1] 'crabgrass' in basket:", "crabgrass" in basket)  # False

# set() from a string — each character becomes an element
a = set("abracadabra")
b = set("alacazam")
print("[1-1] set from string a:", a)  # {'d', 'a', 'r', 'c', 'b'}
print("[1-1] set from string b:", b)  # {'m', 'l', 'a', 'z', 'c'}

# PITFALL: {} creates an empty DICT, NOT an empty set!
empty_dict = {}
empty_set = set()  # ← correct way to make an empty set
print("[1-1] type({}):", type(empty_dict))  # <class 'dict'>
print("[1-1] type(set()):", type(empty_set))  # <class 'set'>
