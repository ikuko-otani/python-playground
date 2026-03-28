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

## Ch 5.1.2 — Using Lists as Queues

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
