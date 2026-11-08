def more_zeros(s):
    result = []
    for ch in s:
        binary = bin(ord(ch))[2:]         
        if binary.count('0') > binary.count('1') and ch not in result:
            result.append(ch)
    return result
