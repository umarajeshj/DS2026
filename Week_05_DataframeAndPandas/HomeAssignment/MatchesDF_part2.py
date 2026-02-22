import pandas as pd

#1.Readeing csv file
try:
    df=pd.read_csv("Week_05/matches.csv")
except FileNotFoundError:
    print("Error reading file")
    exit()

#6.Select the Season column and verify the output type.
season_col = df['Season']
print(season_col)
print("\n" + "*"*40 + "\n")

#7.Select the following columns together:Season,team1,team2,winner
subset = df[['Season', 'team1', 'team2', 'winner']]
print(subset)
print("\n" + "*"*40 + "\n")

#8.Select all columns except:umpire1,umpire2,umpire3
df_no_umpires = df.drop(columns=['umpire1', 'umpire2', 'umpire3'])
print(df_no_umpires)
print("\n" + "*"*40 + "\n")

#9.Store the winner column in a variable and inspect its index.
winner_col = df['winner']
print(winner_col.index)
print("\n" + "*"*40 + "\n")

#10. Rename the column win_by_runs to runs_margin.
df.rename(columns={"win_by_runs":"runs_margin"},inplace=True)
print(df.info())