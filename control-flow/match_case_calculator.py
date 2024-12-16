num1 = input("Enter first number:")
num2 = input("Enter second number:")
operation = input("Choose operation (+, -, *, /):")

match operation:
    case '+':
        result = num1 + num2
        print(f"The result is: {result}")
    case '-':
        result = num1 - num2
        print(f"The result is: {result}")
    case '*':
        result = num1 * num2
        print(f"The result is: {result}")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        result = num1 / num2
        print(f"The result is: {result}")
    case _:
        print("Invalid operation.")