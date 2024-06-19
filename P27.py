# 27. Write a program in python that converts a string into a list of its characters.
def string_to_list(my_string):
    return list(my_string)


input_string = "Hi, I am a student!"
char_list = string_to_list(input_string)
print(f"List of characters: {char_list}")
