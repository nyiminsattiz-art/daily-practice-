def multiplication_table(size):
    result = []

    start = 1
    for i in range(1, size + 1):
        lst = []
        for j in range(start, (size * start) + 1, start):
            lst.append(j)
        start += 1
        result.append(lst)
    return result
