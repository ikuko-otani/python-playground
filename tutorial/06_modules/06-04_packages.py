# Chapter 6.4: Packages
# Ref: https://docs.python.org/3/tutorial/modules.html#packages

# =============================================================================
# [Block 1] What is a Package? — Package structure and __init__.py
# =============================================================================
# A package is a directory with __init__.py that groups related modules.
#
# Example package structure (sound package):
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

# Core logic: three ways to import from a package

# Pattern 1: import the full dotted path (must use full name)
import sound.effects.echo

sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# Pattern 2: from-import the submodule (use without package prefix)
from sound.effects import echo

echo.echofilter(input, output, delay=0.7, atten=4)

# Pattern 3: from-import a specific function/class directly
from sound.effects.echo import echofilter

echofilter(input, output, delay=0.7, atten=4)

# =============================================================================
# [Block 2] __init__.py and __all__ — Controlling 'from package import *'
# =============================================================================
# __all__ in __init__.py controls what 'from package import *' exports.
#
# In sound/effects/__init__.py:

# Core logic: defining __all__ in __init__.py
# __all__ = ["echo", "surround", "reverse"]
# This means: from sound.effects import * => imports echo, surround, reverse

# Pitfall: if a name in __all__ is shadowed by a local definition,
# the local definition takes precedence over the submodule.

# Example of shadowing (in __init__.py):
__all__ = ["echo", "surround", "reverse"]


def reverse(msg: str) -> str:  # <-- shadows the reverse.py submodule!
    return msg[::-1]
