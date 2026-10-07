def get_order(order):
    new = (
        order.replace("burger", "Burger ")
        .replace("fries", "Fries ")
        .replace("chicken", "Chicken ")
        .replace("pizza", "Pizza ")
        .replace("sandwich", "Sandwich ")
        .replace("onionrings", "Onionrings ")
        .replace("milkshake", "Milkshake ")
        .replace("coke", "Coke ")
             )
    
    new = new.split()
    burger = ""
    fries = ""
    chicken = ""
    pizza = ""
    sandwich = ""
    onionrings = ""
    milkshake = ""
    coke = ""

    for item in new:
        if item == "Burger":
            burger += item + " "
        elif item == "Fries":
            fries += item + " "
        elif item == "Chicken":
            chicken += item + " "
        elif item == "Pizza":
            pizza += item + " "
        elif item == "Sandwich":
            sandwich += item + " "
        elif item == "Onionrings":
            onionrings += item + " "
        elif item == "Milkshake":
            milkshake += item + " "
        elif item == "Coke":
            coke += item + " "
        
    result = burger + fries + chicken + pizza + sandwich + onionrings + milkshake + coke
    return(result[:-1])
        
