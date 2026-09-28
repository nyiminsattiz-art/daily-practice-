def is_isogram(word: str) -> bool:
    word = word.lower()

    if word == "":
        return False

    word_count = []
    for letter in word:
        if not letter.isalpha():
            continue
        else:
            word_count.append(word.count(letter))

    same = True
    for number in word_count:
        if word_count[0] != number:
            same = False
            break
    if len(word_count) == 0:
        return False
    return same
