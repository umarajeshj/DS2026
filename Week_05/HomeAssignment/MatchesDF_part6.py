import pandas as pd
#1.Reading csv file

df=pd.read_csv("Week_05/matches.csv")
subset = df[['Season', 'winner', 'win_by_runs', 'venue']]

# 24. Identify the number of missing values in each column. 
missingValuesCount = df.isnull().sum()
print(missingValuesCount)
print("\n" + "*"*40 + "\n")

# 25. Display rows where the winner value is missing. 
winnerMissing = df[df['winner'].isnull()]
print(winnerMissing.head())

# 26. Replace missing values in the winner column with "No Result". 
df['winner'] = df['winner'].fillna("No Result")

# 27. Drop rows where both umpire1 and umpire2 are missing. 
orgCount = df.shape[0]
df = df.dropna(subset=['umpire1', 'umpire2'], how='all')
print(f"Removed rows : {orgCount-df.shape[0]}")

# 28. Drop columns that have more than 30% missing values. 
orgColcount = df.shape[1]
threshold = len(df) * 0.7
df = df.dropna(axis=1, thresh=threshold)
print(f"Dropped columns : {orgColcount - df.shape[1]} ")

