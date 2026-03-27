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

# =============================================================
# [2] insert
# insert(i, x): inserts x before the element at index i
# =============================================================
d = ["a", "b", "d"]
d.insert(2, "c")  # insert 'c' before index 2
print("insert:", d)  # ['a', 'b', 'c', 'd']

# =============================================================
# [3] remove
# remove(x): removes the FIRST occurrence of x; raises ValueError if not found
# Pitfall: only removes ONE item even if x appears multiple times
# =============================================================
e = [1, 2, 3, 2, 4]
e.remove(2)
print("remove (only first):", e)  # [1, 3, 2, 4]

# ValueError example — catch so the script doesn't crash
try:
    e.remove(99)
except ValueError as err:
    print("remove ValueError:", err)

# =============================================================
# [4] pop
# pop([i]): removes and RETURNS the item at index i
#           if no index given, removes and returns the LAST item
# =============================================================
f = [10, 20, 30, 40]
last = f.pop()
print("pop() last:", last, "| list:", f)  # pop() last: 40 | list: [10, 20, 30]

item = f.pop(0)
print("pop(0) first:", item, "| list:", f)  # pop(0) first: 10 | list: [20, 30]
