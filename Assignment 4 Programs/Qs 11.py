# Write a password validation program that checks if a given password meets certain
# criteria (e.g. at least 8 characters, one capital case, one lower case, one numeric and
# one special character). Use a nested function to validate each criterion separately


def validatePassword(password: str) -> bool:
    has8chars = False
    hasLower = False
    hasUpper = False
    hasSpecialChar = False
    hasDigit = False

    if len(password) >= 8:
        has8chars = True
        for char in password:
            if char.islower():
                hasLower = True
            elif char.isupper():
                hasUpper = True
            elif char.isdigit():
                hasDigit = True
            elif not char.isalnum():
                hasSpecialChar = True

    if hasSpecialChar and hasDigit and has8chars and hasLower and hasUpper:
        return True
    else: 
        return False


password = input("Enter a password: ")
if validatePassword(password):
    print("Password is valid.")
else:
    print("Password is invalid.")
    
