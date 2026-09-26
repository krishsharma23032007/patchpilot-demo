def calculate_total(price, quantity):
    # BUG: should multiply price by quantity
    return price + quantity


def apply_discount(total, discount_percent):
    return total - (total * discount_percent / 100)
