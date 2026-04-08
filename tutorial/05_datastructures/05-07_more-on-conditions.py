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
