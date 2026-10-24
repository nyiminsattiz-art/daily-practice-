def sort_nested_list(lst):
    flat = []

    for a in lst:
        for b in a:
            for c in b:
                flat.append(c)
    flat.sort()

    index = 0
    result = []

    for a in lst:
        new_a = []
        for b in a:
            new_b = []
            for c in b:
                new_b.append(flat[index])
                index += 1
            new_a.append(new_b)
        result.append(new_a)
    return result
