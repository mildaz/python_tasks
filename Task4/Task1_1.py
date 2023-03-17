# 1)Ask the user to enter the text and a letter. Count how many occurrences of the letter provided. 
# 1.1) Based on the task 1, count the occurrences of each character in the text provided and display them in the output

text = input("Enter text: ").lower()
textList = [i for i in text]
print(textList)

### THIS CODE WORKS:
# #invalidList = ["", "-", ".", ",", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(invalidList)
# uniqueText = []
# for i in textList:
#     if i == " " or i == "-" or i == "." or i == ",":
#         continue
#     if i not in uniqueText:
#         uniqueText.append(i)
# print(uniqueText)

# for i in uniqueText:
#     print("Letter ", i, "occurrences: ", end="")
#     countFound = 0
#     for b in range(0, len(textList)):
#         if textList[b] == i:
#             countFound += 1
#     print(countFound)
#     print()


## THIS COULD BE BETTER VERSION WITH LIST OF INVALID CHARACTERS TO CHECK
## PROBLEM WITH LOOP CHECKING CHARACTERS
invalidList = ["", "-", ".", ",", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(invalidList)
uniqueText = []
for i in textList:
    for name in invalidList:
        if i == name:
            break # not sure how to do this so it works
    if i not in uniqueText:
        uniqueText.append(i)
print(uniqueText)

for i in uniqueText:
    print("Letter ", i, "occurrences: ", end="")
    countFound = 0
    for b in range(0, len(textList)):
        if textList[b] == i:
            countFound += 1
    print(countFound)
    print()

