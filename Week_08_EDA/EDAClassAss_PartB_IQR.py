import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("Week_08_EDA/FoodDelivery_Dataset.csv")

#11.PERCENTILE-calculate Q!,Q3,IQR
q1 = df['Delivery Time'].quantile(0.25)
q3 = df['Delivery Time'].quantile(0.75)

#12.Calculate IQR
iqr = q3-q1

# IQR range middle 50% of these delivery times 
#are spread across a range of 36 minutes

#13. Bounds --used to find outliers
lower_bound = q1-(1.5*iqr) # 31.8 - (1.5 * 36.2) -->31.8 - 54.3 = -22.5
upper_bound = q3+(1.5*iqr) # 68 + (1.5 * 36.2) --> 68 + 54.3 = 122.3

#14 Outliers
outliers = df[(df['Delivery Time'] < lower_bound) | (df['Delivery Time'] > upper_bound)]

print("IQR/Outliers for Delivery Time")
print("------"*20)
print(f" Q1 (25th Percentile): {q1:.1f} minutes")
print(f" Q3 (75th Percentile): {q3:.1f} minutes")
print(f" IQR:  {iqr:.1f} minutes") 
print(f"lower_bound : {lower_bound}")
print(f"upper_bound : {upper_bound}")
print(f"Detected {len(outliers)} outliers:")
print(outliers['Delivery Time'])
print("------"*20)
#-->No outliers, as delivery time is within the lower_bound and upper_bound values.consistent data

#15.PERCENTILE + IQR
q1_orderAmt = df['Order Amount'].quantile(0.25)
q3_orderAmt = df['Order Amount'].quantile(0.75)

iqr_orderAmt = q3_orderAmt - q1_orderAmt

lower_bound_oa = q1_orderAmt-(1.5*iqr_orderAmt) # 31.8 - (1.5 * 36.2) -->31.8 - 54.3 = -22.5
upper_bound_oa = q3_orderAmt+(1.5*iqr_orderAmt) # 68 + (1.5 * 36.2) --> 68 + 54.3 = 122.3

outliers_oa = df[(df['Order Amount'] < lower_bound_oa) | (df['Order Amount'] > upper_bound_oa)]

print("IQR/Outliers for Order Amount")
print(f" Q1 (25th Percentile): {q1_orderAmt:.1f}")
print(f" Q3 (75th Percentile): {q3_orderAmt:.1f}")
print(f"IQR:  {iqr_orderAmt:.1f}") 
print(f"lower_bound : {lower_bound_oa}")
print(f"upper_bound : {upper_bound_oa}")
print(f"Detected {len(outliers_oa)} outliers:")
print(outliers_oa['Order Amount'])

#No outliers