# Chapter 9.3: A First Look at Classes
# Ref: https://docs.python.org/3/tutorial/classes.html#a-first-look-at-classes


# ============================================================
# 9.3.1 Class Definition Syntax
# Basic class definition syntax using the 'class' statement.
# ============================================================


# Define a simple class with a class body
class SimpleClass:
    """A simple example class."""

    # class variable shared by all instances
    kind: str = "generic"


print(SimpleClass.kind)  # generic
print(SimpleClass.__doc__)  # A simple example class.


# ============================================================
# 9.3.2 Class Objects
# Attribute references and instantiation; __init__ method.
# ============================================================


# Class with __init__ and a method
class MyClass:
    """A slightly more complex class"""

    i: int = 12345

    def __init__(self, value: int) -> None:
        # instance variable set in __init__
        self.data: int = value

    def greet(self) -> str:
        return f"Hello, my data is {self.data}"


x = MyClass(99)
print(MyClass.i)  # 12345 (class variable)
print(x.data)  # 99 (instance variable)
print(x.greet())  # Hello, my data is 99


# ============================================================
# 9.3.3 Instance Objects
# Data attributes are created dynamically on the instance.
# ============================================================

# Dynamically add and access instance attributes
x.counter = 1
while x.counter < 4:
    x.counter *= 2
print(x.counter)  # 4

# The instance does NOT affect the class variable
del x.counter


# ============================================================
# 9.3.4 Method Objects
# x.f() is equivalent to MyClass.f(x) — 'self' is passed automatically.
# ============================================================

# Store a method object and call it later
xf = x.greet  # method object (not yet called)
print(xf())  # Hello, my data is 99

# Equivalent call using the class directly
print(MyClass.greet(x))  # Hello, my data is 99


# ============================================================
# 9.3.5 Class and Instance Variables
# Class variables are shared; instance variables are per-object.
# Mutable class variables are a common pitfall.
# ============================================================


# Correct pattern: instance variable for mutable state
class Dog:
    # class variable — shared by all Dog instances
    species: str = "Canis familiaris"

    def __init__(self, name: str) -> None:
        # instance variable — unique to each instance
        self.name: str = name
        self.tricks: list[str] = []
        # ✅ correct: per-instance list

    def add_trick(self, trick: str) -> None:
        self.tricks.append(trick)


d1 = Dog("Rex")
d2 = Dog("Buddy")
d1.add_trick("roll over")
d2.add_trick("play dead")
print(d1.tricks)  # ['roll over'] ← not shared with d2
print(d2.tricks)  # ['play dead']
print(Dog.species)  # Canis familiaris


# Anti-pattern: mutable class variable (pitfall)
class DogBad:
    tricks: list[str] = []
    # ❌ shared across ALL instances!

    def __init__(self, name: str) -> None:
        self.name: str = name

    def add_trick(self, trick: str) -> None:
        self.tricks.append(trick)


b1 = DogBad("Rex")
b2 = DogBad("Buddy")
b1.add_trick("roll over")
b2.add_trick("play dead")
print(b1.tricks)  # ['roll over', 'play dead'] ← b2's trick is here too!
print(b2.tricks)  # ['roll over', 'play dead'] ← same object
