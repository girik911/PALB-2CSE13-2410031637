def kth_smallest(arr, k):
    arr.sort()
    return arr[k - 1]


# Example
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(kth_smallest(arr, k))
