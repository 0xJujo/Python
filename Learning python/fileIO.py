# Open a file in write mode
file = open("example.txt", "w")

# Write content to the file
file.write("Hello, World!")
file.write("\nThis is a sample file.")

# Close the file
file.close()

# Open the file in read mode
file = open("example.txt", "r")

# Read and print the contents of the file
content = file.read()
print(content)

# Close the file
file.close()