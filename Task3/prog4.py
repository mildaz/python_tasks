"""
4)Create calculator:
  Ask user to provide 2 numbers and one operation to be performed (*,/,+.- or %). If the operation 
  provided does not match one of these, the program should print 
  "Operation provided isn't valid, please,try again" - in this case, the program should
  ask for the operation to be provided again
"""

num1 = float(input("Enter a number: "))
num2 = float(input("Enter another number: "))

while True:
        operation = input("Enter one of the following operations (*,/,+.- or %): ")
        if operation == "*":
                result = num1 * num2
        elif operation == "/":
                result = num1 / num2
        elif operation == "+":
                result = num1 + num2
        elif operation == "-":
                result = num1 - num2
        elif operation == "%":
                result = num1 % num2
        else:
                print("Operation is not correct")
                continue
        print("Result is " + str(result))
        break






