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
    print(i)
