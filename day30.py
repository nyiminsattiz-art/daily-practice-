def decipher_this(s):
    s = s.split()

    str_word = ""
    result = ""

    for word in s:
        number = ""
        alpha = ""
        for letter in word:
            if letter.isdigit():
                number += letter
            else:
                alpha += letter
        connecting = chr(int(number)) + alpha
        str_word += connecting + " "

    str_word = str_word.split()
    for i in str_word:
        if len(i) == 1 or len(i) == 2:
            result += i + " "
        elif len(i) == 3:
            result += i[0] + i[2] +  i[1] + " "
        elif len(i) == 4:
            result += i[0] + i[-1] + i[2] + i[1] + " "
        else:
            result += i[0] + i[-1] + i[2:-1] + i[1] + " "
    return result[:-1]
