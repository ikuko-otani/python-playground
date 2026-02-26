# 3.2 First Steps Towards Programming
# Basic examples from section 3.2 of the Python tutorial

# Multiple assignment
a, b = 0, 1
# Fibonacci sequence: each number is the sum of the previous two
while a < 10:
  print(a)
  a, b = b, a+b

i = 256 * 256
# Strings are printed without quotes, and a space is inserted between items
print('The value of i is', i)

# Fibonacci series up to 1000
a, b = 0, 1
while a < 1000:
  # The keyword argument end can be used to avoid the newline after the output,
  # or end the output with a different string
  print(a, end=',')
  a, b = b, a+b

print("multiple assignment demo")

# Swap two variables using multiple assignment
x, y = 1, 2
print("Before swap:", x, y)

x, y = y, x
print("After swap", x, y)
