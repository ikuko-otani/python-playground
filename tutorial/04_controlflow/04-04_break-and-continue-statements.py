# break exits the innermost loop immediately.

for n in range(2, 10):
    print("n:", n)
    for x in range(2, n):
        print("x:", x)
        if n % x == 0:
            print(f"{n} equals {x} * {n // x}")
            break  # stop checking once a divisor is found
