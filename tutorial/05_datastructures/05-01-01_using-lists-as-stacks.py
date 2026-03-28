# Chapter 5.1: More on Lists — list object methods
# Ref: https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print("after appends:", stack)

# pop (LIFO: last-in first-out)
print("pop 7:", stack.pop())
print("stack:", stack)
print("pop 6:", stack.pop())
print("pop 5:", stack.pop())
print("final:", stack)

history = ["google.com", "github.com"]
history.append("stackoverflow.com")
history.append("docs.python.org")
print("history:", history)

current = history.pop()
print("back to:", current, "remaining:", history)
current = history.pop()
print("back to:", current, "remaining:", history)

# Undo
document = "Hello"
changes = []
changes.append("Hello World")
changes.append("Hello Python")
print("changes:", changes)

document = changes.pop()
print("undo to:", document)  # Hello Python
document = changes.pop()
print("undo to:", document)  # Hello World
