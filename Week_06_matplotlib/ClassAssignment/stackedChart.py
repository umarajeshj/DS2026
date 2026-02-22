import matplotlib.pyplot as plt
months = ['January', 'February', 'March', 'April']
product_a_sales = [120, 150, 170, 200]
product_b_sales = [80, 100, 90,50]


plt.bar(months,product_a_sales, color="skyblue")
plt.bar(months,product_b_sales,bottom = product_a_sales, color="g")

plt.title("Stacked chart example")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()