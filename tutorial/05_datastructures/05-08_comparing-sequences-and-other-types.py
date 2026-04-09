# Chapter 5.8: Comparing Sequences and Other Types
# Ref: https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types


# -------------------------------------------------------
# Block 1: Lexicographical comparison of lists
# -------------------------------------------------------

# Compare lists element by element from the start
result1 = [1, 2, 3] < [1, 2, 4]
result2 = [1, 2] < [1, 2, -1]
result3 = [1, 2, 3] == [1.0, 2.0, 3.0]
result4 = [1, 2, 3] < [1, 3]

print("[1,2,3] < [1,2,4]:", result1)  # True
print("[1,2] < [1,2,-1]:", result2)  # True
print("[1,2,3] == [1.0,2.0,3.0]:", result3)  # True
print("[1,2,3] < [1,3]:", result4)  # True
