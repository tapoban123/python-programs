# Write a conversion program to convert decimal to binary and binary to decimal using functions.


def decimalToBin(binary):
    decimal, i = 1, 0
    temp = 0
    while binary != 0:
        temp = binary % 10
        if temp != 0:
            decimal += i ** 2
        binary //= 10
        i += 1
    return decimal


def binaryToDecimal(number):
    return format(number, "b")


print(decimalToBin(101))
print(binaryToDecimal(5))
