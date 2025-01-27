### Write a program that uses list comprehensions to generate lists of numbers. even numbers, Odd numbers, squares, etc.


n = int(input("Enter the value of n: "))

numbers = [x for x in range(1, n + 1)]
even_numbers = [x for x in range(1, n + 1) if x % 2 == 0]
odd_numbers = [x for x in range(1, n + 1) if x % 2 != 0]
squares = [x**2 for x in range(1, n + 1)]

print(f"Numbers: {numbers}")
print(f"Even numbers: {even_numbers}")
print(f"Odd numbers: {odd_numbers}")
print(f"Squares: {squares}")
