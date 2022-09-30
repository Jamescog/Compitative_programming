def countSwaps(a):
    no_of_swaps = 0
    for i in range(len(a)):
        for j in range(len(a) - i -1):
            if a[j] > a[j + 1]:
                a [j], a[j + 1] = a[j + 1], a[j]
                no_of_swaps += 1
    print("Array is sorted in {} swaps.".format(no_of_swaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[len(a) - 1]))  
