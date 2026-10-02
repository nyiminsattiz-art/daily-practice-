import math

def square_it(digits):
    digits = str(digits)

    length = len(digits)
    root = math.isqrt(length)

    checking = root - 1
    result = ""
    if (root * root) == length:
        for index, number in enumerate(digits):
            if index == checking:
                result += number + "\n"
                checking += root
            else:
                result += number
    else:
        return "Not a perfect square!"
    
    return result[:-1]
