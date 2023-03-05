year = int(input("Enter year: "))

if (year % 400 == 0):
    print("Both numbers are even: True")
elif(year % 4 == 0) and (year % 100 != 0):
    print("Both numbers are even: True")
else:
    print("Leap year : False")

