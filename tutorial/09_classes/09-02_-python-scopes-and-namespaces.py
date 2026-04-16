# Chapter 9.2: Python Scopes and Namespaces
# Ref: https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces

# =============================================================================
# Block 1: What is a Namespace?
# A namespace is a mapping from names to objects (implemented as a dict).
# 日本語訳：名前空間とは名前からオブジェクトへのマッピング（辞書として実装）。
# =============================================================================

# Built-in namespace: always available
# 日本語訳：ビルトイン名前空間 — 常に参照可能
print(abs(-5))   # built-in function
print(len([1, 2, 3]))  # built-in function

# Global namespace: defined at module level
# 日本語訳：グローバル名前空間 — モジュールレベルで定義
spam = "global spam"
print(spam)


# =============================================================================
# Block 2: Scope and LEGB Rule
# Python searches names in the order: Local → Enclosing → Global → Built-in
# 日本語訳：スコープの検索順序（LEGBルール）: ローカル → エンクロージング → グローバル → ビルトイン
# =============================================================================

def outer():
    x = "enclosing"  # Enclosing scope
    # 日本語訳：エンクロージングスコープの変数

    def inner():
        x = "local"  # Local scope (shadows enclosing)
        # 日本語訳：ローカルスコープの変数（エンクロージングを隠す）
        print(f"inner x: {x}")  # -> "local"

    inner()
    print(f"outer x: {x}")  # -> "enclosing"


outer()


# =============================================================================
# Block 3: global statement
# 'global' allows reassignment of a module-level variable inside a function.
# 日本語訳：global 文 — 関数内からモジュールレベルの変数を再束縛する
# =============================================================================

count = 0  # global variable


def increment():
    global count  # ✍️ declare global
    count += 1


increment()
increment()
print(f"count after 2 increments: {count}")  # -> 2


# =============================================================================
# Block 4: nonlocal statement
# 'nonlocal' allows reassignment of a variable in the nearest enclosing scope.
# 日本語訳：nonlocal 文 — 最も近いエンクロージングスコープの変数を再束縛する
# =============================================================================

def make_counter():
    n = 0

    def counter():
        nonlocal n  # ✍️ declare nonlocal
        n += 1
        return n

    return counter


c = make_counter()
print(c())  # -> 1
print(c())  # -> 2
print(c())  # -> 3


# =============================================================================
# Block 5: Scope and Namespace Example (from official tutorial 9.2.1)
# Demonstrates local / nonlocal / global with do_* nested functions.
# 日本語訳：公式チュートリアル9.2.1のスコープ実演 — do_local / do_nonlocal / do_global
# =============================================================================

def scope_test():
    def do_local():
        spam = "local spam"
        # 日本語訳：ローカルスコープにのみ存在 — scope_test には影響しない

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        # 日本語訳：エンクロージングスコープ（scope_test）の spam を変更

    def do_global():
        global spam
        spam = "global spam (modified)"
        # 日本語訳：グローバルスコープの spam を変更

    spam = "test spam"  # enclosing scope variable

    do_local()
    print(f"After do_local:    {spam}")   # -> "test spam"

    do_nonlocal()
    print(f"After do_nonlocal: {spam}")   # -> "nonlocal spam"

    do_global()
    print(f"After do_global:   {spam}")   # -> "nonlocal spam" (global changed, not enclosing)


scope_test()
print(f"Global spam after scope_test: {spam}")  # -> "global spam (modified)"
