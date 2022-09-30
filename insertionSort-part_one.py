def insertionSort1(n, arr):
    unsorted = arr[n - 1]
    i = n - 1
    while i > 0 and arr[i - 1] > unsorted:
        arr[i] = arr[i - 1]
        print(*arr)
        i -= 1
    arr[i] = unsorted
    print(*arr)
