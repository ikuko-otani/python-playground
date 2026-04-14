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

# f.readlines() — read all lines into a list
with open(filepath, "r", encoding="utf-8") as f:
    lines: list[str] = f.readlines()
print(lines)

# f.write(string) — write string, returns number of characters written
with open(filepath, "a", encoding="utf-8") as f:
    n: int = f.write("Appended line.\n")
print(n)

# f.tell() and f.seek(offset, whence)
with open(filepath, "rb") as f:
    # binary mode required for seek with non-0 whence
    f.seek(0, 2)  # move to end of file
    end_pos: int = f.tell()
    f.seek(0)  # back to start
    start_pos: int = f.tell()
print(f"File size: {end_pos} bytes, start pos: {start_pos}")

# ============================================================
# 7.2.2 Saving structured data with json
# ============================================================

import json

# json.dumps(x) — serialize Python object to JSON string
data: dict = {"name": "Bill", "city": "Berlin", "score": 42}
json_str: str = json.dumps(data)
print(json_str)

# json.dump(x, f) — write serialized object to a file
jsonfilepath = os.path.join(script_dir, "data.json")
with open(jsonfilepath, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# json.load(f) — deserialize JSON file back to Python object
with open(jsonfilepath, "r", encoding="utf-8") as f:
    loaded: dict = json.load(f)
print(loaded)
print(type(loaded))  # <class 'dict'>

# Note: pickle can serialize arbitrary Python objects (not just JSON-compatible types),
# but it is NOT human-readable and NOT safe for untrusted data.
