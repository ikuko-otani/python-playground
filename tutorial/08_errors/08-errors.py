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
# try/except/else/finally — 例外処理の基本パターン
# else: runs only if NO exception was raised in the try block
# else: try ブロックで例外が発生しなかった場合のみ実行される
# finally: ALWAYS runs, whether or not an exception occurred
# finally: 例外の有無に関わらず必ず実行される（DB・ファイルのクリーンアップに使う）
# =============================================================

print("--- 8.3 Handling Exceptions ---")


def divide(x: float, y: float) -> float | None:
    try:
        result = x / y
    except ZeroDivisionError:
        print("  [8.3] Cannot divide by zero!")
        return None
    else:
        print("  [8.3] Division succeeded:", result)
        return result
    finally:
        print("  [8.3] finally block always runs")


divide(10, 2)
divide(10, 0)

# Catching multiple exception types
print()
for value in ["10", 10, None]:
    try:
        print("  [8.3] int():", int(value))  # type: ignore
    except (ValueError, TypeError) as e:
        print(f"  [8.3] Caught {type(e).__name__}: {e}")

# =============================================================
# [8.4] Raising Exceptions
# raise re-raises the current exception or raises a new one.
# raise は現在の例外を再送出するか、新しい例外を発生させる。
# In FastAPI: raise HTTPException(status_code=404, detail="Not found")
# FastAPI では: raise HTTPException(status_code=404, detail="Not found")
# =============================================================

print("--- 8.4 Raising Exceptions ---")


def get_user(user_id: int) -> dict:
    users = {1: "Alice", 2: "Bob"}
    if user_id not in users:
        raise ValueError(f"User {user_id} not found")
    return {"id": user_id, "name": users[user_id]}


try:
    get_user(99)
except ValueError as e:
    print("  [8.4] Caught ValueError:", e)

# raise without argument re-raises the current exception
try:
    try:
        raise RuntimeError("original error")
    except RuntimeError:
        print("  [8.4] Caught, logging, then re-raising...")
        raise  # re-raise the same exception
except RuntimeError as e:
    print("  [8.4] Re-caught RuntimeError:", e)

# =============================================================
# [8.5] Exception Chaining
# raise NewException from original_exception
# raise NewException from original_exception (例外の連鎖)
# raise X from None — suppresses the original exception context
# raise X from None — 元の例外コンテキストを抑制する
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
    print("  [8.5] ValueError:", e)
    print("  [8.5] __cause__:", e.__cause__)

# =============================================================
# [8.6] User-defined Exceptions
# Custom exception classes inherit from Exception (or its subclasses).
# カスタム例外クラスは Exception（またはそのサブクラス）を継承する。
# Best practice: create a base class for your app, then specific ones.
# ベストプラクティス: アプリ用の基底クラスを作り、その下に具体的な例外を置く。
# =============================================================

print("--- 8.6 User-defined Exceptions ---")


class AppError(Exception):
    """Base exception for this application."""
    pass


class NotFoundError(AppError):
    """Raised when a resource is not found."""

    def __init__(self, resource: str, resource_id: int) -> None:
        self.resource = resource
        self.resource_id = resource_id
        super().__init__(f"{resource} with id={resource_id} not found")


class ValidationError(AppError):
    """Raised when input validation fails."""
    pass


try:
    raise NotFoundError("User", 42)
except NotFoundError as e:
    print(f"  [8.6] NotFoundError: {e}")
    print(f"  [8.6] resource={e.resource}, id={e.resource_id}")
except AppError as e:
    print("  [8.6] Generic AppError:", e)

# =============================================================
# [8.7] Defining Clean-up Actions
# finally runs even if an exception propagates or return is called.
# finally は例外が伝播した場合や return が呼ばれた場合でも必ず実行される。
# Real-world use: closing DB connections, releasing locks, flushing buffers.
# 実務での使用例: DBコネクションのクローズ、ロックの解放、バッファのフラッシュ。
# =============================================================

print("--- 8.7 Defining Clean-up Actions ---")


def open_resource(name: str) -> None:
    print(f"  [8.7] Opening resource: {name}")
    try:
        if name == "bad":
            raise RuntimeError("Resource failed to open")
        print(f"  [8.7] Using resource: {name}")
    except RuntimeError as e:
        print(f"  [8.7] Error: {e}")
    finally:
        print(f"  [8.7] Closing resource: {name} (always runs)")


open_resource("good")
print()
open_resource("bad")

# =============================================================
# [8.8] Predefined Clean-up Actions — "with" statement (concept)
# The "with" statement ensures clean-up even if an error occurs.
# with 文はエラーが発生しても確実にクリーンアップを実行する。
# Already covered in Ch.7 (file I/O). Same principle applies to DB sessions.
# 7章のファイルI/Oで既習。DB セッションにも同じ原則が適用される。
# Example: with open("file.txt") as f: ...
#          with SessionLocal() as db: ...  (FastAPI pattern)
# =============================================================

print("--- 8.8 Predefined Clean-up (with statement — concept only) ---")
print("  [8.8] See Ch.7 for with/open usage. In FastAPI: 'with SessionLocal() as db:'")

# =============================================================
# [8.9] Raising and Handling Multiple Unrelated Exceptions (Python 3.11+)
# ExceptionGroup allows raising/handling multiple unrelated exceptions at once.
# ExceptionGroup は複数の無関係な例外を同時に送出・捕捉できる。(Python 3.11+)
# Use case: concurrent task runners, test frameworks.
# 使用例: 並行タスクランナー、テストフレームワーク。
# Syntax: except* TypeError as eg: ...
# =============================================================

print("--- 8.9 Multiple Unrelated Exceptions (Python 3.11+ concept) ---")
print("  [8.9] ExceptionGroup and except* are Python 3.11+ features.")
print("  [8.9] Example: raise ExceptionGroup('multi', [ValueError('v'), TypeError('t')])")

# =============================================================
# [8.10] Enriching Exceptions with Notes (Python 3.11+)
# exception.add_note(str) attaches additional context to an exception.
# exception.add_note(str) は例外に追加コンテキストを付与する。(Python 3.11+)
# =============================================================

print("--- 8.10 Enriching Exceptions with Notes (Python 3.11+ concept) ---")
try:
    err = ValueError("base error")
    err.add_note("Hint: check your input value")
    err.add_note("Ref: https://docs.python.org/3/tutorial/errors.html#enriching-exceptions-with-notes")
    raise err
except ValueError as e:
    print("  [8.10] ValueError:", e)
    for note in e.__notes__:
        print("  [8.10] note:", note)
