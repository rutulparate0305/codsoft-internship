def calculator():
    # Input of two Numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Selecting the operation
    operation = input("Choose an operation (+, -, *, /): ")
    
    # Calculation logic
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Invalid operation selected."
    
    # Displaying the result
    return f"The result of {num1} {operation} {num2} is {result}"

# Run the calculator function
print(calculator())