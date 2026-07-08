def food_order(price, quantity):
    if not isinstance(price, (int, float)) or price <= 0:
        return "invalid price"
    
    if not isinstance(quantity, int) or quantity <= 0:
        return "invalid quantity"
    
    total = price * quantity
    return total
