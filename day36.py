def format_words(words):
    if words == [] or words == [""] or words == None:
        return("")
    
    word_list = []

    for word in words:
        if len(word) != 0:
            word_list.append(word)
        

    result = ""

    if len(word_list) == 1:
        result += word_list[0]
    elif len(word_list) == 2:
        result += word_list[0] + " and " + word_list[1]
    else:
        for i in word_list[:-2]:
            result += i + ", "
        result += word_list[-2] + " and " + word_list[-1]
    return result
