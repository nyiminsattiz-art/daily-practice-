def decompose_single_strand(single_strand):
    result1 = ""
    position1 = 2
    
    for index1, word1 in enumerate(single_strand):
        if index1 == position1:
            result1 += word1 + " "
            position1 += 3
        else:
            result1 += word1

    result2 = ""
    position2 = 2
    for index2, word2 in enumerate(single_strand[1:]):
        if index2 == position2:
            result2 += word2 + " "
            position2 += 3
        else:
            result2 += word2
    result2 = single_strand[0] + " " + result2
    
    result3 = ""
    position3 = 2

    for index3, word3 in enumerate(single_strand[2:-1]):
        if index3 == position3:
            result3 += word3 + " "
            position3 += 3
        else:
            result3 += word3
    result3 = single_strand[:2] + " " + result3 + single_strand[-1]
    
    
    return f"Frame 1: {result1[:-1]}\nFrame 2: {result2}\nFrame 3: {result3}"
