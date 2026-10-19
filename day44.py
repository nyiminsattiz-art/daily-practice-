def decrypt(encrypted_text, n):
    if encrypted_text == "" or encrypted_text == None or n<= 0:
        return encrypted_text

    count = 0
    while count < n:
        middle = len(encrypted_text) // 2
        odd = encrypted_text[:middle]
        even = encrypted_text[middle:]
        result = ""
        for i in range(len(odd)):
            result += even[i]
            result += odd[i]
        if len(even) > len(odd):
            result += even[-1]
        count += 1
        encrypted_text = result
    return result


def encrypt(text, n):
    
    if text == "" or text == None or n<= 0:
        return text

    count = 0
    result = text

    while count < n:
        even = ""
        odd = ""
        for index, number in enumerate(result):
            if index % 2 == 0:
                even += number
            else:
                odd += number
        count += 1
        result = odd + even
    return result
    

