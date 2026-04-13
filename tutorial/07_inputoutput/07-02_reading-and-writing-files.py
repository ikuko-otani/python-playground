# Chapter 7.2: Reading and Writing File
# Ref: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

# ============================================================
# 7.2 Opening files with open() and the with statement
# 日本語訳：open() と with 文によるファイルオープン
# ============================================================

# open(filename, mode, encoding)
# - 'r'  : read (default)
# - 'w'  : write (overwrites)
# - 'a'  : append
# - 'r+' : read and write
# - 'b'  : binary mode (add to mode, e.g. 'rb')
# Always use 'with' to ensure the file is properly closed.
# 日本語訳：with を使うと close() を忘れても安全にファイルが閉じられる

# ✍️ Core: open a file for writing, then reading
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Berlin!\n")
    f.write("Python file I/O is essential.\n")

with open("sample.txt", "r", encoding="utf-8") as f:
    contents: str = f.read()
print(contents)

# ============================================================
# 7.2.1 Methods of File Objects
# 日本語訳：ファイルオブジェクトのメソッド
# ============================================================

# f.read(size) — read entire file or up to 'size' bytes/chars
# 日本語訳：ファイル全体、またはsize文字分を読み込む
with open("sample.txt", "r", encoding="utf-8") as f:
    chunk: str = f.read(5)
print(chunk)  # 'Hello'

# f.readline() — read one line at a time
# 日本語訳：1行ずつ読み込む（末尾に \n が含まれる）
with open("sample.txt", "r", encoding="utf-8") as f:
    line1: str = f.readline()
    line2: str = f.readline()
print(repr(line1))
print(repr(line2))

# Iterating over a file object — memory-efficient line reading
# 日本語訳：for ループによる行読み込みはメモリ効率が良い（推奨）
with open("sample.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line, end="")

# f.readlines() — read all lines into a list
# 日本語訳：全行をリストとして取得する（list(f) と同等）
with open("sample.txt", "r", encoding="utf-8") as f:
    lines: list[str] = f.readlines()
print(lines)

# f.write(string) — write string, returns number of characters written
# 日本語訳：文字列を書き込み、書き込んだ文字数を返す
with open("sample.txt", "a", encoding="utf-8") as f:
    n: int = f.write("Appended line.\n")
print(n)  # 15

# f.tell() and f.seek(offset, whence)
# 日本語訳：tell() は現在位置を返す。seek() はファイル位置を移動する
# whence: 0=先頭(default), 1=現在位置, 2=末尾
with open("sample.txt", "rb") as f:  # binary mode required for seek with non-0 whence
    f.seek(0, 2)                      # move to end of file
    end_pos: int = f.tell()
    f.seek(0)                         # back to start
    start_pos: int = f.tell()
print(f"File size: {end_pos} bytes, start pos: {start_pos}")

# ============================================================
# 7.2.2 Saving structured data with json
# 日本語訳：json モジュールで構造化データを保存・読み込みする
# ============================================================

import json

# json.dumps(x) — serialize Python object to JSON string
# 日本語訳：PythonオブジェクトをJSON文字列にシリアライズ
data: dict = {"name": "Ikuko", "city": "Berlin", "score": 42}
json_str: str = json.dumps(data)
print(json_str)

# json.dump(x, f) — write serialized object to a file
# 日本語訳：シリアライズしてファイルに書き込む
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

# json.load(f) — deserialize JSON file back to Python object
# 日本語訳：JSONファイルをPythonオブジェクトに読み込む
with open("data.json", "r", encoding="utf-8") as f:
    loaded: dict = json.load(f)
print(loaded)
print(type(loaded))  # <class 'dict'>

# Note: pickle can serialize arbitrary Python objects (not just JSON-compatible types),
# but it is NOT human-readable and NOT safe for untrusted data.
# 日本語訳：pickle は任意のPythonオブジェクトを保存できるが、
#           人間が読めず、信頼できないデータには使わないこと（セキュリティリスク）
