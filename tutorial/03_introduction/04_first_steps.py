# 3.2 first-steps-towards-programming
# Basic examples from section 3.2 of the Python tutorial

a, b = 0, 1 # Multiple assignment
while a < 10:
  print(a)
  a, b = b, a+b

i = 256 * 256
print('The value of i is', i)

# Fibonacci series up to 1000
a, b = 0, 1
while a < 1000:
  print(a, end=',')
  a, b = b, a+b
