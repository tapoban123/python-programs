### Write a Python program to find the reverse Of a given integer number.

userInput = int(input("Enter a integer: "))

eachEle = 0
inputValue = userInput
reversedValue = 0

while (inputValue != 0):
    eachEle = inputValue % 10
    reversedValue += eachEle
    inputValue = (inputValue - eachEle) // 10

    if inputValue > 0:
        reversedValue *= 10

print(f"{userInput} reversed to {reversedValue}")
