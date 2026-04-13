# Chapter 7.1: Input and Output
# Ref: https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting

# =============================================================================
# 7.1.1 Formatted String Literals (f-strings)
# =============================================================================

# --- Block 1: Basic f-string and format specifier ---
# 日本語訳：f-stringの基本と書式指定子

import math

year = 2016
event = "Referendum"
result = f"Results of the {year} {event}"
print(result)
# => Results of the 2016 Referendum

print(f"The value of pi is approximately {math.pi:.3f}.")
# => The value of pi is approximately 3.142.

# --- Block 2: Column alignment with f-string ---
# 日本語訳：f-stringによる列揃え（最小フィールド幅指定）

table: dict[str, int] = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 7678}
for name, phone in table.items():
    print(f"{name:10} ==> {phone:10d}")
# => Sjoerd     ==>       4127
# => Jack       ==>       4098
# => Dcab       ==>       7678

# --- Block 3: Conversion flags and debug (=) specifier ---
# 日本語訳：変換フラグ (!r, !s, !a) とデバッグ用 = 指定子

animals = "eels"
print(f"My hovercraft is full of {animals}.")
print(f"My hovercraft is full of {animals!r}.")
# => My hovercraft is full of eels.
# => My hovercraft is full of 'eels'.

bugs = "roaches"
count = 13
area = "living room"
print(f"Debugging {bugs=} {count=} {area=}")
# => Debugging bugs='roaches' count=13 area='living room'

# =============================================================================
# 7.1.2 The str.format() Method
# (f-string で代替可能 / f-string preferred in modern Python)
# =============================================================================

# --- Block 4: str.format() positional and keyword args ---
# 日本語訳：str.format() の位置引数・キーワード引数

print("{0} and {1}".format("spam", "eggs"))
# => spam and eggs

print("This {food} is {adjective}.".format(food="spam", adjective="absolutely horrible"))
# => This spam is absolutely horrible.

# --- Block 5: Passing dict with ** unpacking ---
# 日本語訳：辞書を ** 展開して format() に渡す（面接頻出）

table2: dict[str, int] = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637678}
print("Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}".format(**table2))
# => Jack: 4098; Sjoerd: 4127; Dcab: 8637678

# Number table using str.format() with width specifiers
for x in range(1, 11):
    print("{0:2d} {1:3d} {2:4d}".format(x, x * x, x * x * x))

# =============================================================================
# 7.1.3 Manual String Formatting  ← 読み飛ばしOK (概念のみ)
# =============================================================================

# rjust(), ljust(), center() pad a string in a field of given width.
# zfill() pads a numeric string with leading zeros.
# 日本語訳：rjust/ljust/center は文字列をフィールド幅に合わせてパディング。
#           zfill は数値文字列の先頭をゼロ埋め。

print("12".zfill(5))      # => 00012
print("-3.14".zfill(7))   # => -003.14

# =============================================================================
# 7.1.4 Old String Formatting (% operator)  ← 読み飛ばしOK (概念のみ)
# =============================================================================

# The % operator (printf-style) is the legacy formatting method.
# 日本語訳：% 演算子による旧来のフォーマット（レガシー、現代では非推奨）。

print("The value of pi is approximately %5.3f." % math.pi)
# => The value of pi is approximately 3.142.
