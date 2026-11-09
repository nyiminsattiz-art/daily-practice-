def vowel_indices(word):
    result = []
    for position, letter in enumerate(word.lower(), start=1):
        if letter in "aeiouy":
            result.append(position)
    return result
