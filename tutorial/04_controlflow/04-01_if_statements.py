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

# Nested if statements and combined conditions
age = 30
has_id = False

if age >= 18:
  if has_id:
    print("Allowed to enter")
  else:
    print("ID required")
else:
  print("Not allowed (under 18)")

# Check if a character is a lowercase vowel
ch = "e"

if ch in "aeiou":
  print("Lowercase vowel")
else:
  print("Not a lowercase vowel")

# Check if a number is in a valid range
score = 85

if 0 <= score <= 100:
  print("Valid score")
else:
  print("Invalid score")

# Conditional logic examples
def classify_number(x: int) -> str:
  """Classify an integer as nagative, zero, or positive."""
  if x < 0:
    return "negative"
  if x == 0:
    return "zero"
  return "positive"

def is_leap_year(year: int) -> bool:
  """Return True if the given year is a leap year."""
  if year % 400 == 0:
    return True
  if year % 100 == 0:
    return False
  if year % 4 == 0:
    return True
  return False

print(classify_number(-5))
print(classify_number(0))
print(classify_number(10))

print(is_leap_year(2000))
print(is_leap_year(1900))
print(is_leap_year(2024))
