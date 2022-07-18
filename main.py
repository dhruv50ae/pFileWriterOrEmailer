
PLACEHOLDER = "[name]"


with open("myFile.txt") as namesFile:
    names = namesFile.readlines()
    print(names)

with open("newFile.txt") as letterFile:
    letterContents = letterFile.read()
    for name in names:
        strippedName = name.strip()
        newLetter = letterContents.replace(PLACEHOLDER, strippedName)
        print(newLetter)
        with open(f"./send/letterFor{strippedName}.txt", mode="w") as completedLetter:
            completedLetter.write(newLetter)