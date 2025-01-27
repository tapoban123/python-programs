# Write a program to find the number of vowels, consonants, digits, whitespaces in the input string.


def findInString(givenString: str):
    vowels = [x for x in "AEIOU"]
    consonants = [x for x in "ABCDEFGHIJKLMNOPQRSTUSWXYZ"]
    digits = str([x for x in range(0, 10)])
    
    vowelCount = 0
    consonantsCount = 0
    digitsCount = 0
    
    data = {}
    
    for char in set([x for x in "".join(givenString.split()).upper()]):
        if char in vowels:
            vowelCount += 1
            data["vowels"] = vowelCount
        elif char in consonants:
            consonantsCount += 1
            data["consonants"] = consonantsCount
        elif char in digits:
            digitsCount += 1
            data["digits"] = digitsCount
            
    
    return data


givenString = "Hello World123"
print(findInString(givenString=givenString)) 
    
