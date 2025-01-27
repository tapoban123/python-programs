### Write a program that produces a list of prime numbers.

import math

n = int(input("Enter how many prime numbers you want to generate: "))

prime_numbers = []
isPrime = True

print(f"Among the first {n} numbers, these are the prime numbers: ", end=" ")
for i in range(1, n + 1):
    for j in range(2, round(math.sqrt(i)) + 1):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
