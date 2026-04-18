# Chapter 9.5: Inheritance
# Ref: https://docs.python.org/3/tutorial/classes.html#inheritance


# ============================================================
# Block 1: Basic Inheritance — defining a derived class
# ============================================================


# Base class (parent)
class Animal:
    def __init__(self, name: str):
        self.name = name

    def speak(self) -> str:
        return f"{self.name} makes a sound."

    def describe(self) -> str:
        return f"I am {self.name}."


# Derived class inherits from Animal
class Dog(Animal):
    def speak(self) -> str:
        return f"{self.name} says: Woof!"


dog = Dog("Rex")
print(dog.speak())  # Rex says: Woof!
print(dog.describe())  # inherited from Animal => I am Rex.
