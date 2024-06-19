# 3. Write a python program that calculates the factorial of a given number.
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)


digit = 5
print(f"The factorial of {digit} is {factorial(digit)}")
