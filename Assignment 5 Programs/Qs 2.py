def createCharCountDict(inputString: str):
    charCountDict = {x: [y for y in inputString].count(x) for x in set(y for y in inputString)}
    return charCountDict

userInput = input("Enter a string: ")
print(createCharCountDict(userInput))