# Chapter 6.3: The dir() Function
# Ref: https://docs.python.org/3/tutorial/modules.html#the-dir-function

import builtins
import sys

# -------------------------------------------------------
# Section 1: dir() with a module — list names in a module
# -------------------------------------------------------

# Call dir() on the sys module
module_names: list[str] = dir(sys)
print(module_names)
