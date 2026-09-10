def title_case(title, minor_words=''):
    if title == "":
        return ""
    title = title.lower()
    minor_words = minor_words.lower().split()
    title = title[0].upper() + title[1:]
    title = title.split(" ")
    result = []

    for words in title:
        if words not in minor_words:
            words = words[0].upper() + words[1:]
            result.append(words)
        else:
            result.append(words)
    result = " ".join(result)
    return result
    
