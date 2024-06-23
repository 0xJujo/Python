name = "Nishit"
num = "42"

# Accessing characters in a string
print(name[0:4])  # Output: Nish

# String concatenation
full_name = name + " Prabhu"
print(full_name)  # Output: Nishit Prabhu

# String length
print(len(name))  # Output: 6

# Converting to uppercase and lowercase
print(name.upper())  # Output: NISHIT
print(name.lower())  # Output: nishit

# Checking if a string starts or ends with a specific substring
print(name.startswith("N"))  # Output: True
print(name.endswith("t"))  # Output: True

# Finding the index of a substring
print(name.index("sh"))  # Output: 3

# Replacing substrings
new_name = name.replace("it", "ab")
print(new_name)  # Output: Nishab

# Splitting a string into a list of substrings
sentence = "Hello, how are you?"
words = sentence.split(" ")
print(words)  # Output: ['Hello,', 'how', 'are', 'you?']

# Joining a list of strings into a single string
new_sentence = " ".join(words)
print(new_sentence)  # Output: Hello, how are you?

