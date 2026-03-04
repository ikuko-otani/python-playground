# Basic if/elif/else example for practice
x = int(input("Please enter an integer: "))

if x < 0:
  print("Negative changed to zero")
elif x == 0:
  print("Zero")
elif x == 1:
  print("single")
else:
  print("More")

# Check if a number is even or odd
n = 7

if n % 2 == 0:
  print("Even")
else:
  print("Odd")

# Check if a number is positive, negative, or Zero
y = -3

if y > 0:
  print("Positive")
elif y < 0:
  print("Negative")
else:
  print("Zero")
