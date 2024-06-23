try:
    # Code that may raise an exception
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    
    result = num1 / num2
    print("Result:", result)
    
except ValueError:
    print("Invalid input. Please enter a valid number.")
    
except ZeroDivisionError:
    print("Cannot divide by zero.")
    
except Exception as e:
    print("An error occurred:", e)