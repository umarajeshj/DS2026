import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Data understanding
df = pd.read_csv("Week10_ML/simple_linear_regression.csv")
print(df.head())

print("\nMissing values in each column:")
print(df.isnull().sum())

plt.figure(figsize=(10, 6))
plt.scatter(df['Area'], df['Price'], color='blue', alpha=0.5)
plt.title('Area vs. Price')
plt.xlabel('Area')
plt.ylabel('Price')
plt.grid(True)
plt.show()

#Data Cleaning
df['Price'] = df['Price'].fillna(df['Price'].mean())

data = df['Price'].values
mean = np.mean(data)
std_dev = np.std(data)
z_scores = (data - mean) / std_dev
df['Price_ZScore'] = z_scores
print(df[['Price', 'Price_ZScore']].head())

df_cleaned = df[df['Price_ZScore'].abs() <= 3]

print(f"Original rows: {len(df)}")
print(f"Rows after removing outliers: {len(df_cleaned)}")

#Feature Scaling
# 1. Apply standardization on Area
area_original = df_cleaned['Area']
mu = area_original.mean()
sigma = area_original.std()

df_cleaned['Area_Scaled'] = (area_original - mu) / sigma

# 2. Compare the values before and after scaling
comparison = df_cleaned[['Area', 'Area_Scaled']].head()
print("Comparison of Original vs. Scaled Area:")
print(comparison)

# Verify the new mean (~0) and standard deviation (~1)
print(f"\nNew Mean: {df_cleaned['Area_Scaled'].mean():.2f}")
print(f"New Std Dev: {df_cleaned['Area_Scaled'].std():.2f}")

#Model Implementation 
# 1. Prepare the data
# Using the cleaned and standardized Area as 'x' and Price as 'y'
x = df_cleaned['Area_Scaled'].values
y = df_cleaned['Price'].values

# 2. Initialize parameters
c = 0.0  # Intercept 
m = 0.0  # Slope 

# 3. Implement the linear regression equation: y_pred = b0 + b1*x
def predict(x, c, m):
    return c + m * x

# Calculate initial predictions (will be all zeros initially)
y_pred = predict(x, c, m)

print(f"Initial parameters: b0 = {c}, b1 = {m}")
print(f"First 5 predictions: {y_pred[:5]}")