# 19. Write a python program that removes all punctuation from a given string
import string


def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))


user_input = input("Enter a string: ")
result = remove_punctuation(user_input)
print("String after removing punctuation:", result)
