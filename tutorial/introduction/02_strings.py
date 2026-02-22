# 3. A Non-Formal Intruduction to Python
# 3.1.2 Strings

strings = []

strings.append('"Isn\'t it a nice day?" they said.')
strings.append("First line.\nSecond line.")

strings.append("This is a backslash: \\")
strings.append("This is a tab:\tSee?")
strings.append("This is a carriage return:\rSee?")
strings.append("This is a vertical tab:\vSee?")
strings.append("This is a form feed:\fSee?")
strings.append("This is a backspace: \bSee?")
strings.append("This is a bell: \aSee?")
strings.append("This is a null character: \0See?")
strings.append("This is a Unicode character: \u03A9See?")  # Omega symbol
strings.append(r"C:\users\name\documents")  # r for raw string, ignores escape sequences

strings.append("""\
This is a multi-line string.
It can contain blank lines and "quotes" without needing to escape them.\
""")

strings.append(3 * "Repeat me! " + "And me too!")  # String multiplication
strings.append("Concatenation: " "Hello, " "world!")  # Adjacent string literals are concatenated
strings.append('This is a long string that'
' spans multiple lines.')  # Adjacent string literals are concatenated even without a backslash

s = "This is a variable."
strings.append(s + " This string is concatenated with a variable.") # String concatenation with a variable by using the + operator

word = "Python"
strings.append(f"This is an f-string. The word is: {word}.")  # f-string allows for embedding expressions inside string literals, using curly braces {}

strings.append(word.upper())  # String method to convert to uppercase
strings.append(word.lower())  # String method to convert to lowercase

strings.append("This is the first character: " + word[0])  # Indexing to get the first character
strings.append("This is the last character: " + word[-1])  # Indexing to get the last character
strings.append("This is a substring: " + word[1:4])  # Slicing to get a substring (characters from index 1 to 3)
strings.append("This is the first three characters: " + word[:3])  # Slicing to get the first three characters
strings.append("This is characters from index 3 to the end: " + word[3:])  # Slicing to get characters from index 3 to the end
strings.append("This is the last two characters: " + word[-2:])  # Slicing to get the last two characters

strings.append("This is every second character: " + word[::2])  # Slicing with a step to get every second character
strings.append("This is the reversed string: " + word[::-1])  # Slicing with a negative step to reverse the string

for letter in "Hello":
    strings.append(letter)  # Iterating over a string gives you each character

for s in strings:
    print(s)

sentence = "This is a sentence with some words."
print(sentence.split())  # Splitting a string into a list of words
print(sentence.split("s"))  # Splitting a string using 's' as the delimiter
print(sentence.split(" ", 2))  # Splitting a string into a list of words, but only at the first 2 occurrences of the delimiter
print(sentence.strip("This."))  # Stripping characters from the beginning and end of the string
print(sentence.replace("s", "X"))  # Replacing all occurrences of 's' with 'X'

print(sentence.find("some"))  # Finding the index of the first occurrence of "some"
print(sentence.find("notfound"))  # Finding a substring that doesn't exist returns -1
print(sentence.startswith("This"))  # Checking if the string starts with "This"
print(sentence.endswith("words."))  # Checking if the string ends with "words."
print(sentence.count("s"))  # Counting the number of occurrences of 's' in the string

print(sentence.join(["This", "is", "a", "joined", "string."]))  # Joining a list of strings into a single string with a separator

# Show the index and the character at that index, as well as the character at the negative index
for i in range(len(sentence)):
    print(i, sentence[i], sentence[-(i+1)])
