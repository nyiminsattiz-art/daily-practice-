def fuel_price(litres, price_per_litre):
    two_and_above = 0.05
    four_and_above = 0.10
    six_and_above = 0.15
    eight_and_above = 0.20
    ten_and_above = 0.25
   
    
    total = 0
    if litres < 2:
        total = litres * price_per_litre
    elif litres >= 2 and litres < 4:
        total = litres * (price_per_litre - two_and_above)
    elif litres >= 4 and litres < 6:
        total = litres * (price_per_litre - four_and_above)
    elif litres >= 6 and litres < 8:
        total = litres * (price_per_litre - six_and_above)
    elif litres >= 8 and litres < 10:
        total = litres * (price_per_litre - eight_and_above)
    elif litres >= 10:
        total = litres * (price_per_litre - ten_and_above)
    return total
