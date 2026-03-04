import pandas as pd

df = pd.read_csv("Week_07_EDA/missing_values_demo.csv")

print("Original data :\n",df)
print("\n" + "-"*40 + "\n")

#isnull
df_any = df.isnull().sum()
print(" Columnwise null values count:\n",df_any)
print("\n" + "-"*40 + "\n")

#dropna -- subset
df_removeNa = df.dropna()
print("After dropping all null values:\n",df_removeNa)
print("\n" + "-"*40 + "\n")

# Drop rows with NaN in the 'Age' column
df_cleaned = df.dropna(subset=['age'])
print("Drop rows with NaN in the 'Age' column:\n",df_cleaned)
print("\n" + "-"*40 + "\n")

#fillna
df['name'] = df['name'].fillna("Unknown")
df['score'] = df['score'].fillna(0)
print("Fill na,name with 'Unknown' and Score with '0' : \n",df)
