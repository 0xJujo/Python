# # Open a file in write mode
# file = open("example.txt", "w")

# # Write content to the file
# file.write("Hello, World!")
# file.write("\nThis is a sample file.")

# # Close the file
# file.close()

# # Open the file in read mode
# file = open("example.txt", "r")

# # Read and print the contents of the file
# content = file.read()
# print(content)

# # Close the file
# file.close()

# Open a file in write mode
with open("example.txt", "w") as file:
    # Write content to the file
    file.write("Hello, World!")
    file.write("\nThis is a sample file.")

# Open the file in read mode
with open("example.txt", "r") as file:
    # Read and print the contents of the file
    content = file.read()
    print(content)