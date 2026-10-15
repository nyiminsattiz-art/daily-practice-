def min_value(digits):
    result = []

    for number in digits:
        if number not in result:
            result.append(number)
        
    result = sorted(result)
    final = ""
    for i in result:
        final += str(i)
    return int(final)
        

