def binarySearch(arr, key, start, end):
    # start = 0
    # end = 0
    mid = 0

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binarySearch(arr, key, start, mid - 1)
        elif arr[mid] < key:
            return binarySearch(arr, key, mid + 1, end)

    return -1


arr = [x for x in range(1, 21)]
print(binarySearch(arr, 90, 0, len(arr)))
