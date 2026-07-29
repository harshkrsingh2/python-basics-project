
def calculator():
    operation = input("Enter operation (add, subtract, multiply, divide): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Invalid operation"

print(calculator())


