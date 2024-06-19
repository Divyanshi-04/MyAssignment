# 23. Write a program that converts temperature from Celsius to
# Fahrenheit and vice versa based on user input.
def celsius_to_fahrenheit(celsius):
    return (9/5) * celsius + 32


def fahrenheit_to_celsius(fahrenheit):
    return (5/9) * (fahrenheit - 32)


celsius_temp = 45
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C is equivalent to {fahrenheit_temp:.2f}°F")
