# 5)Write a program that takes an integer as input and prints out whether that integer is prime or not.

integer = int(input("Enter a number (integer): "))
list = []
for i in range(1,integer + 1):
    if integer%i == 0:
        list.append(i)
print(list)

if len(list) <= 2:
    print("Prime")
else:
    print("Not a prime")