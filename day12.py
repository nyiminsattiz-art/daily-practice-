def to_csv_text(array):
    result = ""
    for lst in array:
        for number in lst:
            result += str(number) + ","
        result = result[:-1]
        result += "\n"
    return result[:-1]
