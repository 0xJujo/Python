def process_data(data):
    match data:
        case 1:
            print("Processing data for case 1")
        case 2:
            print("Processing data for case 2")
        case 3:
            print("Processing data for case 3")
        case _:
            print("Invalid data")

# Example usage
process_data(1)  # Output: Processing data for case 1
process_data(2)  # Output: Processing data for case 2
process_data(4)  # Output: Invalid data

def print_table(number):
    if number < 1 or number > 10:
        print("Number should be between 1 and 10")
    else:
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")

# Example usage
print_table(5)