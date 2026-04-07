# Chapter 5.6: Looping Techniques
# Ref: https://docs.python.org/3/tutorial/datastructures.html#looping-techniques

# ============================================================
# 1. dict.items() — Loop over key-value pairs in a dictionary
# 日本語訳：辞書のキーと値を同時にループする
# ============================================================

knights = {"gallahad": "the pure", "robin": "the brave"}
for k, v in knights.items():
    print(k, v)

# ============================================================
# 2. enumerate() — Loop with index and value
# 日本語訳：インデックスと値を同時にループする
# ============================================================

for i, v in enumerate(["tic", "tac", "toe"]):
    print(i, v)

# ============================================================
# 3. zip() — Loop over two sequences simultaneously
# 日本語訳：2つのシーケンスを同時にループする
# ============================================================

questions = ["name", "quest", "favorite color"]
answers = ["lancelot", "the holy grail", "blue"]
for q, a in zip(questions, answers):
    print(f"What is your {q}?  It is {a}.")

# ============================================================
# 4. reversed() — Loop over a sequence in reverse
# 日本語訳：シーケンスを逆順にループする
# ============================================================

for i in reversed(range(1, 10, 2)):
    print(i)

# ============================================================
# 5. sorted() — Loop over a sorted copy of a sequence
# 日本語訳：シーケンスのソート済みコピーをループする
# ============================================================

basket = ["apple", "orange", "apple", "pear", "orange", "banana"]
for f in sorted(basket):
    print(f)

# ============================================================
# 6. sorted(set(...)) — Loop over unique sorted elements
# 日本語訳：重複を除去してソートしたものをループする（慣用句）
# ============================================================

for f in sorted(set(basket)):
    print(f)

# ============================================================
# 7. Avoid modifying a list while iterating — create a new list
# 日本語訳：ループ中にリストを変更しない——新しいリストを作る
# ============================================================
import math

raw_data = [56.2, float("nan"), 51.7, 55.3, 52.5, float("nan"), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print(filtered_data)
