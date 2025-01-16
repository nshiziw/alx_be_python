def division(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return x / y

print(division(3, 1))