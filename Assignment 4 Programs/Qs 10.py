# Write a program that calculates the average of a variable number of values passed as arguments to a function.


def average(values: list):
    valuesSum = 0

    for x in values:
        valuesSum += x
    return valuesSum / len(values)

values = list(map(int, input("Enter the values separated by a space: ").split()))
print(f"Average = {average(values)}")
