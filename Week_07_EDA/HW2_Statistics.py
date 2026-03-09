import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'ID': [1, 2, 3, 4, 5, 6],
    'Name': ['Abi', 'Bala', 'John', 'David', 'Sam', 'Raj'],
    'CreditScore': [700, 650, np.nan, np.nan, 800, np.nan],
    'LoanAmount': [100, 200, 150, np.nan, 300, np.nan],
    'Age': [25, 30, np.nan, np.nan, np.nan, 40]  # Only 3 valid values
}
df = pd.DataFrame(data)

print("Original data\n",df)
print("===="*40)

#1. thresh =3 --> Any row with fewer than 3 valid data points will be dropped.
df_thresh_rows = df.dropna(thresh=3)
print("After thresh\n",df_thresh_rows) #David row dropped

# 2. Use dropna(axis=1, thresh=4)
df_clean_cols = df.dropna(axis=1, thresh=4)
print("Columns remaining:\n", df_clean_cols.columns.tolist())

# 3. Replace CreditScore with median
df['CreditScore'] = df['CreditScore'].fillna(df['CreditScore'].median())

# 4. Replace LoanAmount with mean
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].mean())

# 5. Calculate mean and standard deviation after imputation
print("After replace :\n",df)
mean_val = df['CreditScore'].mean()
std_val = df['CreditScore'].std()
df['CreditScore_Z'] = (df['CreditScore'] - mean_val) / std_val
print("DataFrame with Z-Scores:")
print(df[['CreditScore', 'CreditScore_Z']])

threshold = 2
# outliers = df[df['CreditScore_Z'].abs() > threshold]
# print("\nDetected Outliers:")
# print(outliers)

df['is_outlier'] = df['CreditScore_Z'].abs() > threshold
plt.figure(figsize=(8, 5))
colors = df['is_outlier'].map({True: 'red', False: 'blue'})
plt.scatter(df['CreditScore'], df['LoanAmount'], c=colors, s=100)
plt.title(f"Outlier Detection (Threshold > {threshold})")
plt.xlabel("Credit Score")
plt.ylabel("Loan Amount")
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()