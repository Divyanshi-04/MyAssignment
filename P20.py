# 20. Write a python program that takes a list of numbers and returns their
# sum
def calculate_sum(numbers):
    return sum(numbers)


try:
    input_numbers = input("Enter a list of numbers (separated by spaces): ")
    numbers_list = [float(num) for num in input_numbers.split()]
    result = calculate_sum(numbers_list)
    print(f"The sum of the numbers is: {result:.2f}")
except ValueError:
    print("Invalid input. Please enter valid numeric values.")

