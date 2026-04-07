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
