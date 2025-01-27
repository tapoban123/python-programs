# Write a program that converts English text into PigLatin. following the rules: If the word starts with a vowel, "way" is added to the end of the word (e.g., "apple" becomes "appleway"). If the word starts with one or more consonants, those consonants are moved to the end of the word, followed by "ay" (e.g., "banana" becomes "ananabay").

def englishToPiglatin(givenString: str) -> str:
    newString = ""
    vowels = "AEIOU".lower()
    consonants = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower()
    
    for word in givenString.lower().split():
        if word[0] in vowels:
            word += "way"
            newString += word
        elif word[0] in consonants:
            wordChars = [x for x in word]
            firstChar = wordChars.pop(0)
            wordChars.append(firstChar)
            pigLatinWord = "".join(wordChars) + "ay"
            newString += pigLatinWord
        else:
            continue
    
    return newString
            
givenString = "Apple"
print(englishToPiglatin(givenString))