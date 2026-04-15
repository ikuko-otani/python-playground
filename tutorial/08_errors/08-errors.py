# Chapter 8: Errors and Exceptions
# Ref: https://docs.python.org/3/tutorial/errors.html

# =============================================================
# [8.1] Syntax Errors
# The parser reports syntax errors before the program runs.
# パーサーはプログラムの実行前に構文エラーを報告する。
# Example: while True print('Hello')  → SyntaxError
# (This cannot be run; shown here as a comment for reference)
# =============================================================

# print("--- 8.1 Syntax Errors (concept only) ---")
# while True print('Hello')  # SyntaxError: invalid syntax

# =============================================================
# [8.2] Exceptions
# Even syntactically correct code can raise exceptions at runtime.
# 構文的に正しいコードでも実行時に例外が発生することがある。
# Common built-in exceptions: ZeroDivisionError, NameError, TypeError
# =============================================================

print("--- 8.2 Exceptions ---")

try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("ZeroDivisionError:", e)

try:
    print(undefined_variable)
except NameError as e:
    print("NameError:", e)

try:
    "2" + 2
except TypeError as e:
    print("TypeError:", e)

# =============================================================
# [8.3] Handling Exceptions
# try/except/else/finally — the core pattern for exception handling
# else: runs only if NO exception was raised in the try block
# finally: ALWAYS runs, whether or not an exception occurred
# =============================================================

print("--- 8.3 Handling Exceptions ---")


def divide(x: float, y: float) -> float | None:
    try:
        result = x / y
    except ZeroDivisionError:
        print("[8.3] Cannot divide by zero!")
        return None
    else:
        print("[8.3] Division succeeded:", result)
        return result
    finally:
        print("[8.3] finally block always runs")


divide(10, 2)
divide(10, 0)

# Catching multiple exception types
print()
for value in ["10", 10, None]:
    try:
        print("[8.3] int():", int(value))  # type: ignore
    except (ValueError, TypeError) as e:
        print(f"[8.3] Caught {type(e).__name__}: {e}")

# =============================================================
# [8.4] Raising Exceptions
# raise re-raises the current exception or raises a new one.
# In FastAPI: raise HTTPException(status_code=404, detail="Not found")
# =============================================================

print("--- 8.4 Raising Exceptions ---")


def get_user(user_id: int) -> dict:
    users = {1: "Alice", 2: "Bob"}
    if user_id not in users:
        raise ValueError(f"User {user_id} not found")
    return {"id": user_id, "name": users[user_id]}


print(get_user(1))

try:
    get_user(99)
except ValueError as e:
    print("[8.4] Caught ValueError:", e)

# raise without argument re-raises the current exception
try:
    try:
        raise RuntimeError("original error")
    except RuntimeError:
        print("[8.4] Caught, logging, then re-raising...")
        raise  # re-raise the same exception
except RuntimeError as e:
    print("[8.4] Re-caught RuntimeError:", e)

# =============================================================
# [8.5] Exception Chaining
# raise NewException from original_exception
# raise X from None — suppresses the original exception context
# =============================================================

print("--- 8.5 Exception Chaining ---")


def fetch_data(key: str) -> str:
    data = {"name": "Alice"}
    try:
        return data[key]
    except KeyError as e:
        raise ValueError(f"Invalid key: {key}") from e


try:
    fetch_data("age")
except ValueError as e:
    print("[8.5] ValueError:", e)
    print("[8.5] __cause__:", e.__cause__)
