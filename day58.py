def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None
    
    result = []
    while lng > 0 and wdth > 0:
        side = min(lng, wdth)
        result.append(side)
        if lng > wdth:
            lng -= wdth
        else:
            wdth -= lng
    return result;

