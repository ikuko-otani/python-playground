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

