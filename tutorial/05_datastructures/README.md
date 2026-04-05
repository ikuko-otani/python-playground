# 5. Data Structures

## 5.1. More on Lists

#### Common Pitfalls

- `sort()`, `reverse()`, `insert()`, `remove()`, `clear()` all return `None`.
  The classic mistake: `result = my_list.sort()` → `result` is `None`, not the sorted list.
  Use `sorted()` if you need a new sorted list and want to keep the original intact.
- `remove(x)` deletes only the **first** occurrence of `x`.
  If `x` appears multiple times, the rest remain. Raises `ValueError` if not found.
- `index(x)` raises `ValueError` if `x` is not in the list.
  Always guard with `try/except ValueError` or check membership with `in` first.
- `append(list)` adds the list **as a single nested element**; use `extend()` to flatten.
- `copy()` is a **shallow copy** — nested mutable objects are still shared by reference.
  Use `copy.deepcopy()` when you need a fully independent copy.
- Sorting a list with mixed types (e.g., `[None, 'hello', 10]`) raises `TypeError`
  because Python cannot compare across incompatible types.
  Complex numbers also have no defined ordering (`3+4j < 5+7j` is invalid).

#### When to Prefer `deque` over `list`

- `list.pop(0)` and `list.insert(0, x)` are **O(n)** — all elements shift.
- `collections.deque` supports O(1) `appendleft()` / `popleft()` at both ends.
- In backend/queue scenarios (e.g., task queues, BFS), always reach for `deque` first.
- This is directly relevant to **5.1.2 Using Lists as Queues** in the tutorial.

#### Design Principle

Mutating methods (`sort`, `reverse`, `insert`, `remove`, `clear`, `append`, `extend`, `pop`)
return `None` by design. This is Python's signal that the operation modifies the object
**in place** rather than producing a new value. Recognising this pattern avoids many bugs.

### 5.1.1. Using Lists as Stacks

#### Tips
- `list.append`/`pop()` provide an O(1) LIFO stack, which is ideal for history, undo stacks, and simulating recursion.
- `pop(0)`/`insert(0, x)` are O(n) and therefore slow; for queues or BFS you should use `from collections import deque`.
- Example: `stack = []; stack.append(x); top = stack.pop()` (these operations do not return `None`).

#### Pitfalls
- Mutating methods like `sort`, `reverse`, `insert`, and `remove` all return `None`; for example, `result = lst.sort()` will make `result` be `None`.
- Typical interview question: “list vs deque?” → For stacks (LIFO), lists are efficient; for queues (FIFO), use `deque` which supports O(1) operations at both ends.

### 5.1.2. Using Lists as Queues

### Key Points

- A queue follows **FIFO** (First-In, First-Out) order.
- **Do NOT use `list.pop(0)` for queue dequeue operations** — it is O(n) because
  Python must shift all remaining elements leftward. This is a classic interview trap.
- **Always use `collections.deque` with `popleft()`** — both `append()` and `popleft()`
  are O(1), making it the correct Python queue implementation.
- `deque` supports operations at **both ends**: `append`/`pop` (right), `appendleft`/`popleft` (left).
- `deque(maxlen=N)` creates a **bounded queue** — the oldest item is auto-discarded
  when the queue exceeds capacity. Useful for sliding window and rate-limiting patterns.
- In real backend code (FastAPI background tasks, message processing), you would typically
  use a proper message broker (Redis Queue, Celery, etc.) rather than an in-process deque,
  but understanding deque is essential for DSA interviews (e.g., BFS, sliding window).
- **Interview tip**: if asked to implement a queue in Python, immediately reach for
  `collections.deque` — using `list` will raise red flags with experienced interviewers.

### Complexity Summary

| Operation       | `list`  | `collections.deque` |
|-----------------|---------|---------------------|
| append (right)  | O(1)    | O(1)                |
| pop (right)     | O(1)    | O(1)                |
| pop (left)      | **O(n)**| **O(1)**            |
| appendleft      | **O(n)**| **O(1)**            |


