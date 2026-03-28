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
