# 3)Write a program that takes an integer as input and prints out all the factors of that integer.

integer = int(input("Enter a number (integer): "))

for i in range(1,integer + 1):
    if integer%i == 0:
        print(i)