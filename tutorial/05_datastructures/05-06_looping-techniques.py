# Chapter 5.6: Looping Techniques
# Ref: https://docs.python.org/3/tutorial/datastructures.html#looping-techniques

# ============================================================
# 1. dict.items() — Loop over key-value pairs in a dictionary
# ============================================================

knights = {"gallahad": "the pure", "robin": "the brave"}
for k, v in knights.items():
    print(k, v)

# ============================================================
# 2. enumerate() — Loop with index and value
# ============================================================

for i, v in enumerate(["tic", "tac", "toe"], 1):
    print(i, v)

# ============================================================
# 3. zip() — Loop over two sequences simultaneously
# ============================================================

questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
for q, a in zip(questions, answers):
    print(f"What is your {q}?  It is {a}.")

# ============================================================
# 4. reversed() — Loop over a sequence in reverse
# ============================================================

for i in reversed(range(1, 10, 2)):
    print(i, end=" ")
print()

# ============================================================
# 5. sorted() — Loop over a sorted copy of a sequence
# ============================================================

basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
for f in sorted(basket):
    print(f, end=" ")
print()

# ============================================================
# 6. sorted(set(...)) — Loop over unique sorted elements
# ============================================================

for f in sorted(set(basket)):
    print(f, end=" ")
print()

# ============================================================
# 7. Avoid modifying a list while iterating — create a new list
# ============================================================
import math

raw_data = [56.2, float("nan"), 51.7, 55.3, 52.5, float("nan"), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)
