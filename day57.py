def thirt(n):
    while True:
        total = 0
        for index, digit in enumerate(str(n)[::-1]):
            total += int(digit) * (10 ** index % 13)
            
        if total == n:
            return total
        n = total

