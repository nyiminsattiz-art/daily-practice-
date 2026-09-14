def dig_pow(n, p):
    total = 0
    exponent = p

    for number in str(n):
        total += int(number) ** exponent
        exponent += 1
    
    if total % n == 0:
        return total // n
    else:
        return -1
