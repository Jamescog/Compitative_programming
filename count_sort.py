def countingSort(arr):
    frequency = []
    for i in range(100):
        frequency.append(arr.count(i))
    return frequency
