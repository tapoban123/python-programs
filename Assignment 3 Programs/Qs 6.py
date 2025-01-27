# Write a program that check if the input sentence is palindromeor not, ignoring spacing, punctuation and capital. e.g. never odd or even, no lemon, no melon, My gym.

def isPallindrome(givenString:str):
    if ("".join(givenString.split()).lower()[::-1] == "".join(givenString.split()).lower()):
        return True

    return False

givenString = "Never odd or even"

if isPallindrome(givenString):
    print("Given String is Pallindrome")
else:
    print("Given String is not Pallindrome")