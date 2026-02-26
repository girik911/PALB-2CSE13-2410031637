def matrix_median(matrix):
    elements = []

    for row in matrix:
        elements.extend(row)

    elements.sort()
    n = len(elements)

    return elements[n // 2]


print(matrix_median([[1,3,5],[2,6,9],[3,6,9]]))
