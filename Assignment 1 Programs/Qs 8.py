### Write a Python program to find the sum Of the following series.
# x - x3/3! + x5/5! - ... n terms

### Also print the value Of the sin(x) from math module and verify the result.

import math

xInput = float(input("Enter the value of x: "))
nInput = int(input("Enter the value of n: "))

term = xInput
my_sum = 0

for i in range(1, nInput + 1):
    my_sum += term
    term = (-term * xInput ** 2) / ((2 * i) * (2 * i + 1))
    
print(my_sum)
print(math.sin(xInput))