# Basic range(n): from 0 to n-1
for i in range(5):
  print("range(5):", i)

print("---")

# range(start, end)
for i in range(5, 10):
  print("range(5, 10):", i)

print("---")

# range(start, end, step)
for i in range(0, 10, 3):
  print("range(0, 10, 3):", i)

print("---")

# Negative step
for i in range(-10, -100, -30):
  print("range(-10, -100, -30):", i)
