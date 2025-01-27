# Write a program that counts the number of words in a given text string. Consider words as sequences of characters separated by spaces or punctuation. Display the list of words.

def countWords(givenString:str):
    count = 0
    
    for word in givenString.split():
        count += 1
        print(word)
        
    return count

givenString = "Hello World"
wordsCount = countWords(givenString)
print(f"Number of words = {wordsCount}")
