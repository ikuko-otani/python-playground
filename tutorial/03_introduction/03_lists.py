# 3.1.3 Lists

squares = [1, 4, 9, 16, 25] # A list of the first five square numbers
print(squares)
print(squares[0])
print(squares[-1])  # Negative indexing
print(squares[-3:])  # Slicing a list

print(sum(squares))
print(max(squares), min(squares))

squares += [36, 49, 64, 81, 100]  # Concatenating lists
print(squares)

cubes = [1, 8, 27, 65, 125]  # Something's wrong here
print(cubes)
cubes[3] = 4 ** 3  # Fix the wrong value (4 cubed is 64)
print(cubes)

cubes.append(6 ** 3)  # Add the cube of 6 to the list

for i in range(7, 11):
    cubes.append(i ** 3)
print(cubes)

rgb = ['red', 'green', 'blue']
rgba = rgb
print(id(rgb) ==id(rgba))  # rgb and rgba refer to the same list
rgba.append('alpha')
print(rgb)  # rgb is changed too, because rgb and rgba are the same list

rgba_shallow_copy = rgb[:]  # Make a copy of the list
print(id(rgb) == id(rgba_shallow_copy))  # rgb and rgba_shallow_copy are different lists
rgba_shallow_copy[-1] = 'gamma'  # Change the last element of rgba_shallow_copy
print(rgb)  # rgb is not changed, because rgb and rgba_shallow_copy are different lists  
print(rgba_shallow_copy)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(len(letters))
print(letters[2:5])  # Slicing a list
letters[2:6] = ['C', 'D', 'E', 'F']  # Replace a slice with a different sized list
print(letters)

letters[2:6] = []  # Remove a slice
print(letters)

letters_copy = letters[:]
letters_copy[2:2] = ['X', 'Y', 'Z']  # Insert elements at index 2
print(letters_copy)

letters_copy = letters[:]
letters_copy[2:] = ['X', 'Y', 'Z']  # Replace a slice from index 2 to the end with a different sized list
print(letters_copy)

letters_copy = letters[:]
letters_copy[:2] = ['X', 'Y', 'Z']  # Replace a slice from the beginning to index 2 with a different sized list
print(letters_copy)

letters[:] = []  # Clear the list
print(letters)

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]  # A list of lists
print(x)
print(x[0])
print(x[1][2])

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
for row in matrix:
    for value in row:
        print(value, end=" ")
