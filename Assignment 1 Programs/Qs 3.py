### Write a Python program to display Fibonacci series upto n numbers.

val1 = 0
val2 = 1
sum = 0

userInput = int(input("Enter the value of n: "))

if userInput < 1:
    print("Invalid value of n.")

elif userInput == 1:
    print(val1)

elif userInput >= 2:
    print(val1, val2, end=" ")

    if userInput >= 3:
        for i in range(userInput - 2):
            sum = val1 + val2
            val1 = val2
            val2 = sum

            print(sum, end=" ")
