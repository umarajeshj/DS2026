import matplotlib.pyplot as plt
import pandas as pd

df1 = pd.read_csv("Week_06/ClassAssignment/monthly_budget_march2025.csv")
plt.pie(df1['Amount_USD'], labels=df1['Category'], autopct='%1.1f%%', startangle=90)
plt.title("Pie chart example")
plt.show()