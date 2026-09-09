def tribonacci(signature, n):
    special_condition = []
    if n == 0:
        return []
    result = signature
    for i in range(n - 3 ):
        sum_up = signature[i] + signature[i + 1] + signature[i + 2]
        result.append(sum_up)
    if n == 1:
        special_condition.append(signature[0])
        return special_condition
    elif n == 2:
        return signature[:2]
    return result
    
