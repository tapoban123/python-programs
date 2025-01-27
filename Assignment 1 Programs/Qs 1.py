### Write a Python to find the factorial of a given input number.

userInput = int(input("Enter a number: "))

value = 1

for i in range(1, userInput + 1):
    value *= i

print(f"The factorial of {userInput} = {value}")