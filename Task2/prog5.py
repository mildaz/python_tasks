# valid time period: From 01.01.0000 till 31.12.9999

#day = int(print("Enter day of the month (dd/mm/yyyy): "))
#month = int(print("Enter month (dd/mm/yyyy)"))
#year = int(print("Enter year (dd/mm/yyyy)"))

import datetime

inputDate = input("Enter the date in format 'dd/mm/yyyy' : ")

day, month, year = inputDate.split('/')

print(day)
print(month)
print(year)


isValidDate = True
try:
   datetime.datetime(int(year), int(month), int(day))
except ValueError:
    isValidDate = False

if(isValidDate):
    print("Date valid : True")
else:
    print("Date valid : False")
