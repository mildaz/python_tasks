age = int(input("What is your age: "))
d_licence = input("Do you have a driver licence? (yes/no): ")

if age >= 18 and d_licence == "yes":
    answer = True
else:
    answer = False
print("You are able to drive: " + str(answer))
