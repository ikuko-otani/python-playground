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
