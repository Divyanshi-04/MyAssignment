# 11. Write a python program that generates the first n numbers in the Fibonacci sequence.
n = int(input("Enter n: "))
a, b = 0, 1
for _ in range(n):
    print(a, end=' ')
    a, b = b, a + b
