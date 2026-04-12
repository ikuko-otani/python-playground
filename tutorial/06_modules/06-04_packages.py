# Chapter 6.4: Packages
# Ref: https://docs.python.org/3/tutorial/modules.html#packages

# =============================================================================
# [Block 1] What is a Package? — Package structure and __init__.py
# 日本語訳：パッケージとは何か？ — パッケージ構造と __init__.py の役割
# =============================================================================
# A package is a directory with __init__.py that groups related modules.
# 日本語訳：パッケージは __init__.py を持つディレクトリで、関連モジュールをまとめる。
#
# Example package structure (sound package):
# 日本語訳：パッケージ構造の例（sound パッケージ）
#
# sound/                  <- Top-level package
#     __init__.py         <- Makes this directory a package
#     effects/            <- Subpackage
#         __init__.py
#         echo.py
#         surround.py
#         reverse.py
#     filters/            <- Subpackage
#         __init__.py
#         equalizer.py
#         vocoder.py
#     formats/            <- Subpackage
#         __init__.py
#         wavread.py
#         wavwrite.py

# ✍️ Core logic: three ways to import from a package
# ✍️ コアロジック：パッケージからのインポート 3 パターン

# Pattern 1: import the full dotted path (must use full name)
# パターン1：完全パスでインポート（呼び出し時も完全名が必要）
# import sound.effects.echo
# sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# Pattern 2: from-import the submodule (use without package prefix)
# パターン2：サブモジュールを from-import（パッケージ名なしで使える）
# from sound.effects import echo
# echo.echofilter(input, output, delay=0.7, atten=4)

# Pattern 3: from-import a specific function/class directly
# パターン3：関数・クラスを直接 from-import（推奨パターン）
# from sound.effects.echo import echofilter
# echofilter(input, output, delay=0.7, atten=4)

# 📋 Print summary
print("=== Block 1: Package Import Patterns ===")
print("Pattern 1: import sound.effects.echo  -> sound.effects.echo.echofilter(...)")
print("Pattern 2: from sound.effects import echo  -> echo.echofilter(...)")
print("Pattern 3: from sound.effects.echo import echofilter  -> echofilter(...)")
print()

# =============================================================================
# [Block 2] __init__.py and __all__ — Controlling 'from package import *'
# 日本語訳：__init__.py と __all__ — 'from package import *' の制御
# =============================================================================
# __all__ in __init__.py controls what 'from package import *' exports.
# 日本語訳：__init__.py 内の __all__ は 'from package import *' の公開リストを制御する。
#
# In sound/effects/__init__.py:
# 日本語訳：sound/effects/__init__.py に記述する内容：

# ✍️ Core logic: defining __all__ in __init__.py
# ✍️ コアロジック：__init__.py での __all__ 定義
# __all__ = ["echo", "surround", "reverse"]
# # This means: from sound.effects import * => imports echo, surround, reverse
# # 日本語訳：from sound.effects import * で echo, surround, reverse のみが読み込まれる

# ⚠️ Pitfall: if a name in __all__ is shadowed by a local definition,
# the local definition takes precedence over the submodule.
# ⚠️ 落とし穴：__all__ に同名のローカル定義があると、サブモジュールより優先される。
#
# Example of shadowing (in __init__.py):
# 日本語訳：シャドーイングの例（__init__.py 内）：
# __all__ = ["echo", "surround", "reverse"]
# def reverse(msg: str) -> str:   # <-- shadows the reverse.py submodule!
#     return msg[::-1]            # ← reverse.py ではなくこの関数が公開される

# 📋 Print summary
print("=== Block 2: __all__ in __init__.py ===")
print("__all__ = ['echo', 'surround', 'reverse']")
print("=> from sound.effects import * imports only those listed in __all__")
print("⚠️  If 'reverse' is also defined as a function in __init__.py,")
print("   the function shadows the 'reverse' submodule in 'import *'")
print()

# =============================================================================
# [Block 3] Intra-package References — Absolute vs Relative Imports
# 日本語訳：パッケージ内参照 — 絶対インポートと相対インポート
# =============================================================================
# Inside a package, you can use absolute or relative imports.
# 日本語訳：パッケージ内では絶対インポートと相対インポートの両方が使える。

# ✍️ Core logic: relative import syntax (from surround.py inside effects/)
# ✍️ コアロジック：相対インポートの構文（effects/surround.py の中から）
# from . import echo           # . = current package (effects/)
# from .. import formats       # .. = parent package (sound/)
# from ..filters import equalizer  # ../filters/ = sibling subpackage

# Key rule: relative imports use leading dots to indicate hierarchy.
# 日本語訳：相対インポートは先頭のドット数でパッケージ階層を示す。
# .   => same package
# ..  => parent package
# ... => grandparent package

# ⚠️ Pitfall: relative imports do NOT work in the __main__ module.
# Scripts run directly (python script.py) must use absolute imports.
# ⚠️ 落とし穴：__main__ として実行されるスクリプトでは相対インポートは使えない。

# 📋 Print summary
print("=== Block 3: Intra-package References ===")
print("Absolute: from sound.effects import echo   (always safe)")
print("Relative: from . import echo               (. = current package)")
print("Relative: from .. import formats           (.. = parent package)")
print("Relative: from ..filters import equalizer  (sibling subpackage)")
print("⚠️  Relative imports cannot be used in the __main__ module (top-level script)")
print()

# =============================================================================
# [Block 4] FastAPI Real-world Connection — Package patterns in production
# 日本語訳：FastAPI 実務との接続 — 本番コードでのパッケージパターン
# =============================================================================
# FastAPI projects use exactly the same package/subpackage structure.
# 日本語訳：FastAPI プロジェクトはまったく同じパッケージ/サブパッケージ構造を使う。
#
# Typical FastAPI project layout:
# 日本語訳：典型的な FastAPI プロジェクトのレイアウト：
#
# app/
#     __init__.py
#     main.py            <- FastAPI() instance
#     routers/           <- Subpackage for route handlers
#         __init__.py
#         users.py
#         items.py
#     models/            <- Subpackage for SQLAlchemy/Pydantic models
#         __init__.py
#         user.py
#         item.py
#     core/              <- Subpackage for config, security, DB session
#         __init__.py
#         config.py
#         security.py

# ✍️ Core logic: how FastAPI imports routers (from . import pattern)
# ✍️ コアロジック：FastAPI でのルーター読み込み方法（from . import パターン）
# In app/main.py:
# from app.routers import users, items          # absolute import
# from .routers import users, items             # relative import (same effect)
# app.include_router(users.router)
# app.include_router(items.router)

# In app/routers/users.py:
# from ..models.user import UserSchema          # relative: go up to app/, then models/
# from ..core.security import get_current_user  # relative: app/core/security.py

# 📋 Print summary
print("=== Block 4: FastAPI Real-world Connection ===")
print("app/")
print("  __init__.py")
print("  main.py      <- from app.routers import users, items")
print("  routers/     <- APIRouter subpackage")
print("    __init__.py")
print("    users.py   <- from ..models.user import UserSchema")
print("    items.py")
print("  models/")
print("    __init__.py")
print("    user.py")
print()
print("Key interview point: 'from . import router' is relative import inside a package.")
print("'from app.routers import users' is the absolute equivalent.")
