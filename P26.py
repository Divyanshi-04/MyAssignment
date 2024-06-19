# 26. Write a program in python that checks if a string starts with a given
# prefix or ends with a given suffix.
def check_prefix_suffix(my_string, prefix, suffix):
    return my_string.startswith(prefix), my_string.endswith(suffix)


input_string = "Hi, I am a student!"
prefix_to_check = "Hi"
suffix_to_check = "student!"
starts_with, ends_with = check_prefix_suffix(input_string, prefix_to_check, suffix_to_check)
print(f"Starts with '{prefix_to_check}': {starts_with}")
print(f"Ends with '{suffix_to_check}': {ends_with}")
