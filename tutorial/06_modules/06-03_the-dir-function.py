# Chapter 6.3: The dir() Function
# Ref: https://docs.python.org/3/tutorial/modules.html#the-dir-function

import builtins
import sys

# -------------------------------------------------------
# Section 1: dir() with a module — list names in a module
# -------------------------------------------------------

# Call dir() on the sys module
module_names: list[str] = dir(sys)
print("module_names:", module_names)

# -------------------------------------------------------
# Section 2: dir() with no arguments — current scope
# -------------------------------------------------------

# Define some names in the current scope for demonstration

my_var = 42
my_list = [1, 2, 3]

# Call dir() with no arguments
current_scope_names: list[str] = dir()
print("current_scope_names:", current_scope_names)
