def sum_dig_pow(a, b): 
    result = []
    for num in range(a, b + 1):
        if num < 10:
            result.append(num)
        else:
            digits = str(num)
            sum_num = 0
            for position, digits in enumerate(digits):
                sum_num += int(digits) ** (position + 1)
            if sum_num == num:
                result.append(num)
    return result

