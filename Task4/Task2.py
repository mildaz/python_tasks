# 2)Write the program to sort the list (without using sort function). You can implement any algorithm
import string 

### To sort only numbers: ###
# print("SORTING NUMBERS")
# list = [3,6,2,-3,2,9,0,1,9,9,1.1]

# newlist = []
# listB = list[:]

# for i in range(0, len(list)):
#     maxvalue = max(listB)
#     newlist.append(maxvalue)
#     listB.remove(maxvalue)

# print("Sorted number list: ", newlist)

### To sort all characters: ###
text = input("Enter text: ")
textList = text.split()

characters = [i for i in string.printable]
# print(characters)

sortedList = []
for i in characters:
    for b in textList:
        if b[0] == i:
            sortedList.append(b)


for i in sortedList:
    print(i) 
    
#print("Sorted list: ", sortedList)