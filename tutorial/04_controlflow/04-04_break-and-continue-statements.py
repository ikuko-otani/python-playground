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


# Linear search with break
# Find the first target value and stop immediately
def find_first(nums: list, target: int) -> int:
    """Return the index of the first occurrence of target, or -1 if not found."""
    for i, num in enumerate(nums):
        if num == target:
            return i  # return is preferred over break
    return -1


# Skip invalid values with continue
# Sum only positive numbers, ignoring non-positive ones.
def sum_positives(nums: list) -> int:
    """Return the sum of positive numbers in the list"""
    total = 0
    for num in nums:
        if num <= 0:
            continue
        total += num
    return total


# --- Quicke smoke tests ---
print(find_first([3, 1, 4, 1, 5], 4))  # Expected: 2
print(find_first([3, 1, 4, 1, 5], 9))  # Expected: -1
print(sum_positives([1, -2, 3, 0, 5]))  # Expected: 9
