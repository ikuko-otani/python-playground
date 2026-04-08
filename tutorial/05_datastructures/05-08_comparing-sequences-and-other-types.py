# Chapter 5.8: Comparing Sequences and Other Types
# Ref: https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types


# -------------------------------------------------------
# Block 1: Lexicographical comparison of lists
# 日本語訳：リストの辞書式比較（先頭要素から順番に比較）
# -------------------------------------------------------

# Compare lists element by element from the start
# 日本語訳：先頭から順に要素を比較する
 result1 = [1, 2, 3] < [1, 2, 4]
result2 = [1, 2] < [1, 2, -1]
result3 = [1, 2, 3] == [1.0, 2.0, 3.0]
result4 = [1, 2, 3] < [1, 3]

print("[1,2,3] < [1,2,4]:", result1)          # True
print("[1,2] < [1,2,-1]:", result2)            # True
print("[1,2,3] == [1.0,2.0,3.0]:", result3)   # True
print("[1,2,3] < [1,3]:", result4)             # True


# -------------------------------------------------------
# Block 2: Lexicographical comparison of tuples
# 日本語訳：タプルの辞書式比較
# -------------------------------------------------------

# Tuples are compared the same way as lists
# 日本語訳：タプルもリストと同様に辞書式に比較される
result5 = (1, 2, 3) < (1, 2, 4)
result6 = (1, 2, 3, 4) < (1, 2, 4)
result7 = (1, 2) < (1, 2, -1)
result8 = (1, 2, 3) == (1.0, 2.0, 3.0)

print("(1,2,3) < (1,2,4):", result5)           # True
print("(1,2,3,4) < (1,2,4):", result6)         # True
print("(1,2) < (1,2,-1):", result7)            # True
print("(1,2,3) == (1.0,2.0,3.0):", result8)   # True


# -------------------------------------------------------
# Block 3: String comparison by Unicode code point
# 日本語訳：文字列の比較（Unicodeコードポイント順）
# -------------------------------------------------------

# Strings are compared character by character using Unicode code points
# 日本語訳：文字列は文字ごとに Unicode コードポイントで比較される
result9  = 'ABC' < 'C'
result10 = 'C' < 'Pascal'
result11 = 'Pascal' < 'Python'
result12 = 'abc' > 'ABC'   # lowercase > uppercase in Unicode

print("'ABC' < 'C':", result9)         # True
print("'C' < 'Pascal':", result10)     # True
print("'Pascal' < 'Python':", result11) # True
print("'abc' > 'ABC':", result12)      # True


# -------------------------------------------------------
# Block 4: Comparing sequences of different lengths
# 日本語訳：長さの異なるシーケンスの比較
# -------------------------------------------------------

# If one sequence is a prefix of the other, the shorter one is smaller
# 日本語訳：一方が他方の先頭部分列なら、短い方が小さい
result13 = [1, 2] < [1, 2, 3]
result14 = (1,) < (1, 0)
result15 = 'ab' < 'abc'

print("[1,2] < [1,2,3]:", result13)   # True
print("(1,) < (1,0):", result14)      # True
print("'ab' < 'abc':", result15)      # True


# -------------------------------------------------------
# Block 5: Comparing different types raises TypeError
# 日本語訳：異なる型同士の大小比較は TypeError を発生する
# -------------------------------------------------------

# == and != work across types, but < > raise TypeError for unorderable types
# 日本語訳：== と != は型を越えて使えるが、< > はオーダー隣接ない型には TypeError 

result16 = (1, 2, 3) == [1, 2, 3]   # False: different types
result17 = (1, 2, 3) != [1, 2, 3]   # True

print("(1,2,3) == [1,2,3]:", result16)  # False
print("(1,2,3) != [1,2,3]:", result17)  # True

# Uncommenting the line below will raise TypeError:
# 日本語訳：下記の行のコメントを外すと TypeError が発生する例
# print( (1, 2) < [1, 2] )   # TypeError: '<' not supported between instances of 'tuple' and 'list'

try:
    result_err = (1, 2) < [1, 2]
except TypeError as e:
    print("TypeError caught:", e)
