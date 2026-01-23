def calculate_bill(*args,tax=0.5,discount=0):
    """
    args order: item_cost,qty,tax,discount
    """
    item_cost =args[0]
    qty = args [1]
   # item_cost,qty = args
    total = (item_cost * qty) + (item_cost * qty * tax) - discount
    return total
bill1 = calculate_bill(1000,2)
print(bill1)