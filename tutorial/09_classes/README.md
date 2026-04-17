## 9.3 A First Look at Classes

Key concepts:
- Class definition syntax (`class` statement, class body)
- Class Objects: attribute references, instantiation, `__init__`
- Instance Objects: dynamic data attributes
- Method Objects: `x.f()` == `MyClass.f(x)`, `self` is auto-passed
- Class vs Instance Variables: mutable class variable pitfall

Note:
- Always define mutable state (`list`, `dict`) as instance variables in `__init__`
- This pattern is the same principle used in Pydantic models and SQLAlchemy ORM

## 9.4 Random Remarks

- Instance attributes override class attributes with the same name.
  This lookup order is a common source of subtle bugs when you accidentally shadow a class-level default on a single instance.
- Python does not enforce data hiding (no real `private` keyword).
  A single leading underscore in `_name` is only a convention meaning “internal use”, not a hard access restriction.
- Always use `self.` for instance attributes and methods.
  This explicitness makes it obvious which names are per-instance state versus local variables, and is part of Python’s design philosophy.
- The name `self` is not a keyword, just a strong convention for the first parameter of instance methods.
  You technically can rename it, but doing so hurts readability and will look unprofessional in code reviews or interviews.
- Methods are just functions stored as attributes on a class.
  You can assign a top-level function to a class attribute and have it behave like a method when accessed via an instance, but this pattern should be used sparingly for clarity.
- Inside a method, call other methods via `self.other_method(...)` instead of referencing the class directly.
  This respects inheritance and allows subclasses to override behavior cleanly.
- Every value in Python is an object and has a `__class__` attribute (for example, `42.__class__` is `int`).
  This underpins tools like `isinstance` and is important when reasoning about dynamic types in real-world backend code.

### Code Examples

```python
# Example 1: Instance attribute overriding a class attribute

class Warehouse:
    # class attributes (shared defaults)
    purpose = "storage"
    region = "west"

w1 = Warehouse()
w2 = Warehouse()

# override only on this instance
w2.region = "east"

print("w1.region:", w1.region)  # uses class attribute: "west"
print("w2.region:", w2.region)  # uses instance attribute: "east"
```

Instance attributes with the same name as a class attribute take precedence on that single object, which can be surprising if you expect all instances to share the same value.

```python
# Example 2: No enforced data hiding, only conventions

class BankAccount:
    def __init__(self, balance: int) -> None:
        self._balance = balance  # leading underscore means “internal use”

acc = BankAccount(100)
# This is allowed in Python, even though it breaks encapsulation:
acc._balance = 9999
print("Balance is now:", acc._balance)
```

Python uses naming conventions (like a single leading underscore) instead of strict access modifiers, so teams rely on discipline and code reviews for proper encapsulation.

```python
# Example 3: Using self for instance attributes and method calls

class Bag:
    def __init__(self) -> None:
        self.data = []

    def add(self, x) -> None:
        # must use self.data, not just data
        self.data.append(x)

    def add_twice(self, x) -> None:
        # call another method via self to respect overrides in subclasses
        self.add(x)
        self.add(x)

bag = Bag()
bag.add_twice("apple")
print("Bag contents:", bag.data)
```

The explicit self prefix makes it clear which names are per-instance state and ensures that method calls can be overridden by subclasses cleanly.

```python
# Example 4: A top-level function attached as a method

def greet(self, name: str) -> str:
    return f"Hello, {name}!"

class Greeter:
    say_hello = greet  # becomes a bound method when accessed via an instance

g = Greeter()
print(g.say_hello("Berlin"))
```

Functions become methods when they are stored on a class and accessed through an instance, but this pattern should be used sparingly to keep the codebase easy to follow.

```python
# Example 5: Everything is an object with a __class__

print((42).__class__)                # <class 'int'>
print("backend".__class__)           # <class 'str'>
print([1, 2, 3].__class__)           # <class 'list'>

class Custom:
    pass

c = Custom()
print(c.__class__)                   # <class '__main__.Custom'>
```

Every value in Python has a class, which is the foundation for dynamic typing and tools like isinstance used heavily in real-world backend code.
