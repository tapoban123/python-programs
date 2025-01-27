# Write a program to check whether the input email-ID is validor not.The common rules for a valid email address: No spaces,no special characters except(@ hyphens(-), and periods(.), can consist of letters(a-z,A-Z),digits(0-9).


def isEmailValid(givenEmail):
    for char in givenEmail:
        if char not in [
            "@",
            "-",
            ".",
            *[x for x in "abcdefghijklmnopqrstuvwxyz"],
            *[x for x in "0123456789"],
        ]:
            return False

    return True


givenEmail = "hello@gmail.com"

if isEmailValid(givenEmail):
    print("Email is Valid")
else:
    print("Email is Invalid")
