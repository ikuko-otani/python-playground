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
