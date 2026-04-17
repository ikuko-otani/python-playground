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
