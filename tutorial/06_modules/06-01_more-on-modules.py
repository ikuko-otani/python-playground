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
