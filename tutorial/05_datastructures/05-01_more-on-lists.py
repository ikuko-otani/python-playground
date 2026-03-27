# Chapter 5.1: More on Lists — list object methods
# Ref: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists

# =============================================================
# [1] append / extend
# append: adds a single item to the end of the list
# extend: appends all items from an iterable to the list
# =============================================================
a = [1, 2, 3]
a.append(4)
print("append:", a)

b = [1, 2, 3]
b.extend([4, 5, 6])
print("extend:", b)

# Key difference: append vs extend
# append([4, 5]) adds the list AS A SINGLE ELEMENT → nested list
# extend([4, 5]) unpacks and appends each element individually
c = [1, 2, 3]
c.append([4, 5])
print("append with list:", c)  # [1, 2, 3, [4, 5]]
