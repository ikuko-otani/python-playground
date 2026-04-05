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

# =============================================================
# [2-1] Set operations — tutorial's a / b example
# =============================================================

# Reuse a and b from section [1-1]

# Difference: letters in a but not in b
print("[2-1] a - b (difference)  :", a - b)  # {'r', 'd', 'b'}

# Difference: letters in b but not in a
print("[2-1] b - a (difference)  :", b - a)  # {'z', 'l', 'm'}

# Union: letters in a or b (or both)
print("[2-1] a | b (union)       :", a | b)  # {'l', 'c', 'm', 'z', 'a', 'r', 'b', 'd'}

# Intersection: letters in both a and b
print("[2-1] a & b (intersection):", a & b)  # {'a', 'c'}

# Symmetric difference: letters in a or b but not both
print("[2-1] a ^ b (sym. diff.)  :", a ^ b)  # {'b', 'r', 'm', 'd', 'z', 'l'

# =============================================================
# [2-2] Equivalent methods — same result, different style
# =============================================================

print("[2-2] a.difference(b)          :", a.difference(b))
print("[2-2] b.difference(a)          :", b.difference(a))
print("[2-2] a.union(b)               :", a.union(b))
print("[2-2] a.intersection(b)        :", a.intersection(b))
print("[2-2] a.symmetric_difference(b):", a.symmetric_difference(b))

# KEY DIFFERENCE: operators require both sides to be sets.
# Methods accept ANY iterable on the right side.
print("[2-2] a.union(['x', 'y']):", a.union(["x", "y"]))
print("[2-2] a.union(('s', 't')):", a.union(("s", "t")))

# =============================================================
# [2-3] Subset / Superset checks
# =============================================================

x = {1, 2, 3}
y = {1, 2, 3, 4, 5}
print("[2-3] x.issubset(y)   :", x.issubset(y))  # True  x ⊆ y
print("[2-3] y.issuperset(x) :", y.issuperset(x))  # True  y ⊇ x
print("[2-3] x <= y          :", x <= y)  # True  (same as issubset)
print("[2-3] x < y           :", x < y)  # True  (strict subset: x ⊊ y)

# =============================================================
# [3-1] Mutating methods: add, remove, discard, pop, clear
# =============================================================

s = {"apple", "banana", "cherry"}

# add: adds a single element; no-op if already present
s.add("date")
s.add("apple")  # already in set — no error, no duplicate
print("[3-1] after add:", s)

# remove vs discard
# Use remove() when absence is a bug (you WANT the KeyError).
# Use discard() when absence is acceptable (safe delete).

# remove: removes element; raises KeyError if not found
s.remove("banana")
print("[3-1] after remove('banana'):", s)

try:
    s.remove("mango")  # not in set → KeyError
except KeyError as err:
    print("[3-1] remove KeyError:", err)

# discard: removes element; SILENTLY does nothing if not found
s.discard("mango")  # no error even though 'mango' is absent
print("[3-1] after discard('mango') — no error:", s)

# pop: removes and returns an ARBITRARY element (sets are unordered!)
popped = s.pop()
print("[3-1] popped element:", popped, "| remaining:", s)

# clear: remove all elements from the set
t = {1, 2, 3}
t.clear()
print("[3-1] after clear():", t)  # set()

# =============================================================
# [4-1] Set comprehension — similar to list comprehension
# Ref: tutorial mentions {x for x in 'abracadabra' if x not in 'abc'}
# =============================================================

# Tutorial's official example
result = {x for x in "abracadabra" if x not in "abc"}
print("[4-1] set comprehension:", result)  # {'r', 'd'}

# Practical example: unique even squares
even_squares = {x**2 for x in range(10) if x % 2 == 0}
print("[4-1] even squares set:", even_squares)  # {0, 64, 4, 36, 16

# Use case: extract unique domain names from a list of emails
emails = ["alice@example.com", "bob@example.com", "carol@test.org", "dave@test.org"]
domains = {email.split("@")[1] for email in emails}
print("[4-1] unique domains:", domains)  # {'test.org', 'example.com'}
