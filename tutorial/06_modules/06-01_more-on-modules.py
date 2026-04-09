# Chapter 6.1: More on Modules
# Ref: https://docs.python.org/3/tutorial/modules.html#more-on-modules

# =============================================================================
# Section 1: Basic import and module namespace
# モジュールのインポートと名前空間
# =============================================================================
# Each module has its own private namespace used as the global namespace.
# モジュールはそれぞれ独立したプライベート名前空間を持つ。

import math

result = math.sqrt(16)
print(f"math.sqrt(16) = {result}")  # 4.0

pi_val = math.pi
print(f"math.pi = {pi_val}")  # 3.141592653589793

# =============================================================================
# Section 2: from module import name
# 特定の名前だけをインポートする
# =============================================================================
# Import specific names directly into the importing module's namespace.
# 特定の名前をインポート元の名前空間に直接取り込む。

from math import sqrt, floor

print(sqrt(25))   # 5.0 — no 'math.' prefix needed
print(floor(3.9))  # 3

# =============================================================================
# Section 3: from module import * (wildcard import)
# ワイルドカードインポートとその落とし穴
# =============================================================================
# Imports all names that do not begin with an underscore (_).
# アンダースコアで始まらないすべての名前をインポートする。
# WARNING: Avoid in production code — pollutes the local namespace.
# 注意：本番コードでは避けること。ローカル名前空間が汚染される。

from os.path import *

print(join("/usr", "local", "bin"))   # /usr/local/bin
print(exists("/usr"))                 # True

# =============================================================================
# Section 4: import as alias
# エイリアスを使ったインポート
# =============================================================================
# Rename a module or name upon import for convenience.
# インポート時にモジュールや名前を別名（エイリアス）に変更できる。

import numpy as np          # common convention in data science
import datetime as dt       # shorter alias for datetime module

# 'as' for a specific name:
from math import factorial as fact

print(fact(5))         # 120
print(dt.date.today()) # today's date

# =============================================================================
# Section 5: if __name__ == "__main__" pattern
# スクリプトとしても実行できるようにする慣用パターン
# =============================================================================
# When a module is run directly, __name__ is set to "__main__".
# モジュールが直接実行される場合、__name__ は "__main__" になる。
# When imported, __name__ is the module's file name (without .py).
# インポートされた場合は、__name__ はファイル名（.py なし）になる。

def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Berlin"))  # Hello, Berlin!
    print("Running as a script, not as an imported module.")
    # スクリプトとして実行中。インポートされたモジュールとしてではない。

# =============================================================================
# Section 6: sys.path — module search path
# sys.path: モジュール検索パス
# =============================================================================
# sys.path is a list of directories where Python looks for modules.
# sys.path はモジュールを探すディレクトリのリスト。
# It can be modified at runtime, but prefer PYTHONPATH env var in production.
# 実行時に変更できるが、本番環境では PYTHONPATH 環境変数を推奨。

import sys

print("sys.path (first 3 entries):")
for p in sys.path[:3]:
    print(f"  {p}")

# To add a custom path (demo only — not for production):
# カスタムパスを追加する例（デモのみ）
custom_path = "/tmp/my_modules"
if custom_path not in sys.path:
    sys.path.append(custom_path)
    print(f"Added to sys.path: {custom_path}")

# =============================================================================
# Section 7: importlib.reload — reloading a module
# importlib.reload でモジュールを再読み込みする
# =============================================================================
# Use importlib.reload() when you need to re-execute a module's code.
# モジュールのコードを再実行したい場合に importlib.reload() を使う。
# Useful in interactive sessions; rarely needed in production.
# 対話的セッションで有用。本番では滅多に使わない。

import importlib
import math as _math_reload_target

importlib.reload(_math_reload_target)
print(f"math module reloaded: {_math_reload_target.__name__}")
