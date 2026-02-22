def calculate_bill(item_cost,quantity,tax=0.5,discount=0):
    total = (item_cost * quantity) + (item_cost * quantity * tax) - discount
    return total

positionalCalculation = calculate_bill(1000,2)
print("Bill 1 with default tax and discount : ",positionalCalculation)
customTax = calculate_bill(1000,2,tax=0.1)
print("Bill 2 with custom tax : ",customTax)
customDiscount = calculate_bill(1000,2,discount=50)
print("Bill 3 with custom discount : ",customDiscount)
customTaxAndDiscount = calculate_bill(1000,2,0.1,50)
print("Bill 4 with custom tax and discount : ",customTaxAndDiscount)
