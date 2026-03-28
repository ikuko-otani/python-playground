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

# =============================================================
# [5] clear
# clear(): removes ALL items from the list; equivalent to del a[:]
# =============================================================
g = [1, 2, 3]
g.clear()
print(("clear:", g))  # []

# =============================================================
# [6] index
# index(x[, start[, stop]]): returns zero-based index of first occurrence of x
#   optional start/stop narrow the search range (slice notation)
#   raises ValueError if x is not found
# =============================================================
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]
print("index('banana'):", fruits.index("banana"))  # 3
print("index('banana', 4):", fruits.index("banana", 4))  # 6

# ValueError when item not found
try:
    fruits.index("grape")
except ValueError as err:
    print("index ValueError:", err)

# =============================================================
# [7] count
# count(x): returns the number of times x appears in the list
# =============================================================
print("count('apple'):", fruits.count("apple"))  # 2
print("count('tangerine'):", fruits.count("tangerine"))  # 0

# =============================================================
# [8] Tutorial's official fruits example — reproduce exactly
# Ref: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# =============================================================
fruits = ["orange", "apple", "pear", "banana", "kiwi", "apple", "banana"]

fruits.reverse()
print("after reverse:", fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']

fruits.append("grape")
print("after append:", fruits)
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']

fruits.sort()
print("after sort:", fruits)
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

popped = fruits.pop()
print("after pop:", fruits, "| popped:", popped)
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange'] | popped: pear

# =============================================================
# [9] reverse
# reverse(): reverses the list IN PLACE; returns None
# =============================================================
nums = [3, 1, 4, 1, 5]
result = nums.reverse()
print("reverse returns:", result)  # None
print("reversed list  :", nums)  # [5, 1, 4, 1, 3]

# =============================================================
# [10] sort vs sorted — destructive vs non-destructive
# sort():   modifies the list IN PLACE (destructive) — returns None
# sorted(): returns a NEW sorted list; original is unchanged (non-destructive)
#
# Pitfall: result = my_list.sort()  → result is None, NOT the sorted list!
# =============================================================
original = [3, 1, 4, 1, 5, 9]

# sort() — in-place, returns None
sort_return = original.sort()
print("sort() returns :", sort_return)  # None
print("original after sort:", original)  # [1, 1, 3, 4, 5, 9]

# sorted() — non-destructive
original2 = [3, 1, 4, 1, 5, 9]
sorted_list = sorted(original2)
print("sorted() returns:", sorted_list)  # [1, 1, 3, 4, 5, 9]
print("original2 unchanged:", original2)  # [3, 1, 4, 1, 5, 9]

# sort with key and reverse
words = ["banana", "Apple", "kiwi", "ORANGE"]
words.sort(key=str.lower)
print("sort key=str.lower:", words)

words.sort(key=str.lower, reverse=True)
print("sort reverse=True:", words)

# =============================================================
# [11] Mixed types cannot be sorted — triggers TypeError
# Ref: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
#   "not all data can be sorted or compared"
#   "[None, 'hello', 10] doesn't sort because integers can't be
#    compared to strings and None can't be compared to other types"
# =============================================================
mixed = [None, "hello", 10]
try:
    mixed.sort()
except TypeError as err:
    print("mixed sort TypeError:", err)

# =============================================================
# [12] copy
# copy(): returns a SHALLOW copy of the list; equivalent to a[:]
# Shallow means nested objects are NOT copied — they share references
# =============================================================
h = [1, 2, [3, 4]]
h_copy = h.copy()
h_copy[0] = 99
h_copy[2].append(5)  # nested list IS shared!
print("original:", h)
print("copy:", h_copy)
