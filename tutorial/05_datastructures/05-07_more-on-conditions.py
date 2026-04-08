# Chapter 5.7: More on Conditions
# Ref: https://docs.python.org/3/tutorial/datastructures.html#more-on-conditions

# -------------------------------------------------------
# 1. Membership test operators: `in` / `not in`
# 日本語訳：メンバーシップテスト演算子 `in` / `not in`
# -------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

# ✍️ core logic
print("banana" in fruits)      # True
print("grape" not in fruits)   # True

# -------------------------------------------------------
# 2. Identity test operators: `is` / `is not`
# 日本語訳：オブジェクト同一性テスト演算子 `is` / `is not`
# -------------------------------------------------------

a = [1, 2, 3]
b = a          # same object
c = [1, 2, 3]  # equal value, different object

# ✍️ core logic
print(a is b)       # True  — same object in memory
print(a is c)       # False — different object, same value
print(a is not c)   # True
print(a == c)       # True  — value comparison

# -------------------------------------------------------
# 3. Chained comparisons
# 日本語訳：比較演算子のチェーン（連鎖比較）
# -------------------------------------------------------

x = 5

# ✍️ core logic
print(1 < x < 10)        # True  — equivalent to (1 < x) and (x < 10)
print(1 < x < 4)         # False
print(0 <= x <= 5)       # True
print(x == 5 != 0)       # True

# -------------------------------------------------------
# 4. Boolean operators: `and` / `or` / `not` — precedence
# 日本語訳：Boolean 演算子の優先順位  not > and > or
# -------------------------------------------------------

# ✍️ core logic
print(not False)                     # True
print(True and False)                # False
print(False or True)                 # True
print(not False and True or False)   # True — not > and > or の優先順位確認

# -------------------------------------------------------
# 5. Short-circuit evaluation
# 日本語訳：ショートサーキット評価（左から評価し、結果が確定したら右を評価しない）
# Returns the last evaluated operand, not True/False
# 日本語訳：戻り値は True/False ではなく、最後に評価されたオペランド
# -------------------------------------------------------

# ✍️ core logic
print(0 or "hello")       # 'hello' — 0 is falsy, so evaluates right side
print("hi" or "hello")   # 'hi'    — 'hi' is truthy, short-circuits
print("" and "hello")    # ''      — '' is falsy, short-circuits
print("hi" and "hello")  # 'hello' — 'hi' is truthy, evaluates right side

# -------------------------------------------------------
# 6. Assigning boolean expressions to variables
# 日本語訳：Boolean 式の結果を変数に代入する（first-truthy / last-falsy パターン）
# -------------------------------------------------------

string1 = ""
string2 = ""
string3 = "Python"

# ✍️ core logic
non_null = string1 or string2 or string3
print(non_null)   # 'Python' — first truthy value in the chain

# --- Interview tip ---
# `or` chain picks the first truthy value; useful as a default fallback.
# 日本語訳：`or` チェーンは最初の truthy 値を返す。デフォルト値のフォールバックとして便利。
# Example: value = user_input or "default"
# Note: For more explicit assignment, use the walrus operator :=
# 日本語訳：より明示的な代入には `:=`（walrus operator）を使う
x_val: int
if (x_val := 10) > 5:
    print(f"x_val={x_val} is greater than 5")  # x_val=10 is greater than 5
