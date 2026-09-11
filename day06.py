def check_valid_tr_number(number):
    number = str(number)
    if number[0] == '0':
        return False
    if len(number) != 11 or not number.isdigit():
        return False
    
    sum_even = 0
    sum_odd = 0
    for index, word in enumerate(number[:9]):
        if index % 2 == 0:
            sum_even += int(word)
        else:
            sum_odd += int(word)
    check1 = (sum_even * 7 - sum_odd) % 10 == int(number[9])
    
    total = 0
    for i in number[:10]:
        total += int(i)
    check2 = total % 10 == int(number[10])
    
    return check1 and check2

