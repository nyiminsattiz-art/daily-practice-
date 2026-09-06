def square_or_square_root(arr):
    result = []
    for i in arr:
        root = round(i ** 0.5)
        if root * root == i:
            result.append(round(i ** 0.5))
        else:
            result.append(i ** 2)
    return result