### 5.1.3. List Comprehensions

#### Core Syntax

```
[expression  for item in iterable]                   # basic
[expression  for item in iterable  if condition]     # with filter
[expression  for x in iter1  for y in iter2]         # cartesian product
[expression  if cond else alt  for item in iterable] # ternary (no filter)
```

#### Why List Comprehensions Matter

- More concise and readable than `for` + `append` for building lists.
- Generally **faster** than equivalent `for`-loop code (CPython optimisation).
- Interviewers expect you to reach for list comprehensions naturally in Python;
  using a raw loop where a comprehension fits is considered non-idiomatic.

#### Common Pitfalls

- **`if` position changes semantics entirely:**
  - `[x for x in nums if cond]` → filter (items can be *removed*)
  - `[x if cond else y for x in nums]` → ternary (all items *kept*, value swapped)
  Mixing these up is one of the most common mistakes in technical screens.
- **Deep nesting hurts readability:** more than two `for` clauses in one
  comprehension is a code smell. Extract to a helper function or use
  `itertools.product` instead.
- **Side-effect expressions are an anti-pattern:**
  `[print(x) for x in items]` works but is misleading — use a plain `for` loop
  if the goal is side effects, not building a list.
- **Memory: list comprehension builds the full list in RAM.**
  For large datasets, use a **generator expression** `(expr for x in iter)`
  instead; it is lazy and O(1) in memory until iterated.

#### List Comprehension vs Generator Expression

| | List Comprehension `[...]` | Generator Expression `(...)` |
|---|---|---|
| Brackets | Square `[]` | Round `()` |
| Returns | `list` (eager, all in RAM) | `generator` (lazy, one at a time) |
| Reusable? | Yes | No — exhausted after one pass |
| Best for | Small/medium data, random access | Large data, streaming, `sum()`/`max()` |

#### Production / FastAPI Context

- Use list comprehensions for shaping API response payloads:
  `[item.dict() for item in db_results if item.is_active]`
- Avoid comprehensions inside tight loops over large collections — prefer
  `filter()` + `map()` with generators, or reach for `pandas`/`polars`.
- For matrix/table operations, `zip(*matrix)` is cleaner than a nested
  comprehension for transposing; idiomatic Python prefers built-ins.

## 5.2. The del Statement

#### What `del` Does

- `del` removes a **name binding** or **object reference** from a namespace or sequence.
- `del a[i]`  → removes element at index `i` from list `a` in-place; returns nothing.
- `del a[i:j]`→ removes a slice; equivalent to `a[i:j] = []` but more explicit.
- `del a[:]`  → empties the list in-place; equivalent to `a.clear()`.
- `del a`     → removes the variable `a` from the namespace entirely.
  Accessing `a` after this raises `NameError`.
- `del d[key]`→ removes a key-value pair from a dict; raises `KeyError` if missing.

#### `del` vs `pop()` — When to Use Which

| | `del a[i]` | `a.pop(i)` |
|---|---|---|
| Returns the value? | ❌ No | ✅ Yes |
| Typical use | Discard; value not needed | Need the removed value |
| Readability | More explicit intent | Communicates "take out" |

#### Common Pitfalls

- `del a` ≠ `a = []`: `del a` removes the name itself; `a = []` just rebinds it to an empty list.
- `del d[key]` raises `KeyError` if the key doesn't exist.
  Use `d.pop(key, None)` as a safer alternative when the key may be absent.
- Deleting from a list while iterating over it causes skipped elements or `IndexError`.
  Collect indices to delete first, then delete in reverse order, or use a list comprehension.

#### Practical Notes (FastAPI / Backend)

- In FastAPI, you rarely manipulate raw dicts with `del`; Pydantic models with
  `model.model_dump(exclude={"password"})` are the preferred pattern.
