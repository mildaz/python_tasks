### 1)Write a program that takes a user input (an integer) 
### and determines whether it is positive, negative, or zero.

number = int(input("Enter a number (integer): "))

if number > 0:
    print("Number is positive")
elif number < 0:
    print("Number is negative")
else:
    print("Number is zero")
