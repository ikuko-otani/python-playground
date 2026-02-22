# 3. A Non-Formal Intruduction to Python
# 3.1.1 Numbers
print(2+2)
print(50 - 5*6)
print((50 - 5*6) / 4)

print(7/3)      # float
print(7 // 3)   # floor division
print(7 % 3)    # modulo

print(2 ** 10)  # exponentiation

nums = [1, 2, 3, 4]
n = len(nums)
print("len(nums) = ", n)

print(4 * 3.75 - 1)

tax = 12.5 / 100
price = 100.50
price += price * tax
print(price)  # assignment operator
print(round(price, 2))
