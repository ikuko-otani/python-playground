# Chapter 6.1: More on Modules
# Ref: https://docs.python.org/3/tutorial/modules.html#more-on-modules

# =============================================================================
# Section 1: Basic import and module namespace
# =============================================================================
# Each module has its own private namespace used as the global namespace.

import math

result = math.sqrt(16)
print(f"math.sqrt(16) = {result}")  # 4.0

pi_val = math.pi
print(f"math.pi = {pi_val}")  # 3.141592653589793

# =============================================================================
# Section 2: from module import name
# =============================================================================
# Import specific names directly into the importing module's namespace.

from math import floor, sqrt

print(sqrt(25))  # 5.0 — no 'math.' prefix needed
print(floor(3.9))  # 3

# =============================================================================
# Section 3: from module import * (wildcard import)
# =============================================================================
# Imports all names that do not begin with an underscore (_).
# WARNING: Avoid in production code — pollutes the local namespace.

# =============================================================================
# Section 4: import as alias
# =============================================================================
# Rename a module or name upon import for convenience.

# shorter alias for datetime module
import datetime as dt

# 'as' for a specific name:
from math import factorial as fact

print(fact(5))  # 120
print(dt.date.today())

# =============================================================================
# Section 5: if __name__ == "__main__" pattern
# スクリプトとしても実行できるようにする慣用パターン
# =============================================================================
# When a module is run directly, __name__ is set to "__main__".
# When imported, __name__ is the module's file name (without .py).


def greet(name: str) -> str:
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("Aida"))
    print("Running as a script, not as an imported module.")
