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

def fizz_buzz(n: int) -> None:
  """Print FizzBuzz from 1 to n."""
  for i in range(1, n + 1):
    if i % 15 == 0:
      print("FizzBuzz")
    elif i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)

fizz_buzz(20)

def classify_string(s: str) -> str:
  """Classify a string as empty, digits, letters, or mixed"""
  if len(s) == 0:
    return "empty"
  if s.isdigit():
    return "digits"
  if s.isalpha():
    return "letters"
  return "mixed"

print(classify_string("123"))

from typing import List

def linear_search(nums: List[int], target: int) -> bool:
  """Return True if target exists in nums."""
  for x in nums:
    if x == target:
      return True
  return False

print(linear_search([1, 2, 3], 4))
