# break exits the innermost loop immediately.

for n in range(2, 10):
    print("n:", n)
    for x in range(2, n):
        print("x:", x)
        if n % x == 0:
            print(f"{n} equals {x} * {n // x}")
            break  # stop checking once a divisor is found

# continue skips the rest of the current iteration and moves to the next.

for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}")
        continue  # skip the odd-number print for even numbers
    print(f"Found an odd number {num}")
