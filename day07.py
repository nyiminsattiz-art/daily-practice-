def split_by_mask(strng, mask):
    result = []
    if len(strng) != sum(mask):
        return None
    count = 0
    for i in mask:
        count += i
        word = strng[count - i:count]

        result.append(word)
    return result
