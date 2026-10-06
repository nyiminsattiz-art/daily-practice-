def validate(n):
    n = str(n)
    length = len(n)


    lst = []

    if length % 2 == 0:
        for index, i in enumerate(n):
            if index % 2 == 0:
                even = int(i) * 2
                lst.append(even)
            else:
                lst.append(int(i))

    else:
        for index, j in enumerate(n):
            if index % 2 != 0:
                odd = int(j) * 2
                lst.append(odd)
            else:
                lst.append(int(j))

    result = []
    for k in lst:
        if k > 9:
            total = 0
            k = str(k)
            for l in k:
                total += int(l)
            result.append(total)
        else:
            result.append(k)

    total_value = 0
    for number in result:
        total_value += number
    if total_value % 10 == 0:
        return(True)
    else:
        return(False)
    
