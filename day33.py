def mine_location(field):
    result = []
    
    for lst in field:
        if 1 in lst:
            flag = field.index(lst)
            result.append(flag)

    area = field[flag]

    for mine in area:
        if mine == 1:
            result.append(area.index(mine))
    return result
