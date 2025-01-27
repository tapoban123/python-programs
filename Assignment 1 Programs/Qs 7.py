### Write a Python program to check a given number a palindrome or not.

userInput = int(input("Enter a number: "))

inputValue = userInput
eachEle = 0
reversedValue = 0

while (inputValue > 0):
    eachEle = inputValue % 10
    reversedValue += eachEle
    inputValue = (inputValue - eachEle) // 10

    if inputValue > 0:
        reversedValue *= 10

if (reversedValue == userInput):
    print(f"{userInput} is a Pallindrome number.")

else:
    print(f"{userInput} is not a Pallindrome number.")