### Write a program that generates the Fibonacci sequence as a list upto a specified number of terms.

num1 = 0
num2 = 1 
my_sum = 0

n = int(input("Enter the number of elements: "))

print(num1, num2, end=" ")

for i in range(n):
    my_sum = num1 + num2
    num1, num2 = num2, my_sum
    
    print(my_sum, end=" ")