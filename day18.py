def elevator(left, right, call):
    if left == 0 and right == 0 and call == 0:
        return "right"
    left_floor = abs(left - call)
    right_floor = abs(right - call)
    if left_floor < right_floor:
        return "left"
    else:
        return "right"
