def order_word(s):
    if s == None or len(s) == 0:
        return "Invalid String!"
    
    num = []
    result = ""
    for i in s:
        number = ord(i)
        num.append(number)
    
    
    num = sorted(num)

    for i in num:
        result += chr(i)
    return result
    
