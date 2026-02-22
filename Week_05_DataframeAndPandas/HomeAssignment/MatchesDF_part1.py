import pandas as pd

#1.Readeing csv file
try:
    df=pd.read_csv("Week_05/matches.csv")
except FileNotFoundError:
    print("Error reading file")
    exit()

# #2.Display the first 5 rows of the DataFrame
print("First 5 rows of dataframe :")
print(df.head())
print("\n" + "*"*40 + "\n")

# 3. Print the shape of the DataFrame (rows, columns)
print(f"rows : {df.shape[0]}\ncolumns : {df.shape[1]}")
print("\n" + "*"*40 + "\n")

# 4. Display all column names
print("Column names:")
for col in df.columns:
    print(col)
print("\n" + "*"*40 + "\n")


#5. column datatypes and non-null counts
df.info()
print("\n" + "*"*40 + "\n")