# Chapter 4.8: Defining Functions
# Ref: https://docs.python.org/3/tutorial/controlflow.html#defining-functions


# --- [1] Define a function that PRINTS Fibonacci numbers up to n ---
# The function body is executed only when the function is CALLED, not when defined.
# Calling print() inside a function is convenient for quick output,
# but makes the result hard to reuse (you cannot assign it to a variable).
def fib_print(n):
    """Print Fibonacci series up to n."""
    # Track the two most recent values
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()  # Newline at the end


# Proof that defining alone does nothing — output only appears after the call below
print("--- fib_print ---")
fib_print(100)
# Expected: 0 1 1 2 3 5 8 13 21 34 55 89


# --- [2] Define a function that RETURNS a list of Fibonacci numbers up to n ---
# Returning a value makes the result reusable — assign it, pass it, test it.
# This is the preferred pattern in backend code (FastAPI endpoints, unit tests, etc.).
def fib_list(n):
    """Return a list containing Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result


print("--- fib_list ---")
print(fib_list(100))
# Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


# --- [3a] Comparing functions with and without explicit return ---
# This function has no return statement — Python implicitly returns None
def do_nothing():
    """A function body that does nothing and returns nothing explicitly."""
    pass  # Valid body, but no return


# This function explicitly returns a value
def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}!"


print("--- return / None experiment ---")

# Capture the return value of each
result_nothing = do_nothing()
result_greet = greet("world")

print(f"do_nothing() returned: {result_nothing}")  # None
print(f"greet() returned: {result_greet}")  # Hello, world!
print(f"Type of None result: {type(result_nothing)}")  # <class 'NoneType'


# --- [3b] return with no value also produces None ---
# An early return (no value) is useful for guard clauses in real backend code.
def check_positive(n):
    """Return early if n is not positive; otherwise print confirmation."""
    if n <= 0:
        # Early exit — implicitly returns None
        return
    print(f"{n} is positive!")


print("--- bare return ---")
val_negative = check_positive(-1)
val_positive = check_positive(5)

print(f"check_positive(-1) returned: {val_negative}")  # None
print(f"check_positive(5) returned: {val_positive}")  # None (print is a side effect)


# --- [4a] Functions are first-class objects — assign them to variables ---
# This is the foundation of higher-order functions, callbacks, and dependency injection
# (a common pattern in FastAPI with Depends()).
f = fib_list  # Assign the function object itself (no parentheses!)
print("--- function as object ---")
print(f"f is fib_list: {f is fib_list}")  # True — same object
print(f(50))  # Call fib_list via the alias f
# Expected: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
