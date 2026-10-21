def to_hex(x):
    digits = "0123456789ABCDEF"
    if x < 0:
        x = 0
    elif x > 255:
        x = 255
           
    colorFirst = x // 16
    colorSecond = x % 16
    return digits[colorFirst] + digits[colorSecond]

def rgb(r, g, b):
    result = to_hex(r) + to_hex(g) + to_hex(b)
    return result
    
    
