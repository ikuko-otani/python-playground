# Chapter 5.1.2: Using Lists as Queues
# Ref: https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-queues

# --- [1] WHY list is inefficient as a queue ---
# Inserting or removing from the LEFT end of a list requires Python
# to shift every remaining element — O(n) time complexity.
# This becomes a performance bottleneck in real backend processing pipelines.
bad_queue = ["first", "second", "third"]

# Enqueue: append to the right (OK — O(1))
bad_queue.append("fourth")

# Dequeue: pop from the LEFT — THIS IS SLOW for large lists (O(n))
first_out = bad_queue.pop(0)

print(f"[1] Dequeued: {first_out}")  # first
print(f"[1] Remaining: {bad_queue}")  # ['second', 'third', 'fourth']
print(f"[1] FIFO order preserved? Yes, but pop(0) is O(n) — avoid in production!")

# --- [2] The RIGHT way: collections.deque ---
# deque (double-ended queue) supports O(1) appends AND poplefts.
# This is the standard library solution for implementing queues in Python.

from collections import deque

# Initialize a queue with initial items
queue = deque(["Eric", "John", "Michael"])
print(f"[2] Initial queue: {queue}")
queue.append("Terry")
queue.append("Graham")
print(f"[2] After enqueue Terry and Graham: {queue}")

# --- [3] Dequeue: remove from the left end — O(1) ---
# popleft() is the key advantage of deque over list.pop(0).
# Always use popleft() for FIFO queue operations.

first_out = queue.popleft()
second_out = queue.popleft()

print(f"[3] First dequeued: {first_out}")  # Eric
print(f"[3] Second dequeued: {second_out}")  # John
print(f"[3] Remaining queue: {queue}")  # deque(['Michael', 'Terry', 'Graham'])

# --- [4] Additional deque operations useful in interviews ---
# appendleft / extendleft allow efficient manipulation at BOTH ends.
# maxlen parameter creates a bounded queue — useful for sliding window problems.

demo = deque([1, 2, 3])

# appendleft: add to the LEFT end — O(1)
demo.appendleft(0)
print(f"[4] After appendleft(0): {demo}")  # deque([0, 1, 2, 3])

# rotate: rotate n steps to the right (negative = left)
demo.rotate(1)
print(f"[4] After rotate(1): {demo}")  # deque([3, 0, 1, 2])
demo.rotate(-2)
print(f"[4] After rotate(-2): {demo}")  # deque([1, 2, 3, 0])

# maxlen: bounded deque — oldest item is dropped automatically when full
bounded = deque([1, 2, 3], maxlen=3)
bounded.append(4)
print(f"[4] Bounded deque after append(4): {bounded}")  # deque([2, 3, 4], maxlen=3)
