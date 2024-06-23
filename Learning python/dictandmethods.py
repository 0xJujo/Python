# Create a dictionary
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}

# Accessing values in the dictionary
print(student["name"])  # Output: John
print(student.get("age"))  # Output: 20

# Modifying values in the dictionary
student["grade"] = "B"
print(student)  # Output: {'name': 'John', 'age': 20, 'grade': 'B'}

# Adding new key-value pairs to the dictionary
student["city"] = "New York"
print(student)  # Output: {'name': 'John', 'age': 20, 'grade': 'B', 'city': 'New York'}

# Removing a key-value pair from the dictionary
del student["age"]
print(student)  # Output: {'name': 'John', 'grade': 'B', 'city': 'New York'}

# Checking if a key exists in the dictionary
if "grade" in student:
    print("Grade:", student["grade"])  # Output: Grade: B

# Getting the number of key-value pairs in the dictionary
print("Number of items:", len(student))  # Output: Number of items: 3

# Getting a list of all keys in the dictionary
keys = student.keys()
print("Keys:", keys)  # Output: Keys: dict_keys(['name', 'grade', 'city'])

# Getting a list of all values in the dictionary
values = student.values()
print("Values:", values)  # Output: Values: dict_values(['John', 'B', 'New York'])


# Printing all key-value pairs in the dictionary
for key, value in student.items():
    print(key, ":", value)
    
# Clearing all key-value pairs from the dictionary
student.clear()
print(student)  # Output: {}
