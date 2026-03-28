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
