# 1)Ask the user to enter the text and a letter. Count how many occurrences of the letter provided. 


text = input("Enter text: ").lower()
textList = [i for i in text]
#print(textList)
letter = input("Enter letter: ").lower()


countFound = 0
for i in range(0, len(textList)):
    if textList[i] == letter:
        countFound += 1

print("Letter ", letter, "occurrences: ", countFound)