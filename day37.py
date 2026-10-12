def hamming(a,b):
    count = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            count += 1
    return count

