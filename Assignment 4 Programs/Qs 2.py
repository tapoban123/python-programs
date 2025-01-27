def isPrime(number: int):
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True


givenNumber = 5
if isPrime(givenNumber):
    print(f"{givenNumber} is a Prime number.")
else:
    print(f"{givenNumber} is not Prime.")
