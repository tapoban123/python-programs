### Write a program that reverses the order of elements in a given list without using the built-in reverse() function.

userInput = list(
    map(int, input("Enter the elements to be reversed separated by a space: ").split())
)

print(f"Input list: {userInput}")
print(f"Reversed list: {userInput[::-1]}")
