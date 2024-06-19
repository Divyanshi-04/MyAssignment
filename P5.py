# 5. Write a program that takes a string input from the user and writes it to a text file
text = input("Enter some text: ")
with open('user_input.txt', 'w') as file:
    file.write(text)
