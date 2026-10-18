def race(v1, v2, g):
    result = []
    if v1 >= v2:
        return None
    totalSeconds = (g * 3600) / (v2 - v1)
    
    hour = totalSeconds // 3600
    remainingSeconds1 = totalSeconds % 3600
    result.append(int(hour))
    
    minute = remainingSeconds1 // 60
    remainingSeconds2 = remainingSeconds1 % 60
    result.append(int(minute))
    result.append(int(remainingSeconds2))
    return result
    
