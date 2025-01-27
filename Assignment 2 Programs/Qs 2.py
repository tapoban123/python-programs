### Write a program that sorts a list of numbers in ascending order using bubble sorting algorithm.

givenList = list(map(int, input("Enter numbers separated by space: ").split()))

unsorted = False

for i in range(0, len(givenList) + 1):
    for j in range(0, len(givenList) - i - 1):
        if givenList[j] > givenList[j + 1]:
            givenList[j], givenList[j + 1] = givenList[j + 1], givenList[j]
            unsorted = True

    if not unsorted:
        break

print(givenList)
