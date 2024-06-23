# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements in a tuple
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3

# Tuple methods
print(len(my_tuple))  # Output: 5
print(my_tuple.count(3))  # Output: 1
print(my_tuple.index(4))  # Output: 3

# Modifying a tuple (not directly possible)
# But you can convert it to a list, modify, and convert back to a tuple
my_list = list(my_tuple)
my_list[0] = 10
my_tuple = tuple(my_list)
print(my_tuple)  # Output: (10, 2, 3, 4, 5)