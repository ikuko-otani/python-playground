words = ["cat", "window", "defenestrate"]

print("Loop 1: iterate over elsements")
for w in words:
  print(w, len(w))

print("Loop 2: iterate over indices")
for i in range(len(words)):
  print(i, words[i], len(words[i]))

numbers = [1, 3, 5, 2, 4]

# Sum all numbers using a for-loop
total = 0
for x in numbers:
  total += x
print("Sum:", total)

# Find the maximum using indices
max_value = numbers[0]
for i in range(1, len(numbers)):
  if numbers[i] > max_value:
    max_value = numbers[i]
print("Max:", max_value)

max_value = numbers[0]
for n in numbers:
  if n > max_value:
    max_value = n
print("Max:", max_value)

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]
print("Matrix:", matrix)

# Print all elements row by row
print("Row by row:")
for row in matrix:
  for value in matrix:
    print(value, end=" ")
  print()

# Flatten matrix into a single list
flattened = []
for row in matrix:
  for value in row:
    flattened.append(value)

print("Flattened:", flattened)

# Compute row sums
row_sums = []
for row in matrix:
  row_total = 0
  for value in row:
    row_total += value
  row_sums.append(row_total)

print("Row sums:", row_sums)

col_sums = [0, 0, 0]
for row in matrix:
  for i in range(len(row)):
    col_sums[i] += row[i]
print("Column sums:", col_sums)

from typing import List

def contains_duplicated_bruteforce(nums: List[int]) -> bool:
  """Return True if there are any duplicate values in nums."""
  n = len(nums)
  for i in range(n):
    print("i:", nums[i])
    for j in range (i + 1, n):
      print("j:", nums[j])
      if nums[i] == nums[j]:
        return True
  return False

print(contains_duplicated_bruteforce([1, 2, 3, 4]))   # False
print(contains_duplicated_bruteforce([1, 2, 3, 1]))   # True
print(contains_duplicated_bruteforce([1, 1, 1, 1]))   # True
