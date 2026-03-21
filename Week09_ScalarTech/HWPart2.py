import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Week09_ScalarTech/scaling_homework_dataset_100_rows.csv')
#1 Min,Max,Mean,Std values for Age,Exp,Salary,PerfScore,Bonus
target_features = ['Age','Experience','Salary','PerformanceScore','Bonus']

# Check and print the count of missing values (NaN)
missing_counts = df[target_features].isna().sum()
print("--- Count of Missing Values ---")
print(missing_counts)
corr_matrix = df[target_features].corr()

# plt.figure(figsize=(8, 8))
# sns.heatmap(corr_matrix, 
#             annot=True,      # Displays the correlation numbers in each cell
#             cmap='coolwarm', # Color scale: Red (positive), Blue (negative)
#             fmt=".2f",       # Rounds numbers to 2 decimal places
#             linewidths=0.5)  # Adds slight spacing between squares

# plt.title('Correlation Heatmap of Employee Features')
# plt.show()

print(f"Statistic values :\n {df[target_features].agg(['min', 'max', 'mean', 'std'])}")
# Age and Exp -->measured in years (less numbers)
# Salary and Bonus -->measured in Rs (heavy values)
#Perf score --numerical but small numbers which has impact on bonus and salary

std_scaler = StandardScaler()
df_scaled = df.copy()
df_scaled[target_features] = std_scaler.fit_transform(df[target_features])

print("\n--- Standard Scaler Features (First 5 rows) ---")
print(df_scaled[target_features].head()) #Mean 0,std 1

scalarmm = MinMaxScaler()
df_scaled[target_features] = scalarmm.fit_transform(df[target_features])
print("\n--- Min Max Scaler Features (First 5 rows) ---")
print(df_scaled[target_features].head()) #Min 0, max 1 #nused when there are o outiers/distribution is normal

scalerob = RobustScaler()
df_scaled[target_features] = scalerob.fit_transform(df[target_features])
print("\n--- Robust Scaler Features (First 5 rows) ---")
print(df_scaled[target_features].head())  #Median and IQR

sns.pairplot(df[target_features], corner=True)    
plt.suptitle('Pairplot of Employee Features by Department', y=1.02)
plt.show()