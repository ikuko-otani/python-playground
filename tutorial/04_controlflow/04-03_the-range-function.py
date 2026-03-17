# Basic range(n): from 0 to n-1
for i in range(5):
  print("range(5):", i)

print("---")

# range(start, stop)
for i in range(5, 10):
  print("range(5, 10):", i)

print("---")

# range(start, stop, step)
for i in range(0, 10, 3):
  print("range(0, 10, 3):", i)

print("---")

# Negative step
for i in range(-10, -100, -30):
  print("range(-10, -100, -30):", i)

words = ['Mary', 'had', 'a', 'little', 'lamb']

# Iterate over indices using range(len(...))
for i in range(len(words)):
  print("index:", i, "word:", words[i])

nums = [1, 3, 5, 7]

# Compare neighbors using indices
for i in range(len(nums) - 1):
  print("pair:", nums[i], nums[i + 1])

# Iterate backwords over indices
for i in range(len(nums) - 1, -1, -1):
  print("reverse index:", i, "value:", nums[i])

# Show that range is an iterable, not a real list
r = range(4)
print("range object:", r)

# Convert range to a list explicitly
print("list(range(4)):", list(r))

# Use range as an iterable for sum()
total = sum(range(4))
print("sum(range(4)):", total)
