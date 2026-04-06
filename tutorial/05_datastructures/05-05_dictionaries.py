# Chapter 5.5: Dictionaries
# Ref: https://docs.python.org/3/tutorial/datastructures.html#dictionaries


# ============================================================
# Block 1: Creating dictionaries and basic operations
# 日本語訳：辞書の作成と基本操作（追加・アクセス・削除）
# ============================================================

# Create a dictionary with initial key-value pairs
# 日本語訳：初期キーと値のペアで辞書を作成する
tel: dict[str, int] = {"jack": 4098, "sape": 4139}

# Add a new key-value pair
# 日本語訳：新しいキーと値のペアを追加する
tel["guido"] = 4127

# Access a value by key (raises KeyError if not found)
# 日本語訳：キーで値にアクセスする（存在しない場合 KeyError が発生）
value = tel["jack"]

# Delete a key-value pair with del
# 日本語訳：del でキーと値のペアを削除する
del tel["sape"]

print(tel)          # {'jack': 4098, 'guido': 4127}
print(value)        # 4098


# ============================================================
# Block 2: Safe access with get(), key existence check with in
# 日本語訳：get() による安全なアクセス、in によるキーの存在確認
# ============================================================

# Use get() to avoid KeyError — returns None or a default value
# 日本語訳：get() で KeyError を避ける — None またはデフォルト値を返す
result_none = tel.get("irv")               # key does not exist -> None
result_default = tel.get("irv", 0)         # key does not exist -> 0

# Check if a key exists using the in keyword
# 日本語訳：in キーワードでキーの存在を確認する
is_guido_in = "guido" in tel
is_jack_out = "jack" not in tel

print(result_none)      # None
print(result_default)   # 0
print(is_guido_in)      # True
print(is_jack_out)      # False


# ============================================================
# Block 3: Listing keys with list() and sorted()
# 日本語訳：list() と sorted() でキーの一覧を取得する
# ============================================================

# list(d) returns keys in insertion order
# 日本語訳：list(d) は挿入順でキーを返す
keys_list = list(tel)

# sorted(d) returns keys in sorted order
# 日本語訳：sorted(d) はソートされた順でキーを返す
keys_sorted = sorted(tel)

print(keys_list)    # ['jack', 'guido']
print(keys_sorted)  # ['guido', 'jack']


# ============================================================
# Block 4: Building dictionaries with dict() constructor
# 日本語訳：dict() コンストラクタで辞書を作成する
# ============================================================

# Build from a list of (key, value) tuples
# 日本語訳：(key, value) タプルのリストから辞書を作成する
tel2 = dict([("sape", 4139), ("guido", 4127), ("jack", 4098)])

# Build using keyword arguments (keys must be valid identifiers)
# 日本語訳：キーワード引数で辞書を作成する（キーは識別子として有効な文字列のみ）
tel3 = dict(sape=4139, guido=4127, jack=4098)

print(tel2)  # {'sape': 4139, 'guido': 4127, 'jack': 4098}
print(tel3)  # {'sape': 4139, 'guido': 4127, 'jack': 4098}


# ============================================================
# Block 5: Dict comprehension
# 日本語訳：辞書内包表記（面接頻出！）
# ============================================================

# Create a dict mapping numbers to their squares
# 日本語訳：数値をキー、その2乗を値にした辞書を作る
squares: dict[int, int] = {x: x**2 for x in (2, 4, 6)}

# Practical example: invert a dictionary (swap keys and values)
# 日本語訳：実用例：辞書を反転させる（キーと値を入れ替える）
original = {"a": 1, "b": 2, "c": 3}
inverted: dict[int, str] = {v: k for k, v in original.items()}

print(squares)   # {2: 4, 4: 16, 6: 36}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
