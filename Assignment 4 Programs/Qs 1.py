def findMean(numbers: list[int | float]):
    numbersSum = 0
    for num in numbers:
        numbersSum += num

    return numbersSum / len(numbers)


def findMedian(numbers: list[int | float]):
    n = len(numbers)
    numbers.sort()
    return numbers[(n + 1) / 2] if n % 2 != 0 else ((numbers[n // 2] + numbers[n // 2 + 1]) // 2)


def findMode(numbers: list[int | float]):
    return 3 * findMedian(numbers) - 2 * findMean(numbers)


numbers = list(map(float, input("Enter the elements separated by a space: ").split()))

print(
    f"Mean = {findMean(numbers)}",
    f"Median = {findMedian(numbers)}",
    f"Mode = {findMode(numbers)}",
    sep="\n",
)
