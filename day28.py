def order_weight(strng):
    strng = strng.split()
    pair = []

    for word in strng:
        total = 0
        for char in word:
            total += int(char)
        pair.append((total, word))

    pair.sort()
    result = ""
    for total, word in pair:
        result += word + " "
    return result[:-1]
