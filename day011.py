def number(lines):
    result = []
    if len(lines) == 0:
        return []
    else:
        position = 0
        for i in range(1, len(lines) + 1):
            word = f"{i}: {lines[position]}"
            result.append(word)
            position += 1
    return result
