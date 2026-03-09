import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Week_07_EDA/Employee_Missing_Data_100_Rows.csv")
print('\nOriginal row count :',df.shape[0])

# print("Original data :\n",df)
# print("\n" + "-"*40 + "\n")

#1.Total missing values per column
df_missingCount = df.isna().sum()
print(f"{'Column name':<20}|{'No.of missing values'}")
print("-" * 40)
for col,count in df_missingCount.items():
    print(f"{col:<20}|  {count}")


#2.Drop rows with any missing values (delete row if any one cell is empty)
df_removeNa = df.dropna(how='any')
df_afterDropping = df_removeNa.isna().sum()
print("After dropping rows with any missing value:",df_removeNa.shape[0])


#3.Drop rows with all missing values
df_removeNaAll = df.dropna(how='all')

print("After dropping rows with all missing value: ",df_removeNaAll.shape[0])

#dropna(thresh=3)
df_removeNaThresh = df.dropna(thresh=6)
print("After dropping rows using thresh: ",df_removeNaThresh.shape[0])

#Replace missing values using mean, median and 0 (Age as 0, salary as mean, perfscore as median)

# plt.scatter(df['Department'],df['Salary'],alpha=0.5, c='green')
# plt.title('Scatter Plot: Age vs Employee count')
# plt.ylabel('salaries')
# plt.xlabel('No.of employees')
# plt.show()

df_ageFill = df['Age'].fillna(0)
df_perf_fill= df['PerformanceScore'].fillna(df['PerformanceScore'].median())
df_salaryFill = df['Salary'].fillna(df['Salary'].mean())

print("After filling:")
print(f"{'Column name':<20}|{'No.of missing values'}")
print("-" * 40)
print(f"{'Age':<20}|{df_ageFill.isna().sum()}")
print(f"{'Salary':<20}|{df_perf_fill.isna().sum()}")
print(f"{'PerformanceScore':<20}|{df_salaryFill.isna().sum()}")

#ffill and bfill
df_ffill = df['Age'].ffill()
df_bfill = df['Age'].bfill()
print(f"{'Method':<15} | {'Missing Values Remaining'}")
print("-" * 40)
print(f"{'Original':<15} | {df['Age'].isna().sum()}")
print(f"{'ffill':<15} | {df_ffill.isna().sum()}")
print(f"{'bfill':<15} | {df_bfill.isna().sum()}")


# original_age = df['Age'].copy()
# ffill_age = df['Age'].ffill()
# bfill_age = df['Age'].bfill()
# mask = original_age.isna()
# comparison = pd.DataFrame({
#     'Original (NaN)': original_age[mask],
#     'ffill Value': ffill_age[mask],
#     'bfill Value':bfill_age[mask]
# })
# print("Rows that were updated:")
# print(comparison)