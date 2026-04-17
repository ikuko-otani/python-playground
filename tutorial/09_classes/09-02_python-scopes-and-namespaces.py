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


# =============================================================================
# Block 2: Scope and LEGB Rule
# Python searches names in the order: Local → Enclosing → Global → Built-in
# =============================================================================


def outer():
    x = "enclosing"  # Enclosing scope

    def inner():
        x = "local"  # Local scope (shadows enclosing)
        print(f"inner x: {x}")  # -> "local"

    inner()
    print(f"outer x: {x}")  # -> "enclosing"


outer()


# =============================================================================
# Block 3: global statement
# 'global' allows reassignment of a module-level variable inside a function.
# =============================================================================

count = 0  # global variable


def increment():
    global count  # declare global
    count += 1


increment()
increment()
print(f"count after 2 increments: {count}")


# =============================================================================
# Block 4: nonlocal statement
# 'nonlocal' allows reassignment of a variable in the nearest enclosing scope.
# =============================================================================


def make_counter():
    n = 0

    def counter():
        nonlocal n  # declare nonlocal
        n += 1
        return n

    return counter


c = make_counter()
print(c())  # 1
print(c())  # 2
print(c())  # 3


# =============================================================================
# Block 5: Scope and Namespace Example (from official tutorial 9.2.1)
# Demonstrates local / nonlocal / global with do_* nested functions.
# =============================================================================


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam (modified)"

    spam = "test spam"

    do_local()
    print(f"After do_local:    {spam}")
    # "test spam"

    do_nonlocal()
    print(f"After do_nonlocal: {spam}")
    # "nonlocal spam"

    do_global()
    print(f"After do_global:   {spam}")
    # "nonlocal spam" (global changed, not enclosing)


scope_test()
print(f"Global spam after scope_test: {spam}")
# "global spam (modified)"
