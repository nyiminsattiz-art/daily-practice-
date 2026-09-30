def rev_rot(strng, sz):
    if sz <= 0:
        return ""
    new_strng = ""

    for index, number in enumerate(strng):
        if (index + 1) % sz == 0:
            new_strng += number + " "
        else:
            new_strng += number
    new_strng = new_strng.split(" ")


    total = 0
    result = ""

    for data in new_strng:
        if len(data) != sz:
            continue
        for number in data:
            total += int(number)
        if total % 2 != 0:
            data = data[1:] + data[0]
            result += data
            total = 0
        else:
            data = data[::-1]
            result += data
            total = 0
    return result
