def find_children(dancing_brigade):
    mothers = ""
    children = ""

    for letter in dancing_brigade:
        if letter.isupper():
            mothers += letter
        else:
            children += letter
        
    mothers = "".join(sorted(mothers))

    result = ""

    for mother in mothers:
        result += mother + mother.lower() * children.count(mother.lower())
    return result
