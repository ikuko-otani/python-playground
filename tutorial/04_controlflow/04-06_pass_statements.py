# 04-06_pass_statements.py
# 4.6 pass Statements
# Ref: https://docs.python.org/3/tutorial/controlflow.html#pass-statements

# --- [1] Busy-wait loop: does nothing until keyboard interrupt ---
# This is the most common textbook example of pass.
# In real backend code, you would rarely write this;
# use asyncio or event-driven patterns instead.

# Uncomment to try (stop with Ctrl+C):
# while True:
#     pass  # Busy-wait for keyboard interrupt (Ctrl+C)

print("[1] Busy-wait loop: see commented-out code above")
