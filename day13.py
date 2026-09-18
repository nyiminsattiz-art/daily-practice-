HEX = set("0123456789ABCDEF")

def find_corrupted_byte(dump):
    for index, word in enumerate(dump):
        if len(word) != 2:
            return index
        for i in word:
            if i not in HEX:
                return index
    return -1
            

