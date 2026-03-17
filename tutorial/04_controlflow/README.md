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
