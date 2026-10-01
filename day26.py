def valid_phone_number(phone_number):
    if len(phone_number) != 14:
        return False
    
    rule = "1234567890 ()-"
    for i in phone_number:
        if i not in rule:
            return False
    first_three = ""
    second_three = ""
    third_three = ""

    for index, number in enumerate(phone_number):
        if index == 1 or index == 2 or index == 3:
            first_three += number
        elif index == 6 or index == 7 or index == 8:
            second_three += number
        elif index == 10 or index == 11 or index == 12 or index == 13:
            third_three += number

    result = f"({first_three}) {second_three}-{third_three}"       

    if phone_number == result:
        return True
    else:
        return False
