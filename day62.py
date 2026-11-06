def balance(left, right):
    leftSide = 0
    rightSide = 0
    for i in left:
        if i == "!":
            leftSide += 2
        elif i == "?":
            leftSide += 3
            
    for j in right:
        if j == "!":
            rightSide += 2
        elif j == "?":
            rightSide += 3
    if leftSide > rightSide:
        return "Left"
    elif rightSide > leftSide:
        return "Right"
    return "Balance"
