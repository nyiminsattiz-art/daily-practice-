def in_array(array1, array2):
    array2 = " ".join(array2)
    result = []

    for word in array1:
        if word in array2 and word not in result:
            result.append(word)
    return sorted(result)
