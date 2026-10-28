def nth_fib(n):
    result = [0, 1]

    i = 0
    j = 1
    for k in range(2, n):
        number = 0
        number += result[i] + result[j]
        result.append(number)
        i += 1
        j += 1
    
    return (result[n - 1])
