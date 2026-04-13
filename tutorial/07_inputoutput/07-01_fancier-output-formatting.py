# Chapter 7.1: Input and Output
# Ref: https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting

# =============================================================================
# 7.1.1 Formatted String Literals (f-strings)
# =============================================================================

# --- Block 1: Basic f-string and format specifier ---

import math

year = 2016
event = "Referendum"
result = f"Results of the {year} {event}"
print(result)
# Results of the 2016 Referendum

print(f"The value of pi is approximately {math.pi:.5f}")
# The value of pi is approximately 3.14159

# --- Block 2: Column alignment with f-string ---

table: dict[str, int] = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 7678}
for name, phone in table.items():
    print(f"{name:10} ==> {phone:10d}")
# Sjoerd     ==>       4127
# Jack       ==>       4098
# Dcab       ==>       7678

# --- Block 3: Conversion flags and debug (=) specifier ---

animals = "eels"
print(f"My hovercraft is full of {animals}.")
print(f"My hovercraft is full of {animals!r}.")
# My hovercraft is full of eels.
# My hovercraft is full of 'eels'.

bugs = "roaches"
count = 13
area = "living room"
print(f"Debugging {bugs=} {count=} {area=}")
# Debugging bugs='roaches' count=13 area='living room'

# =============================================================================
# 7.1.2 The str.format() Method
# (f-string preferred in modern Python)
# =============================================================================

# --- Block 4: str.format() positional and keyword args ---
print("{0} and {1}".format("spam", "eggs"))

print(
    "This {food} is {adjective}.".format(food="spam", adjective="absolutely horrible")
)

# --- Block 5: Passing dict with ** unpacking ---

table2: dict[str, int] = {"Sjoerd": 4127, "Jack": 4098, "Dcab": 8637678}
print("Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}".format(**table2))

# Number table using str.format() with width specifiers
for x in range(1, 11):
    print("{0:2d} {1:3d} {2:4d}".format(x, x * x, x * x * x))
