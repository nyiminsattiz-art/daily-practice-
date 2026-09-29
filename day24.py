def word_count(s):
    exclusive_words = [ "a", "the", "on", "at", "of", "upon", "in", "as"]
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    splitting = ""

    for word in s:
        if word in alphabets:
            splitting += word
        else:
            splitting += " "
            
    splitting = splitting.split(" ")
    word_counting = []

    for i in splitting:
        if len(i) == 0:
            continue
        else:
            word_counting.append(i)

    count = 0
    for j in word_counting:
        if j in exclusive_words:
            continue
        else:
            count += 1

    return count
