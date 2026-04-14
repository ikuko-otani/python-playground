# Chapter 7.2: Reading and Writing File
# Ref: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

# ============================================================
# 7.2 Opening files with open() and the with statement
# ============================================================

# open(filename, mode, encoding)
# - 'r'  : read (default)
# - 'w'  : write (overwrites)
# - 'a'  : append
# - 'r+' : read and write
# - 'b'  : binary mode (add to mode, e.g. 'rb')
# Always use 'with' to ensure the file is properly closed.

# Core: open a file for writing, then reading
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
filepath = os.path.join(script_dir, "sample.txt")

with open(filepath, "w", encoding="utf-8") as f:
    f.write("Hello, World!\n")
    f.write("Python file I/O is essential.\n")

with open(filepath, "r", encoding="utf-8") as f:
    contents: str = f.read()
print(contents)

# ============================================================
# 7.2.1 Methods of File Objects
# ============================================================

# f.read(size) — read entire file or up to 'size' bytes/chars
with open(filepath, "r", encoding="utf-8") as f:
    chunk: str = f.read(5)
print(chunk)  # 'Hello'

# f.readline() — read one line at a time
with open(filepath, "r", encoding="utf-8") as f:
    line1: str = f.readline()
    line2: str = f.readline()
print(repr(line1))
print(repr(line2))

# Iterating over a file object — memory-efficient line reading
with open(filepath, "r", encoding="utf-8") as f:
    for line in f:
        print(line, end="")
