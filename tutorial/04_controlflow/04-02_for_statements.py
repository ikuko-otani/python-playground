words  = ["cat", "window", "defenestrate"]

print("Loop 1: iterate over elsements")
for w in words:
  print(w, len(w))

print("Loop 2: iterate over indices")
for i in range(len(words)):
  print(i, words[i], len(words[i]))

