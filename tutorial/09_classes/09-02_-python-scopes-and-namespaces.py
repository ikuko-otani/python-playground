# Chapter 9.2: Python Scopes and Namespaces
# Ref: https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces

# =============================================================================
# Block 1: What is a Namespace?
# A namespace is a mapping from names to objects (implemented as a dict).
# =============================================================================

# Built-in namespace: always available
print(abs(-5))  # built-in function
print(len([1, 2, 3]))  # built-in function

# Global namespace: defined at module level
spam = "global spam"
print(spam)
