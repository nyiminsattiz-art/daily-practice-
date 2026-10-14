def valid_ISBN10(isbn): 
    if len(isbn) != 10:
        return False
    total = 0
    for i in range(10):
        word = isbn[i]
        
        if word.isdigit():
            number = int(word)
        elif i == 9 and word == "X":
            number = 10
        else:
            return False
        
        total += number * (i + 1)
    return total % 11 == 0
        
