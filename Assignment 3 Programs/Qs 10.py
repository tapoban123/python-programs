# Write a program that implement a simple Caesar cipher encryption and decryption program that works on strings.

def caesarCipher(givenString: str, shift: int):
    alphabets = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    encryptedString = ""
    
    for char in givenString:
        if char.isspace():
            encryptedString += char
        else:            
            charNo = alphabets.index(char)
            encryptedString += alphabets[charNo+ shift] 
        
        
    