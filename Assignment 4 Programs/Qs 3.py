def factorial(num: int):
    if num == 1:
        return num
    else:
        return num * factorial(num - 1)


givenNumber = 5
print(factorial(givenNumber))
