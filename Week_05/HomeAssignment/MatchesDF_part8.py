import pandas as pd

df=pd.read_csv("Week_05/matches.csv")

# 33. Sort the DataFrame by: • Season (ascending) • Match date (descending) 
df['date'] = pd.to_datetime(df['date'], dayfirst=True)
df_sorted = df.sort_values(by=['Season', 'date'], ascending=[True, False])
print(df_sorted[['Season', 'date', 'team1', 'team2']].head())
print("\n" + "*"*40 + "\n")

# 34. Sort matches by highest run margin. 
df_runmargin_sorted = df.sort_values(by='win_by_runs', ascending=False)

# 35. Create a DataFrame containing the top 10 matches with the highest run margin. 
top_10_margin_df = df_runmargin_sorted.head(10).copy()
print(top_10_margin_df[['winner', 'win_by_runs']])
print("\n" + "*"*40 + "\n")

# 36. Reset the index of the final DataFrame.
top_10_margin_df.reset_index(drop=True, inplace=True)
print(top_10_margin_df[['winner', 'win_by_runs']].head())
