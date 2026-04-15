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
