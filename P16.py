# 16. Write a program in python that counts the frequency of each character in
# a string.
string = input("Enter string: ")
frequency = {}
for char in string:
    frequency[char] = frequency.get(char, 0) + 1
print(frequency)
