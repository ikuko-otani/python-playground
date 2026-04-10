# Chapter 6.2: Standard Modules
# Ref: https://docs.python.org/3/tutorial/modules.html#standard-modules

import sys

# Check the Python version
sys.version

# sys.version_info gives a named tuple with major, minor, micro, etc.
print(sys.version_info)
print(sys.version_info.major, sys.version_info.minor)

# sys.platform returns a string identifying the operating system
print(sys.platform)

if sys.platform == "linux":
    print("Running on Linux")
elif sys.platform == "darwin":
    print("Running on macOS")
else:
    print(f"Running on: {sys.platform}")

# sys.path is a list of strings specifying the module search path
print(sys.path)

# Append a custom path to sys.path
sys.path.append("/tmp/my_modules")
print(sys.path[-1])

# Remove the custom path (revert for safety)
sys.path.pop()

# sys.argv is a list of command-line arguments passed to the script
print(sys.argv)

# Safely access command-line arguments with default value
name: str = sys.argv[1] if len(sys.argv) > 1 else "world"
print(f"Hello, {name}!")
