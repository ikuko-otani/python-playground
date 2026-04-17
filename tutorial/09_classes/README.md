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
