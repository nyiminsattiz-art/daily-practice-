def what_time_is_it(angle):
    
    hour = int(angle // 30) % 12 or 12
    minute = int((angle % 30) * 2)
    return f"{hour:02d}:{minute:02d}"
