import pandas as pd
import numpy as np
#1.Reading csv file

df=pd.read_csv("Week_05/matches.csv")

# 29. Create a new column is_super_over: • True if the match result indicates a tie • False otherwise 
df['is_super_over'] = df['result'] == 'tie'

# 30. Create a new column match_result: • "Runs" if win is by runs • "Wickets" if win is by wickets • "No Result" otherwise 
conditions = [
    (df['win_by_runs'] > 0),
    (df['win_by_wickets'] > 0)
]
choices = ['Runs', 'Wickets']
df['match_result'] = np.select(conditions, choices, default='No Result')

# 31. Convert the Season column to the appropriate data type if required. 
if df['Season'].dtype == 'object':
    df['Season'] = df['Season'].str.extract('(\\d+)').astype(int)


# 32. Standardize the team names in team1 and team2 to uppercase. 
df['team1'] = df['team1'].str.upper()
df['team2'] = df['team2'].str.upper()

print("--- New Columns Preview ---")
print(df[['team1', 'team2', 'Season', 'match_result', 'is_super_over']].head())