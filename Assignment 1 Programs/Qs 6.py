### Write a Python program to print the following number pattern using loop.
# *
# * *
# * * *
# * * * *
# * * * * *

userInput = int(input("Enter number of lines: "))

for i in range(1, userInput + 1):
    for _ in range(i):
        print("*", end=" ")

    print(end="\n")
