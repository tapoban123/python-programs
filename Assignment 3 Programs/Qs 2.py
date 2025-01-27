#  Write a program that counts the number of occurrences of all the characters in a given string.

def countChar(givenString):
    charsAndCount = {}
    count = 0
    for c in givenString:
        for char in givenString:
            if c == char:
                count += 1
        charsAndCount[c] = count
        count = 0

    return charsAndCount


givenString = "Hello World"
print(countChar(givenString=givenString))
