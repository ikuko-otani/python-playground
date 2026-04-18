# Chapter 9.5: Inheritance
# Ref: https://docs.python.org/3/tutorial/classes.html#inheritance


# ============================================================
# Block 1: Basic Inheritance — defining a derived class
# 日本語訳：基本的な継承 — 派生クラスの定義
# ============================================================

# Base class (parent)
# 日本語訳：基底クラス（親クラス）
class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return f"{self.name} makes a sound."

    def describe(self) -> str:
        return f"I am {self.name}."


# Derived class inherits from Animal
# 日本語訳：Animalを継承した派生クラス
class Dog(Animal):
    def speak(self) -> str:  # ✍️ override the base method
        return f"{self.name} says: Woof!"


dog = Dog("Rex")
print(dog.speak())     # ✍️ => Rex says: Woof!
print(dog.describe())  # 📋 inherited from Animal => I am Rex.


# ============================================================
# Block 2: Calling the Base Class Method with super()
# 日本語訳：super() を使って基底クラスのメソッドを呼び出す
# ============================================================

# Extending (not just replacing) the base class method
# 日本語訳：基底クラスのメソッドを置き換えるのではなく拡張する
class Cat(Animal):
    def speak(self) -> str:  # ✍️ extend base method via super()
        base_sound = super().speak()
        return base_sound + " (Cat version: Meow!)"


cat = Cat("Whiskers")
print(cat.speak())  # 📋 => Whiskers makes a sound. (Cat version: Meow!)


# ============================================================
# Block 3: Overriding __init__ and calling super().__init__()
# 日本語訳：__init__ をオーバーライドして super().__init__() を呼び出す
# ============================================================

class Bird(Animal):
    def __init__(self, name: str, can_fly: bool) -> None:  # ✍️
        super().__init__(name)   # ✍️ initialize the base class
        self.can_fly = can_fly   # ✍️ add a new attribute

    def speak(self) -> str:
        return f"{self.name} says: Tweet!"

    def info(self) -> str:
        fly_status = "can fly" if self.can_fly else "cannot fly"
        return f"{self.name} {fly_status}."


parrot = Bird("Parrot", True)
penquin = Bird("Penguin", False)
print(parrot.info())   # 📋 => Parrot can fly.
print(penquin.info())  # 📋 => Penguin cannot fly.


# ============================================================
# Block 4: isinstance() and issubclass()
# 日本語訳：isinstance() と issubclass() の使い方
# ============================================================

# isinstance(obj, cls) — check if obj is an instance of cls or its subclass
# 日本語訳：obj が cls またはそのサブクラスのインスタンスかどうかを確認する
print(isinstance(dog, Dog))     # ✍️ => True
print(isinstance(dog, Animal))  # ✍️ => True (Dog is a subclass of Animal)
print(isinstance(dog, Cat))     # ✍️ => False

# issubclass(sub, cls) — check class hierarchy
# 日本語訳：クラスの継承関係を確認する
print(issubclass(Dog, Animal))  # ✍️ => True
print(issubclass(Cat, Dog))     # ✍️ => False


# ============================================================
# Block 5: Multiple Inheritance (9.5.1)
# 日本語訳：多重継承（9.5.1）
# ============================================================

# Python supports multiple inheritance; MRO (Method Resolution Order)
# is determined by the C3 linearization algorithm.
# 日本語訳：Pythonは多重継承をサポートする。MRO（メソッド解決順序）は
# C3線形化アルゴリズムによって決まる。
class Flyable:
    def move(self) -> str:
        return "Flying!"


class Swimmable:
    def move(self) -> str:
        return "Swimming!"


class Duck(Flyable, Swimmable, Animal):  # ✍️ multiple inheritance
    def __init__(self, name: str) -> None:
        Animal.__init__(self, name)  # ✍️ explicit base class init

    def speak(self) -> str:
        return f"{self.name} says: Quack!"


duck = Duck("Donald")
print(duck.speak())   # 📋 => Donald says: Quack!
print(duck.move())    # 📋 => Flying! (Flyable is first in MRO)
print(Duck.__mro__)   # 📋 show Method Resolution Order
