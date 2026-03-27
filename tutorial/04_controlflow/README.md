# 4. More Control Flow Tools

## 4.1 if Statements

- **Branching logic** is everywhere: validation, edge, cases, and early returns.
- Clear conditions make your code easier to read.
- Avoid deep nesting when possible; prefer early returns and guard clauses.
- Keep each `if` block short and forcused.
- Put the "edge cases" at the top as guard clauses when it makes sense.

## 4.2 for Statements

- Being Comfortable with both `for x in list` and index-based loops reduces bugs.
- Prefer element-based loops when you do not need the index.
- Use index-based loops when you need positions or neighboring elements.

## 4.3. The range() Function

- You use range() with for-loops to control how many times you iterate.
- `for i in range(len(nums))` is a common pattern when you need indices.
- Using a negative step like `range(len(nums) - 1, -1, -1)` helples when you scan arrays backwards.
- `range(n)` gives 0 to n-1.
- `range(start, stop)` includes start, exludes stop.
- `range(start, stop, step)` can move forwords or backwards.
- Convert to a list only when you really need all values at once (`list(range(n))`).

## 4.4. break and continue Statements

- `break`: exits the **innermost** loop immediately; useful for early termination
- `continue`: skips the **rest of the current iteration**; useful for filtering out invalid/unwanted values.
- **`return` is preferred over `break`** because it exits the function entirely and avoids extra flag variables.
- `continue` is idiomatic for **guard clauses inside loops** - reject bad input early and keep the happy path un-indented.
- `break` matters in **nested loops**: it only exits the *inner* loop.
  To exit all loops at once, use a function with `return`.
- Linear search with `break`: O(n) time, O(1) space.

## 4.6. pass Statements

- `pass` is a **no-op statement**: syntactically required but does nothing at runtime.
- Common use cases:
  - Busy-wait loops (rare in production; prefer `asyncio`)
  - Empty class bodies (e.g., custom exception stubs: `class NotFoundError(Exception): pass`)
  - Unimplemented function placeholders during top-down design
- `...` (Ellipsis) is an **object** (`<class 'ellipsis'>`), not a keyword.
  - Preferred in **typed stubs** (`.pyi` files) and **abstract method bodies**.
  - Tools like `mypy` and `pyright` (used in FastAPI projects) treat `...` as a signal for "not yet implemented".
- In FastAPI / Pydantic v2 context: `...` is also used as a **required field marker** in `Field(...)` — a completely different meaning.
- Interview tip: if asked "what does `pass` do?", always mention the Ellipsis alternative and when you'd choose each.

## 4.7. match  Statements

> Python 3.10+ required (`python --version` to verify)

- `match` performs **structural pattern matching** — it matches both shape and content.
- **No fall-through**: unlike `switch` in C/Java, Python `match` stops after the first matching `case`. No `break` needed.
- **No error on no-match**: if no `case` matches, Python does nothing (no exception). This differs from languages where `switch` without `default` can be risky.
- Pattern types to know:
  - **Literal**: `case 200:` — matches exact values
  - **Wildcard**: `case _:` — catch-all, always last
  - **OR**: `case 401 | 403 | 404:` — multiple values in one branch
  - **Sequence**: `case [first, *rest]:` — unpacks lists/tuples by structure
  - **Class**: `case Point(x, y):` — unpacks class instances; requires `__match_args__` for positional syntax
  - **Guard**: `case pattern if condition:` — adds extra filtering to a pattern
  - **Dict** (bonus): `case {"type": t}:` — matches dict structure, great for event routing
- `__match_args__` on a class enables **positional** pattern syntax instead of `case Point(x=x, y=y)`.
- Real-world uses in FastAPI / backend:
  - HTTP response code branching (replaces long `if/elif` chains)
  - WebSocket / event-driven message dispatch
  - Command pattern routing in background tasks
- `match` is NOT just a `switch` replacement — its power comes from **destructuring** (unpacking values inline), which makes it closer to pattern matching in Haskell/Rust/Scala.

## 4.7. Defining Functions

### Basic syntax

- Use the `def` keyword followed by the function name, parameters in parentheses, and a colon.
- The function body must be indented (PEP 8: 4 spaces).
- An optional docstring on the first line documents the function's purpose.

```python
def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}!"
```

### Why use functions?

- Reusability: write once, call many times — no duplicated logic.
- Structure: break a large problem into small, named units.
- Testability: a function with a clear input/output is easy to unit-test (pytest).
- Readability: a well-named function acts as self-documenting code.

### Definition vs Call

- `def fib_list(n):` — definition: registers the function object in the namespace; nothing runs yet.
- `fib_list(100)` — call: executes the body and returns a result.
- A common interview mistake: forgetting that def alone does not execute anything.

### return and None
- Every Python function returns a value. If `return` is omitted, Python implicitly returns `None`.
- A bare `return` (no value) also returns `None` — useful for early-exit guard clauses.
- Always prefer `return` with a value in backend code: it makes the result assignable, testable, and composable.

### Functions as objects (first-class)
- Functions are objects; you can assign them to variables and call them via an alias.

```python
f = fib_list   # no parentheses — assigns the object, not the result
f(50)          # same as fib_list(50)
```

- This is the foundation of higher-order functions, callbacks, and FastAPI's `Depends()`.

### Local namespace

- Variables defined inside a function are local — isolated from the outer scope.
- This isolation makes functions predictable and safe to test independently.


### Interview one-liners

- *"Why use functions?"* → "To encapsulate logic for reuse, readability, and testability — the same principles that make FastAPI route handlers and service-layer functions clean."
- *"What does a function return if there's no return statement?"* → "It implicitly returns None. In Python, every function call is an expression."
- *"What is a first-class function?"* → "A function treated as a value — assignable to a variable, passable as an argument. It's how we implement callbacks and dependency injection."
