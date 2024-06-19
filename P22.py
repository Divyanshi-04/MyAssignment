# 22. Write a python program that returns the minimum and maximum
# values in a list of numbers.
def find_min_max(lst):
    return min(lst), max(lst)


my_numbers = [10, 5, 8, 3, 15]
min_val, max_val = find_min_max(my_numbers)
print(f"Minimum value: {min_val}, Maximum value: {max_val}")
