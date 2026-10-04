def kebabize(st):
    result = ""

    for word in st:
        if word.isalpha():
            if word.isupper():
                result += "-" + word.lower()
            else:
                result += word
    if len(result) == 0:
        return ""
    if result[0] == "-":
        return(result[1:])
    else:
        return (result)
