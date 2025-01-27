### Write a Python program to check whether a given input number is a prime number or not.

userInput = int(input("Enter a number: "))

for i in range(2, userInput):
    if (userInput % i == 0):
        print(f"{userInput} is not a Prime number.")
        break
else:
    print(f"{userInput} is a Prime number.")