# Write a program to check whether the input strings are anagrams of each other or not. e.g. listen, silent


def isAnagram(string1: str, string2: str):
    str1Chars = set([x for x in string1])
    str2Chars = set([x for x in string2])
    if (len(string1) == len(string2)) and (str1Chars == str2Chars):
        return True

    return False


string1 = "Hello World"
string2 = "Hello Wrld"

if isAnagram(string1, string2):
    print("Yes, the input strings are anagrams of each other.")
else:
    print("No, the input string are not anagrams of each other.")
