def deaf_grandma(you):
    result = []

    for word in you:
        if word == "BYE":
            result.append("OK, BYE!")
            break
        elif word == word.upper():
            result.append("NO, NOT SINCE 1938!")
        else:
            result.append("HUH?! SPEAK UP, SONNY!")
    return result
