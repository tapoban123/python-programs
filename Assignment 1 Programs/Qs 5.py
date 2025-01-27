### Write a Python program to calculate the sum Of all numbers from 1 to a given number.

userInput = int(input("Enter the value of n: "))

sum = 0

for i in range(1, userInput + 1):
    sum += i

print(f"The sum of all the numbers from 1 to {userInput} = {sum}")
