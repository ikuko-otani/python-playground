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


# -------------------------------------------------------
# Block 2: Lexicographical comparison of tuples
# -------------------------------------------------------

# Tuples are compared the same way as lists
result5 = (1, 2, 3) < (1, 2, 4)
result6 = (1, 2, 3, 4) < (1, 2, 4)
result7 = (1, 2) < (1, 2, -1)
result8 = (1, 2, 3) == (1.0, 2.0, 3.0)

print("(1,2,3) < (1,2,4):", result5)  # True
print("(1,2,3,4) < (1,2,4):", result6)  # True
print("(1,2) < (1,2,-1):", result7)  # True
print("(1,2,3) == (1.0,2.0,3.0):", result8)  # True


# -------------------------------------------------------
# Block 3: String comparison by Unicode code point
# -------------------------------------------------------

# Strings are compared character by character using Unicode code points
result9 = "ABC" < "C"
result10 = "C" < "Pascal"
result11 = "Pascal" < "Python"
result12 = "abc" > "ABC"  # lowercase > uppercase in Unicode

print("'ABC' < 'C':", result9)  # True
print("'C' < 'Pascal':", result10)  # True
print("'Pascal' < 'Python':", result11)  # True
print("'abc' > 'ABC':", result12)  # True

print(ord("A"), ord("a"), ord("C"))  # 65 97 67


# -------------------------------------------------------
# Block 4: Comparing sequences of different lengths
# -------------------------------------------------------

# If one sequence is a prefix of the other, the shorter one is smaller
result13 = [1, 2] < [1, 2, 3]
result14 = (1,) < (1, 0)
result15 = "ab" < "abc"

print("[1,2] < [1,2,3]:", result13)  # True
print("(1,) < (1,0):", result14)  # True
print("'ab' < 'abc':", result15)  # True


# -------------------------------------------------------
# Block 5: Comparing different types raises TypeError
# 日本語訳：異なる型同士の大小比較は TypeError を発生する
# -------------------------------------------------------

# == and != work across types, but < > raise TypeError for unorderable types

result16 = (1, 2, 3) == [1, 2, 3]  # False: different types
result17 = (1, 2, 3) != [1, 2, 3]  # True

print("(1,2,3) == [1,2,3]:", result16)  # False
print("(1,2,3) != [1,2,3]:", result17)  # True

# TypeError: '<' not supported between instances of 'tuple' and 'list'

try:
    result_err = (1, 2) < [1, 2]
except TypeError as e:
    print("TypeError caught:", e)
