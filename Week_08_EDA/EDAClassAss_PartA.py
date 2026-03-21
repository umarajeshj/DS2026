import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Week_08_EDA/FoodDelivery_Dataset.csv")

#1.Min,max,avg of delivery time
print("Min Delivery time : ",df["Delivery Time"].min())
print("Max Delivery time : ",df["Delivery Time"].max())
print("Average Delivery time : ",df["Delivery Time"].mean())

#2.Univariate --orders >Rs.1000
order_amount = [df["Order Amount"]>1000]
print("Count of orders >Rs.1000 : ",len(order_amount))

#Univariate-Ratings 5,3 and 1
print("Count of orders with Ratings=5 : ",len([df["Rating"]==5]))
print("Count of orders with Ratings=3 : ",len([df["Rating"]==3]))
print("Count of orders with Ratings=1 : ",len([df["Rating"]==1]))

#Bivariate -positive correlation for orders [1, 10, 20, 40, 60]
target_orders = [1, 10, 20, 40, 60]
filtered_df = df[df['Order'].isin(target_orders)]
plt.figure(figsize=(8, 5))
plt.scatter(filtered_df['Distance'], filtered_df['Delivery Time'], color='blue', marker='o')
plt.title('Distance vs Delivery Time (Orders 1, 10, 20, 40, 60)')
plt.xlabel('Distance (km)')
plt.ylabel('Delivery Time (min)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#5.Bivariate -negative correlation
plt.figure(figsize=(8, 5))
plt.scatter(filtered_df['Distance'], filtered_df['Rating'], color='red', marker='o')
plt.title('Distance vs Customer Rating (Orders 1, 10, 20, 40, 60)')
plt.xlabel('Distance (km)')
plt.ylabel('Customer Rating')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#6.Bivariate - Discount vs amount for distance with 1 km distance vs 7–9 km distance
plt.scatter(df['Distance'], df['Discount'], alpha=0.6, color='darkorange', edgecolors='w')
plt.title('Bivariate Analysis: Distance vs Discount Percentage', fontsize=14)
plt.xlabel('Distance (km)', fontsize=12)
plt.ylabel('Discount (%)', fontsize=12)
plt.axvspan(7, 9, color='green', alpha=0.1, label='Target Long-Distance Range')
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend()
plt.show()
# -->more distance-->more discount--to promote far away customers/delivery fee

#7.MULTIVARIATE – Happy Customers: Find 3 orders where Rating = 5. pairplot
happy_orders = df[df['Rating'] == 5].head(3)
print(happy_orders[['Order', 'Distance', 'Delivery Time', 'Order Amount']])
# -->less distance as delivery time is less/consistent order amount

#8.Unhappy Customers: Find 3 orders where Rating = 1. pairplot
unhappy_orders = df[df['Rating'] == 1].head(3)
print(unhappy_orders[['Order', 'Distance', 'Delivery Time', 'Order Amount']])

#9.CORRELATION TYPE – Write Positive, Negative, or No Correlation for each pair:  Seaborn chart  
corr_a = df['Distance'].corr(df['Delivery Time'])
corr_b = df['Distance'].corr(df['Rating'])
corr_c = df['Items Ordered'].corr(df['Order Amount'])
corr_d = df['Discount'].corr(df['Rating'])

print(f"a) Distance vs Time:    {corr_a:.2f} (Positive)")
print(f"b) Distance vs Rating:  {corr_b:.2f} (Negative)")
print(f"c) Items vs Amount:     {corr_c:.2f} (Positive)")
print(f"d) Discount vs Rating:  {corr_d:.2f} (Negative)")

#a) Distance ↔ Delivery Time  
# b) Distance ↔ Customer Rating    
# c) Items Ordered ↔ Order Amount    
# d) Discount % ↔ Customer Rating 

#10.Conclusion -- Delivery time affects the  ratings(Negative correlation) irrespective of the distance.