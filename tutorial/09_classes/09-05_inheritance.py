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


# ============================================================
# Block 2: Calling the Base Class Method with super()
# ============================================================


# Extending (not just replacing) the base class method
class Cat(Animal):
    # extend base method via super()
    def speak(self) -> str:
        base_sound = super().speak()
        return base_sound + " (Cat version: Meou!)"


cat = Cat("Whiskers")
print(cat.speak())
# Whiskers makes a sound. (Cat version: Meou!)


# ============================================================
# Block 3: Overriding __init__ and calling super().__init__()
# ============================================================


class Bird(Animal):
    def __init__(self, name: str, can_fly: bool) -> None:
        super().__init__(name)  # initialize the base class
        self.can_fly = can_fly  # add a new attribute

    def speak(self) -> str:
        return f"{self.name} says: Tweet!"

    def info(self) -> str:
        fly_status = "can fly" if self.can_fly else "cannot fly"
        return f"{self.name} {fly_status}."


parrot = Bird("Parrot", True)
penguin = Bird("Penguin", False)
print(parrot.info())  # Parrot can fly.
print(penguin.info())  # Penguin cannot fly.


# ============================================================
# Block 4: isinstance() and issubclass()
# ============================================================

# isinstance(obj, cls) — check if obj is an instance of cls or its subclass
print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  #  True (Dog is a subclass of Animal)
print(isinstance(dog, Cat))  # False

# issubclass(sub, cls) — check class hierarchy
print(issubclass(Dog, Animal))  # True
print(issubclass(Cat, Dog))  # False


# ============================================================
# Block 5: Multiple Inheritance (9.5.1)
# ============================================================


# Python supports multiple inheritance; MRO (Method Resolution Order)
# is determined by the C3 linearization algorithm.
class Flyable:
    def move(self) -> str:
        return "Flying!"


class Swimmable:
    def move(self) -> str:
        return "Swimmable!"


class Duck(Flyable, Swimmable, Animal):
    def __init__(self, name: str) -> None:
        Animal.__init__(self, name)
        # explicit base class init

    def speak(self) -> str:
        return f"{self.name} says: Quack!"


duck = Duck("Donald")
print(duck.speak())  #  Donald says: Quack!
print(duck.move())  # Flying! (Flyable is first in MRO)
print(Duck.__mro__)  # show Method Resolution Order
