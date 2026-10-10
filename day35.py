def twos_difference(lst): 
    lst = sorted(lst)
    result = []

    start = 1
    for number in lst:
        for i in lst[start:]:
            if abs(number - i) == 2:
                result.append((number, i))
        start += 1
    return result

