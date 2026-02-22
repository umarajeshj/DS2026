import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Week_06/ClassAssignment/Calorie_Tracking_Dataset.csv");
# Plot Graph
# plt.plot(df["Date"],df["Daily Weight (kg)"],marker='D',linestyle='-',color='b',label='DataTesting')
# plt.title("Date Vs Weight(kg)")
# plt.xlabel('Date')
# plt.ylabel('weight(kg)')
# plt.legend()
# plt.show()

# #bar graph
# plt.bar(df['Date'],df["Total Water Intake (Liters)"],bottom=0,align="center",color="skyblue")
# plt.title("Date Vs Water Intake(litres)")
# plt.xlabel("Date")
# plt.ylabel("Water intake(l)")
# plt.show()

#Scatter plot
df1 = pd.read_csv("Week_06/ClassAssignment/ad_spend_vs_sales_revenue.csv")
plt.scatter(df1["Ad_Spend_USD"],df1["ROI_Percent"],s=None, c="yellow", marker=None, cmap=None, alpha=None, edgecolors="red", label="Amount")
plt.title("Ad_Spend_USD Vs ROI_Percent")
plt.xlabel("Ad_Spend_USD")
plt.ylabel("ROI_Percent")
plt.legend()
plt.show()