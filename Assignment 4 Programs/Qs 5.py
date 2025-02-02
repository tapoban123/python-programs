# Write a function to compute the LCM of two numbers.


def hcf(num1: int, num2: int):
    minNum = min(num1, num2)

    while minNum:
        if num1 % minNum == 0 and num2 % minNum == 0:
            break
        minNum -= 1

    return minNum


def lcm(num1: int, num2: int):
    return (num1 * num2) / hcf(num1, num2)


print("LCM of 15 and 20 =" + lcm(15, 20))
