def merge_sorted_arrays(a, b):
    n = len(a)
    m = len(b)
    
    for i in range(n):
        if a[i] > b[0]:
            a[i], b[0] = b[0], a[i]
            
            # Reorder b[]
            first = b[0]
            j = 1
            while j < m and b[j] < first:
                b[j - 1] = b[j]
                j += 1
            b[j - 1] = first
    
    return a, b
