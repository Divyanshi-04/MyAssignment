# 24. Write a program that acts as a simple calculator. It should take
# two numbers and an operator (+, -, *, /) as input and print the result.
def calculator(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter an operator (+, -, *, /): ")
result = calculator(num1, num2, op)
print(f"Result: {result}")
