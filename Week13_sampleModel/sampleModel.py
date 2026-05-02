import pandas as pd
from sklearn.preprocessing import StandardScaler,MinMaxScaler,RobustScaler
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
# 1. Read CSV and print dimensions
df = pd.read_csv("Week13_sampleModel/diabetes_dataset_with_missing.csv.xls")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# 2. Print sum of null values
print("\n--- Null Values Per Column ---")
print(df.isnull().sum())

# 3. Print rows with at least 1 null value
print("\n--- Rows with Null Values ---")
print(df[df.isnull().any(axis=1)])

# 4. Missing percentage
missing_pct = (df.isnull().sum() / len(df)) * 100
print(missing_pct.sort_values(ascending=False))

# 5.Filling the values (Median)
cols_to_fix = ['insulin', 'glucose', 'bmi', 'blood_pressure', 'age']

for col in cols_to_fix:
    df[col] = df[col].fillna(df[col].median())

# Verify 
print("\n--- Nulls after filling ---")
print(df.isnull().sum())

features = ['glucose','bmi','age','insulin','blood_pressure']

# 6.Scale 
scaler = RobustScaler()
df[features] = scaler.fit_transform(df[features])
print("--- Scaled Data Sample ---")
print(df[features].head())

# 7.Calculate Q1, Q3 and IQR
Q1 = df[features].quantile(0.25)
Q3 = df[features].quantile(0.75)
IQR = Q3 - Q1
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
print("lower_bound :\n ",lower_bound)
print("upper_bound : \n",upper_bound)
outlier_mask = (df[features] < lower_bound) | (df[features] > upper_bound)

print("\n--- Outlier Counts per Column ---")
print(outlier_mask.sum())

# Print actual rows containing outliers
print("\n--- Sample of Rows with Outliers ---")
print(df[outlier_mask.any(axis=1)].head())

# plot
plt.figure(figsize=(10,6))
sns.scatterplot(data=df, x='glucose', y='insulin', hue='diabetes')
plt.title("Scatterplot for Outlier Detection (Scaled Data)")
plt.show()

# 7. Logistic Regression Model
X = df[features]
y = df['diabetes']

# Split 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# Final evaluation
y_pred = model.predict(X_test)
print(f"\nModel Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")