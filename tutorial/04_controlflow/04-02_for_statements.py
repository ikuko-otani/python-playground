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
print("Sum: ", total)

# Find the maximum using indices
max_value = numbers[0]
for i in range(1, len(numbers)):
  if numbers[i] > max_value:
    max_value = numbers[i]
print("Max :", max_value)

max_value = numbers[0]
for n in numbers:
  if n > max_value:
    max_value = n
print("Max :", max_value)

matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]

# Print all elements row by row
for row in matrix:
  for value in matrix:
    print(value, end=" ")
  print()

# Flatten matrix into a single list
flattened = []
for row in matrix:
  for value in row:
    flattened.append(value)

print("Flattened: ", flattened)

