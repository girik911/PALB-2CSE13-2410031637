def largest_element(arr):
    largest = arr[0]
    
    for num in arr:
        if num > largest:
            largest = num
            
    return largest


# Example
arr = [1, 8, 7, 56, 90]
print(largest_element(arr))