- `del` is useful in **memory-sensitive** code (e.g., releasing large in-memory datasets
  after processing), though the GC usually handles this automatically.
- Knowing `del` exists—and understanding that CPython uses reference counting—shows
  depth of understanding in interviews.


## 5.3. Tuples and Sequences

#### Key Characteristics

- Tuples are **immutable sequences**: once created, elements cannot be reassigned.
  However, if a tuple contains mutable objects (e.g., lists), those inner objects
  can still be mutated. Tuple immutability is shallow, not deep.
- Tuples are **hashable** (if all elements are hashable), so they can be used as
  dictionary keys or set members — lists cannot. This is a common interview question.

#### Common Pitfalls

- Single-element tuple requires a **trailing comma**: `(42,)` — not `(42)`.
  Without the comma, Python treats it as a parenthesised expression, not a tuple.
- Sequence unpacking raises `ValueError` if the number of variables doesn't match
  the number of elements. Use starred assignment (`first, *rest = seq`) to handle
  variable-length sequences safely.
- Tuple immutability is often confused with "all contents are frozen".
  A tuple holding a list still allows that list to be mutated.

#### Practical Patterns

- **Variable swap without a temp**: `a, b = b, a` — idiomatic Python; shows fluency.
- **Loop unpacking**: `for key, value in items:` — standard pattern in backend data
  processing (also used in `dict.items()` and SQLAlchemy row iteration).
- **Function returning multiple values**: Python functions that return `x, y`
  actually return a tuple. Callers can unpack directly: `width, height = get_size()`.
- **Named tuples** (`collections.namedtuple` or `typing.NamedTuple`) extend plain
  tuples with field names — useful for lightweight data containers in service layers
  where full Pydantic models would be overkill.

#### When to Choose tuple vs list

| Use case | tuple | list |
|---|---|---|
| Fixed collection (coordinates, RGB, DB row) | ✅ Preferred | — |
| Mutable collection (accumulating results) | — | ✅ Preferred |
| Dictionary key or set member | ✅ Hashable | ❌ Not hashable |
| Function returning multiple values | ✅ Idiomatic | — |
| Sequence of homogeneous items to modify | — | ✅ Preferred |

## 5.4. Sets

#### Core Characteristics
- A set is an **unordered collection of unique elements** — no duplicates, no guaranteed order.
- Backed by a hash table internally; membership test `x in s` is **O(1) average** vs O(n) for lists.
- Elements must be **hashable** (immutable): `str`, `int`, `float`, `tuple` are OK; `list`, `dict`, `set` are NOT.

#### Common Pitfalls
- `{}` creates an **empty dict**, NOT an empty set. Always use `set()` for an empty set.
- `set.remove(x)` raises `KeyError` if `x` is absent; use `set.discard(x)` for a safe silent delete.
- `set.pop()` removes an **arbitrary** element — never rely on which element gets removed (sets are unordered).
- Set operators (`|`, `&`, `-`, `^`) require **both operands to be sets**. Methods (`.union()`, `.intersection()`, etc.) accept any iterable on the right-hand side — prefer methods when mixing types.
- Sets are **mutable** but their elements must be immutable. To use a set as a dict key or put it inside another set, use `frozenset()` instead.

#### When to Reach for Sets in Backend Code
- **Deduplication**: `unique_ids = list(set(raw_ids))` — fast O(n) dedupe.
- **Membership testing at scale**: checking if a user ID is in a large allow-list → set lookup beats list lookup dramatically.
- **Graph / BFS / DFS**: `visited = set()` is the standard pattern for tracking visited nodes in coding interviews.
- **Set-difference for delta detection**: `new_items = incoming_set - existing_set` is a clean pattern for sync/upsert logic in data pipelines.

#### `frozenset` in Brief
- Immutable version of `set`; hashable → can be used as a dict key or as a set element.
- Useful for caching results keyed by a collection of IDs (e.g., `frozenset(user_ids)` as a cache key).
