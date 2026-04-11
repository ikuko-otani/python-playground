# Chapter 6.3: The dir() Function
# Ref: https://docs.python.org/3/tutorial/modules.html#the-dir-function

import sys
import builtins

# -------------------------------------------------------
# Section 1: dir() with a module — list names in a module
# 日本語訳：dir() にモジュールを渡して定義済み名前を一覧表示する
# -------------------------------------------------------

# ✍️ Call dir() on the sys module
# ✍️ sys モジュールの名前一覧を取得する
module_names: list[str] = dir(sys)
print(module_names)

# -------------------------------------------------------
# Section 2: dir() with no arguments — current scope
# 日本語訳：引数なしの dir() で現在のスコープの名前を一覧表示する
# -------------------------------------------------------

# 📋 Define some names in the current scope for demonstration
# 📋 デモ用に現在のスコープに変数を定義する
my_var = 42
my_list = [1, 2, 3]

# ✍️ Call dir() with no arguments
# ✍️ 引数なしで dir() を呼び出す
current_scope_names: list[str] = dir()
print(current_scope_names)

# -------------------------------------------------------
# Section 3: dir() with builtins — built-in names
# 日本語訳：builtins モジュールで組み込み関数・例外の一覧を取得する
# -------------------------------------------------------

# ✍️ Call dir() on the builtins module
# ✍️ builtins モジュールの名前一覧を取得する
builtin_names: list[str] = dir(builtins)
print(builtin_names)
