# Chapter 5.7: More on Conditions
# Ref: https://docs.python.org/3/tutorial/datastructures.html#more-on-conditions

# -------------------------------------------------------
# 1. Membership test operators: `in` / `not in`
# -------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

print("'banana' in fruits:", "banana" in fruits)
print("'grape' not in fruits", "grape" not in fruits)

# -------------------------------------------------------
# 2. Identity test operators: `is` / `is not`
# -------------------------------------------------------

a = [1, 2, 3]
b = a  # same object
c = [1, 2, 3]  # equal value, different object

print("a is b:", a is b)  # True  — same object in memory
print("a is c:", a is c)  # False — different object, same value
print("a is not c", a is not c)  # True
print("a == b:", a == b)  # True  — value comparison

# -------------------------------------------------------
# 3. Chained comparisons
# -------------------------------------------------------

x = 5

print("1 < x < 10:", 1 < x < 10)  # True  — equivalent to (1 < x) and (x < 10)
print("1 < x < 4:", 1 < x < 4)  # False
print("0 <= x <= 5:", 0 <= x <= 5)  # True
print("x == 5 != 0:", x == 5 != 0)  # True

# -------------------------------------------------------
# 4. Boolean operators: `and` / `or` / `not` — precedence
# -------------------------------------------------------

print("not False:", not False)  # True
print("True and False:", True and False)  # False
print("False or True:", False or True)  # True
print(
    "not False and True or False:", not False and True or False
)  # True — not > and > or

# -------------------------------------------------------
# 5. Short-circuit evaluation
# Returns the last evaluated operand, not True/False
# -------------------------------------------------------

# 'hello' — 0 is falsy, so evaluates right side
print("0 or 'hello':", 0 or "hello")

# 'hi' — 'hi' is truthy, short-circuits
print("'hi' or 'hello':", "hi" or "hello")

# '' — '' is falsy, short-circuits
print("'' and 'hello'", "" and "hello")

# 'hello' — 'hi' is truthy, evaluates right side
print("'hi' and 'hello':", "hi" and "hello")

# -------------------------------------------------------
# 6. Assigning boolean expressions to variables
# 日本語訳：Boolean 式の結果を変数に代入する（first-truthy / last-falsy パターン）
# -------------------------------------------------------

string1 = ""
string2 = ""
string3 = "Python"

non_null = string1 or string2 or string3
print("non_null:", non_null)  # 'Python' — first truthy value in the chain

# `or` chain picks the first truthy value; useful as a default fallback.
# Example: value = user_input or "default"
# Note: For more explicit assignment, use the walrus operator :=

x_val: int
if (x_val := 10) > 5:
    print(f"x_val={x_val} is greater than 5")
