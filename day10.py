def bonus_time(salary, bonus):
    if bonus == True:
        salary = str(salary * 10)
        return "$" + salary
    else:
        return "$" + str(salary)
