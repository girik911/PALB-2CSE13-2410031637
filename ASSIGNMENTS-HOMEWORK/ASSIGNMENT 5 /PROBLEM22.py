def smallest_subarray(arr, x):
    n = len(arr)
    min_length = n + 1
    curr_sum = 0
    start = 0

    for end in range(n):
        curr_sum += arr[end]

        while curr_sum > x:
            min_length = min(min_length, end - start + 1)
            curr_sum -= arr[start]
            start += 1

    return 0 if min_length == n + 1 else min_length


# Example
print(smallest_subarray([1,4,45,6,0,19], 51))
