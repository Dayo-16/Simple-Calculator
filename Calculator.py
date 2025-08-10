# Minimal calculator — assumes user types valid numbers and operators.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the operation (+, -, *, /): ")

if op == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif op == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif op == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif op == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, /.")
