# Create a list
my_list = [1, 2, 3, 2, 2, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1

# Modifying elements
my_list[2] = 10
print(my_list)  # Output: [1, 2, 10, 4, 5]

# Appending elements
my_list.append(6)
print(my_list)  # Output: [1, 2, 10, 4, 5, 6]

# Removing elements
my_list.remove = [x for x in my_list if x != 2]
print(my_list)  # Output: [1, 10, 4, 5, 6]

# Inserting elements
my_list.insert(2, 3)
print(my_list)  # Output: [1, 10, 3, 4, 5, 6]

# Sorting elements
my_list.sort()
print(my_list)  # Output: [1, 3, 4, 5, 6, 10]

# Reversing elements
my_list.reverse()
print(my_list)  # Output: [10, 6, 5, 4, 3, 1]