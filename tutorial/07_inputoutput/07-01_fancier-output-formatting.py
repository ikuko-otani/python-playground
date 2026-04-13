# Chapter 7.1: Input and Output
# Ref: https://docs.python.org/3/tutorial/inputoutput.html#fancier-output-formatting

# =============================================================================
# 7.1.1 Formatted String Literals (f-strings)
# =============================================================================

# --- Block 1: Basic f-string and format specifier ---

import math

year = 2016
event = "Referendum"
result = f"Results of the {year} {event}"
print(result)
# Results of the 2016 Referendum

print(f"The value of pi is approximately {math.pi:.5f}")
# The value of pi is approximately 3.14159
