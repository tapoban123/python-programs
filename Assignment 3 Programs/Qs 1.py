# Write a program that checks if a substring exists with in a given string and prints a message indicating whether it was found.


def findSubString(givenString, subString):
    n = len(givenString)
    m = len(subString)

    for i in range(n - m + 1):
        j = 0
        while j < m and givenString[i + j] == subString[j]:
            j += 1

        if j == m:
            return True

    else:
        return False


givenString = "She sells seashells at the seashore."
inputString = input("Enter a string: ")
isSubstring = findSubString(givenString, inputString)

print("Found substring" if isSubstring else "Substring not found.")
