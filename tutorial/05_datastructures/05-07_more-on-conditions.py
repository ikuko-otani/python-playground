# Chapter 5.7: More on Conditions
# Ref: https://docs.python.org/3/tutorial/datastructures.html#more-on-conditions

# -------------------------------------------------------
# 1. Membership test operators: `in` / `not in`
# -------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)
print("grape" not in fruits)

# -------------------------------------------------------
# 2. Identity test operators: `is` / `is not`
# -------------------------------------------------------

a = [1, 2, 3]
b = a  # same object
c = [1, 2, 3]  # equal value, different object

print(a is b)  # True  — same object in memory
print(a is c)  # False — different object, same value
print(a is not c)  # True
print(a == b)  # True  — value comparison
