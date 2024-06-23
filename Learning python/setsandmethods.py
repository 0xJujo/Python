# Create a set
fruits = {"apple", "banana", "orange"}

# Print the set
print(fruits)  # Output: {'banana', 'orange', 'apple'}

# Add an element to the set
fruits.add("grape")
print(fruits)  # Output: {'banana', 'orange', 'apple', 'grape'}

# Remove an element from the set
fruits.remove("banana")
print(fruits)  # Output: {'orange', 'apple', 'grape'}

# Check if an element is in the set
print("apple" in fruits)  # Output: True
print("mango" in fruits)  # Output: False

# Get the length of the set
print(len(fruits))  # Output: 3

# Iterate over the set
for fruit in fruits:
    print(fruit)

# Clear the set
fruits.clear()
print(fruits)  # Output: set()